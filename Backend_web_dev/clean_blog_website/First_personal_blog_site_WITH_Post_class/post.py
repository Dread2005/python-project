import requests


class Post:
    def __init__(self, post_id, title, subtitle, body, date, author, image_url):
        self.title = title
        self.id = post_id
        self.subtitle = subtitle
        self.body = body
        self.date = date
        self.author = author
        self.image = image_url
