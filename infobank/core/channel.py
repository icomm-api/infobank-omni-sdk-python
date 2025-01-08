import requests
import re
from infobank.core.models import (
    RequestHeaders,
)
from infobank.core.exceptions import (
    InfobankException
)

API_VERSION='/v1'

def validate_url(url: str):
    REGEX_URL = r'^(http|https)://'
    if not re.match(REGEX_URL, url):
        raise InfobankException("invalid Url : " + url)

class _Channel:
    api_url: str
    schema :str
    token :str
    
    def __init__(self):
        pass
        
    def __init__(
        self,
        api_url :str
    ):
        self.api_url = api_url
        
    def set_token(
        self,
        schema :str,
        token:str
    ):
        self.headers = RequestHeaders(
            authorization='%s %s' % (schema, token),
            content_type= "application/json"
        )
        
    def post(
        self,
        body :str,
        timeout : int
        ) -> requests.Response:
        
        headers = self.headers.dict(
            by_alias=True,
            exclude_none=True
        )
        
        return requests.post(
            self.api_url,
            headers=headers,
            data=body.encode('utf-8'),
            timeout=timeout
        )

class AuthChannel(_Channel):
    def __init__(
        self,
        api_url :str,
        client_id :str,
        client_passwd :str
    ):
        self.api_url = api_url + API_VERSION + '/auth/token'
        self.client_id = client_id
        self.client_passwd = client_passwd
    
    def post(
        self,
        timeout : int
        ) -> requests.Response:
        
        request_headers = RequestHeaders(
            X_IB_Client_Id= self.client_id,
            X_IB_Client_Passwd= self.client_passwd
        )
        
        headers = request_headers.dict(
            by_alias=True,
            exclude_none=True
        )
        
        return requests.post(
            self.api_url,
            headers=headers,
            timeout=timeout
        )
