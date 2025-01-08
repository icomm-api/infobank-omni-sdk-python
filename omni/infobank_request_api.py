from infobank.core.infobank_request_api import (
    _InfobankApi
)
from infobank.omni.models import (
    OmniMessage,
    ResponseApi
)

class OmniApi (_InfobankApi):
    @classmethod
    def send_message(
        cls,
        message: OmniMessage
    ) -> ResponseApi:
        """통합발송은 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/send/omni
        
        응답 결과 json 포맷은 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/send/omni#response
        
        Args:
            message (OmniMessage): 

        Returns:
            ResponseApi(
                *,
                status_code: int | None = None,
                response: Response | None = None,
                code: str,
                result: str,
                data: Data | None,
                ref: str | None
            )
        """
        

        response = cls.http_client.request_omni_message_to_api(
            message= message
        )
        
        return ResponseApi(
            **response.json(),
            status_code=response.status_code,
            response=response
        )