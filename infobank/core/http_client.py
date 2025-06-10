import requests
import datetime
import json
import os
import mimetypes
import logging

from datetime import datetime

from infobank.core.exceptions import (
    InfobankException
)
from infobank.sms.models import (
    SMSMessage
)
from infobank.international.models import (
    InterSMSMessage
)
from infobank.mms.models import (
    MMSMessage
)
from infobank.rcs.models import (
    RCSMessage
)
from infobank.kko.models import (
    AlimTalkMessage,
    FriendTalkMessage,
    BrandMessage
)
from infobank.omni.models import (
    OmniMessage
)
from infobank.core.models import (
    ResponseToken,
    RequsetMessage
)
from infobank.imageupload.models import (
    ImageFile
)
from infobank.messageform.models import (
    MessageFormMessage
)
from infobank.sms.channel import (
    SMSChannel
)
from infobank.international.channel import (
    InterSMSChannel
)
from infobank.rcs.channel import (
    RCSChannel
)
from infobank.mms.channel import (
    MMSChannel
)
from infobank.kko.channel import (
    AlimTalkChannel,
    FriendTalkChannel,
    BrandMessageChannel
)
from infobank.report.channel import (
    ReportChannel
)
from infobank.omni.channel import (
    OmniChannel    
)
from infobank.imageupload.channel import (
    ImageFileChannel
)
from infobank.messageform.channel import (
    MessageFormChannel
)

from infobank.core.channel import (
    _Channel,
    AuthChannel,
    validate_url
)

response_token=None
token_expired=0

_logger = logging.getLogger('infobank.core.http_client')

