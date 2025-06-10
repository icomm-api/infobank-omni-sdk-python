import requests
from infobank.core.channel import (
    _Channel
)
from infobank.core.models import (
    RequestHeaders
)
from infobank.imageupload.models import (
    ImageServiceType,
    ImageMessageType,
    ImageSubType
)

API_VERSION='/v1'

class ImageFileChannel(_Channel):
    def __init__(
        self,
        api_url :str
    ):
        self.api_url = api_url + API_VERSION + '/file'
    
    def set_token(
        self,
        schema :str,
        token:str
    ):
        self.headers = RequestHeaders(
            authorization='%s %s' % (schema, token)
        )
        
    def post(
        self,
        service_type :ImageServiceType,
        message_type : ImageMessageType,
        sub_type : ImageSubType,
        files,
        timeout : int
        ) -> requests.Response:
        
        
        uri = self.api_url + '/%s' % (
            service_type.value
        )
        
        if message_type != None and len(message_type) > 0:
            uri = uri + '/%s' %(message_type.value)
        
        if sub_type != None and len(sub_type) >0:
            uri = uri + '/%s' %(sub_type.value)
            
        headers = self.headers.dict(
            by_alias=True,
            exclude_none=True
        )
        
        return requests.post(
            uri,
            headers=headers,
            files=files,
            timeout=timeout
        )