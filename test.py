import requests
from bs4 import BeautifulSoup
query='kohli'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
response = requests.get(f"https://www.google.com/search?q={query}&sxsrf=AJOqlzUuff1RXi2mm8I_OqOwT9VjfIDL7w:1676996143273&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiq-qK7gaf9AhXUgVYBHYReAfYQ_AUoA3oECAEQBQ&biw=1920&bih=937&dpr=1#imgrc=1th7VhSesfMJ4M")
soup = BeautifulSoup(response.content, "html.parser")
imgs = soup.find_all("img")
del imgs[0]
urls=[]
for i in imgs:
        url=i.get('src')
        print(url)
        urls.append(url)
for i in urls:
        data=requests.get(i).content
        print(data)