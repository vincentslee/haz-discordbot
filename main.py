import discord

from transformers import pipeline, Conversation

# This gets the token id and guild id from the bot.txt file, which is formatted like so:
# 1 | [GUILD]
# 2 | [TOKEN]
f = open("bot.txt", "r")
f = f.read()
txt = f.split()
GUILD = int(txt[0])
TOKEN = txt[1]

#List of commands users can input, listed out for use in /help function
commandslist = [
"/help - *Gives list of commands*",
"/ping - *Pong*",
"/haz - *Use this command to talk to haz, for example, '/haz, how are you today?'*"

]


# Bot
class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        # These two lines instantiate the two different models that the bot uses
        self.conversational_pipeline = pipeline("conversational")
        self.textgen = pipeline(task="text-generation", model="gpt2")

        # All requests to the chat functionality must be put in a queue, otherwise the bot
        # can have trouble handling them
        self.queue = []

    # Message Commands
    async def on_message(self, message):
        if message.author == self.user:
            return

        # /Ping
        if message.content.casefold() == '/ping':
            print(message)
            await message.channel.send('pog')

        # DM's user a list of commands
        if message.content.casefold() == '/help':
            msg = ""
            for i in range(len(commandslist)):
                msg = msg + commandslist[i]
                msg = msg + '\n'
            await message.delete()
            await message.author.send(msg)

        # hazbot chatting
        if message.content.startswith('/haz'):
            # This removes the "/haz" from the user's message
            self.queue.append([str(message.content).replace("/haz",''), message.author.id])
            await message.channel.send("Haz is typing...")

            for i in range(len(self.queue)):
                # The bot uses two separate models, one for answering questions and one for prompts
                # The first is question answering, which uses the transformers conversational pipeline.
                # Each time the bot gets a question, the conversational pipeline creates a new conversation.
                # This is not necessarily the best use, since users can actually continue a conversation after creating
                # one, but I've found that for this application, creating a new conversation for each request
                # is the best method
                if self.queue[0][0][-1] == '?':
                    converse = Conversation(self.queue[0][0])
                    response = self.conversational_pipeline([converse])
                    await message.reply(format_response(str(response)))
                    del self.queue[0]

                # Anything that is not a question is given to the text generation pipeline, which will
                # generate text based on the user's prompt, basically continuing their prompt
                else:
                    response = self.textgen(self.queue[0][0])
                    response = response[0].get("generated_text")
                    await message.reply(str(response))
                    del self.queue[0]


# the transformers library uses a strange formatting when using their conversation pipeline,
# this function trims all the irrelivant text from the response
def format_response(text):
    response = ''
    for chr in reversed(text):
        if chr == '>':
            break
        else:
            response += chr

    return response[::-1]

# This runs the bot
client = CustomClient()
client.run(TOKEN)