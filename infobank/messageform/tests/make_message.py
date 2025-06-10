from typing import (
    List
)
from infobank.messageform.models import (
    MessageFormMessage,
    MessageForm,
)
from infobank.messageform.models import (
    SMSMessage
)
from infobank.messageform.models import (
    MMSMessage
)
from infobank.messageform.models import (
    RCSMessage,
    RCSContent,
    RCSStandAlone,
    RCSCarousel,
    RCSTemplate,
    RCSSubContent,
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

from infobank.messageform.models import (
    make_rcs_dial_button,
    make_rcs_calendar_button,
    make_rcs_com_t_button,
    make_rcs_com_v_button,
    make_rcs_copy_button,
    make_rcs_map_loc_button,
    make_rcs_map_qry_button,
    make_rcs_map_send_button,
    make_rcs_url_button
)
from infobank.messageform.models import (
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


def get_mandantory_validate_message(
    
) -> MessageForm:
    return MessageForm(
        sms=SMSMessage(
            text='text'
        )
    )
    
def get_messageform_sms_message(
    
) -> MessageForm:
    return MessageForm(
            sms = SMSMessage(
            from_='0316281500',
            text='text',
            origin_cid='1234',
            ttl='86400'
        )
    )
    
def get_messageform_mms_message(
    
) -> MessageForm:
    return MessageForm(
        mms = MMSMessage(
            from_='0316281500',
            title='title',
            text='text',
            file_key=[
                'filekey'
            ],
            origin_cid='1234',
            ttl='86400'
        )
    )

def get_messageform_rcs_standalone_message(
    buttons :List[RCSButton] = None
) -> MessageForm:
    return MessageForm(
        rcs = RCSMessage(
            from_='0316281500',
            content = RCSContent(
                standalone=RCSStandAlone(
                    text='text',
                    title='title',
                    button=buttons,
                    sub_content=[
                        RCSSubContent(
                            sub_title='subTitle',
                            sub_desc='subDesc',
                            sub_media='subMedia',
                            sub_media_url='subMediaUrl'
                        )
                    ]
                )
            ),
            format_id='formatId',
            group_id='groupid',
            expiry_option='1',
            copy_allowed='1',
            header='1',
            footer='1234',
            brand_id='brandId',
            brand_key='brandKey',
            agency_id='agencyId',
            agency_key='agencyKey',
            ttl=86400
        )
    )
    
def get_messageform_rcs_carousel(
    buttons :List[RCSButton] = None
) -> RCSCarousel:
    return RCSCarousel(
        text='text',
        title='title',
        media='media',
        media_url='mediaUrl',
        button=buttons
    )

def get_messageform_rcs_carousel_message(
    *carousel : RCSCarousel
) -> MessageForm:
    return MessageForm(
        rcs = RCSMessage(
            from_='0316281500',
            content = RCSContent(
                carousel=list(carousel)
            ),
            format_id='formatId',
            group_id='groupid',
            expiry_option='1',
            copy_allowed='1',
            header='1',
            footer='1234',
            brand_id='brandId',
            brand_key='brandKey',
            agency_id='agencyId',
            agency_key='agencyKey',
            ttl=86400
        )
    )

def get_messageform_rcs_template_message(
    
) -> MessageForm:
    return MessageForm(
        rcs = RCSMessage(
            from_='0316281500',
            content=RCSContent(
                template=RCSTemplate(
                    description='description',
                    sub_content=RCSSubContent(
                        sub_title='subTitle',
                        sub_desc='subDesc',
                        sub_media='subMedia',
                        sub_media_url='subMediaUrl'
                    )
                )
            ),
            format_id='formatId',
            group_id='groupid',
            expiry_option='1',
            copy_allowed='1',
            header='1',
            footer='1234',
            brand_id='brandId',
            brand_key='brandKey',
            agency_id='agencyId',
            agency_key='agencyKey',
            ttl=86400
        )
    )
    
def get_rcs_url_button(
    
) -> RCSButton:
    return make_rcs_url_button(
        name='name',
        url='http://'
    )
    
def get_rcs_map_loc_button(
    
) -> RCSButton:
    return make_rcs_map_loc_button(
        name = 'name',
        label= 'label',
        latitude='37.4220041',
        longitude='-122.0862515',
        fallback_url='https://'
    )

def get_rcs_map_qry_button(
    
) -> RCSButton:
    return make_rcs_map_qry_button(
        name = 'name',
        query= 'query',
        fallback_url='https://'
    )

def get_rcs_map_send_button(
    
) -> RCSButton:
    return make_rcs_map_send_button(
        name = 'name'
    )
    
def get_rcs_calendar_button(
    
) -> RCSButton:
    return make_rcs_calendar_button(
        name = 'name',
        start_time='startTime',
        end_time='endTime',
        title='제목',
        description='설명'
    )
    
def get_rcs_copy_button(
    
) -> RCSButton:
    return make_rcs_copy_button(
        name= 'name',
        text= 'text'
    )
    
def get_rcs_com_t_button(
    
) -> RCSButton:
    return make_rcs_com_t_button(
        name = 'name',
        phone_number='01012341234',
        text='text'
    )
    
def get_rcs_com_v_button(
    
) -> RCSButton:
    return make_rcs_com_v_button(
        name = 'name',
        phone_number='01012341234'   
    )

def get_rcs_dial_button(
    
) -> RCSButton:
    return make_rcs_dial_button(
        name = 'name',
        phone_number='01012341234'
    )
    

def get_messageform_alimtalk_message(
    msg_type :AlimTalkMessageType,
    buttons :List[AlimTalkButton] = None,
    quick_reply_button :List[AlimTalkButton] = None
) -> MessageForm:
    return MessageForm(
        alimtalk=AlimTalkMessage(
            sender_key='senderKey',
            msg_type=msg_type,
            template_code='templateCode',
            text='text',
            title='title',
            attachment=AlimTalkAttachMent(
                button=buttons,
                item=AlimTalkAttachMentItem(
                    list=[
                        AlimTalkAttachMentItemList(
                            title='title',
                            description='description'
                        ),
                        AlimTalkAttachMentItemList(
                            title='title',
                            description='description'
                        ),
                    ],
                    summary=AlimTalkAttachMentItemSummary(
                        title='title',
                        description='description'
                    )
                ),
                item_highlight=AlimTalkAttachMentItemHighlight(
                    title='title',
                    description='description'
                )
            ),
            supplement=AlimTalkSupplement(
                quick_reply=quick_reply_button
            ),
            price='100',
            currency_type='KWR'
        )
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
