from typing import List
import pytest
import json
from pydantic import (
    ValidationError
)

from infobank.infobank_client import (
    InfobankClient
)
from infobank.messageform.models import (
    MessageFormMessage,
    MessageForm,
    ResponseApi,
    Data
)
from infobank.messageform.models import (
    SMSMessage
)
from infobank.messageform.models import (
    MMSMessage
)
from infobank.messageform.models import (
    RCSMessage,
    RCSStandAlone,
    RCSCarousel,
    RCSTemplate,
    RCSButton,
    RCSButtonType
)
from infobank.messageform.models import (
    AlimTalkMessage,
    AlimTalkMessageType,
    AlimTalkAttachMent,
    AlimTalkAttachMentItem,
    AlimTalkAttachMentItemHighlight,
    AlimTalkAttachMentItemSummary,
    AlimTalkSupplement,
    AlimTalkButtonType,
    AlimTalkButton,
    AlimTalkAttachMentItemList
)
from infobank.messageform.tests.make_message import (
    get_mandantory_validate_message,
    get_messageform_sms_message,
    get_messageform_mms_message,
    get_messageform_rcs_standalone_message,
    get_messageform_rcs_carousel,
    get_messageform_rcs_carousel_message,
    get_messageform_rcs_template_message,
    get_messageform_alimtalk_message
)
from infobank.messageform.tests.make_message import (
    get_rcs_calendar_button,
    get_rcs_com_t_button,
    get_rcs_com_v_button,
    get_rcs_copy_button,
    get_rcs_dial_button,
    get_rcs_map_loc_button,
    get_rcs_map_qry_button,
    get_rcs_map_send_button,
    get_rcs_url_button
)
from infobank.messageform.tests.make_message import (
    get_alimtalk_al_button,
    get_alimtalk_bc_button,
    get_alimtalk_bk_button,
    get_alimtalk_bt_button,
    get_alimtalk_ds_button,
    get_alimtalk_md_button,
    get_alimtalk_wl_button,
    get_alimtalk_ac_button,
    get_alimtalk_bf_button
)
from infobank.client import (
    Client
)

api = InfobankClient(
    api_url=Client.api_url,
    client_id=Client.client_id,
    client_passwd=Client.client_passwd
)

def test_validate_mandatory_value():
    with pytest.raises(ValidationError):
        get_mandantory_validate_message()


@pytest.mark.parametrize(
    'message_forms',
    [
        (
            [
                get_messageform_sms_message()
            ]
        ),
        (
            [
                get_messageform_mms_message()
            ]
        ),
        (
            [
                get_messageform_rcs_standalone_message()
            ]
        ),
        (
            [
                get_messageform_rcs_carousel_message(
                    get_messageform_rcs_carousel(
                        
                    )
                )
            ]
        ),
        (
            [
                get_messageform_alimtalk_message(
                    msg_type=AlimTalkMessageType.AI
                )    
            ]
        ),
        (
            [
                get_messageform_alimtalk_message(
                    msg_type=AlimTalkMessageType.AT
                )   
            ]
        )
    ]
)
def test_create_messageform(
    message_forms :List[MessageForm]
):
    message=MessageFormMessage(
        message_form=message_forms
    )
    response =api.create_message_form(
        message=message
    )
    
    requset_body = json.dumps(
        message.dict(
            by_alias=True,
            exclude_none=True
            ),
        indent=2,
        sort_keys=True,
        ensure_ascii=False
    )
    response =api.create_message_form(
        message= message
    )
    
    requset_body = json.dumps(
        message.dict(
            by_alias=True,
            exclude_none=True
            ),
        indent=2,
        sort_keys=True,
        ensure_ascii=False
    )
    assert response.status_code == 200, "(request:{request}\nstatus_code:{status_code} response:{response})".format(
        request = requset_body,
        status_code = response.status_code,
        response = response
    )
    assert response.code == 'A000', "(request:{request}\nresponse:{response})".format(
        request = requset_body,
        response = response
    )
    assert response.result == 'Success', "(request:{request}\nresponse:{response})".format(
        request = requset_body,
        response = response
    )


