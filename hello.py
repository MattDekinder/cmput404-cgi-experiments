#!/usr/bin/env python
import os, json, urlparse, sys
from templates import login_page

logged_in = False
username = 'matt'
password = 'asdf'
content_length = os.environ["CONTENT_LENGTH"]
cookie = os.environ["HTTP_COOKIE"]
if 'logged-in=True' in cookie:
	logged_in = True

#if this header is here, then the server has sent stuff
elif content_length:
	bytes_to_read = int(content_length)
	content = sys.stdin.read(bytes_to_read)

	params=  urlparse.parse_qs(content)
	if params['username'][0]==username and params['password'][0]==password:
		print 'Set-Cookie: logged-in=True'
		logged_in = True


print 'Content-Type: text/html'
print '\r\n'

if not logged_in:
	print    r"""
		<h1> Welcome! </h1>

		<form method="POST" action="hello.py">
		    <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
		    <label> <span>Password:</span> <input type="password" name="password"></label>

		    <button type="submit"> Login! </button>
		</form>
		"""

if logged_in:
	print "hello"


#print urlparse.parse_qs(os.environ['QUERY_STRING'])

#user_agent = os.environ['HTTP_USER_AGENT']
#if 'Firefox' in user_agent:
#	print 'Firefox'
#elif 'Chrome' in user_agent:
#	print 'Chrome'
#elif 'Curl' in user_agent:
#	print 'curl'
#else:
#	print user_agent


#print json.dumps(dict(os.environ))
