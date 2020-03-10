import pytest
from requests import get
from get_all_films import *
import os.path

#All URLs
imdb_url = "https://www.imdb.com/"
test_list_url = 'https://www.imdb.com/list/ls092117658'
ratings_url = 'https://www.imdb.com/user/ur51298763/ratings'
rating_next_url = 'https://www.imdb.com/user/ur51298763/ratings?sort='\
					'date_added%2Cdesc&mode=detail&paginationKey=mfq5'\
					'ijak6z7uymjwuuwsomnsegl34knnqsdztp6xeepepyyfxdfi'\
					'wpol52uhtjimq3iwclnm7gq7uk2y4kjyayykmnytcmxy6rdx'\
					'y4447iyfrvleknv4axfhhxudjs5nyx7yfaczqzbr564pajlx'\
					'uqffl4f7yiuinvqyrr6wc5vkrduszupds7ann5wibi674uhs'\
					'm3nia3ly7bqr&lastPosition=100'
ids = ['tt1675434', 'tt0482571', 'tt0055928']

#Tests whether imdb is up and the connection works
def test_connection_to_imdb():
	assert get(imdb_url).status_code == 200
	
def test_get_movie_ids_from_page():
	assert get_movie_ids_from_page(get_soup(test_list_url)) == ids

def test_get_next_page_url():
	assert get_next_page_url(get_soup(ratings_url)) == rating_next_url

def test_is_there_next_page_yes():
	assert is_there_next_page(get_soup(ratings_url)) == True

def test_is_there_next_page_no():
	assert is_there_next_page(get_soup(test_list_url)) == False

def test_get_movies_from_url():
	assert get_movies_from_url(test_list_url) == ids	

