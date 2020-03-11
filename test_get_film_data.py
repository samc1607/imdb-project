import pytest
import json
from get_film_data import *


test_json_record_1 = '{"test":"test value","total":"1"}'
test_json_record_2 = '{"test":"value test","total":"2"}'
test_json = '{"Tag":[' + test_json_record_1 + ',' + test_json_record_2 + ']}'
json_records = [test_json_record_1, test_json_record_2]

def test_create_json_file():
	assert create_json_file(json_records) == json.loads(test_json)