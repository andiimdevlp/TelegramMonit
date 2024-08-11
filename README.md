# Telegram Monit

This project uses the `Telethon` library to monitor messages in a Telegram chat and forward them to another chat.

[Versão em Português](README_ptbr.md)
## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/andiimdevlp/TelegramMonit.git
   cd TelegramMonit

2. **Install dependencies:**
   
   ```bash
   pip install -r requirements.txt

3. **Configure environment variables:**

    Create a .env file in the root of the project and add your credentials:

    ```bash
    TELEGRAM_API_ID=YOUR_API_ID
    TELEGRAM_API_HASH=YOUR_API_HASH
    TELEGRAM_PHONE_NUMBER=YOUR_PHONE_NUMBER
    SOURCE_CHAT_ID=-1001111111111
    TARGET_CHAT_ID=-1002222222222

4. **Run the bot:**

    ```bash
    python3 main.py

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.

<a href="https://www.buymeacoffee.com/andiimdev" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

## Licença

This project is licensed under the MIT License. See the [LICENSE](https://choosealicense.com/licenses/mit/) file for details.
