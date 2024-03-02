import os
from atproto import Client

def get_next_joke():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    jokes_file = os.path.join(script_dir, 'deine_mutter_witze.txt')
    with open(jokes_file, 'r', encoding='utf-8') as file:
        jokes = file.readlines()
        return jokes

def post_joke(joke):
    client = Client(base_url='https://bsky.social/xrpc')
    client.login('nutzername.bsky.social', 'password') # SET PASSWORD AND USERNAME ACCORDINGLY
    client.send_post(joke)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    jokes = get_next_joke()
    counter_file_path = os.path.join(script_dir, 'counter.txt')

    # checking, if counter-file exists. if not, create and initialize
    if not os.path.exists(counter_file_path):
        with open(counter_file_path, 'w') as counter_file:
            counter_file.write('0')

    # read counter
    with open(counter_file_path, 'r+') as counter_file:
        counter = int(counter_file.read().strip())
        joke = jokes[counter]
        post_joke(joke)

        # add +1 to counter. if end is reached, reset to 0
        counter += 1
        if counter >= len(jokes):
            counter = 0

        counter_file.seek(0)
        counter_file.write(str(counter))
        counter_file.truncate()

if __name__ == "__main__":
    main()
