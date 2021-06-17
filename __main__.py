POST_BASE_URL = 'https://www.instagram.com/p/'
MAX_POSTS = 10
POSTS_FILE = 'posts.json'

import instaloader
import json

loader = instaloader.Instaloader()

def get_posts(username:str, amount:int=None):
    user = instaloader.Profile.from_username(loader.context, username)
    posts = []
    for post in user.get_posts():
        posts.append(POST_BASE_URL + post.shortcode)
        if amount and len(posts) >= amount:
            break
    return posts

def __main__():
    print('Starting...')
    with open(POSTS_FILE, 'r') as file:
        file = json.load(file)
        for username in file.keys():
            posts = get_posts(username, MAX_POSTS)
            for post_url in posts:
                if not post_url in file[username]:
                    print(f"{username} posted {post_url}")
                    file[username].append(post_url)
        with open(POSTS_FILE, 'w') as file_2:
            json.dump(file, file_2)
    print('Done')

if __name__ == '__main__':
    __main__()

