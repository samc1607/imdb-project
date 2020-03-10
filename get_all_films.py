from requests import get
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import re
import math

imdb_url = 'https://www.imdb.com'
url = 'https://www.imdb.com/user/ur51298763/ratings'

def main():
	pass
	#movie_ids = []
	#soup = get_soup(url + '0')
	#total = get_total_number_of_movies(soup, is_ratings(url))
	#movie_ids.extend(get_movie_ids_from_page(soup))
	#if total > 100:
	#	for i in range(100, total, 100):
	#		movie_ids.extend(get_movie_ids_from_page(get_soup(url + str(i))))
	#		sleep(randint(1,3))
	#print(movie_ids)

def get_soup(url):
	response = get(url)
	return BeautifulSoup(response.text, 'html.parser')

#Gets all the movie ids from a specific imdb page
def get_movie_ids_from_page(soup):
	movie_ids = []
	movies = soup.find_all('div', class_ = 'lister-item-image ribbonize')
	for movie in movies:
		movie_ids.append(movie['data-tconst'])
	return movie_ids

#Gets the total number of movies in a list/ratings page
#def get_total_number_of_movies(soup, ratings):
#	if ratings:
#		total_number_of_films = soup.find('span', id = 'lister-header-current-size')
#	else:
#		total_number_of_films = soup.find('div', class_ = 'desc lister-total-num-results')
#	return int(re.sub("[^0-9]", "", total_number_of_films.text))

def get_next_page_url(soup):
	return imdb_url + soup.find('a', class_ = 'flat-button lister-page-next next-page')['href']

def is_there_next_page(soup):
	if soup.find('a', class_ = 'flat-button lister-page-next next-page') is not None:
		return True
	else:
		return False

if __name__== "__main__":
  main()

