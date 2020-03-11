from get_all_films import get_movies_from_url
import urllib.request
import json
import ssl

#Taken from Omar Einea https://stackoverflow.com/users/4794459/omar-einea
#Here: https://stackoverflow.com/questions/35569042/ssl-certificate-verify-failed-with-python3
#To fix ssl cert verification error
ssl._create_default_https_context = ssl._create_unverified_context

#list_url = 'https://www.imdb.com/list/ls092117658'
#omdb_api_url = "http://www.omdbapi.com/?apikey=35b37e66&i=tt0120338"

#def create_json_file(filename, url):
#	json_file = ""
#	#for records in json_records_list


def main():
	pass
#	print((get_json_from_url(omdb_api_url, 'tt0120338')))


def get_json_from_omdb_api(ID):
	omdb_api_url = "http://www.omdbapi.com/?apikey=35b37e66&i="
	return urllib.request.urlopen(omdb_api_url + ID).read().decode()
	

if __name__ == "__main__":
	main()

