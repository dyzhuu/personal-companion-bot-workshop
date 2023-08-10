# Personal Companion Discord Bot

## Presented by GDSC - Google Developer Student Club

🤖 Introduction to Discord Bot Development 🤖

Welcome to the GDSC Personal Companion Discord Bot Event! We are thrilled to have you here for an exciting journey into the world of AI-powered Discord bots! This event is all about creating your very own personal companion bot, which will be your loyal virtual friend on Discord. Whether you prefer to work individually or in groups, this event offers a fantastic opportunity to learn, collaborate, and build something truly awesome!

🚀 What to Expect 🚀

During this session, you will gain hands-on experience in building an AI-driven Discord bot using the power of OpenAI API and the Discord API. Our talented mentors and organizers are ready to guide you every step of the way, providing you with valuable insights into bot development, AI integration, and creative custom features.

🎯 Learning Objectives 🎯

By the end of the event, you will:

Master the basics of Discord bot development.
Harness the potential of OpenAI API to imbue your bot with AI capabilities.
Utilize the Discord API to seamlessly integrate your bot into Discord servers.
Understand how to expand your bot's functionalities with custom commands and interactions with other APIs.

Happy coding! 🚀🤖

---

## Step 1: Clone The Repository
Download the code by clicking the green `Code` button and then `Download ZIP`

<img width="500px" src="./images/download.jpeg">

---

## Step 2: Install Software

### Step 2.1: Install Python
To get started, you first need [install Python](https://www.python.org/downloads/). If you already have Python, you can move on to the next step.

Double-check that Python and pip are installed by running `python3 --version` and `pip --version`in your CLI.\
**(use `python` if `python3` doesn't work)**

It should tell you the respective version numbers in the form of `Python 3.x.x` and `pip 23.x.x`

**FOR WINDOWS DEVICES:** If the above fails, try the following:

# ❗❗TODO:

- get python path
<img width="500px" src="./images/path.jpeg">
- add to system env variables
<img width="500px" src="./images/systemenv.jpeg">

---

### Step 2.2: Create Environment
Open the code in your IDE of choice. If you don't have one already, you can install a free one [here](https://code.visualstudio.com/download)

Open up the CLI and enter the command:

`pip install virtualenv`

cd into your project folder and run

`virtualenv venv`

You should see that a folder named `venv` has been created.

**Mac / Linux:** `source venv/bin/activate`\
**Windows:** `venv\Scripts\activate`

Once the venv has been activated, you should see `(venv)` at the beginning of the path. You can now install the required modules using the following command:

`pip install -r requirements.txt`

You can do a final check with `pip list` to see that all the modules have been installed correctly.

---
# ❗❗TODO:

## Step 3: Configuration Setup

### Step 3.1: Discord Bot setup
To create and configure a discord bot, head to the [Discord Developer Portal](https://discord.com/developers/applications)

Once you have logged in, click `New Application` in the top left corner.

Enter the details and then enter into the application.

Click on the `Bot` tab on the left, this is where you can set the name and icon of your bot.

Scroll down and enable all **Privileged Gateway Intents**

<img width="500px" src="./images/intents.jpeg">

Navigate to the `OAuth2` tab and click on `URL Generator`

Enable the `bot` and `applications.commands` **scopes**

<img width="500px" src="./images/scopes.jpeg">

Enable `Send Messages` under **Bot Permissions**, along with any other permissions you wish to grant your bot.

<img width="500px" src="./images/permissions.jpeg">

### Step 3.2: OpenAi Api key

---

## Step 4: Run

---

## Step 5: Extra for Experts
- custom commands
- read the discord.py docs for more features
