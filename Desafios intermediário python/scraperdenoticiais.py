import requests
from bs4 import BeautifulSoup
import pandas as pd

# Requisição para o site de notícias
url = "https://news.ycombinator.com/"
response = requests.get(url)

# Parsear o HTML com BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extrair títulos das notícias
titles = [title.text for title in soup.find_all(class_='storylink')]

# Armazenar os dados em um DataFrame
df = pd.DataFrame({
    'Título': titles
})

# Salvar em um arquivo CSV
df.to_csv('noticias.csv', index=False)

#como rodar: python scraper_noticias.py
