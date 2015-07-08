#!/usr/bin/python
import json, requests, datetime, time, os, config

def retrieve_votes(product_id):
	HEAD = {'Authorization': config.ph_token}
	URL_POST_DETAILS = '%s/posts/%s' % (config.ph_base_uri, id)
	
	response = requests.get(URL_POST_DETAILS, headers=HEAD)
	response = response.json()
	product_name = response['post']['name'].replace(' ','_').lower()
	votes_count = response['post']['votes_count']
	
	print "Votes Count: %s" % votes_count
	
	URL_VOTES = '%s/posts/%s/votes' % (config.ph_base_uri, id)
	PARAMS = {'order': 'asc'}
	
	nb_vote = 0
	nb_page = 0
	last_id = ""
	votes = []
		
	while nb_vote < votes_count:
		if nb_page != 0: PARAMS['newer'] = last_id
		response = requests.get(URL_VOTES, headers=HEAD, data=PARAMS)
		response = response.json()
			
		for vote in response['votes']:
			nb_vote+=1			
			
			date = vote['created_at']
			year = int(date[:4])
			month = int(date[5:7])
			day = int(date[8:10])
			hour = int(date[11:13])
			minute = int(date[14:16])
			second = int(date[17:19])
			date = datetime.datetime(year, month, day, hour, minute, second)
			timestamp = time.mktime(date.timetuple())
				
			data = {
				'created_at'	:	timestamp,
				'nb_vote'		: 	nb_vote,
				'id_vote'		:	vote['id'],
				'username'		:	vote['user']['username']
			}
				
			votes.append(data)
			last_id = vote['id']
			
			print nb_vote, data['username']
		nb_page+=1
	print "All votes were downloaded"
	return votes
	
def get_name(id):
	HEAD = {'Authorization': config.ph_token}
	URL_POST_DETAILS = '%s/posts/%s' % (config.ph_base_uri, id)
	response = requests.get(URL_POST_DETAILS, headers=HEAD)
	response = response.json()
	return response['post']['name'].replace(' ','_').lower()
	
def export_to_json(data):
	product_name = get_name(id)
	with open('samples/votes_%s_%s.json' % (id, product_name), 'w') as outfile:
		json.dump(data, outfile, indent=4, separators=(',', ':'))	
	print "Export to 'samples/votes_%s_%s.json'" % (id, product_name)

if __name__ == '__main__':
	id = raw_input("ID of your product? ")
	votes = retrieve_votes(id)
	export_to_json(votes)
	
