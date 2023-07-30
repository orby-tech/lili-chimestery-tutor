import os
import sys
from flask import Flask, request, abort, render_template
from dotenv import load_dotenv
from flask_cors import CORS
import requests

CHAT_ID = os.getenv("CHAT_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")
DEVELOPMENT = os.getenv("DEVELOPMENT")

def send_message(chat_id, text):
    method = "sendMessage"
    token = BOT_TOKEN
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    CORS(app)

    load_dotenv(".env")

    @app.route("/", methods=["GET"])
    def hello():
        return render_template('index.html')

    @app.route("/save-contacts", methods=["POST"])
    def save_contacts():
        print(request.data, file=sys.stderr)

        send_message(CHAT_ID, f"""
{ 'Тестовое сообщение'  if DEVELOPMENT else '' }                     
                
Новая заявка на сайте:
Имя: {request.json['username']}
whatsapp: {request.json['whatsapp']}
telegram: {request.json['telegram']}
Email: {request.json['email']}
""")


        return "OK"
    
    return app



if __name__ == "__main__":
    create_app().run(host="0.0.0.0")
