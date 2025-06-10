from infobank.core.infobank_request_api import (
    _InfobankApi
)

class SMSApi (_InfobankApi):
    from infobank.sms.models import (
        SMSMessage,
        ResponseApi
    )

    @classmethod
    def send_message(
        cls,
        message: SMSMessage
    ) -> ResponseApi:
        """SMS는 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/send/sms#sms
        
        응답 결과 json 포맷은 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/send/sms#response
        
        Args:
            message (SMSMessage): 

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
        response = cls.http_client.request_sms_message_to_api(
            message=message
        )
        from infobank.sms.models import (
            ResponseApi
        )
        return ResponseApi(
            **response.json(),
            status_code=response.status_code,
            response=response
        )