class HttpClient:
    
    def __init__(
        self,
        api_url:str,
        client_id:str,
        client_passwd:str,
        logger: logging.Logger = _logger
    ):
        self.api_url = api_url
        self.client_id = client_id
        self.client_passwd = client_passwd
        
        self.logger = logger

    def auth_from_api(
        self
    ) -> ResponseToken:
        global response_token
        global token_expired
        
        channel = AuthChannel(
            api_url=self.api_url,
            client_id=self.client_id,
            client_passwd=self.client_passwd
        )
        validate_url(channel.api_url)
        
        current_timestamp = datetime.now().timestamp()
        if token_expired == 0 or (token_expired) < current_timestamp:
            response = channel.post(
                timeout=5
            )
            
            if response.status_code != 200:
                headers = '\n'.join(f"{key}: '{value}'" for key, value in response.request.headers.items())
                raise InfobankException(
                    "Failure, Authenticate %s %s\n%s" % (response.request.method, response.url, headers)
                )
            
            data = response.json()['data']
            response_token = ResponseToken(
                response = response,
                code = response.json()['code'],
                schema_ = data['schema'],
                token = data['token'],
                expired = data['expired']
            )
            
            token_expired = datetime.now().timestamp() + 86000.0

        return response_token
    
    def request_message_to_api_from_channel(
        self,
        channel :_Channel,
        message :RequsetMessage
    )-> requests.Response:
        
        validate_url(channel.api_url)
        
        body = json.dumps(
            message.dict(
                by_alias=True,
                exclude_none=True
                ),
            indent=2,
            sort_keys=True,
            ensure_ascii=False
        )
        
        self.logger.debug("{headers}\n{body}".format(
                headers = channel.headers,
                body = body
            )           
        )
        
        response = channel.post(
            body=body,
            timeout=5
        )
        
        self.logger.debug("{response}".format(
                response = response.text,
            )           
        )

        return response

    def request_sms_message_to_api(
        self,
        message: SMSMessage
    ) -> requests.Response:
        
        response_token = self.auth_from_api()
        
        channel = SMSChannel(
            api_url=self.api_url
        )
        
        channel.set_token(
            schema=response_token.schema_,
            token=response_token.token
        )
        
        response = self.request_message_to_api_from_channel(
            channel,
            message
        )
        return response
    
    def request_international_sms_message_to_api(
        self,
        message: InterSMSMessage
        ) -> requests.Response:
        
        response_token = self.auth_from_api()
        
        channel = InterSMSChannel(
            api_url=self.api_url
        )
        
        channel.set_token(
            schema=response_token.schema_,
            token=response_token.token
        )
        
        response = self.request_message_to_api_from_channel(
            channel,
            message
        )
        return response

    def request_mms_message_to_api(
        self,
        message: MMSMessage
    ) -> requests.Response:
        response_token = self.auth_from_api()
        
        channel = MMSChannel(
            api_url=self.api_url
        )
        
        channel.set_token(
            schema=response_token.schema_,
            token=response_token.token
        )
        
        response = self.request_message_to_api_from_channel(
            channel,
            message
        )
        return response
        
    def request_rcs_message_to_api(
        self,
        message: RCSMessage
    ) -> requests.Response:
        
        response_token = self.auth_from_api()
        
        channel = RCSChannel(
            api_url=self.api_url
        )
        
        channel.set_token(
            schema=response_token.schema_,
            token=response_token.token
        )
        
        response = self.request_message_to_api_from_channel(
            channel,
            message
        )
        return response
    
    def request_alimtalk_message_to_api(
        self,
        message: AlimTalkMessage
    ) -> requests.Response:
        
        response_token = self.auth_from_api()
        
        channel = AlimTalkChannel(
            api_url=self.api_url
        )
        
        channel.set_token(
            schema=response_token.schema_,
            token=response_token.token
        )
        
        response = self.request_message_to_api_from_channel(
            channel,
            message
        )
        return response
    
    def request_friendtalk_message_to_api(
        self,
        message: FriendTalkMessage
    ) -> requests.Response:
        
        response_token = self.auth_from_api()
        
        channel = FriendTalkChannel(
            api_url=self.api_url
        )
        
        channel.set_token(
            schema=response_token.schema_,
            token=response_token.token
        )
        
        response = self.request_message_to_api_from_channel(
            channel,
            message
        )
        return response
    
    def request_brandmessage_message_to_api(
        self,
        message: BrandMessage
    ) -> requests.Response:
        
        response_token = self.auth_from_api()
        
        channel = BrandMessageChannel(
            api_url=self.api_url
        )
        
        channel.set_token(
            schema=response_token.schema_,
            token=response_token.token
        )
        
        response = self.request_message_to_api_from_channel(
            channel,
            message
        )
        return response
    
    def request_omni_message_to_api(
        self,
        message: OmniMessage
    ) -> requests.Response:
        
        response_token = self.auth_from_api()
        channel = OmniChannel(
            api_url=self.api_url
        )
        
        channel.set_token(
            schema=response_token.schema_,
            token=response_token.token
        )
        
        response = self.request_message_to_api_from_channel(
            channel,
            message
        )
        return response
    
    def request_reports_to_api(
        self
    ) -> requests.Response:
        
        response_token = self.auth_from_api()
        
        channel = ReportChannel(
            api_url=self.api_url
        )
        channel.api_url = channel.api_url +"/polling"
        
        channel.set_token(
            schema=response_token.schema_,
            token=response_token.token
        )
        
        self.logger.debug("{headers}".format(
                headers = channel.headers,
            )           
        )
        
        response = channel.get(
            timeout=5
        )
        
        self.logger.debug("{response}".format(
                response = response.text,
            )           
        )
        
        return response
    
    def delete_result_to_api(
        self,
        report_id: str
    ) -> requests.Response:
        
        response_token = self.auth_from_api()
        
        channel = ReportChannel(
            api_url=self.api_url
        )
        channel.api_url = channel.api_url +"/polling"
        
        channel.set_token(
            schema=response_token.schema_,
            token=response_token.token
        )
        
        self.logger.debug("{headers}".format(
                headers = channel.headers,
            )           
        )
        
        response = channel.delete(
            report_id=report_id,
            timeout=5
        )
        
        self.logger.debug("{response}".format(
                response = response.text,
            )           
        )
        
        return response
    
    def inquiry_report(
        self,
        report_id: str
    ) -> requests.Response:
        
        response_token = self.auth_from_api()
        
        channel = ReportChannel(
            api_url=self.api_url
        )
        channel.api_url = channel.api_url + "/inquiry/" + report_id
        
        channel.set_token(
            schema=response_token.schema_,
            token=response_token.token
        )
        
        self.logger.debug("{headers}".format(
                headers = channel.headers,
            )           
        )
        
        response = channel.get(
            timeout=5
        )
        
        self.logger.debug("{response}".format(
                response = response.text,
            )           
        )
        
        return response
    
    def request_image_file_to_api(
        self,
        image_file :ImageFile
    ) -> requests.Response:
        
        response_token = self.auth_from_api()

        channel = ImageFileChannel(
            api_url= self.api_url
        )
        
        channel.set_token(
            schema=response_token.schema_,
            token=response_token.token
        )
        
        files = {
            'file': (
                os.path.basename(image_file.file_path),
                open(image_file.file_path, 'rb'),
                mimetypes.guess_type(image_file.file_path)[0]
            )
        }
        
        self.logger.debug("{headers}\nfile={files}".format(
                headers = channel.headers,
                files = '@'+image_file.file_path
            )           
        )

        response = channel.post(
            files=files,
            service_type=image_file.service_type,
            message_type=image_file.message_type,
            timeout=5
        )
        
        self.logger.debug("{response}".format(
                response = response.text,
            )           
        )
            
        return response
    
    
    def create_message_form_to_api(
        self,
        message : MessageFormMessage
    ) -> requests.Response:
        response_token = self.auth_from_api()
        channel = MessageFormChannel(
            api_url=self.api_url
        )
        
        channel.set_token(
            schema=response_token.schema_,
            token=response_token.token
        )
        
        response = self.request_message_to_api_from_channel(
            channel=channel,
            message=message
        )
        return response
    
    def request_message_form_to_api(
        self,
        form_id :str
    ) -> requests.Response:
        response_token = self.auth_from_api()
        
        channel = MessageFormChannel(
            api_url=self.api_url
        )
        
        channel.set_token(
            schema=response_token.schema_,
            token=response_token.token
        )
        
        self.logger.debug("{headers}".format(
                headers = channel.headers,
            )           
        )
        
        response = channel.get(
            form_id=form_id,
            timeout=5
        )
        
        self.logger.debug("{response}".format(
                response = response.text,
            )           
        )
        
        return response
    
    def modify_message_form_to_api(
        self,
        form_id :str,
        message : MessageFormMessage
    ) -> requests.Response:
        response_token = self.auth_from_api()
        
        channel = MessageFormChannel(
            api_url=self.api_url
        )
        
        channel.set_token(
            schema=response_token.schema_,
            token=response_token.token
        )
        
        body = json.dumps(
            message.dict(
                by_alias=True,
                exclude_none=True
                ),
            indent=2,
            sort_keys=True,
            ensure_ascii=False
        )
        
        self.logger.debug("{headers}\n{body}".format(
                headers = channel.headers,
                body = body
            )           
        )
        
        response = channel.put(
            form_id=form_id,
            body=body,
            timeout=5
        )
        
        self.logger.debug("{response}".format(
                response = response.text,
            )           
        )
        
        return response
    
    def delete_message_form_to_api(
        self,
        form_id :str
    ) -> requests.Response:
        response_token = self.auth_from_api()
        
        channel = MessageFormChannel(
            api_url=self.api_url
        )
        
        channel.set_token(
            schema=response_token.schema_,
            token=response_token.token
        )
       
        self.logger.debug("{headers}".format(
                headers = channel.headers
            )           
        )
        
        response = channel.delete(
            form_id=form_id,
            timeout=5
        )
        
        self.logger.debug("{response}".format(
                response = response.text,
            )           
        )
        
        return response
    
