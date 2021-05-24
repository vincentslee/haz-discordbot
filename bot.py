import discord

from transformers import pipeline, Conversation

f = open("bot.txt", "r")
f = f.read()
txt = f.split()

TOKEN = txt[1]
GUILD = int(txt[0])

#User ids that can't be trusted
blacklist = []

#List of commands users can input, listed out for use in !help function
commandslist = [
"/help - *Gives list of commands*",
"/ping - *Pong*",
"/haz - *Use this command to talk to haz, for example, '/haz, how are you today?'*"

]


class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        self.conversational_pipeline = pipeline("conversational")
        self.textgen = pipeline(task="text-generation", model="gpt2")
        self.queue = []

    #Message Commands
    async def on_message(self, message):
        if message.author == self.user:
            return

        #!Ping
        if message.content.casefold() == '/ping':
            print(message)
            await message.channel.send('pog')

        #DM's user a list of commands
        if message.content.casefold() == '/help':
            msg = ""
            for i in range(len(commandslist)):
                msg = msg + commandslist[i]
                msg = msg + '\n'
            await message.delete()
            await message.author.send(msg)

        if message.content.startswith('/hello'):
            prompt = 'hello'
            self.converse = Conversation(prompt)
            response = self.conversational_pipeline([self.converse])
            await message.channel.send(format_response(str(response)))

        #Magic 8 ball
        if message.content.startswith('/haz'):
            self.queue.append([str(message.content).replace("/haz",''), message.author.id])
            await message.channel.send("Haz is typing...")
            for i in range(len(self.queue)):
                if self.queue[0][0][-1] == '?':
                    converse = Conversation(self.queue[0][0])
                    response = self.conversational_pipeline([converse])
                    await message.reply(format_response(str(response)))
                    del self.queue[0]
                    print(self.queue)
                else:
                    response = self.textgen(self.queue[0][0])
                    response = response[0].get("generated_text")
                    await message.reply(str(response))
                    del self.queue[0]
                    print(self.queue)



def format_response(text):
    response = ''
    for chr in reversed(text):
        if chr == '>':
            break
        else:
            response += chr

    return response[::-1]


client = CustomClient()
client.run(TOKEN)