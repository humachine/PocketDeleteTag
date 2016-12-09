from urlparse import urlparse, parse_qs
def ReadConsumerKey(filename='pocket.apikeys'):
    """Attempt to read consumer key from locally saved file.

    Args:
        filename:   str, name of file containing consumer key
    Returns:
        consumer_key: str, consumer key of user
    """
    try:
        f = open("pocket.apikeys", "r")
        consumer_key = f.read().strip()
    except IOError:
        consumer_key = "TESTKEY"
    return consumer_key

def GetRequestTokenFromResponse(response):
    """Split response and obtain the request token.

    Args:
        response: str, string containing HTTP response of request token request.
    Returns:
        request_token: str, request token retrieved from response.
    """
    contents = response.split('=')
    if len(contents) <= 1:
        raise IOError
    request_token = contents[1]
    return request_token

def ParseURLEncodedToDict(url):
    return parse_qs(urlparse(url).query)

def BuildAccessTokReqURL(url_no_params, request_token, redirect_uri):
    url_no_params = url_no_params.rstrip('?')
    return url_no_params + "?" + "request_token=" + request_token + "&" + "redirect_uri=" + redirect_uri
