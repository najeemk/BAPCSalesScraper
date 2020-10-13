from datetime import datetime, timezone, timedelta
import json
import praw

HOUR_RECALL = 2
ASTRISK_SIZE = 60
SUBREDDIT_NAME = "buildapcsales"
PASSWORD_FILE = "password.json"

def print_submission(post_time_local, post_title, post_permalink):
    print("\n" + "*" * ASTRISK_SIZE)
    print(post_time_local.strftime('%Y-%m-%d %I:%M:%S %p'))
    print(post_title)
    print(post_permalink)
    print("*" * ASTRISK_SIZE + "\n")

# load the file
with open(PASSWORD_FILE, "r") as password:
    client_information = json.load(password)

# create a PRAW Reddit Instance
reddit = praw.Reddit(
    client_id=client_information["client_id"],
    client_secret=client_information["client_secret"],
    user_agent=client_information["user_agent"]
)

# main loop
if __name__ == "__main__":

    for submission in reddit.subreddit(SUBREDDIT_NAME).stream.submissions():

        post_time_utc = datetime.utcfromtimestamp(int(submission.created_utc))
        elapsed_time = datetime.utcnow() - post_time_utc

        post_time_local =  post_time_utc.replace(tzinfo=timezone.utc).astimezone(tz=None)
        post_permalink = f"https://reddit.com{submission.permalink}"

        if elapsed_time < timedelta(hours=HOUR_RECALL):
            # hides spoiler and NSFW content (this usually marks a sale that is over)
            if (submission.spoiler == False) and (submission.over_18 == False):
                print_submission(post_time_local, submission.title, post_permalink)
