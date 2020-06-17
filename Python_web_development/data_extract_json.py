import urllib.request, urllib.parse, urllib.error
import json

#example link- http://py4e-data.dr-chuck.net/comments_448541.json

while True:
    url = input('Enter location: ')
    if len(url) < 1:
        break
    
    print('Retrieving http:',url)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    print('Retrieved', len(data), 'characters')
    info = json.loads(data)

    count = 0
    sum_ = 0
    
    for item in info['comments']:
        sum_ +=  int(item['count'])
        count += 1
    print('Count: ' ,count)
    print('Sum: ',sum_)
