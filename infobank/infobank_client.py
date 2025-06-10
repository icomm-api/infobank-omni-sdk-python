class InfobankClient:
    
    from typing import (
        Union
    )
    
    def __init__(
        self,
        api_url :str,
        client_id :str,
        client_passwd :str
    ):        
        
        from infobank.sms.infobank_request_api import (
            SMSApi
        )
        self.sms=SMSApi(
            api_url=api_url,
            client_id=client_id,
            client_passwd=client_passwd
        )
        
        from infobank.mms.infobank_request_api import (
            MMSApi
        )
        self.mms=MMSApi(
            api_url=api_url,
            client_id=client_id,
            client_passwd=client_passwd
        )
        
        from infobank.international.infobank_request_api import(
            InterSMSApi
        )
        self.inter=InterSMSApi(
            api_url=api_url,
            client_id=client_id,
            client_passwd=client_passwd
        )
        
        from infobank.rcs.infobank_request_api import(
            RCSApi
        )
        self.rcs=RCSApi(
            api_url=api_url,
            client_id=client_id,
            client_passwd=client_passwd
        )
        
        from infobank.kko.infobank_request_api import(
            KkoApi
        )
        self.kko=KkoApi(
            api_url=api_url,
            client_id=client_id,
            client_passwd=client_passwd
        )
        
        from infobank.omni.infobank_request_api import(
            OmniApi
        )
        self.omni=OmniApi(
            api_url=api_url,
            client_id=client_id,
            client_passwd=client_passwd
        )
        
        from infobank.imageupload.infobank_request_api import(
            ImageUploadApi
        )
        self.image = ImageUploadApi(
            api_url=api_url,
            client_id=client_id,
            client_passwd=client_passwd
        )
        
        from infobank.report.infobank_request_api import(
            ReportApi
        )
        self.report = ReportApi(
            api_url=api_url,
            client_id=client_id,
            client_passwd=client_passwd
        )
        
        from infobank.messageform.infobank_request_api import(
            MessageFormApi
        )
        self.messageform = MessageFormApi(
            api_url=api_url,
            client_id=client_id,
            client_passwd=client_passwd
        )
        
    from infobank.sms.models import(
        SMSMessage,
        ResponseApi as SMSResponse
    )
    from infobank.mms.models import(
        MMSMessage,
        ResponseApi as MMSResponse
    )
    from infobank.international.models import(
        InterSMSMessage,
        ResponseApi as InterSMSResponse
    )
    from infobank.rcs.models import(
        RCSMessage,
        ResponseApi as RCSResponse
    )
    from infobank.kko.models import(
        AlimTalkMessage,
        ResponseApi as AlimTalkResponse
    )
    from infobank.kko.models import(
        FriendTalkMessage,
        ResponseApi as FriendTalkResponse
    )
    from infobank.kko.models import(
        BrandMessage,
        ResponseApi as BrandMessageResponse
    )
    from infobank.omni.models import(
        OmniMessage,
        ResponseApi as OmniResponse
    )
        
    def send_message(
        self,
        message :Union[
            SMSMessage,
            MMSMessage,
            InterSMSMessage,
            RCSMessage,
            AlimTalkMessage,
            FriendTalkMessage,
            BrandMessage,
            OmniMessage
        ]
    )-> Union[
        SMSResponse,
        MMSResponse,
        InterSMSResponse,
        RCSResponse,
        AlimTalkResponse,
        FriendTalkResponse,
        BrandMessageResponse,
        OmniResponse
    ]:
        """SMS(SMSMessage) : https://infobank-guide.gitbook.io/omni_api/api-reference/send/sms#sms
        
        MMS(MMSMessage) : https://infobank-guide.gitbook.io/omni_api/api-reference/send/sms#mms
        
        국제 SMS(InterSMSMessage) : https://infobank-guide.gitbook.io/omni_api/api-reference/send/international
        
        RCS(RCSMessage) : https://infobank-guide.gitbook.io/omni_api/api-reference/send/rcs
        
        알림톡(AlimTalkMessage) : https://infobank-guide.gitbook.io/omni_api/api-reference/send/kakao#alimtalk
        
        통합발송(OmniMessage) : https://infobank-guide.gitbook.io/omni_api/api-reference/send/omni

        Args:
            message (Union[ SMSMessage, MMSMessage, InterSMSMessage, RCSMessage, AlimTalkMessage, OmniMessage ]): _description_

        Returns:
            Union[
                class ResponseApi(
                    *,
                    status_code: int | None = None,
                    response: Response | None = None,
                    code: str,
                    result: str,
                    msg_key: str | None,
                    ref: str | None
                )
                |
                class ResponseApi(
                    *,
                    status_code: int | None = None,
                    response: Response | None = None,
                    code: str,
                    result: str,
                    data: Data | None,
                    ref: str | None
                )
            ]
        """
        from infobank.sms.models import(
            SMSMessage
        )
        from infobank.mms.models import(
            MMSMessage
        )
        from infobank.international.models import(
            InterSMSMessage
        )
        from infobank.rcs.models import(
            RCSMessage
        )
        from infobank.kko.models import(
            AlimTalkMessage
        )
        from infobank.kko.models import(
            FriendTalkMessage
        )
        from infobank.kko.models import(
            BrandMessage
        )
        from infobank.omni.models import(
            OmniMessage
        )
        
        if isinstance(message, SMSMessage):
            return self.sms.send_message(
                message=message
            )
        elif isinstance(message, MMSMessage):
            return self.mms.send_message(
                message=message
            )
        elif isinstance(message, InterSMSMessage):
            return self.inter.send_message(
                message=message
            )
        elif isinstance(message, RCSMessage):
            return self.rcs.send_message(
                message=message
            )
        elif isinstance(message, AlimTalkMessage):
            return self.kko.send_alimtalk_message(
                message=message
            )
        elif isinstance(message, FriendTalkMessage):
            return self.kko.send_friendtalk_message(
                message=message
            )
        elif isinstance(message, BrandMessage):
            return self.kko.send_brandmessage_message(
                message=message
            )
        elif isinstance(message, OmniMessage):
            return self.omni.send_message(
                message=message
            )

    from infobank.imageupload.models import(
        ImageFile,
        ResponseApi as ImageResponse
    )
    def request_image_upload(
        self,
        image_file : ImageFile
    ) -> ImageResponse:
        """이미지 업로드는 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/management/file
        
        응답 결과 json 포맷은 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/management/file#response
        
        Args:
            message (ImageFile): 

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
        return self.image.request_image_file(
            image_file=image_file
        )
        
    from infobank.report.models import(
        ResponseApi as ReportResponse
    )
    def request_reports(
        self
    ) -> ReportResponse :
        """리포트 조회는 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/report/polling#get

        Returns:
            class ResponseApi(
                *,
                status_code: int | None = None,
                response: Response | None = None,
                code: str,
                result: str,
                data: ReportData | None
            )
        """
        return self.report.request_reports(
            
        )
        
    def delete_reports(
        self,
        report_id : str
    ) ->ReportResponse:
        """리포트 삭제는 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/report/polling#delete

        Args:
            report_id (str): 조회 시 받은 report Id

        Returns:
            class ResponseApi(
                *,
                status_code: int | None = None,
                response: Response | None = None,
                code: str,
                result: str,
                data: ReportData | None
            )
        """
        return self.report.delete_reports(
            report_id=report_id
        )

    def inquiry_report(
        self,
        report_id :str
    ) ->ReportResponse:
        """메시지키를 기준으로 리포트를 조회합니다.

         https://infobank-guide.gitbook.io/omni_api/api-reference/report/inquiry

        Args:
            report_id (str): 메시지 키

        Returns:
            class ResponseApi(
                *,
                status_code: int | None = None,
                response: Response | None = None,
                code: str,
                result: str,
                data: ReportData | None
            )
        """
        return self.report.inquiry_report(
            report_id=report_id
        )
        
    from infobank.messageform.models import(
        MessageFormMessage,
        ResponseApi as MessageFormResponse
    )
    def create_message_form(
        self,
        message : MessageFormMessage
    )->MessageFormResponse :
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
        return self.messageform.create_message_form(
            message=message
        )
    
    def modify_message_form(
        self,
        form_id :str,
        message: MessageFormMessage
    )->MessageFormResponse:
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
        return self.messageform.modify_message_form(
            form_id= form_id,
            message=message
        )
    
    def request_message_form(
        self,
        form_id :str
    )->MessageFormMessage:
        return self.messageform.request_message_form(
            form_id=form_id
        )
        
    def delete_message_form(
        self,
        form_id :str
    )->MessageFormResponse:
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
        return self.messageform.delete_message_form(
            form_id = form_id
        )