import requests

from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)

soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_="news-title")
matn = ""
for n in news:
    matn += n.text

# kerakmas so'zlar
stopwords = ["учун", "бўйича", "лекин", "билан", "ва", "бор", "ҳам", "хил", "йил"]
# bulutni yaratamiz
wordcloud = WordCloud(width=1000, height=1000,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=20).generate(matn)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()