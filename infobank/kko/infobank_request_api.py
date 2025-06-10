from infobank.core.infobank_request_api import (
    _InfobankApi
)

class KkoApi (_InfobankApi):
    
    from infobank.kko.models import (
        AlimTalkMessage,
        ResponseApi
    )
    @classmethod
    def send_alimtalk_message(
        cls,
        message: AlimTalkMessage
    ) -> ResponseApi:
        """알림톡는 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/send/kakao#alimtalk
        
        응답 결과 json 포맷은 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/send/kakao#response
        
        Args:
            message (AlimTalkMessage): 

        Returns:
            class ResponseApi(
                *,
                status_code: int | None = None,
                response: Response | None = None,
                code: str,
                result: str,
                msg_key: str | None,
                ref: str | None
            )
        """
        response = cls.http_client.request_alimtalk_message_to_api(
            message= message
        )
        
        from infobank.kko.models import (
            ResponseApi
        )
        
        return ResponseApi(
            **response.json(),
            status_code=response.status_code,
            response=response
        )
        
    from infobank.kko.models import (
        FriendTalkMessage,
        ResponseApi
    )
    @classmethod
    def send_friendtalk_message(
        cls,
        message: FriendTalkMessage
    ) -> ResponseApi:
        response = cls.http_client.request_friendtalk_message_to_api(
            message= message
        )
        
        from infobank.kko.models import (
            ResponseApi
        )
        
        return ResponseApi(
            **response.json(),
            status_code=response.status_code,
            response=response
        )
        
    from infobank.kko.models import (
        BrandMessage,
        ResponseApi
    )
    @classmethod
    def send_brandmessage_message(
        cls,
        message: BrandMessage
    ) -> ResponseApi:
        response = cls.http_client.request_brandmessage_message_to_api(
            message= message
        )
        
        from infobank.kko.models import (
            ResponseApi
        )
        
        return ResponseApi(
            **response.json(),
            status_code=response.status_code,
            response=response
        )
