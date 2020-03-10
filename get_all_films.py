from requests import get
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import re
import math
import csv


imdb_url = 'https://www.imdb.com'
#url = 'https://www.imdb.com/user/ur51298763/ratings'


def get_movies_from_url(url):
	movie_ids = []
	soup = get_soup(url)
	movie_ids.extend(get_movie_ids_from_page(soup))
	while is_there_next_page(soup):
		soup = get_soup(get_next_page_url(soup))
		movie_ids.extend(get_movie_ids_from_page(soup))
	return movie_ids


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


def get_next_page_url(soup):
	return imdb_url + soup.find('a', class_ = 'flat-button lister-page-next next-page')['href']


def is_there_next_page(soup):
	if soup.find('a', class_ = 'flat-button lister-page-next next-page') is not None:
		return True
	else:
		return False

