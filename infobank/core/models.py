import sys
import requests
import pkg_resources

from pydantic import (
    BaseModel,
    Field,
    Extra,
)
from typing import (
    List,
    Optional
)
from infobank.core.exceptions import (
    InfobankException
)

def convert_to_snake_case(string: str) -> str:
    converted = ''
    for char in string:
        if char.isupper():
            converted += '_' + char.lower()
        else:
            converted += char
    return converted.lstrip('_')

def to_camel_case(string: str) -> str:
    output = "".join(word.capitalize() for word in string.split("_"))
    return output[0].lower() + output[1:]

def to_header_specific_case(string: str) -> str:
    return "-".join(word.capitalize() for word in string.split("_"))

def get_package_version() -> str:
    sdk_version = ""

    if "infobank" in sys.modules:
        try:
            sdk_version = (
                "/" + pkg_resources.get_distribution("infobank-omni-sdk-python").version
            )
        except pkg_resources.DistributionNotFound as e:
            # Ignore as package is not installed in development environment.
            
            pass
    return sdk_version

class CamelCaseModel(BaseModel):           
    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        
class RequestHeaders(CamelCaseModel):
    accept: str = "application/json"
    content_type: Optional[str] = None
    user_agent: str = (
        f"@infobank-omni-sdk-python{get_package_version()} python/{sys.version.split(' ')[0]}"
    )
    X_IB_Client_Id :Optional[str] = Field(alias='X-IB-Client-Id', default=None)
    X_IB_Client_Passwd :Optional[str] = Field(alias='X-IB-Client-Passwd', default=None)
    authorization :Optional[str] = None
    
    class Config:
        alias_generator = to_header_specific_case
        allow_population_by_field_name = True

    def __init__(self, **data: str) -> None:
        super().__init__(**data)
    
    def __str__(self) -> str:
        data_str = '\n'.join(f"{key}='{value}'" for key, value in self.dict().items() if value is not None)
        return f"{data_str}"



class RequsetMessage(CamelCaseModel):
    def __init__(self, **data):
        super().__init__(**data)
        
        for field in data:
            if field != 'from':
                convert_field = convert_to_snake_case(field)
                if convert_field not in self.__fields__:
                    raise InfobankException("Undefined field: " + field)


class _FallBackType():
    SMS="SMS"
    MMS="MMS"

class _FallBack(RequsetMessage):
    type: str
    text: str = Field(
        max_length=2000
    )
    title :Optional[str] = Field(
        max_length=20
    )
    file_key :Optional[List[str]] = Field(
        max_items=3
    )
    origin_cid :Optional[str] = Field(
        alias='originCID',
        max_length=9
    )
    
    
class ResponseBase(CamelCaseModel):
    status_code: Optional[int] = None
    response: Optional[requests.Response] = None
    
    class Config(CamelCaseModel.Config):
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
    
class ResponseToken(ResponseBase):
    code :str
    token :str
    schema_ :str = Field(
        alias='schema'
    )
    expired :str

class _ResponseApi(ResponseBase):
    code :str
    result :str


class _SMSMessage(RequsetMessage):
    from_ :str = Field(
        alias='from'
    )
    text :str
    origin_cid : Optional[str] = Field(
        alias='originCID',
        max_length=9
    )


class _MMSMessage(RequsetMessage):
    from_ :str = Field(
        alias='from'
    )
    text :str
    title :Optional[str]
    file_key :Optional[List[str]] = Field(
        max_items=3
    )
    origin_cid :Optional[str] = Field(
        alias='originCID',
        max_length=9
    )


class _RCSButtonType():
    URL = "URL"
    MAP_LOC = "MAP_LOC"
    MAP_QRY = "MAP_QRY"
    MAP_SEND = "MAP_SEND"
    CALENDAR = "CALENDAR"
    COPY = "COPY"
    COM_T = "COM_T"
    COM_V = "COM_V"
    DIAL = "DIAL"
    
class _RCSButton(RequsetMessage):
    type :str
    name :str
    url :Optional[str]
    label :Optional[str]
    latitude :Optional[str]
    longitude :Optional[str]
    fallback_url :Optional[str]
    query :Optional[str]
    start_time :Optional[str]
    end_time :Optional[str]
    title :Optional[str]
    description :Optional[str]
    text :Optional[str]
    phone_number :Optional[str]

