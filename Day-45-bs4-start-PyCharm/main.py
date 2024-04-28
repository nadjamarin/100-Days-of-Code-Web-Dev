from bs4 import BeautifulSoup
import lxml
import requests

# ---------------- Scraping a live website ----------------
response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# article_tag = soup.find(name="a", class_="storylink")
# articles = soup.select_all(selector="span a")
# print(articles)
articles = soup.find_all(name="a", href="https://arxiv.org/abs/2402.12354")
# ^ storylink class was not on the website, wasn't able to get full list of texts and links

article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)
# print(int(article_upvotes[0].split()[0]))

# Find article with most number of upvotes, print the title and link
max_upvotes = max(article_upvotes)
max_upvotes_index = article_upvotes.index(max_upvotes)
print(f"Title: {article_texts[max_upvotes_index]}\nLink: {article_links[max_upvotes_index]}")


# ---------------- Scraping local website.html ----------------
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# # print(type(contents))
#
# soup = BeautifulSoup(contents, "html.parser")
# # Can access different parts of the HTML code through the soup object
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
#
# # Print entire HTML doc with indentation (prettify)
# # print(soup.prettify())
#
# # Find first tag of a certain type (anchor tag)
# # print(soup.a)  # Gives first anchor tag
#
# # How to find all tags of a certain type
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# # Print only the text in the anchor tags
# for tag in all_anchor_tags:
#     print(tag.getText())
# # Print only the URL in each anchor tag
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# # Find a specific h1 using the id
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# # Find a specific h3 using the class
# # "class" is a reserved keyword for Python, so can't use it like id
# # use "class_" instead
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.name)
#
# # Can use CSS selectors to find specific anchor tag
# # "p a" is an anchor tag that sits inside a paragraph tag
# company_url = soup.select_one(selector="p a")
# print(company_url)
# # Can also use class or id as a selector
# name = soup.select_one(selector="#name")
# print(name)
# # select() gives a list, not just the first one
# headings = soup.select(selector=".heading")
# print(headings)
