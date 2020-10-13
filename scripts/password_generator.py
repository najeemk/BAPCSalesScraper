# Generates a file "password.json" for use with BAPC Sales

import json

def prompt_client_information():
    '''
    Prompts for client information from the user through the input field
    '''
    client_id = input("Please Give Client ID: ")
    client_secret = input("Please Give Client Secret: ")
    user_agent = "python"
    return client_id, client_secret, user_agent

def generate_json(client_id, client_secret, user_agent, file_name="scripts/password.json"):
    '''
    Generates a JSON object with the client information
    client_id: str
    client_secret: str
    user_agent: str
    file_name: str (default = "password.json")
    '''
    client_information = {
        "client_id": client_id,
        "client_secret": client_secret,
        "user_agent": user_agent
    }

    with open(file_name, "w") as write_file:
        json.dump(client_information, write_file)

if __name__ == "__main__":
    print("First, lets generate the keys! Visit the link below to generate the keys")
    print("https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps")
    input("Press enter to continue...")
    client_id, client_secret, user_agent = prompt_client_information()
    generate_json(client_id, client_secret, user_agent)
else:
    raise Exception("Run Script Directly") 