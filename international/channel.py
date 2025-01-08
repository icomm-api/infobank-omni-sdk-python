from infobank.core.channel import (
    _Channel
)

API_VERSION='/v1'

class InterSMSChannel(_Channel):
    def __init__(
        self,
        api_url :str
    ):
        self.api_url = api_url + API_VERSION + '/send/international'
        super().__init__(
            api_url=self.api_url
        )