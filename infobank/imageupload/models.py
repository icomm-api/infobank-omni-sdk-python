#-*-coding:utf-8-*-
from enum import (
    Enum
)
from pydantic import(
    Field
)
from typing import (
    Optional
)

from infobank.core.models import (
    _ResponseApi,
    CamelCaseModel,
    RequsetMessage
)

class ImageServiceType(str, Enum):
    MMS = "MMS"
    RCS = "RCS"
    FRIENDTALK= "FRIENDTALK"
    BRANDMESSAGE="BRANDMESSAGE"
class ImageMessageType(str, Enum):
    FI = "FI"
    FW = "FW"
    FL = "FL"
    FC = "FC"
    FA = "FA"
    defalut = "defalut"
    wide = "wide"
    wideItemList = "wideItemList"
    carouselFeed = "carouselFeed"
    carouselCommerce ="carouselCommerce"
    
class ImageSubType(str, Enum):
    first= "first"
class Data(CamelCaseModel):
    file_key :str = Field(
        alias='fileKey',
        default=None,
        description='(MMS)파일키'
    )
    media :str = Field(
        alias='media',
        default=None,
        description='(RCS)maapfile 정보'
    )
    img_url :str = Field(
        alias='imgUrl',
        default=None,
        description='(카카오 친구톡)이미지 URL주소'
    )
    expired :Optional[str]
    
class ResponseApi(_ResponseApi):
    data :Optional[Data]
    
class ImageFile(RequsetMessage):
    """이미지 파일 업로드는 아래 페이지에서 확인 가능합니다. 

    https://infobank-guide.gitbook.io/omni_api/api-reference/management/file#request
    """
    service_type :ImageServiceType
    message_type :ImageMessageType = Field(
        default=None
    )
    sub_type: ImageSubType = Field(
        default=None
    )
    file_path: str