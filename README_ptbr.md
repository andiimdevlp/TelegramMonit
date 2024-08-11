# Bot de Monitoramento do Telegram

Este projeto utiliza a biblioteca `Telethon` para monitorar mensagens em um chat do Telegram e encaminhá-las para outro chat.

## Configuração

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/telegram-monitor-bot.git
   cd telegram-monitor-bot

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt

3. **Configure as variáveis de ambiente:**

   Crie um arquivo .env na raiz do projeto e adicione suas credenciais:

   ```bash
   TELEGRAM_API_ID=YOUR_API_ID
   TELEGRAM_API_HASH=YOUR_API_HASH
   TELEGRAM_PHONE_NUMBER=YOUR_PHONE_NUMBER
   SOURCE_CHAT_ID=-1001111111111
   TARGET_CHAT_ID=-1002222222222

4. **Execute o bot:**

   ```bash
   python3 main.py

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

<a href="https://www.buymeacoffee.com/andiimdev" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](https://choosealicense.com/licenses/mit/) para detalhes.
