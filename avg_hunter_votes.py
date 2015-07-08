#!/usr/bin/python
import json, requests, config

def get_user_details(username):
	url = '%s/users/%s' % (config.ph_base_uri, username)
	HEAD = {'Authorization': config.ph_token}
	response = requests.get(url, headers=HEAD)
	response = response.json()
	return {'id_hunter': response['user']['id'], 'posts_count': response['user']['posts_count']}
	
def get_total_votes(username, posts_count):
	url = '%s/users/%s/posts' % (config.ph_base_uri, username)
	PARAMS = { 'order': 'asc'}
	HEAD = {'Authorization': config.ph_token}
	
	i = 0
	total_votes = 0
	
	while posts_count > i:
		if i != 0: PARAMS['newer'] = last_id
		response = requests.get(url, headers=HEAD, data=PARAMS)
		response = response.json()
		
		for post in response['posts']:
			print post['name'], post['votes_count']
			total_votes += post['votes_count']
			last_id = post['id']
			i+=1
	return total_votes
	
def votes_average(posts_count, total_votes):
	return total_votes/posts_count
	
if __name__ == '__main__':
	username = raw_input('Hunter username? ')
	details = get_user_details(username)
	total_votes = get_total_votes( str(details['id_hunter']), details['posts_count'] )
	
	print "==========================="
	print "Details for %s" % username
	print "Nb of posts: %s " % details['posts_count']
	print "Total of upvotes: %s " % total_votes
	print "Average: %s " % votes_average(details['posts_count'], total_votes)

