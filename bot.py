import os
import telegram
from flask import Flask, request, Response

bot = telegram.Bot(token='7862267819:AAHfZIZRwcwSNnx4abMDDxiLNFs1ObTd9hg')
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    chat_id = update['message']['chat']['id']
    text = update['message']['text']
    if text == '/start':
        bot.send_message(chat_id=chat_id, text="Bienvenue chez TestBot ! 😊\nTape /help pour plus d'infos.")
    elif text == '/help':
        bot.send_message(chat_id=chat_id, text="Commandes disponibles :\n/start - Message d'accueil\n/help - Cette aide")
    else:
        bot.send_message(chat_id=chat_id, text="Commande inconnue. Tape /help pour de l'aide.")
    return Response(status=200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
