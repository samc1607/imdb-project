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


def get_json_from_omdb_api(imdb_id):
	omdb_api_url = "http://www.omdbapi.com/?apikey=35b37e66&i="
	return urllib.request.urlopen(omdb_api_url + imdb_id).read().decode()
	

def create_json_file(filename, url):
	imdb_id_list = get_movies_from_url(url)
	with open(filename + ".json", "w") as file:
		file.write('{"movies":[')
		first = True;
		for imdb_id in imdb_id_list:
			if(first):
				file.write(get_json_from_omdb_api(imdb_id))
				first = False
			else:
				file.write(', ')	
				file.write(get_json_from_omdb_api(imdb_id))
				
		file.write(']}')

if __name__ == "__main__":
	main()

