#!/usr/bin/python3
"""
Module to query the Reddit API, parse the titles of all hot articles,
and print a sorted count of given keywords (case-insensitive).
"""

import requests
from collections import Counter


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
        Parses the titles of all hot articles and prints a sorted count of
        given keywords.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-user-agent'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            after = data.get("after")
            posts = data.get("children", [])

            for post in posts:
                title = post.get("data", {}).get("title", "").lower()
                hot_list.append(title)

            if after is not None:
                return count_words(subreddit, word_list, hot_list, after)
            else:
                word_count = Counter()
                word_list_lower = [word.lower() for word in word_list]

                for title in hot_list:
                    for word in title.split():
                        if word in word_list_lower:
                            word_count[word] += 1

                sorted_word_count = sorted(word_count.items(), key=lambda
                                           kv: (-kv[1], kv[0]))

                for word, count in sorted_word_count:
                    print(f"{word}: {count}")
        else:
            return
    except requests.RequestException:
        return
