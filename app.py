import os
from flask import *
import requests
import datetime
import pprint
import psycopg2
from bs4 import BeautifulStoneSoup
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import time
from Message_generater import Message_generater
from linebot.models import FlexSendMessage


CHANNEL_ACCESS_TOKEN = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
CHANNEL_SECRET=os.environ['LINE_CHANNEL_SECRET']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)
app = Flask(__name__)
running_line_group_id = 'Ccff6d282891e398e17cf65a39fc2c7c9'

@app.route('/favicon.ico')
def favicon():
    return "OK.There is noting!"


@app.route('/')
def index():
    return '元気に動作中'


@app.route('/callback', methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.reply_token == "00000000000000000000000000000000":
        return

@handler.add(PostbackEvent)
def handle_postback(event):
    user_id = event.source.user_id
    user_name = line_bot_api.get_profile(user_id).display_name
    answer = event.postback.data
    message = f'{user_name}さんは'
    if answer == 'yes':
        message +='走るみたいです！'
    else:
        message +='走らないみたいです...'
    line_bot_api.reply_message(event.reply_token,TextSendMessage(message))


@app.route('/daily_reminder', methods=['GET'])
def cron_handler():
    daily_reminder_message = Message_generater.gen_reminder()
    line_bot_api.push_message(running_line_group_id,daily_reminder_message)
    return 'OK'
    

if __name__ == "__main__":
    app.run(port=5000)
