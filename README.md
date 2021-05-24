
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/vincentslee/haz-discordbot">
  </a>

  <img src=/images/hazbotlogo.png alt=logo.png>
  
  <p align="center">
    A machine learning powered chatbot for your Discord!
    <br />
    <a href="https://github.com/vincentslee/haz-discordbot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/vincentslee/haz-discordbot/blob/master/images/chatscreenshot.png">View Demo</a>
    ·
    <a href="https://github.com/vincentslee/haz-discordbot/issues">Report Bug</a>
    ·
    <a href="https://github.com/vincentslee/haz-discordbot/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Hazbot is an attempt to give any Discord server a witty penpal to interact with. The name "haz" derives from mid 2000's meme culture, which the bot references quite frequently
in my experience. I got the idea while I was removing myself from inactive Discord servers with no one to talk to, I thought that people would be more active if there was someone they could talk to 24/7.


### Built With

* [Transformers](https://huggingface.co/transformers/index.html)
* [Discord API](https://discord.com/developers/docs/intro)



<!-- GETTING STARTED -->
## Getting Started

 Make sure you read up on the Discord API docs so you know what you're doing. If you've never added a bot to a server before, you may want to try that first with a different bot, here are a bunch you can use for free: https://top.gg/



### Prerequisites

pip install discord

Go here to install pytorch: https://pytorch.org/get-started/locally/

pip install transformers

### Installation

1. Download files
2. Install dependancies using pip, discord.py is straightforward but transformers may require you to install pytorch
3. Create a bot.txt file with this format:
   __________________
   1 | [GUILD]
   
   2 | [TOKEN]
   __________________
   if you do not know what those are, make sure you read the Discord API docs
4. Run main.py, if this does not work either something is wrong with your bot.txt file or you may need to add the bot to a server first
5. Add the bot to your Discord server of choice, if you do not know how to do this, here is a tutorial that is sufficient: https://www.businessinsider.com/how-to-add-a-bot-to-discord



<!-- USAGE EXAMPLES -->
## Usage

While the bot is active on the server, type /haz to talk to it

<img src="images/chatscreenshot.png?raw=true" alt="chatscreenshot.png">



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/vincentslee/haz-discordbot/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Vincent - [vincent-lee](https://www.linkedin.com/in/vincent-lee-4aabb01b0/) - vlee116@gmail.com

Project Link: [https://github.com/vincentslee/haz-discordbot](https://github.com/vincentslee/haz-discordbot)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/vincent-lee-4aabb01b0/
[product-screenshot]: images/screenshot.png