@pytest.mark.parametrize(
    'buttons',
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
def test_create_rcs_standalone_messageform(
    buttons :List[RCSButton]
):
    message=MessageFormMessage(
        message_form=[
            get_messageform_rcs_standalone_message(
                buttons=buttons
            )
        ]
    )
    response =api.create_message_form(
        message= message
    )
    
    requset_body = json.dumps(
        message.dict(
            by_alias=True,
            exclude_none=True
            ),
        indent=2,
        sort_keys=True,
        ensure_ascii=False
    )
    assert response.status_code == 200, "(request:{request}\nstatus_code:{status_code} response:{response})".format(
        request = requset_body,
        status_code = response.status_code,
        response = response
    )
    assert response.code == 'A000', "(request:{request}\nresponse:{response})".format(
        request = requset_body,
        response = response
    )
    assert response.result == 'Success', "(request:{request}\nresponse:{response})".format(
        request = requset_body,
        response = response
    )
    
@pytest.mark.parametrize(
    'buttons',
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
def test_create_rcs_carousel_messageform(
    buttons :List[RCSButton]
):
    message=MessageFormMessage(
        message_form=[
            get_messageform_rcs_carousel_message(
                get_messageform_rcs_carousel(
                    buttons=buttons
                )
            )
        ]
    )
    response =api.create_message_form(
        message= message
    )
    
    requset_body = json.dumps(
        message.dict(
            by_alias=True,
            exclude_none=True
            ),
        indent=2,
        sort_keys=True,
        ensure_ascii=False
    )
    assert response.status_code == 200, "(request:{request}\nstatus_code:{status_code} response:{response})".format(
        request = requset_body,
        status_code = response.status_code,
        response = response
    )
    assert response.code == 'A000', "(request:{request}\nresponse:{response})".format(
        request = requset_body,
        response = response
    )
    assert response.result == 'Success', "(request:{request}\nresponse:{response})".format(
        request = requset_body,
        response = response
    )
    

def test_create_rcs_template_messageform(
    
):
    message=MessageFormMessage(
        message_form=[
            get_messageform_rcs_template_message()
        ]
    )
    response =api.create_message_form(
        message= message
    )
    
    requset_body = json.dumps(
        message.dict(
            by_alias=True,
            exclude_none=True
            ),
        indent=2,
        sort_keys=True,
        ensure_ascii=False
    )
    assert response.status_code == 200, "(request:{request}\nstatus_code:{status_code} response:{response})".format(
        request = requset_body,
        status_code = response.status_code,
        response = response
    )
    assert response.code == 'A000', "(request:{request}\nresponse:{response})".format(
        request = requset_body,
        response = response
    )
    assert response.result == 'Success', "(request:{request}\nresponse:{response})".format(
        request = requset_body,
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
        (AlimTalkMessageType.AI, [get_alimtalk_bf_button()], []),
        (AlimTalkMessageType.AI, [get_alimtalk_ds_button()], []),
        (AlimTalkMessageType.AI, [get_alimtalk_md_button()], []),
        (AlimTalkMessageType.AI, [get_alimtalk_wl_button()], [get_alimtalk_wl_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_al_button()], [get_alimtalk_al_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_bc_button()], [get_alimtalk_bc_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_bk_button()], [get_alimtalk_bk_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_bt_button()], [get_alimtalk_bt_button()]),
        (AlimTalkMessageType.AT, [get_alimtalk_ac_button()], []),
        (AlimTalkMessageType.AT, [get_alimtalk_bf_button()], []),
        (AlimTalkMessageType.AT, [get_alimtalk_ds_button()], []),
        (AlimTalkMessageType.AT, [get_alimtalk_md_button()], []),
        (AlimTalkMessageType.AT, [get_alimtalk_wl_button()], [get_alimtalk_wl_button()]),
    ]
)
def test_create_alimtalk_messageform(
    msg_type :AlimTalkMessageType,
    buttons :List[AlimTalkButton],
    quick_reply_button :List[AlimTalkButton]
):
    message=MessageFormMessage(
        message_form=[
            get_messageform_alimtalk_message(
                msg_type=msg_type,
                buttons=buttons,
                quick_reply_button=quick_reply_button
            )
        ]
    )
    response =api.create_message_form(
        message= message
    )
    
    requset_body = json.dumps(
        message.dict(
            by_alias=True,
            exclude_none=True
            ),
        indent=2,
        sort_keys=True,
        ensure_ascii=False
    )
    assert response.status_code == 200, "(request:{request}\nstatus_code:{status_code} response:{response})".format(
        request = requset_body,
        status_code = response.status_code,
        response = response
    )
    assert response.code == 'A000', "(request:{request}\nresponse:{response})".format(
        request = requset_body,
        response = response
    )
    assert response.result == 'Success', "(request:{request}\nresponse:{response})".format(
        request = requset_body,
        response = response
    )
