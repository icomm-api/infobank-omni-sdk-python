#-*-coding:utf-8-*-
from typing import List
import pytest
import json

from pydantic import (
    ValidationError
)
from infobank.infobank_client import (
    InfobankClient
)
from infobank.omni.models import (
    AlimTalkMessageType,
    AlimTalkButton
)
from infobank.omni.models import(
    RCSButton
)
from infobank.client import (
    Client
)
from infobank.omni.exceptions import(
    InfobankException
)
from infobank.omni.tests.make_message import(
    get_rcs_calendar_button,
    get_rcs_com_t_button,
    get_rcs_com_v_button,
    get_rcs_copy_button,
    get_rcs_dial_button,
    get_rcs_map_loc_button,
    get_rcs_map_qry_button,
    get_rcs_map_send_button,
    get_rcs_url_button,
)
from infobank.omni.tests.make_message import(
    get_alimtalk_al_button,
    get_alimtalk_bc_button,
    get_alimtalk_bk_button,
    get_alimtalk_bt_button,
    get_alimtalk_ds_button,
    get_alimtalk_md_button,
    get_alimtalk_wl_button,
    get_alimtalk_bf_button,
    get_alimtalk_ac_button
)
from infobank.omni.tests.make_message import(
    get_mandantory_validate_message,
    get_message_flow_not_set_message,
    get_message_flow_duplicate_message,
    get_omni_sms_message,
    get_omni_mms_message,
    get_omni_rcs_standalone_message,
    get_omni_rcs_carousel,
    get_omni_rcs_carousel_message,
    get_omni_rcs_template_message,
    get_omni_alimtalk_message,
    get_omni_message
)


def test_validate_mandatory_value(
    
):
    with pytest.raises(ValidationError):
        get_mandantory_validate_message(
            
        )
        
def test_validate_message_flow_value(
    
):
    with pytest.raises(InfobankException):
        get_message_flow_not_set_message(
            
        )

def test_validate_message_flow_duplicate_value(
    
):
    with pytest.raises(InfobankException):
        get_message_flow_duplicate_message(
            
        )


api = InfobankClient(
    api_url=Client.api_url,
    client_id=Client.client_id,
    client_passwd=Client.client_passwd
)

def test_sms_message(
    
):
    message=get_omni_message(
        get_omni_sms_message()
    )
    response = api.send_message(
        message=message
    )

    data = response.data
    destinations  = data.destinations
    
    request_body = json.dumps(
        message.dict(
            by_alias=True,
            exclude_none=True
            ),
        indent=2,
        sort_keys=True,
        ensure_ascii=False
    ),
    assert response.status_code == 200, "(request:{request}\nstatus_code:{status_code} response:{response})".format(
        request = request_body,
        status_code = response.status_code,
        response = response
    )
    assert response.code == 'A000', "(request:{request}\nresponse:{response})".format(
        request = request_body,
        response = response
    )
    for destination in destinations:
        assert len(destination.to) > 0 ,  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert destination.code == 'A000',  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert destination.result == 'Success',  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert len(destination.msg_key) > 0,  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
    
def test_mms_message(
    
):
    message=get_omni_message(
        get_omni_mms_message()
    )
    response = api.send_message(
        message=message
    )

    data = response.data
    destinations  = data.destinations
    
    request_body = json.dumps(
        message.dict(
            by_alias=True,
            exclude_none=True
            ),
        indent=2,
        sort_keys=True,
        ensure_ascii=False
    )
    assert response.status_code == 200, "(request:{request}\nstatus_code:{status_code} response:{response})".format(
        request = request_body,
        status_code = response.status_code,
        response = response
    )
    assert response.code == 'A000', "(request:{request}\nresponse:{response})".format(
        request = request_body,
        response = response
    )
    for destination in destinations:
        assert len(destination.to) > 0 ,  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert destination.code == 'A000',  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert destination.result == 'Success',  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert len(destination.msg_key) > 0,  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
    
