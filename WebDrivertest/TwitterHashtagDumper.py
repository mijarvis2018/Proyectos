from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time
import json
import datetime

# MODIFY THIS VARIABLE
hashtags = 'HASH TO SEARCH CHANGEME'


# Initial variable setup
ObjectSelected = ''
url = ''
p1 = ''
p2 = ''
tweet_selector = 'li.js-stream-item'
text_selector_f = 'p.tweet-text'
id_selector = '.time a.tweet-timestamp'
ids = []
logfile = 'HashtagTweets_%s' % hashtags +'.json'
totaltweets = 0

print 'Setting up Display options'
display = Display(visible=1, size=(1200, 902))
print 'Openeing Display'
display.start()
print 'Setting up chrome config'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery");
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.delete_all_cookies()

print 'Settings done'

def form_url(hashtags):
    p1 = 'https://twitter.com/search?f=hashtag&vertical=default&q='
    p2 =  hashtags
    return p1 + p2

print 'Loading Chrome'
driver.get("https://google.com/") #Change the url if you need
time.sleep(5)
print 'Chrome loaded'



print ('Looking for hastag: #%s' % hashtags)
url = form_url(hashtags)

print ('Url: %s' % url)
driver.get(url)
time.sleep(5)
print 'Page loaded'

print 'Reading tweets...'
try:
    found_tweets = driver.find_elements_by_css_selector(tweet_selector)
    increment = 0
#    for tweet in found_tweets:
#        try:
#            id = tweet.find_element_by_css_selector(id_selector).get_attribute('href').split('/')[-1]
#            ids.append(id)
#        except StaleElementReferenceException as e:
#            print('Lost element reference!', tweet)
    while len(found_tweets) >= increment:
        print ('Scrolling down to load more tweets...')
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        print 'Pausing to load more results'
        time.sleep(5)
        try:
            found_tweets = driver.find_elements_by_css_selector(tweet_selector)
            increment += 20
            print ('Tweets found: %d' % len(found_tweets))
#            for tweet in found_tweets:
#                try:
#                    id = tweet.find_element_by_css_selector(id_selector).get_attribute('href').split('/')[-1]
#                    ids.append(id)
#                except StaleElementReferenceException as e:
#                    print('Lost element reference!', tweet)

        except NoSuchElementException:
            print 'No more tweets!'
    print 'Done looking for tweets!'
    print 'Saving tweets!'
    for tweet in found_tweets:
        totaltweets += 1
        text_f = tweet.find_element_by_css_selector(text_selector_f).text.encode("utf-8")
        try:
            with open(logfile, 'a') as outfile:
                outfile.write('\n')
                json.dump(text_f, outfile)
        except IOError:
            with open(logfile, 'w') as outfile:
                json.dump(text_f, outfile)
    print 'DONE Saving tweets!'
except NoSuchElementException:
    print 'No tweets!'

print ('Tweets found: %d' % len(found_tweets))
print ('Total tweets saved: %d' % totaltweets)

print 'Closing Chrome'
driver.quit()
print 'Chrome Closed'

print 'Closing Display'
display.stop()
print 'Display Closed. Program finished, good bye!'
