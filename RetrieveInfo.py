import requests
import RetrieveInfoUtil as RetInfUtil

CONSUMER_KEY = RetInfUtil.ReadConsumerKey()
REQ_TOK_METHOD_URL = "https://getpocket.com/v3/oauth/request"
# REDIRECT_URI = "tagDelete:authorizationFinished" TODO
REDIRECT_URI = "http://www.google.com"
AUTHORIZE_REQ_URL = "https://getpocket.com/auth/authorize?"
ACCESS_TOK_REQ_URL = "https://getpocket.com/v3/oauth/authorize"

def BuildPayload(consumer_key, redirect_uri):
    """Build Payload from Consumer Key & Redirect URL/Code"""
    payload= {"consumer_key":consumer_key,
            "redirect_uri":redirect_uri}
    return payload

def MakeRequest(method_url, payload):
    r = requests.post(method_url, data=payload)
    return r

#Obtain a request token from Pocket
r = MakeRequest(REQ_TOK_METHOD_URL, BuildPayload(CONSUMER_KEY, REDIRECT_URI))
REQUEST_TOKEN = RetInfUtil.GetRequestTokenFromResponse(r.text)

#Generate Access Token Request URL. The URL directs users to a page where they can authenticate the app
auth_req_url = RetInfUtil.BuildAccessTokReqURL(AUTHORIZE_REQ_URL, REQUEST_TOKEN, REDIRECT_URI)
print auth_req_url
raw_input("Authenticated? ")

#Convert Request token to Access Token
payload = {'consumer_key': CONSUMER_KEY, 'code': REQUEST_TOKEN}
r = MakeRequest(ACCESS_TOK_REQ_URL, payload)
print r.text

#access_token=3c8b5ba3-58e8-fead-92d2-3427fb&username=humachine

