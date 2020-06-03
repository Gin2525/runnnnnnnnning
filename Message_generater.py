import datetime
import json
from linebot.models import FlexSendMessage

class Message_generater:
	phrase = '今日は走る？'
	image_url = 'https://i.imgur.com/1YO0Nng.png'
	image_url2 = 'https://i.imgur.com/1KfezxJ.jpg'

	today_date_obj = datetime.datetime.now()
	today = f'{today_date_obj.month}/{today_date_obj.day}'
	invite_message = f'{today} {phrase}'
	reminder_base = '''
{
  "type": "bubble",
  "hero": {
    "type": "image",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "fit",
    "action": {
      "type": "postback",
      "data": "nothing"
    },
    "url": "*image_url"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "*invite_message",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "spacer"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "height": "md",
            "action": {
              "type": "postback",
              "label": "はい",
              "data": "yes"
            }
          },
          {
            "type": "separator",
            "margin": "md",
            "color": "#FFFFFF"
          },
          {
            "type": "button",
            "style": "secondary",
            "height": "md",
            "action": {
              "type": "postback",
              "label": "いいえ",
              "data": "no"
            }
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "spacer"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "datetimepicker",
              "label": "希望開始時刻",
              "data": "time_picker",
              "mode": "time"
            },
            "style": "primary",
            "height": "md"
          }
        ]
      }
    ]
  }
}
		'''
	def __init__(self):
		pass
	
	@classmethod
	def gen_reminder(cls):
		reminder_text = cls.reminder_base.replace("*image_url",cls.image_url2).replace("*invite_message", cls.invite_message)
		reminder_json = json.loads(reminder_text)
		reminder_flex = FlexSendMessage(alt_text="running_reminder",contents=reminder_json)
		return reminder_flex
