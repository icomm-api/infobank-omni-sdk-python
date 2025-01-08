import requests
from infobank.core.channel import (
    _Channel
)

API_VERSION='/v1'

class ReportChannel(_Channel):
    def __init__(
        self,
        api_url :str,
    ):
        self.api_url = api_url + API_VERSION + '/report'
        super().__init__(
            api_url=self.api_url
        )

    def get(
        self,
        timeout :int
    ) -> requests.Response:
        
        headers = self.headers.dict(
            by_alias=True,
            exclude_none=True
        )
        
        return requests.get(
            url=self.api_url,
            headers=headers,
            timeout=timeout
        )
        
    def delete(
        self,
        report_id :str,
        timeout: int
    ) -> requests.Response:
        headers = self.headers.dict(
            by_alias=True,
            exclude_none=True
        )
        
        uri = self.api_url + "/%s" %(
            report_id
        )
        
        return requests.delete(
            url= uri,
            headers= headers,
            timeout= timeout
        )