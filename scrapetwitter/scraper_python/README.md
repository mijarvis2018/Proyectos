Extra funcionality:

Steps:
1 - Create a virtualenv (activate that virtual env)
2 - Install selenium and tweepy via pip

3- Modify scrape.py
# edit these three variables
  user = 'Put the user to query'

  start = datetime.datetime(2018, 3, 1)  # year, month, day

  end = datetime.datetime(2018, 3, 3)  # year, month, day

2- Run
  python3 scrape.py   # Make sure you are running python3


The result is $USER.json with all the tweets.
