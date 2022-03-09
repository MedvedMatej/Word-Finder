from bs4 import BeautifulSoup
import requests

with open("words.txt", "w", encoding="utf-8") as f:
    for i in range(1,4885):
        print(f'Page {i} in progress.')
        url = f'https://fran.si/iskanje?page={i}&FilteredDictionaryIds=133&View=1&Query=*'
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        tags = doc.find_all(["span"], class_="font_xlarge")
        [f.write(tag.text + "\n") for tag in tags if len(tag.text) == 5]