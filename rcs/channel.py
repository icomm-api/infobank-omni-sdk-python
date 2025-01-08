from infobank.core.channel import (
    _Channel
)

API_VERSION='/v1'

class RCSChannel(_Channel)  :
    def __init__(
        self,
        api_url :str
    ):
        self.api_url = api_url + API_VERSION + '/send/rcs'
        super().__init__(
            api_url=self.api_url
        )
        