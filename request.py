import  requests
from bs4 import BeautifulSoup

url = "https://pontuaredacao.com/introducao/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
html = BeautifulSoup(response.text, "html.parser")

planos = html.find_all("h4", class_="my-0")
precos = html.find_all("h1", class_="pricing-card-title")


print("== LISTAGEM DE PREÇOS E PLANOS DA PONTUA REDAÇÃO ==")
for preco, plano in zip(precos, planos): 
        print(plano.getText(strip=True) + " - " + preco.getText(strip=True) )
