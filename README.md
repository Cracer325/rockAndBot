# Rock And Bot

## Usage
The bot is used to reply salute phrases to comments that contain the phrase Rock and stone or similar 

## How To Use
run ```pip install praw``` <br>
Create a reddit bot (search on google if you dont know how) <br>
put all of the neccessary credentials in the praw.Reddit command and then run it

## How it works
The bot uses praw (python's reddit api) to scrap r/deeprockgalactic of the first 100 comments (you can change the amount) and reply to them the phrase <br>
Warning: the bot will reply multiple times to the same comments, to avoid this you cann add a file that contains all the comments the bot repliede to and make him skip them
