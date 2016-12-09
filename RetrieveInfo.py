import requests
import RetrieveInfoUtil as RetInfUtil

CONSUMER_KEY = RetInfUtil.ReadConsumerKey()
print CONSUMER_KEY

def BuildPayload(consumer_key, redirect_uri):
    """Build Payload from Consumer Key & Redirect URL"""
    payload= {"consumer_key":consumer_key,
            "redirect_uri":redirect_uri}
    return payload

def MakeRequest(method_url, payload):
    r = requests.post(method_url, data=payload)
    return r

    # https://getpocket.com/v3/oauth/request

REQUEST_TOKEN_METHOD_URL="https://getpocket.com/v3/oauth/request"
REDIRECT_URI = "tagDelete:authorizationFinished"
r = MakeRequest(REQUEST_TOKEN_METHOD_URL, BuildPayload(CONSUMER_KEY, REDIRECT_URI))
print RetInfUtil.GetRequestTokenFromResponse(r.text)
