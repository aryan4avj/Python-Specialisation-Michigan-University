from requests import get
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_448538.html'

response = get(url)
# print(response.text[:500])

html_soup = BeautifulSoup(response.text, 'html.parser')

numbers = html_soup('span')
counts = 0
for number in numbers:
    counts += int(number.text)

print(counts)