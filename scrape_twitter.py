import snscrape.modules.twitter as sntwitter
import pandas as pd

tweets_list = []

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('#Accenture since:2023-01-01').get_items()):
    if i>9999:
        break
    tweets_list.append([tweet.date, tweet.id, tweet.url, tweet.content, 
                         tweet.user.username, tweet.replyCount, 
                         tweet.retweetCount, tweet.lang, tweet.source, tweet.likeCount])

tweets_df = pd.DataFrame(tweets_list, columns=['Tweet Date', 'Tweet Id', 'URL',
                          'Content', 'Username', 'Reply Counts', 'Retweet Count',
                          'Language', 'Source', 'Like Count'])
display(tweets_df)
