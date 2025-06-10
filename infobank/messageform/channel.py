import requests
from infobank.core.channel import (
    _Channel
)

API_VERSION='/v1'

class MessageFormChannel(_Channel)  :
    def __init__(
        self,
        api_url :str
    ):
        self.api_url = api_url + API_VERSION + '/form'
        super().__init__(
            api_url=self.api_url
        )
    
    def get(
        self,
        form_id :str,
        timeout :int
    )-> requests.Response:
        headers = self.headers.dict(
            by_alias=True,
            exclude_none=True
        )
        
        url = self.api_url + '/%s' % form_id
        return requests.get(
            url=url,
            headers=headers,
            timeout=timeout
        )
    
    
    def put(
        self,
        form_id :str,
        body :str,
        timeout :int
    )-> requests.Response:
        headers = self.headers.dict(
            by_alias=True,
            exclude_none=True
        )
        
        url = self.api_url + '/%s' % form_id
        
        return requests.put(
            url= url,
            headers=headers,
            data=body.encode('utf-8'),
            timeout=timeout
        )
        
    def delete(
        self,
        form_id :str,
        timeout :int
    )-> requests.Response:
        headers = self.headers.dict(
            by_alias=True,
            exclude_none=True
        )
        
        url = self.api_url + '/%s' % form_id
        
        return requests.delete(
            url= url,
            headers=headers,
            timeout=timeout
        )