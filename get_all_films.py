from requests import get
from bs4 import BeautifulSoup
import re
import math

url = ('https://www.imdb.com/user/ur51298763/ratings?sort=date_'\
		'added%2Cdesc&mode=detail&paginationKey=mfq5ijak6z7uymj'\
		'wuuwsomnsegl34knnqsdztp6xeepepyyfxdfiwpol52uhtjimq3iwc'\
		'lnm7gq7uk2y4kjyc3qnmn3dio7t7rbxu5m47iyfrvleknv4axfhhxu'\
		'djs5nyx6ixac3qfdajjg6bqac2wheaznk2ouqhjumdq6vdrv2pd4x3'\
		'rats7f7appdrvwvo4p2yvgwhiztfo3u6u&lastPosition=0')

def main():
	pass


def round_down_nearest_100(number):
	number = math.floor(number/100.0)*100
	return number


def find_upper_bound(number):
	if number != 0:
		if number % 100 == 0:
			number -= 100
	number = round_down_nearest_100(number)
	return number


def get_soup(url):
	response = get(url)
	return BeautifulSoup(response.text, 'html.parser')


def is_ratings(url):
	return 'ratings' in url


def get_movie_ids_from_page(soup):
	movie_ids = []
	movies = soup.find_all('div', class_ = 'lister-item-image ribbonize')
	for movie in movies:
		movie_ids.append(movie['data-tconst'])
	return movie_ids


def get_total_number_of_movies(soup, ratings):
	if ratings:
		total_number_of_films = soup.find('span', id = 'lister-header-current-size')
	else:
		total_number_of_films = soup.find('div', class_ = 'desc lister-total-num-results')
	return int(re.sub("[^0-9]", "", total_number_of_films.text))


if __name__== "__main__":
  main()

