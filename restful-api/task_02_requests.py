#!/usr/bin/python3
import requests
import csv


URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder API
    Print status code
    Print titles if request successful
    """
    response = requests.get(URL)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch posts and save id, title, body into posts.csv
    """
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()

        structured_data = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body"),
            }
            for post in posts
        ]

        with open("posts.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_data)
