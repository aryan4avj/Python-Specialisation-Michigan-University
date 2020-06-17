import urllib.request
from bs4 import BeautifulSoup

# url = 'http://py4e-data.dr-chuck.net/comments_448538.html'
url = input('Enter - ')

fhand = urllib.request.urlopen(url).read()

soup = BeautifulSoup(fhand, 'html.parser')
numbers = soup('span')
counts = 0
counter = 0
for number in numbers:
    counts += int(number.text)
    counter +=1

print('count',counter)
print('Sum',counts)
