import pytest
import json
from get_film_data import *
import filecmp
import os


url = 'http://www.omdbapi.com/?apikey=35b37e66&i='
test_list_url = 'https://www.imdb.com/list/ls092117658'
imdb_id = 'tt0120338'
test_json = '{"Title":"Titanic","Year":"1997","Rated":"PG-13",'\
			'"Released":"19 Dec 1997","Runtime":"194 min","Gen'\
			're":"Drama, Romance","Director":"James Cameron","'\
			'Writer":"James Cameron","Actors":"Leonardo DiCapr'\
			'io, Kate Winslet, Billy Zane, Kathy Bates","Plot"'\
			':"A seventeen-year-old aristocrat falls in love w'\
			'ith a kind but poor artist aboard the luxurious, '\
			'ill-fated R.M.S. Titanic.","Language":"English, S'\
			'wedish, Italian","Country":"USA","Awards":"Won 11'\
			' Oscars. Another 114 wins & 83 nominations.","Pos'\
			'ter":"https://m.media-amazon.com/images/M/MV5BMDd'\
			'mZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEy'\
			'XkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg","Ratings"'\
			':[{"Source":"Internet Movie Database","Value":"7.'\
			'8/10"},{"Source":"Rotten Tomatoes","Value":"89%"}'\
			',{"Source":"Metacritic","Value":"75/100"}],"Metas'\
			'core":"75","imdbRating":"7.8","imdbVotes":"993,20'\
			'2","imdbID":"tt0120338","Type":"movie","DVD":"10 '\
			'Sep 2012","BoxOffice":"N/A","Production":"Paramou'\
			'nt Pictures","Website":"N/A","Response":"True"}'

#def test_create_json_file():
#	create_json_file('created_json_file', url)
#	assert filecmp.cmp('test_json_file.json', 'created_json_file.json', shallow=False)

def test_get_json_from_omdb_api():
	assert get_json_from_omdb_api(imdb_id) == test_json

def test_create_json_file():
	create_json_file('test_file', test_list_url)
	assert filecmp.cmp('test_file.json', 'validation_file.json',shallow=False)
	os.remove('test_file.json')
