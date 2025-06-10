from typing import (
    Optional,
)
from pydantic import(
    constr,
    Field
)
from infobank.core.models import (
    _SMSMessage,
    _ResponseApi
)


class InterSMSMessage(_SMSMessage):
    """국제 SMS는 아래 페이지에서 확인 가능합니다.
    
    https://infobank-guide.gitbook.io/omni_api/api-reference/send/international#request
    """
    from_ :str = Field(
        alias='from'
    )
    to :constr(regex=r'^\+.*$')  = Field(
        alias='to'
    )
    pass

class ResponseApi(_ResponseApi):
    msg_key :Optional[str]
    ref :Optional[str]
    pass