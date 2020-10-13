# bapc client generation
import json
import praw

def load_client():
    '''
    Loads the password.json and creates the PRAW instance file
    '''
    with open("password.json", "r") as password:
        client_information = json.load(password)

    praw_instance = praw.Reddit(
        client_id=client_information["client_id"],
        client_secret=client_information["client_secret"],
        user_agent=client_information["user_agent"]
    )

    return praw_instance

def load_subreddit(instance, subreddit_name):
    '''
    Returns: a subreddit object
    '''
    return instance.subreddit(subreddit_name)

if __name__ == "__main__":
    # creates an instance and loads the BACPSales Subreddit
    subreddit = load_subreddit(load_client(), "buildapcsales")
    print(f"subreddit: r/{subreddit.display_name}")
    print(f"name: {subreddit.title}\n")

    for submission in subreddit.hot(limit=10):
        print(submission.title)
