Extra funcionality:

Steps:
1- Modify scrape.py
# edit these three variables
  user = 'Put the user to query'
<<<<<<< HEAD

  start = datetime.datetime(2018, 3, 1)  # year, month, day

=======

  start = datetime.datetime(2018, 3, 1)  # year, month, day

>>>>>>> 00d14d6674d821e3248804716a87ee4795352f86
  end = datetime.datetime(2018, 3, 3)  # year, month, day

2- Run
  python scrape.py


The result is $USER.json with all the tweets
