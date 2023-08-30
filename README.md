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

It should output `Python 3.x.x` and `pip 23.x.x`

<br>

#### FOR WINDOWS DEVICES:

You may get an error along the lines of: `Python is not recognized as an internal or external command`\
To resolve this error, follow the steps below:

- Find your Python path (where Python was just installed on your computer, _note that it may be different from the image below_)

  <img width="500px" src="./images/path.jpeg">

- Search for "Edit the system environment variables" in Windows search, and add the path that you found previously to the `PATH` variable. See below.
  <img width="750px" src="./images/systemenv.jpeg">

---

### Step 2.2: Create Environment

Open the code in your IDE of choice. If you don't have one already, you can install a free one [here](https://code.visualstudio.com/download)

Open up the CLI and enter the command:

`pip install virtualenv`

`cd` into your project folder and run

`python3 -m virtualenv venv`

You should see that a folder named `venv` has been created.

You can now activate the virtual environment using the following command.

**Mac / Linux:** `source venv/bin/activate`\
**Windows:** `venv\Scripts\activate`

Once the venv has been activated, you should see `(venv)` at the beginning of the path. You can now install the required modules with

`pip install -r requirements.txt`

You can do a final check with `pip list` to see that all the modules have been installed correctly.

---

## Step 3: Configuration Setup

Rename the `example.env` file in the root directory to `.env`. Notice it has been prepopulated with the following information.

```.env
TOKEN=<YourBotToken>
API_KEY=<YourAPIKey>
BOT_ID=<YourBotId>
```

The env file stores all your application secrets. You will be filing this out with the appropriate values in the following steps:

### Step 3.1: Discord Bot setup

To create and configure a Discord bot, head to the [Discord Developer Portal](https://discord.com/developers/applications)

Once logged in, click `New Application` and enter into the application.

- On the `General Information` tab, there is an option to `copy` the application id. Copy this and replace `<YourBotId>` with it in the `.env` file.

Click on the `Bot` tab on the left, where you can set the name and icon of your bot. Here is also where you can find the Bot Token. _If you don't see one, you may need to generate a new token_.

- Once you have your token, replace `<YourBotToken>` with it in the `.env` file.

On the same `Bot` tab, scroll down and enable all **Privileged Gateway Intents**

<img width="800px" src="./images/intents.jpeg">

Click on `URL Generator` under the `OAuth2` tab.

Enable the `bot` and `applications.commands` **scopes**

<img width="800px" src="./images/scopes.jpeg">

Enable `Send Messages` under **Bot Permissions**, and any other permissions you wish to grant your bot.

<img width="800px" src="./images/permissions.jpeg">

You can now copy and paste the generated URL into your Discord server. Click on the link to authorize the bot.

### Step 3.2: OpenAi Api key

The OpenAI API key is crucial to infuse your Discord bot with AI capabilities provided by OpenAI.

To obtain and set up your OpenAI API key:

- Go to [OpenAI Platform](https://platform.openai.com/signup/)
- Sign up or log into your account
- Once logged in, click Personal (at the top right corner of the page) and then click View API keys
- Click "+ Create new secret key" to generate a new API key if you haven't already. Keep this key secure and do not share it publicly.

Integrate the key into your project:

- Inside the `.env` file, replace `<YourAPIKey>` with the API key you obtained from the OpenAI platform.

---

## Step 4: Run

Run the application with `python3 src` in the root directory

If successful, the console should log: `Logged in as <Bot> 🤖`

To start chatting with the bot, tag the bot and enter the desired message like so:\
`@bot_name How are you today?`

You can customise the bot response with a custom prompt using the `prompt.txt` file. An example prompt has been provided.

---

## Step 5: Extra for Experts

- Read up on the [discord.py documentation](https://discordpy.readthedocs.io/en/stable/intro.html) to learn more about the features and intricacies of Python discord bots.
- Incorporate another API
  - You can take your bot to the next level by incorporating custom APIs. This will allow your bot to fetch real-time data, perform specific tasks, or provide dynamic information beyond its built-in capabilities.
  - You can get started by looking through this [list of free public apis](https://github.com/public-apis/public-apis)
- Adjust your OpenAI model parameters:
  - Temperature: a parameter that determines the randomness of the model's output.
  - Max tokens: a parameter that sets the limit on the number of token's in the model's output.
  - Find out more [here](https://platform.openai.com/docs/api-reference/chat/create)

We have provided some example code in the `examples` folder to get you started. Feel free to customise the bot to your liking, we look forward to seeing all your unique creations! 🚀🤖