@pytest.mark.parametrize(
    'button',
    [
        ([get_rcs_url_button()]),
        ([get_rcs_map_loc_button()]),
        ([get_rcs_map_qry_button()]),
        ([get_rcs_map_send_button()]),
        ([get_rcs_calendar_button()]),
        ([get_rcs_copy_button()]),
        ([get_rcs_com_t_button()]),
        ([get_rcs_com_v_button()]),
        ([get_rcs_dial_button()])
    ]
)
def test_rcs_standalone_message(
    button :List[RCSButton]
):    
    message=get_omni_message(
        get_omni_rcs_standalone_message(
            buttons=button
        )
    )
    response = api.send_message(
        message=message
    )
    
    data = response.data
    destinations  = data.destinations
    
    request_body = json.dumps(
        message.dict(
            by_alias=True,
            exclude_none=True
            ),
        indent=2,
        sort_keys=True,
        ensure_ascii=False
    )
    assert response.status_code == 200, "(request:{request}\nstatus_code:{status_code} response:{response})".format(
        request = request_body,
        status_code = response.status_code,
        response = response
    )
    assert response.code == 'A000', "(request:{request}\nresponse:{response})".format(
        request = request_body,
        response = response
    )
    for destination in destinations:
        assert len(destination.to) > 0 ,  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert destination.code == 'A000',  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert destination.result == 'Success',  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert len(destination.msg_key) > 0,  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
    
@pytest.mark.parametrize(
    'button',
    [
        ([get_rcs_url_button()]),
        ([get_rcs_map_loc_button()]),
        ([get_rcs_map_qry_button()]),
        ([get_rcs_map_send_button()]),
        ([get_rcs_calendar_button()]),
        ([get_rcs_copy_button()]),
        ([get_rcs_com_t_button()]),
        ([get_rcs_com_v_button()]),
        ([get_rcs_dial_button()])
    ]
)
def test_rcs_carousel_message(
    button :List[RCSButton]
):    
    message=get_omni_message(
        get_omni_rcs_carousel_message(
            get_omni_rcs_carousel(
                buttons=button
            ),
            get_omni_rcs_carousel(
                buttons=button
            ),
            get_omni_rcs_carousel(
                buttons=button
            )
        )
    )
    response = api.send_message(
        message=message
    )
    
    data = response.data
    destinations  = data.destinations
    
    request_body = json.dumps(
        message.dict(
            by_alias=True,
            exclude_none=True
            ),
        indent=2,
        sort_keys=True,
        ensure_ascii=False
    )
    assert response.status_code == 200, "(request:{request}\nstatus_code:{status_code} response:{response})".format(
        request = request_body,
        status_code = response.status_code,
        response = response
    )
    assert response.code == 'A000', "(request:{request}\nresponse:{response})".format(
        request = request_body,
        response = response
    )
    for destination in destinations:
        assert len(destination.to) > 0 ,  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert destination.code == 'A000',  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert destination.result == 'Success',  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert len(destination.msg_key) > 0,  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )

def test_rcs_template_messate(
    
):
    message=get_omni_message(
        get_omni_rcs_template_message()
    )
    response = api.send_message(
        message=message
    )

    data = response.data
    destinations  = data.destinations
    
    request_body = json.dumps(
        message.dict(
            by_alias=True,
            exclude_none=True
            ),
        indent=2,
        sort_keys=True,
        ensure_ascii=False
    )
    assert response.status_code == 200, "(request:{request}\nstatus_code:{status_code} response:{response})".format(
        request = request_body,
        status_code = response.status_code,
        response = response
    )
    assert response.code == 'A000', "(request:{request}\nresponse:{response})".format(
        request = request_body,
        response = response
    )
    for destination in destinations:
        assert len(destination.to) > 0 ,  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert destination.code == 'A000',  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert destination.result == 'Success',  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert len(destination.msg_key) > 0,  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        
