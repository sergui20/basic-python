import requests
from bs4 import BeautifulSoup
import urllib

def main():
    for i in range(1, 6):
        response = requests.get('https://xkcd.com/{}'.format(i))
        soup = BeautifulSoup(response.content, 'html.parser')
        image_container = soup.find(id = 'comic')

        image_url = image_container.find('img')['src']
        image_name = image_url.split('/')[-1]
        print('Descargando la imagen {}'.format(image_name))

        # For saving the images in my directory with the original name. I added https because the url doesnt have it
        urllib.urlretrieve('https:{}'.format(image_url), image_name)

if __name__ == "__main__":
    main()