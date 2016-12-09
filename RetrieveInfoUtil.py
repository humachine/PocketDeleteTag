import requests
import urlparse

def MakeRequest(method_url, payload):
    r = requests.post(method_url, data=payload)
    return r

def ReadAccessInfo(filename='pocket.apikeys'):
    '''Attempt to read access info from locally saved file.

    Args:
        filename:   str, name of file containing consumer key
    Returns:
        consumer_key: str, consumer key of user
    '''
    print 'Trying to read file'
    try:
        f = open('pocket.apikeys', 'r')
        cons_key = f.readline()
        access_key = f.readline().strip()
        username  = f.readline().strip()
        if access_key == "" or username == "":
            return ""
        return {'access_key': access_key, 'username': username}
    except IOError:
        return ""

def ReadConsumerKey(filename='pocket.apikeys'):
    '''Attempt to read consumer key from locally saved file.

    Args:
        filename:   str, name of file containing consumer key
    Returns:
        consumer_key: str, consumer key of user
    '''
    try:
        f = open('pocket.apikeys', 'r')
        consumer_key = f.readline().strip()
    except IOError:
        consumer_key = 'TESTKEY'
    return consumer_key

def ParseURLEncodedQuery(url_query):
    return urlparse.parse_qs(url_query)

def BuildAccessTokReqURL(url_no_params, request_token, redirect_uri):
    url_no_params = url_no_params.rstrip('?')
    return url_no_params + '?' + 'request_token=' + request_token + '&' + 'redirect_uri=' + redirect_uri

def SaveAccessInfo(access_info, consumer_key, filename='pocket.apikeys'):
    f = open(filename, 'w')
    f.write(consumer_key + '\n')
    f.write(access_info['access_token'] + '\n')
    f.write(access_info['username'] + '\n')
    f.close()
