from secrets import *
import praw, requests, re


reddit = praw.Reddit(
    client_id = CLIENTID ,
    client_secret = CLIENTSECRET,
    user_agent="python:https://github.com/nobel002/MemeVideoEngine:v0.0.1 (by /u/nobel002)",
    username = USERNAME,
    password = PASSWORD
)

#print(reddit.read_only)
for submission in reddit.subreddit("earthporn").hot(limit=10):
    print(submission.title)
    try:
      img = requests.get(submission.url)
      with open(f"generated/{submission.title}.png", "wb") as file:
        file.write(img.content)
    except:
      print("No image Found")