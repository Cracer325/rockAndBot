import random

import praw

messages = [
    'rock and stone',
    'for  karl',
    'we rock',
    'leave no dwarf behind'
]

sendMessages = [
    'For Karl!',
    'ROCK... AND... STONE!',
    'For Rock and Stone!',
    'Leave no dwarf behind!',
    'We rock!',
    'By the Beard!'
]

reddit = praw.Reddit(user_agent="Rock&Bot 0.1",
                     client_id="...",
                     client_secret="...",
                     username="Rock-And-Bot",
                     password="...")
subreddit = reddit.subreddit('deeprockgalactic')
for comment in subreddit.comments(limit=100):
    print("Found comment!")
    for msg in messages:
        if msg in comment.body.lower():
            print("Replying")
            comment.reply(sendMessages[random.randint(0, 5)])
