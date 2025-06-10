from typing import List
from infobank.kko.models import (
    AlimTalkMessage,
    AlimTalkMessageType,
    AlimTalkButton,   
    AlimTalkFallBack,
    AlimTalkFallBackType
)
from infobank.kko.models import (
    make_alimtalk_al_button,
    make_alimtalk_bc_button,
    make_alimtalk_bk_button,
    make_alimtalk_bt_button,
    make_alimtalk_ds_button,
    make_alimtalk_md_button,
    make_alimtalk_wl_button,
    make_alimtalk_ac_button,
    make_alimtalk_bf_button
)

def get_mandantory_validate_alimtalk_message(
    msg_type :AlimTalkMessageType
) -> AlimTalkMessage:
    return AlimTalkMessage(
        msg_type=msg_type,
        text='text',
        sender_key='senderKey',
        to='01012341234',
    )
    
def get_alimtalk_message(
    msg_type :AlimTalkMessageType,
    buttons :List[AlimTalkButton] = None
) -> AlimTalkMessage:
    return AlimTalkMessage(
        template_code='templateCode',
        msg_type=msg_type,
        text='text',
        sender_key='senderKey',
        to='01012341234',
        button=buttons
    )
 
def get_alimtalk_wl_button(
    
) -> AlimTalkButton:
    return make_alimtalk_wl_button(
        name='name',
        url_mobile='urlMobile',
        url_pc='urlPc'
    )
    
def get_alimtalk_al_button(
    
) -> AlimTalkButton:
    return make_alimtalk_al_button(
        name='name',
        scheme_android='schemeAndroid',
        scheme_ios='schemeIos',
        url_mobile='urlMobile',
        url_pc='urlPc'
    )
    
def get_alimtalk_bk_button(
    
) -> AlimTalkButton:
    return make_alimtalk_bk_button(
        name='name'
    )
    
def get_alimtalk_md_button(
    
) -> AlimTalkButton:
    return make_alimtalk_md_button(
        name='name'
    )
    
def get_alimtalk_ds_button(
    
) -> AlimTalkButton:
    return make_alimtalk_ds_button(
        name='name'
    )
    
def get_alimtalk_bc_button(
    
) -> AlimTalkButton:
    return make_alimtalk_bc_button(
        name='name',
        chat_extra='chatExtra'
    )
    
def get_alimtalk_bt_button(
    
) -> AlimTalkButton:
    return make_alimtalk_bt_button(
        name='버튼명',
        chat_extra='chatExtra',
        chat_event='chatEvent'
    )
    
def get_alimtalk_ac_button(
    
) -> AlimTalkButton:
    return make_alimtalk_ac_button(
        name='버튼명'
    )
    
def get_alimtalk_bf_button(
    
) -> AlimTalkButton:
    return make_alimtalk_bf_button(
        name='버튼명',
        biz_form_id='bizFormId',
        biz_form_key='bizFormKey'
    )
    
def get_alimtalk_fallback_message(
    msg_type :AlimTalkMessageType,
    buttons :List[AlimTalkButton] = None
) -> AlimTalkMessage:
    return AlimTalkMessage(
        template_code='templateCode',
        msg_type=msg_type,
        text='text',
        sender_key='senderKey',
        to='01012341234',
        button=buttons,
        fallback=AlimTalkFallBack(
            type = AlimTalkFallBackType.MMS,
            from_='0316281500',
            title='title',
            text='text'
        )
    )