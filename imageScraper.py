from secrets import *
import praw, requests, os


reddit = praw.Reddit(
    client_id = CLIENTID ,
    client_secret = CLIENTSECRET,
    user_agent="python:https://github.com/nobel002/MemeVideoEngine:v0.0.1 (by /u/nobel002)",
    username = USERNAME,
    password = PASSWORD
)

#print(reddit.read_only)
for submission in reddit.subreddit("memes").top(limit=10):
    #print(submission.title)
    if not(submission.is_self):
      try:
        img = requests.get(submission.url)
        with open(f"generated/images/{submission.title[:10]}.png", "wb") as file:
          file.write(img.content)
      except:
        print("No image Found")
    else:
      print("There's no image to be found here.")

#os.system("python VideoGenerator.py")