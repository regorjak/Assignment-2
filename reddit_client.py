# reddit_client.py

import praw
import sys

def redditClient():
    """
    Set up Reddit API authentication.
    Replace with your own credentials if needed.
    
    Returns:
        praw.Reddit: Authenticated Reddit API client
    """

    try:
        client_id = "lCGbsoWsxtLjaFA2DBStog"
        client_secret = "7qaPpgiQIl_CleY-B-P8LHxw5YmdxA"
        password = "favoRs31"
        username = "RegorJarabe"
        user_agent = "client for SNAM2024"

        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            password=password,
            username=username,
            user_agent=user_agent
        )
        
        return reddit
    
    except Exception as e:
        sys.stderr.write(f"Reddit client setup failed: {e}\n")
        sys.exit(1)
