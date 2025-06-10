from infobank.core.channel import(
    _Channel
)

API_VERSION='/v1'

class AlimTalkChannel(_Channel)  :
    def __init__(
        self,
        api_url :str
    ):
        self.api_url = api_url + API_VERSION + '/send/alimtalk'
        super().__init__(
            api_url=self.api_url
        )

class FriendTalkChannel(_Channel)  :
    def __init__(
        self,
        api_url :str
    ):
        self.api_url = api_url + API_VERSION + '/send/friendtalk'
        super().__init__(
            api_url= self.api_url
        )
        
class BrandMessageChannel(_Channel)  :
    def __init__(
        self,
        api_url :str
    ):
        self.api_url = api_url + API_VERSION + '/send/brandmessage'
        super().__init__(
            api_url= self.api_url
        )