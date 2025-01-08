#-*-coding:utf-8-*-
import pytest
import json

from pydantic import (
    ValidationError
)
from infobank.infobank_client import(
    InfobankClient
)
from infobank.kko.models import (
    AlimTalkMessageType
)
from infobank.kko.tests.make_message import(
    get_mandantory_validate_alimtalk_message,
    get_alimtalk_message,
    get_alimtalk_al_button,
    get_alimtalk_bc_button,
    get_alimtalk_bk_button,
    get_alimtalk_bt_button,
    get_alimtalk_ds_button,
    get_alimtalk_md_button,
    get_alimtalk_wl_button,
    get_alimtalk_ac_button,
    get_alimtalk_bf_button,
    get_alimtalk_fallback_message,
)
from infobank.client import (
    Client
)

api = InfobankClient(
    api_url=Client.api_url,
    client_id=Client.client_id,
    client_passwd=Client.client_passwd
)

@pytest.mark.parametrize(
    'msg_type',
    [
        (AlimTalkMessageType.AT),
        (AlimTalkMessageType.AI)
    ]
)
def test_validate_alimtamlk_mandatory_value(
    msg_type :AlimTalkMessageType
):
    with pytest.raises(ValidationError):
        get_mandantory_validate_alimtalk_message(
            msg_type=msg_type
        )
   
@pytest.mark.parametrize(
    'msg_type, buttons',
    [
        (AlimTalkMessageType.AI, [get_alimtalk_al_button()]),
        (AlimTalkMessageType.AI, [get_alimtalk_bc_button()]),
        (AlimTalkMessageType.AI, [get_alimtalk_bk_button()]),
        (AlimTalkMessageType.AI, [get_alimtalk_bt_button()]),
        (AlimTalkMessageType.AI, [get_alimtalk_ds_button()]),
        (AlimTalkMessageType.AI, [get_alimtalk_md_button()]),
        (AlimTalkMessageType.AI, [get_alimtalk_wl_button()]),
        (AlimTalkMessageType.AI, [get_alimtalk_bf_button()]),
        (AlimTalkMessageType.AI, [get_alimtalk_ac_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_al_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_bc_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_bk_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_bt_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_ds_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_md_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_wl_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_bf_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_ac_button()]),
    ]
)
def test_send_message(
    msg_type :AlimTalkMessageType,
    buttons
):    
    message=get_alimtalk_message(
        msg_type=msg_type,
        buttons=buttons
    )
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

@pytest.mark.parametrize(
    'msg_type',
    [
        (AlimTalkMessageType.AT),
        (AlimTalkMessageType.AI)
    ]
)
def test_fallback_message(
    msg_type
):
    message = get_alimtalk_fallback_message(
        msg_type=msg_type
    )
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
    