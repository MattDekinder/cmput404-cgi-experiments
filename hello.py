#!/usr/bin/env python
import os, json, urlparse, sys
from templates import login_page

print 'Content-Type: text/html'
print '\r\n'

print    r"""
    <h1> Welcome! </h1>

    <form method="POST" action="hello.py">
        <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
        <label> <span>Password:</span> <input type="password" name="password"></label>

        <button type="submit"> Login! </button>
    </form>
    """

#if this header is here, then the serve has sent stuff
content_length = os.environ["CONTENT_LENGTH"]
if content_length:
	bytes_to_read = int(content_length)
	content = sys.stdin.read(bytes_to_read)
	print "<pre>"
	print content
	print "</pre>"



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