class _RCSSubContent(RequsetMessage):
    sub_title :Optional[str]
    sub_desc :Optional[str]
    sub_media :Optional[str]
    sub_media_url :Optional[str]

class _RCSStandAlone(RequsetMessage):
    text :Optional[str]
    title :Optional[str]
    media :Optional[str]
    media_url :Optional[str]
    sub_content :Optional[List[_RCSSubContent]]
    button :Optional[List[_RCSButton]]

class _RCSCarousel(RequsetMessage):
    text :Optional[str]
    title :Optional[str]
    media :Optional[str]
    media_url :Optional[str]
    button :Optional[List[_RCSButton]]

class _RCSTemplate(BaseModel):
    description :Optional[str]
    sub_content :Optional[List[_RCSSubContent]]
    
    class Config:
        alias_generator = to_camel_case
        extra = Extra.allow
        
class _RCSContent(RequsetMessage):
    standalone :Optional[_RCSStandAlone]
    carousel :Optional[List[_RCSCarousel]]
    template :Optional[_RCSTemplate]
    
    def __init__(
        self,
        standalone :Optional[_RCSStandAlone] = None,
        carousel :Optional[List[_RCSCarousel]] = None,
        template :Optional[_RCSTemplate] = None
    ):
        """RCS conetent는 아래 페이지에서 확인 가능합니다.

        https://infobank-guide.gitbook.io/omni_api/api-reference/send/rcs#content
        
        3개 필드 중 1개 필수(standalone, carousel, template)입니다.

        Args:
            standalone (Optional[RCSStandAlone], optional): standalone. Defaults to None.\n
            carousel (Optional[List[RCSCarousel]], optional): carousel. Defaults to None.\n
            template (Optional[RCSTemplate], optional): template. Defaults to None.\n

        Raises:
            InfobankException:
        """
        if standalone is None and carousel is None and template is None:
            raise InfobankException('At least one of standalone, carousel, template or body must be set.')
        
        if sum(bool(x) for x in [standalone, carousel, template]) > 1:
            raise InfobankException('Only one of standalone, carousel, template or body can be set.')
        
        if carousel is not None and len(carousel) <= 0:
            raise InfobankException('carousel is not set')
        
        super().__init__(
            standalone = standalone,
            carousel = carousel,
            template = template
        )

class _RCSMessage(RequsetMessage):
    content:Optional[_RCSContent]
    body :Optional[dict]
    buttons :Optional[list]
    from_ :str = Field(
        alias='from'
    )
    format_id: str
    expiry_option :Optional[str]
    header :Optional[str] = Field(
        max_length=1
    )
    footer :Optional[str] = Field(
        max_length=100
    )
    brand_key :str
    brand_id :Optional[str]
    
    
class _AlimTalkButtonType():
    WL='WL'
    AL='AL'
    BK='BK'
    MD='MD'
    DS='DS'
    BC='BC'
    BT='BT'
    AC='AC'
    BF='BF'

class _AlimTalkMessageType():
    AT='AT'
    AI='AI'

class _FriendTalkMessageType():
    FT='FT'
    FI='FI'
    FW='FW'

class _BrandMessageSendType():
    Free='free'
    basic='basic'

class _AlimTalkButton(RequsetMessage):
    type: str
    name: str
    url_pc : str = Field(
        default=None
    )
    url_mobile: str = Field(
        default=None
    )
    scheme_ios :str = Field(
        default=None
    )
    scheme_android :str = Field(
        default=None
    )
    target :Optional[str]
    chat_extra :str = Field(
        default=None
    )
    chat_event :str = Field(
        default=None
    )
    biz_form_key :str = Field(
        default=None
    )
    biz_form_id :str = Field(
        default=None
    )
    
class _AlimTalkMessage(RequsetMessage):
    sender_key :str
    msg_type :str
    text :str
    
class _FriendTalkMessage(RequsetMessage):
    sender_key :str
    msg_type :str
    text :str

class _BrandMessage(RequsetMessage):
    sender_key :str
    send_type :str
    msg_type :str
    