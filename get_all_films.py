from requests import get
from bs4 import BeautifulSoup
from time import sleep
from random import randint


imdb_url = 'https://www.imdb.com'


#Gets all the movie IDs from imdb lists/ratings
#Returns a list of all IDs
def get_movies_from_url(url):
	movie_ids = []
	soup = get_soup(url)
	movie_ids.extend(get_movie_ids_from_page(soup))
	while is_there_next_page(soup):
		soup = get_soup(get_next_page_url(soup))
		movie_ids.extend(get_movie_ids_from_page(soup))
		sleep(randint(1,3))
	return movie_ids


#Gets the Beautiful Soup of the page at url
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


#Gets the url for the next page
def get_next_page_url(soup):
	return imdb_url + soup.find('a', class_ = 'flat-button lister-page-next next-page')['href']


#Checks whether the list has another page or not
def is_there_next_page(soup):
	if soup.find('a', class_ = 'flat-button lister-page-next next-page') is not None:
		return True
	else:
		return False

