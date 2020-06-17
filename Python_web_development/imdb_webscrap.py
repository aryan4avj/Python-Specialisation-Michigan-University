
#Tutorial from the site given below.
#https://www.dataquest.io/blog/web-scraping-beautifulsoup/

import re
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'


response = get(url)
# print(response.text[:500])    #printing the html code of the webpage
html_soup = BeautifulSoup(response.text, 'html.parser')
headers = {"Accept-Language": "en-US, en;q=0.5"}
# print(type(html_soup))    

movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')

#********************accessing data of first container************************

# # print(type(movie_containers))
# # print(len(movie_containers))  
# # print(movie_containers[0])    #to access data of single movie

# first_movie = movie_containers[0]

# # print(first_movie.div)      #accessing the data in first tag
# # print(first_movie.h3.a)     #accessing the first <a> inside the <h3> tag

# first_name = first_movie.h3.a.text
# print(first_name)

# # first_year = first_movie.h3.span.text     #this will give the the first span of div class above.
# # print(first_year)

# first_year = first_movie.h3.find('span', class_ ='lister-item-year text-muted unbold')
# first_year = first_year.text
# print(first_year)
# # y = re.findall('[0-9]+',first_year)       #without brackets
# # print(y)

# first_rating = float(first_movie.strong.text)
# print(first_rating)

# first_metascore = first_movie.find('span', class_ ='metascore favorable')
# first_metascore = int(first_metascore.text)
# print(first_metascore)

# first_votes = first_movie.find('span', attrs = {'name':'nv'})
# first_votes = first_votes['data-value']
# print(first_votes)

# # eighth_movie_mscore = movie_containers[7].find('div', class_ = 'ratings-metascore')
# # print(type(eighth_movie_mscore))

#*****************************end**********************************

#list to store scrapped data
names =[]
years =[]
imdb_ratings = []
metascores = []
votes =[]

#extracting data from movie containers

for container in movie_containers:
    #if movie has metascore, then extract
    if container.find('div', class_ ='ratings-metascore') is not None:
        
        #names
        name = container.h3.a.text
        names.append(name)

        #years
        year = container.h3.find('span', class_ ='lister-item-year').text
        years.append(year)

        #imdb
        imdb_rating = container.strong.text
        imdb_ratings.append(imdb_rating)

        #metascore

        metascore = container.find('span', class_ ='metascore').text
        metascores.append(int(metascore))

        #votes

        vote = container.find('span', attrs = {'name':'nv'})['data-value']
        votes.append(int(vote))


#checking the data collected
test_df =pd.DataFrame(
    {
    'movie' : names,
    'year' : years,
    'imdb_rating' : imdb_ratings,
    'metascore' : metascores,
    'votes' : votes
})

print(test_df.info())
print(test_df)