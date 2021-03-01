import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success! Response = {response.status_code}')
        # print(f'Content {response.text}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'Hasil Pemanggilan {url}')
        print(f'Title: {soup.title.string}')
    else:
        print(f'There is a requests error {requests.status_code}')
except Exception as e:
    print(f'An error has occurred {e}')
print('Program ended')