@pytest.mark.parametrize(
    'msg_type, buttons, quick_reply_button',
    [
        (AlimTalkMessageType.AI, [get_alimtalk_al_button()], [get_alimtalk_al_button()]),
        (AlimTalkMessageType.AI, [get_alimtalk_bc_button()], [get_alimtalk_bc_button()]),
        (AlimTalkMessageType.AI, [get_alimtalk_bk_button()], [get_alimtalk_bk_button()]),
        (AlimTalkMessageType.AI, [get_alimtalk_bt_button()], [get_alimtalk_bt_button()]),
        (AlimTalkMessageType.AI, [get_alimtalk_ac_button()], []),
        (AlimTalkMessageType.AI, [get_alimtalk_bf_button()], [get_alimtalk_bf_button()]),
        (AlimTalkMessageType.AI, [get_alimtalk_ds_button()], []),
        (AlimTalkMessageType.AI, [get_alimtalk_md_button()], []),
        (AlimTalkMessageType.AI, [get_alimtalk_wl_button()], [get_alimtalk_wl_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_al_button()], [get_alimtalk_al_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_bc_button()], [get_alimtalk_bc_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_bk_button()], [get_alimtalk_bk_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_bt_button()], [get_alimtalk_bt_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_ds_button()], []),
        (AlimTalkMessageType.AT, [get_alimtalk_md_button()], []),
        (AlimTalkMessageType.AT, [get_alimtalk_wl_button()], [get_alimtalk_wl_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_ac_button()], []),
        (AlimTalkMessageType.AT, [get_alimtalk_bf_button()], [get_alimtalk_bf_button()]),
    ]
)
def test_alimtalk_message(
    msg_type :AlimTalkMessageType,
    buttons :List[AlimTalkButton],
    quick_reply_button :List[AlimTalkButton]
):    
    message=get_omni_message(
        get_omni_alimtalk_message(
            msg_type=msg_type,
            buttons=buttons,
            quick_reply_button=quick_reply_button
        )
    )
    response = api.send_message(
        message= message
    )
    data = response.data
    destinations  = data.destinations
    
    request_body = json.dumps(
        message.dict(
            by_alias=True,
            exclude_none=True
            ),
        indent=2,
        sort_keys=True,
        ensure_ascii=False
    )
    assert response.status_code == 200, "(request:{request}\nstatus_code:{status_code} response:{response})".format(
        request = request_body,
        status_code = response.status_code,
        response = response
    )
    assert response.code == 'A000', "(request:{request}\nresponse:{response})".format(
        request = request_body,
        response = response
    )
    for destination in destinations:
        assert len(destination.to) > 0 ,  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert destination.code == 'A000',  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert destination.result == 'Success',  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert len(destination.msg_key) > 0,  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )

@pytest.mark.parametrize(
    'message_flows',
    [
        (
            [
                get_omni_rcs_standalone_message(
                    buttons=[
                        get_rcs_dial_button(),
                        get_rcs_copy_button()
                    ]
                ),
                get_omni_sms_message(),
                get_omni_mms_message()
            ]
        ),
        (
            [
                get_omni_rcs_carousel_message(
                    get_omni_rcs_carousel(
                        buttons=[
                            get_rcs_calendar_button(),
                            get_rcs_url_button()
                        ]
                    ),
                    get_omni_rcs_carousel(
                        buttons=[
                            get_rcs_com_t_button(),
                            get_rcs_com_v_button()
                        ]
                    )
                ),
                get_omni_alimtalk_message(
                    msg_type=AlimTalkMessageType.AI,
                    buttons=[
                        get_alimtalk_al_button()
                    ]
                ),
                get_omni_sms_message()
            ]
        )
    ]
)
def test_send_omni_message(
    message_flows
):
    message=get_omni_message(
        *message_flows
    )
    response = api.send_message(
        message=message
    )
    
    data = response.data
    destinations  = data.destinations
    
    request_body = json.dumps(
        message.dict(
            by_alias=True,
            exclude_none=True
            ),
        indent=2,
        sort_keys=True,
        ensure_ascii=False
    )
    assert response.status_code == 200, "(request:{request}\nstatus_code:{status_code} response:{response})".format(
        request = request_body,
        status_code = response.status_code,
        response = response
    )
    assert response.code == 'A000', "(request:{request}\nresponse:{response})".format(
        request = request_body,
        response = response
    )
    for destination in destinations:
        assert len(destination.to) > 0 ,  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert destination.code == 'A000',  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert destination.result == 'Success',  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )
        assert len(destination.msg_key) > 0,  "(request:{request}\nresponse:{response})".format(
            request = request_body,
            response = response
        )