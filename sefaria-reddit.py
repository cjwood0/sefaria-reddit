from os import getenv
from dotenv import load_dotenv
from praw import Reddit
import urllib3
import json
import re

load_dotenv() # for running locally

USERNAME = getenv('USERNAME')
PASSWORD = getenv('PASSWORD')
CLIENT_ID = getenv('CLIENT_ID')
CLIENT_SECRET = getenv('CLIENT_SECRET')

r = Reddit(username=USERNAME, password=PASSWORD, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent='User-Please')
cites = re.compile(r'(\[|{)(.+?)(?:]|})(?!\()', re.IGNORECASE)
empty_tags = re.compile(r'<[bi]></[bi]>')
bold_tags = re.compile(r'</?b>')
italic_tags = re.compile(r'</?i>')
g_d = re.compile(r'\bGod\b')

http = urllib3.PoolManager()

#comments = [{"body": "[gen 1:1-4]"}, {"body": "{sota 2b}"}]
comments = r.subreddit('judaism').stream.comments(skip_existing=True)
for comment in comments:

  rep = ""
  for language, search in cites.findall(comment.body):
  #for language, search in cites.findall(comment["body"]):
    if language == "[":
      lang = "text"#TODO add heading
      heading = "ref"
    else:
      lang = "he"
      heading = "heRef"

    url=f'https://www.sefaria.org/api/texts/{search}?context=0'
    
    try:
      data = http.request('get', url).data
      response = json.loads(data.decode())
      
      verses = response[lang]
      if type(verses) == str:
        verses = [verses]

      passage = " ".join(verses)
      if len(passage) > 300:
        passage = passage[0:300] + "..."
      #replace tags
      passage = re.sub(g_d, "G_d", passage)
      passage = re.sub(empty_tags, "", passage)
      passage = re.sub(italic_tags, "*", passage)
      passage = re.sub(bold_tags, "**", passage)
  
      if passage:
        passage = f'[{response[heading]}](https://www.sefaria.org/{response["ref"]}?lang=bi&with=all&lang2=en)\n\n{passage}'
        rep = rep + "\n\n" + passage

    except Exception as e:
      print(e)
      continue

  if len(rep) > 0:
    comment.reply(rep)