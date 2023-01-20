import snscrape.modules.twitter as sntwitter
import pandas as pd

tweets_list = []

count = int(input('Enter the maximum count of tweets '))
search = input('Enter the search ')
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(search).get_items()):
    if i>count:
        break
    tweets_list.append([tweet.date, tweet.id, tweet.url, tweet.content, 
                         tweet.user.username, tweet.replyCount, 
                         tweet.retweetCount, tweet.lang, tweet.source, tweet.likeCount])

tweets_df = pd.DataFrame(tweets_list, columns=['Tweet Date', 'Tweet Id', 'URL',
                          'Content', 'Username', 'Reply Counts', 'Retweet Count',
                          'Language', 'Source', 'Like Count'])
display(tweets_df)
print('Scraped the data')
tweets_df.to_csv('twitter_data_'+search+'.csv',index=False)
