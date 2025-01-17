from infobank.core.infobank_request_api import (
    _InfobankApi
)

class MessageFormApi (_InfobankApi):
    from infobank.messageform.models import (
        MessageFormMessage,
        ResponseApi
    )

    @classmethod
    def create_message_form(
        cls,
        message: MessageFormMessage
    ) -> ResponseApi:
        """메시지 폼 등록는 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/management/form#post
        
        Args:
            message (MessageFormMessage): 

        Returns:
            class ResponseApi(
                *,
                status_code: int | None = None,
                response: Response | None = None,
                code: str,
                result: str,
                data: Data | None
            )
        """
        response = cls.http_client.create_message_form_to_api(
            message=message
        )
        
        from infobank.messageform.models import (
            ResponseApi
        )

        
        return ResponseApi(
            **response.json(),
            status_code=response.status_code,
            response=response
        )
        
    @classmethod
    def request_message_form(
        cls,
        form_id :str
    ) -> ResponseApi:
        """메시지 폼 조회는 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/management/form#get

        Args:
            form_id (str): 폼 아이디

        Returns:
            class ResponseApi(
                *,
                status_code: int | None = None,
                response: Response | None = None,
                code: str,
                result: str,
                data: Data | None
            )
        """
        response = cls.http_client.request_message_form_to_api(
            form_id=form_id
        )
        
        from infobank.messageform.models import (
            ResponseApi
        )
        
        return ResponseApi(
            **response.json(),
            status_code=response.status_code,
            response=response
        )
        
    @classmethod
    def modify_message_form(
        cls,
        form_id :str,
        message: MessageFormMessage
    ) -> ResponseApi:
        """메시지 폼 수정는 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/management/form#put

        응답 결과 json 포맷은 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/management/form#response
        
        Args:
            form_id (str): 폼 아이디
            message (MessageFormMessage):

        Returns:
            class ResponseApi(
                *,
                status_code: int | None = None,
                response: Response | None = None,
                code: str,
                result: str,
                data: Data | None
            )
        """

        response =  cls.http_client.modify_message_form_to_api(
            form_id=form_id,
            message=message
        )
        
        from infobank.messageform.models import (
            ResponseApi
        )
        
        return ResponseApi(
            **response.json(),
            status_code=response.status_code,
            response=response
        )
        
    @classmethod
    def delete_message_form(
        cls,
        form_id :str
    ) -> ResponseApi:
        """메시지 폼 삭제는 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/management/form#delete

        Args:
            form_id (str): 폼 아이디

        Returns:
            class ResponseApi(
                *,
                status_code: int | None = None,
                response: Response | None = None,
                code: str,
                result: str,
                data: Data | None
            )
        """
        response = cls.http_client.delete_message_form_to_api(
            form_id=form_id
        )
        
        from infobank.messageform.models import (
            ResponseApi
        )
        
        return ResponseApi(
            **response.json(),
            status_code=response.status_code,
            response=response
        )
    
