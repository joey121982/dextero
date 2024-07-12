import requests
from bs4 import BeautifulSoup
import sys

def get_definition(word, max_count):
    url = f"https://dexonline.ro/definitie/{word}/definitii"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Nu s-a putut accesa pagina pentru cuvântul {word}.\n(lipsește definiția?)")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    dexdef = soup.find_all('span', class_="def")
    
    if not dexdef:
        print(f"Nu s-a găsit nicio definiție pentru cuvântul {word}.")
        return
    
    dexdef = list(dict.fromkeys(dexdef)) # remove duplicate entries
    
    for index, definition in enumerate(dexdef):
        if(index >= max_count): break
        print(f"{index + 1}. - {definition.get_text()}\n")

    print(f"Sursă: {url}")
        
def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("usage: 'dextero <cuvânt> <opțional: număr maxim definiții (default: 3)>'")
        sys.exit(1)
    
    word = sys.argv[1]
    
    if len(sys.argv) == 3:
        max_count = int(sys.argv[2])
    else:
        max_count = 3
    
    get_definition(word, max_count)
