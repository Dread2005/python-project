from bs4 import BeautifulSoup
import requests

live_website = requests.get("https://news.ycombinator.com/")
web_text = live_website.text

soup = BeautifulSoup(web_text, "html.parser")
title = soup.title

# first_article_text = soup.find(name="span", class_="titleline")#name="a", href="https://www.netbsd.org/developers/commit-guidelines.html")
# _article_text = first_article_text.getText()
# print(_article_text)
#
# first_article_link_ = first_article_text.find("a")
# link = first_article_link_.get("href")
# print(link)
#
# first_article_upvote = soup.find(name="span", id="score_40397789", class_="score")
# first_article_upvote_score = first_article_upvote.text
# print(first_article_upvote_score)

article_texts = soup.find_all(name="span", class_="titleline")
article_upvotes = soup.find_all(name="span", class_="score")

# for a in article_texts:
#     # multiple articles
#     articles = a.find("a")
#     articles_text = articles.text
#     link = articles.get("href")
#     print(f"{articles_text}\n{link}")

#splititng multiple strings in a list
#score_upvotes = [score.text.split()[0] for score in article_upvotes]

#for loop in a list:
articles = [article.find("a").text for article in article_texts]
#print(articles)
links = [article.find("a").get("href") for article in article_texts]
#print(links)
score_upvotes = [int(score.text.split()[0]) for score in article_upvotes]
#print(score_upvotes)

larget_number = max(score_upvotes)
largets_index = score_upvotes.index(larget_number)
article_index = articles[largets_index]
links_index = links[largets_index]

print(f"{article_index}\n{links_index}\n{larget_number}")



















