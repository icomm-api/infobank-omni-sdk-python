#-*-coding:utf-8-*-
import pytest
import json

from pydantic import (
    ValidationError
)
from infobank.infobank_client import (
    InfobankClient
)
from infobank.client import (
    Client
)
from infobank.international.tests.make_message import (
    get_mandantory_validate_message,
    get_validate_to_message,
    get_international_sms_message
)


api = InfobankClient(
    api_url=Client.api_url,
    client_id=Client.client_id,
    client_passwd=Client.client_passwd
)

def test_validate_mandatory_value_error():
    with pytest.raises(ValidationError):
        get_mandantory_validate_message()

def test_validate_to_error():
    with pytest.raises(ValidationError):
        get_validate_to_message()


def test_from_send_sms_message():
    message=get_international_sms_message()
    response =api.send_message(
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