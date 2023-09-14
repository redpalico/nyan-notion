import requests
from datetime import datetime

NOTION_API_TOKEN = "secret_8rfeigpLEnyRkEr5rYxNb6DPDRz5IjYl5EN9PIPk7XM"
NOTION_DATABASE_ID = "3ca848f25b654368a0a170ac45ffe71f"

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
