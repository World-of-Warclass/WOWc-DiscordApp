# Leostaer Discord App

## Installation

To install the Leostaer Discord bot, follow these steps:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/World-of-Warclass/Leostaer-bot.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Leostaer-bot
    ```

3. Install the required dependencies using poetry:  
    ```bash
    poetry install
    ```

4. Create a new Discord application and bot on the Discord Developer Portal. Make sure to copy the bot token.

5. Additionally you need to see our entity relationship diagram to create a database to test operation.

6. Create a `.env` file in the project directory and add the following lines, replacing `TOKEN`, `PREFIX`, `HOST`, `DATABASE`, `USER`, and `PASSWORD` with the actual values:
    ```plaintext
    TOKEN=YOUR_BOT_TOKEN
    PREFIX=YOUR_PREFIX
    HOST=YOUR_HOST
    DATABASE=YOUR_DATABASE
    USER=YOUR_USER
    PASSWORD=YOUR_PASSWORD
    ```

7. Start the bot:
    ```bash
    python main.py
    ```

8. The Leostaer Discord App should now be up and running on your server!

## Usage

To use the Leostaer Discord App, simply invite it to your server and use the available commands.
