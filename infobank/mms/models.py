from pydantic import (
    Field
)
from typing import (
    Optional
)    
from infobank.core.models import (
    _MMSMessage,
    _ResponseApi
)


class MMSMessage(_MMSMessage):
    """MMS는 아래 페이지에서 확인 가능합니다.
    
    https://infobank-guide.gitbook.io/omni_api/api-reference/send/sms#request-1
    """
    to :str
    ref :Optional[str] = Field(
        max_length=200
    )


class ResponseApi(_ResponseApi):
    msg_key :Optional[str]
    ref :Optional[str]