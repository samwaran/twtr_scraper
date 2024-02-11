import pandas as pd
from ntscraper import Nitter

scraper = Nitter()

def get_tweet(user, no, from_date, to_date):
    tweets = scraper.get_tweets(user, number=no, since=from_date, until=to_date)
    df = pd.DataFrame()
    dummy_arr=[]
    for tweet in tweets['tweets']:
        data = [tweet['link'],tweet['text'], tweet['user']['name'], tweet['user']['username'], tweet['date'], tweet['stats']['likes'], tweet['stats']['retweets'], tweet['stats']['comments']]
        dummy_arr.append(data)

    df=pd.DataFrame(dummy_arr,columns=['link','text', 'to_name', 'to_username', 'date', 'likes', 'retweets', 'comments'])
    df.to_csv('data.csv', index=None)
    print("completed...100%")

user = str(input("Username: "))
no=int(input("No. of tweets: "))
from_date=str(input("From date (YYYY-MM-DD): "))
to_date=str(input("To date (YYYY-MM-DD): "))

get_tweet(user, no, from_date, to_date)


