Extra funcionality:

Steps:
1- Modify scrape.py
# edit these three variables
  user = 'Put the user to query'
  
  start = datetime.datetime(2018, 3, 1)  # year, month, day
  
  end = datetime.datetime(2018, 3, 3)  # year, month, day

2- Run
  python scrape.py

3- Run
  jsontotxt.py

The result is tweets.txt
