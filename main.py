import requests
from bs4 import BeautifulSoup
import sys

def get_definition(word, max_count):
    url = f"https://dexonline.ro/definitie/{word}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Nu s-a putut accesa pagina pentru cuvântul {word}.")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    header_sections = soup.findAll('h3', class_='tree-heading')
    definition_sections = soup.findAll('div', class_='tree-body')
    
    if (not header_sections) or (not definition_sections):
        print(f"Nu s-a găsit nicio definiție pentru cuvântul {word}.")
        return
    
    def_counter = 0
    for header in header_sections:
        if(def_counter >= max_count):
            return
        definition = definition_sections[def_counter]
        def_counter += 1

        header_text = header.get_text(strip=True)
        print(f'{def_counter}. {header_text}')
        
        content = definition.find_all('span', class_='def html')
        tab = "  "

        if content:
            for c in content:
                text = c.get_text(strip=True)
                print(f'{tab} - {text}')
        print()

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Utilizare: python script.py <cuvant> <optional: numar maxim definitii (default 3)>")
        sys.exit(1)
    
    word = sys.argv[1]
    
    if(len(sys.argv) == 3):
        max_count = int(sys.argv[2])
    else:
        max_count = 3
    get_definition(word, max_count)
