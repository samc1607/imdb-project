import pytest
from requests import get
from get_all_films import *

#All URLs
imdb_url = "https://www.imdb.com/"
test_list_url = 'https://www.imdb.com/list/ls092117658/'
big_test_list_url = 'https://www.imdb.com/list/ls002448041/?sort=list'\
					'_order,asc&st_dt=&mode=detail&page=1'
ratings_url = ('https://www.imdb.com/user/ur51298763/ratings?sort=date_'\
				'added%2Cdesc&mode=detail&paginationKey=mfq5ijak6z7uymj'\
				'wuuwsomnsegl34knnqsdztp6xeepepyyfxdfiwpol52uhtjimq3iwc'\
				'lnm7gq7uk2y4kjyc3qnmn3dio7t7rbxu5m47iyfrvleknv4axfhhxu'\
				'djs5nyx6ixac3qfdajjg6bqac2wheaznk2ouqhjumdq6vdrv2pd4x3'\
				'rats7f7appdrvwvo4p2yvgwhiztfo3u6u&lastPosition=0')
#Tests whether imdb is up and the connection works
def test_connection_to_imdb():
	assert get(imdb_url).status_code == 200
	
def test_round_down_nearest_100_243():
	assert round_down_nearest_100(243) == 200

def test_find_upper_bound(): 
	assert find_upper_bound(1504) == 1500

def test_find_upper_bound_no_film():
	assert find_upper_bound(0) == 0

def test_find_upper_bound_exact_100():
	assert find_upper_bound(1500) == 1400

def test_get_movie_ids_from_page():
	ids = ['tt1675434', 'tt0482571', 'tt0055928']
	assert get_movie_ids_from_page(get_soup(test_list_url)) == ids

def test_get_total_number_of_movies_in_list():
	assert get_total_number_of_movies(get_soup(test_list_url), is_ratings(test_list_url)) == 3

def test_get_total_number_of_movies_in_list_when_more_than_999():
	assert get_total_number_of_movies(get_soup(big_test_list_url), is_ratings(big_test_list_url)) == 1012

def test_is_ratings_negative():
	assert is_ratings(test_list_url) == False

def test_is_ratings_positive():
	assert is_ratings(ratings_url) == True

def test_get_total_number_of_movies_in_ratings():
	assert get_total_number_of_movies(get_soup(ratings_url), is_ratings(ratings_url)) == 1504
