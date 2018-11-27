import twitter

api = twitter.Api(consumer_key='', consumer_secret='', access_token_key='', access_token_secret='', tweet_mode='extended')

statuses = api.GetUserTimeline(screen_name='realDonaldTrump')

#printing out the tweets
print([s.full_text for s in statuses])

for status in statuses:
        retweets = api.GetRetweets(statusid=status.id)
        for i in retweets:
                try:
                        if i.retweeted_status:
                                print(i.retweeted_status.full_text)
                except:
                        pass
