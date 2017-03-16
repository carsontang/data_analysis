#! /Users/ctang/anaconda/bin/python

from collections import defaultdict

import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import numpy as np
from pattern import web
from dateutil.parser import parse

def get_website_html(url):
	return requests.get(url).text

def get_player_table(html):
	dom = web.Element(html)
	tables = [t for t in dom.by_tag('table')]
	return tables[0]

def parse_player_data(data):
	player_name = data[0].by_tag('a')[0].content.encode('ascii', 'ignore')
	height = data[4].content.encode('ascii', 'ignore')
	return {'name': player_name, 'height': height}

def construct_url(id):
	return 'https://api.airbnb.com/v2/listings/%d?client_id=3092nxybyb0otqw18e8nh5nty&_format=v1_legacy_for_p3' % id

def created_at_timestamp_of(id):
	url = construct_url(id)
	json_str = get_website_html(url)
	user_json = json.loads(json_str)
	created_at_key = unicode('created_at')
	user_key = unicode('listing')
	print user_json
	if user_key not in user_json:
		return (id, 'no listing')
	print user_json[user_key]
	# return (parse(user_json[user_key][created_at_key].encode('ascii', 'ignore')), id)

def main():
	created_at_timestamp_of(100)
"""
	id_range = range(5 * 10**6)
	id_range = id_range[1::100000]
	timestamps_and_ids = [created_at_timestamp_of(id) for id in id_range]
	print "fetched all timestamps"
	timestamps, ids = zip(*timestamps_and_ids)
	plt.plot(np.array(timestamps), np.array(ids))
	plt.xlabel("Year")
	plt.ylabel("# of Registered Users (10 million)")
	plt.title("Airbnb User Growth Rate")
	plt.show()
	"""

"""
	url = construct_url(10**9)
	json_str = get_website_html(url)
	user_json = json.loads(json_str)
	if unicode('error_id') in user_json:
		print 'not available'
	else:
		created_at_key = unicode('created_at')
		user_key = unicode('user')
		print user_json[user_key][created_at_key]
	# print user_json[user_key]
"""

if __name__ == '__main__':
	main()
