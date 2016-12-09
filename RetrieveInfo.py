import RetrieveInfoUtil as RetInfUtil
import webbrowser

CONSUMER_KEY = RetInfUtil.ReadConsumerKey()
REQ_TOK_METHOD_URL = 'https://getpocket.com/v3/oauth/request'
REDIRECT_URI = 'http://www.google.com' #Change to application if using web application
AUTHORIZE_REQ_URL = 'https://getpocket.com/auth/authorize?'
ACCESS_TOK_REQ_URL = 'https://getpocket.com/v3/oauth/authorize'

class PocketURLs:
    RetrieveURL = "https://getpocket.com/v3/get"
    AddURL = "https://getpocket.com/v3/add"
    ModifyURL = "https://getpocket.com/v3/send"

def ObtainNewAccessToken(access_info_filename=''):
    #Obtain a request token from Pocket
    payload= {'consumer_key':CONSUMER_KEY, 'redirect_uri':REDIRECT_URI}
    r = RetInfUtil.MakeRequest(REQ_TOK_METHOD_URL, payload)
    REQUEST_TOKEN = RetInfUtil.ParseURLEncodedQuery(r.text)['code'][0]

    #Generate Access Token Request URL. The URL directs users to a page where they can authenticate the app
    auth_req_url = RetInfUtil.BuildAccessTokReqURL(AUTHORIZE_REQ_URL, REQUEST_TOKEN, REDIRECT_URI)
    print auth_req_url
    webbrowser.open(auth_req_url, new=2)
    raw_input('\nPress ENTER once you complete authorizing application ')

    #Convert Request token to Access Token
    payload = {'consumer_key': CONSUMER_KEY, 'code': REQUEST_TOKEN}
    r = RetInfUtil.MakeRequest(ACCESS_TOK_REQ_URL, payload)

    ACCESS_INFO = RetInfUtil.ParseURLEncodedQuery(r.text)
    ACCESS_INFO = {x: ACCESS_INFO[x][0] for x in ACCESS_INFO}

    if access_info_filename!='':
        RetInfUtil.SaveAccessInfo(ACCESS_INFO, CONSUMER_KEY, access_info_filename)
    RetInfUtil.SaveAccessInfo(ACCESS_INFO, CONSUMER_KEY)
    return ACCESS_INFO

def GetListOfArticles(access_info, params={}):
    payload = access_info
    params = {}
    # params = {'count': 10}
    payload.update(params)
    print payload

    r = RetInfUtil.MakeRequest(PocketURLs.RetrieveURL, payload)
    print r.content
    return ""

def BuildTagParams(tagname, detailType='simple'):
    return {'tag': tagname, 'detailType': detailType}

def main():
    ACCESS_INFO = RetInfUtil.ReadAccessInfo()
    if ACCESS_INFO == '':
        ACCESS_INFO = ObtainNewAccessToken()
    TAG_TO_DELETE = 'verge'
    article_list = GetListOfArticles(ACCESS_INFO, BuildTagParams(TAG_TO_DELETE))

main()

