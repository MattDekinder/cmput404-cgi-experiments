#!/usr/bin/env python
import os, json, urlparse
print 'Content-Type: application/json'
print '\r\n'
print urlparse.parse_qs(os.environ['QUERY_STRING'])

user_agent = os.environ['HTTP_USER_AGENT']
if 'Firefox' in user_agent:
	print 'Firefox'
elif 'Chrome' in user_agent:
	print 'Chrome'
elif 'Curl' in user_agent:
	print 'curl'
else:
	print user_agent


#print json.dumps(dict(os.environ))
