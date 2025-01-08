#-*-coding:utf-8-*-
from infobank.core.http_client import (
    HttpClient
)
from infobank.core.channel import(
    validate_url
)

class _InfobankApi:
    token :str = ''
    schema :str = ''
    expired :int = 0
    
    @classmethod
    def __init__ (
        cls,
        api_url :str,
        client_id :str,
        client_passwd:str
    ):
        """Api 초기화
        인포뱅크 비즈플러스에서 발급 받은 계정과 도메인 정보를 넣어서 사용할 수 있습니다.
        
        https://www.ibizplus.co.kr/main

        Args:
            api_url (str): Api 도메인
            
            client_id (str): 아이디
            
            client_passwd (str): 패스워드
        """
        cls.api_url = api_url
        
        validate_url(cls.api_url)
        
        cls.http_client = HttpClient(api_url, client_id, client_passwd)
        
        return
