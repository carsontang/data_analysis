#! /Users/ctang/anaconda/bin/python

from collections import defaultdict

import pandas as pd
import matplotlib.pyplot as plt
import requests
from pattern import web

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

def main():
	table = get_player_table(get_website_html('http://www.basketball-reference.com/players/a/'))
	headers = table.by_tag('th')
	idx_to_attribute = {}

	for header_idx, header in enumerate(headers):
		attribute = header.content.encode('ascii', 'ignore')
		idx_to_attribute[header_idx] = attribute
	rows = table.by_tag('tr')
	
	player_heights = []
	for row in rows:
		if not row.by_tag('td'):
			continue
		data = row.by_tag('td')
		player_heights.append(parse_player_data(data))
	print player_heights

if __name__ == '__main__':
	main()
