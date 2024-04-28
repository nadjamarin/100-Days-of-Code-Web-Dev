import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
# Get the HTML code from the website
response = requests.get(URL)
movies_webpage = response.text

# Make beautiful soup object and find the titles of each movie/ranking
soup = BeautifulSoup(movies_webpage, "html.parser")
title_tags = soup.find_all(name="h3", class_="title")
titles = []
for tag in title_tags:
    titles.append(tag.getText())
# titles = [movie.getText() for movie in title_tags]

titles.reverse()
# print(titles)

# Save the ranked movie titles in a .txt file
with open("movies.txt", "w", encoding="utf8") as file:
    for movie in titles:
        file.write(f"{movie}\n")
