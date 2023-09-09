import urllib.request
import re
from bs4 import BeautifulSoup

# from setuptools.sandbox import save_path
from download_image import download_png_image

url = 'https://genshin.gg/'

# Set a generic User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.1234.5678 Safari/537.36'
}

req = urllib.request.Request(url, headers=headers)

try:
    page = urllib.request.urlopen(req)
    page_soup = BeautifulSoup(page, 'html.parser')
    image_item = page_soup.find('div', {'class': 'character-list'})

    for image in image_item.find_all('img'):
        image_src = image.get('src')
        image_name = image.get('alt')

        pattern = re.compile(r'/Characters/')
        character_urls = []
        if pattern.search(image_src):
            character_urls.append(image_src)
            # print(character_urls)



        # save_path = 'C:/Users/lsj90/Documents/my_project/downloaded_image.png'
        # download_png_image(image_src, save_path)

#         img_file = open(image_name + '.png', 'wb')
#         request_urlopen = urllib.request.urlopen(image_src)
#         imageReadIn = request_urlopen.read()
#         img_file.write(imageReadIn)
#         img_file.close()
except urllib.error.HTTPError as e:
    print(e)

# def url_filter(url_path):
#     with open('urlsgenshin.txt', mode='wb') as file:

# pattern = re.compile(r'/Characters/')
#
# # Initialize an empty list to store character URLs
# character_urls = []
#
# # Iterate through the URLs and filter the character URLs
# for url in image_src:
#     if pattern.search(url):
#         character_urls.append(url)
#
# # Print the filtered character URLs
# for character_url in character_urls:
#     print(character_url)
