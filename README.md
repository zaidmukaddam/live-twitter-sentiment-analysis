# Live Twitter Sentiment Analysis

### Get the sentiment labels of live tweets!


[Try the web application here.](https://share.streamlit.io/zaidmukaddam/live-twitter-sentiment-analysis/main/app.py)


## Overview
- This app uses Tweepy to get tweets from Twitter based on the input name/phrase.
- It then processes the tweets through HuggingFace transformers pipeline function for sentiment analysis.
- The resulting sentiments and corresponding tweets are then put in a dataframe for display which is what you see as result.


> **WEB APPLICATION -** [Live Twitter Sentiment Analysis](https://share.streamlit.io/zaidmukaddam/live-twitter-sentiment-analysis/main/app.py)
<br>

<img src="https://github.com/zaidmukaddam/live-twitter-sentiment-analysis/blob/main/images/1.png" width=700><br>
<img src="https://github.com/zaidmukaddam/live-twitter-sentiment-analysis/blob/main/images/2.png" width=600><br>
<br><img src="https://github.com/zaidmukaddam/live-twitter-sentiment-analysis/blob/main/images/3.png" width=600><br>


## Run Locally
- Clone the repository
    ``` bash
    git clone https://github.com/zaidmukaddam/live-twitter-sentiment-analysis.git
    ```
- Navigate to the directory
    ``` bash
    cd live-twitter-sentiment-analysis
    ```
- Create a virtual environment
    ``` bash
    python3 -m venv venv
    ```
- Install the dependencies:
    ```
    pip install -r requirements.txt
    ```
- Run the app:
    ```
    streamlit run app.py
    ```

## Tech Stacks Used:
- [Tweepy](https://docs.tweepy.org/en/stable/)
- [Hugging Face](https://huggingface.co)
- Transformers
- Twitter API
- Python
