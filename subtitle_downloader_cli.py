import os
import requests
import shutil
import time
from bs4 import BeautifulSoup

base_url = 'https://www.yifysubtitles.com/search?q='
movie_name = input("Enter the movie name:")
movie_name = movie_name.split(' ')
name_len = len(movie_name)
new_url = ''
for i in range(0,name_len):
    if (movie_name[i] == movie_name[name_len-1]):
        new_url = new_url + movie_name[i]
    else:
        new_url = new_url + movie_name[i] + '+'
        
base_url = base_url + new_url
html = requests.get(base_url)
html_content = BeautifulSoup(html.content , 'html.parser')
links = html_content.findAll('a')
movie_links = []
lang_movie_links = []
for i in links:
    if i['href'].startswith('/movie-imdb/'):
        movie_links.append(i['href'])

number = len(movie_links)

for i in range(0,number):
    try:
        movie_links[i] = yify + movie_links.pop(i)
    except:
        pass

if len(movie_links) > 1:
    movie_part_name = input('Enter the Name of the Part:')
    movie_part_name = movie_part_name.split(' ')
    movie_part_name_length = len(movie_part_name)
    new_name = ''
    for i in range(0,movie_part_name_length):
        new_name = new_name + movie_part_name[i] + '-'
    movie_part_name = new_name
        
else:
    movie_part_name = movie_name[0]

lang = int(input('Select the Language of your choice(according to the number): \n 1.English \n 2.Hindi \n 3.Spanish \n 4.Arabic \n 5.Chinese \n 6.Dutch \n 7.Korean \n 8.French \n 9.Italian \n 10.Japanese \n 11.Polish \n 12.Portuguese \n 13.Russian \n 14.Serbian \n 15.Greek \n Enter your choice: '))
languages = ['English',  'Hindi',  'Spanish', 'Arabic', 'Chinese', 'Dutch', 'Korean', 'French', 'Italian', 'Japanese', 'Polish', 'Portuguese', 'Russian', 'Serbian', 'Greek']
lang_str = languages[lang-1]

for i in movie_links:
    html = requests.get(i)
    html_content = BeautifulSoup(html.content , 'html.parser')
    links = html_content.findAll('a')
    for j in links:
            if (lang_str.lower() in j['href']) and (movie_part_name in j['href']) :
                lang_movie_links.append(yify + j['href'])
                lang_not_available = False


if lang_not_available:
    print('Desired language not available \n Try English maybe!')
else:
    try:
        best_subtitle = lang_movie_links[0] + '.zip'
        filename = os.path.basename(best_subtitle)
        print(filename)
        current_path = os.getcwd()
        new_path = os.path.join(current_path , 'files' , filename)
        zip_raw = requests.get(best_subtitle , stream = True)
        with open(new_path , 'wb') as zip_file:
            shutil.copyfileobj(zip_raw.raw , zip_file)
        del zip_raw
        print("Download complete!")
    except:
        print("Movie/File not found!")