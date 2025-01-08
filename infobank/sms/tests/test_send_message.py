#-*-coding:utf-8-*-
import pytest
import json

from pydantic import (
    ValidationError
)
from infobank.infobank_client import (
    InfobankClient
)
from infobank.sms.models import(
    SMSMessage
)
from infobank.client import (
    Client
)
from infobank.sms.tests.make_message import (
    get_mandantory_validate_message,
    get_sms_message
)

api = InfobankClient(
    api_url=Client.api_url,
    client_id=Client.client_id,
    client_passwd=Client.client_passwd
)

def test_validate_mandatory_value():
    with pytest.raises(ValidationError):
        get_mandantory_validate_message()

def test_send_sms_message():
    message=SMSMessage(
        from_="0316281500",
        text="text",
        to="01012341234",
        origin_cid="1234",
        ref="ref"
    )
    
    response = api.send_message(
        message=message
    )
    
    assert response.status_code == 200, "(request:{request}\nstatus_code:{status_code} response:{response})".format(
        request = json.dumps(
            message.dict(
                by_alias=True,
                exclude_none=True
                ),
            indent=2,
            sort_keys=True,
            ensure_ascii=False
        ),
        status_code = response.status_code,
        response = response
    )
    assert response.code == 'A000', "(request:{request}\nresponse:{response})".format(
        request = json.dumps(
            message.dict(
                by_alias=True,
                exclude_none=True
                ),
            indent=2,
            sort_keys=True,
            ensure_ascii=False
        ),
        response = response
    )
    assert len(response.msg_key) > 0,  "(request:{request}\nresponse:{response})".format(
        request = json.dumps(
            message.dict(
                by_alias=True,
                exclude_none=True
                ),
            indent=2,
            sort_keys=True,
            ensure_ascii=False
        ),
        response = response
    )
    