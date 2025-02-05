from bs4 import BeautifulSoup
import requests

top_100_movie_web = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/"
                                 "features/best-movies-2/")
web_text = top_100_movie_web.text

soup = BeautifulSoup(web_text,"html.parser")
website_text = soup.find_all(name="h3", class_="title")
movielist = [movie.getText() for movie in website_text[::-1]]
#print(movielist)
with open("top_100_movies.txt", "w")as best_movies:
    for movie in movielist:
        best_movies.write(f"{movie}\n")




