# Deezbot

A simple telegram bot that uses NLP to decide which messages to reply to with `<verb> deez`.

## Getting started

There's a few ways to get the bot up and running. The easiest way is to use the docker image provided in the repository. If you want to run the bot locally, you can follow the [instructions](#local-setup).

### Docker
A docker image is provided in the repository. To run the bot using docker, follow the steps below:
```
docker run -e BOT_TOKEN=<your_bot_token> ghcr.io/sphericalkat/deezbot:main
```

### Local setup

1. Clone the repository
2. Install the requirements

```
pip install -r requirements.txt
```

3. Create a `.env` file with the following content:

```
BOT_TOKEN=<your_bot_token>
```

A sample `.env` file is provided in the repository. 4. Run the bot

```
python3 bot.py
```
