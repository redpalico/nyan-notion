import requests
from datetime import datetime

NOTION_API_TOKEN = ""
NOTION_DATABASE_ID = ""

now = datetime.now()

headers = {
    "Authorization": f"Bearer {NOTION_API_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

data = {
    "parent": {"database_id": NOTION_DATABASE_ID},
    "properties": {
        "Name": {"title":[
		{"text": {"content": "Gomple Text"}}
	]},

	"Tags": {"multi_select":[
		{"name": "udon"}
	]},

        "abc": {"rich_text":[
               {"text": {"content": "Yomple Text"}}
        ]},

	"Date": {"date":{
		"start": f"{now}",
		"time_zone": "Asia/Tokyo"
	}},
    }
}

response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=data)
print(response.json())
