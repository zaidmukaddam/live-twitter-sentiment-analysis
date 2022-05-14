import os
import tweepy as tw
import streamlit as st
import pandas as pd
from transformers import pipeline
from dotenv import load_dotenv
import re

load_dotenv()


class SA:
    st.set_page_config(layout="wide")

    def __init__(self):
        self.api_key = os.environ['API_KEY']
        self.api_key_secret = os.environ['API_KEY_SECRET']
        self.access_token = os.environ['ACCESS_TOKEN']
        self.access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
        self.auth = tw.OAuthHandler(self.api_key, self.api_key_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tw.API(self.auth, wait_on_rate_limit=True)

        self.classifier = pipeline('sentiment-analysis')

        st.title('Live Twitter Sentiment Analysis')
        st.markdown('Get the sentiment labels of live tweets!')

    def run(self):
        with st.form(key='Enter name'):
            search_words = st.text_input(
                'Enter the topic for which you want to know the sentiment'
            )

            no_of_tweets = st.number_input(
                'Enter the number of latest tweets for which you want to know the sentiment (maximum 50 tweets)', 0, 50, 10
            )

            submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            tweets = tw.Cursor(
                self.api.search_tweets,
                q=search_words,
                lang="en"
            ).items(no_of_tweets)

            tweet_list = [i.text for i in tweets]

            tweet_list = [
                re.sub(r'(http\S+)|(@\S+)|(#\S+)|(RT\s)', '', i)
                for i in tweet_list
            ]

            output = [i for i in self.classifier(tweet_list)]

            labels = [output[i]['label'] for i in range(len(output))]

            df = pd.DataFrame(
                list(zip(tweet_list, labels)),
                columns=[
                    'Latest '+str(no_of_tweets) +
                    ' tweets'+' on '+search_words, 'Sentiment'
                ]
            )

            st.write(df)


if __name__ == '__main__':
    t = SA()
    t.run()
