from flask import Flask, render_template, request,jsonify
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def homepage():
    return render_template("index.html")

@app.route("/images" , methods = ['POST' , 'GET'])
def index():
    if request.method == 'POST':
                try:
                    query = request.form.get('content')
                    print(query)
                    directory = query
                    if not os.path.exists(directory):
                        os.makedirs(directory)
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
                    j=0
                    for i in urls:
                        data=requests.get(i).content
                        print(data)
                        with open(os.path.join(directory, f"{query}_{j}.jpg"), "wb") as f:
                            f.write(data)
                            j+=1
                except Exception as e:
                      print(e)
                return render_template('result.html',query=query)

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='1430')
