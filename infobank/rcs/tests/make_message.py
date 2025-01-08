from typing import (
    List,
)
from infobank.rcs.models import (
    RCSMessage,
    RCSContent,
    RCSStandAlone,
    RCSCarousel,
    RCSTemplate,
    RCSButton,
    RCSFallBack,
    RCSFallBackType,
    RCSSubContent
)
from infobank.rcs.models import (
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


def get_mandantory_validate_message(
    
) -> RCSMessage:
    return RCSMessage(
        from_='1234',
        to='12341234'
    )

def get_content_not_set_message(
    
) -> RCSMessage:
    return RCSMessage(
        from_= '0316281500',
        to= '01012341234',
        content=RCSContent(
            
        ),
        brand_key='brandKey',
        brand_id='brandId',
        format_id='formatId',
        ref=''
    )
    
def get_content_validate_message(
    
) -> RCSMessage:
    return RCSMessage(
        from_= '0316281500',
        to= '01012341234',
        content=RCSContent(
            standalone=RCSStandAlone(
                title='title',
                text='text',
                media='media',
            ),
            template=RCSTemplate(
                description='description'
            )
        ),
        brand_key='brandKey',
        brand_id='brandId',
        format_id='formatId',
        ref=''
    )

def get_rcs_standalone_message(
    buttons :List[RCSButton] = None
) -> RCSMessage:
    return RCSMessage(
        from_= '0316281500',
        to= '01012341234',
        content=RCSContent(
            standalone=RCSStandAlone(
                title='title',
                text='text',
                media='media',
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
        brand_key='brandKey',
        brand_id='brandId',
        format_id='formatId',
        ref=''
    )
    
def get_rcs_carousel(
    buttons :List[RCSButton] = None
) -> RCSCarousel:
    return RCSCarousel(
        title='title',
        text='text',
        media='media',
        media_url='mediaUrl',
        button=buttons
    )
    
def get_rcs_carousel_message(
    *carousel :RCSCarousel
) -> RCSMessage:
    return RCSMessage(
        from_='0316281500',
        to='01012341234',
        content=RCSContent(
            carousel=list(carousel)
        ),
        brand_key='brandKey',
        brand_id='brandId',
        format_id='formatId',
        ref=''
    )
    
def get_rcs_template_message(
    
) -> RCSMessage:
    return RCSMessage(
        from_='0316281500',
        to='01012341234',
        content=RCSContent(
            template=RCSTemplate(
                description='description',
                sub_content=[
                    RCSSubContent(
                        sub_title='subTitle',
                        sub_desc='subDesc',
                        sub_media='subMdeia',
                        sub_media_url='subMediaUrl'
                    )
                ]
            )
        ),
        brand_key='brandKey',
        brand_id='brandId',
        format_id='formatId',
        ref=''
    )
    
def get_rcs_cell_message(
    
) -> RCSMessage:
    return RCSMessage(
        from_='0316281500',
        to='01012341234',
        content=RCSContent(
            template=RCSTemplate(
                name= 'name'
            )
        ),
        format_id='formatId',
        ref='',
        brand_key='brandKey'
    )
    
def get_fallback_message(
    
) -> RCSMessage:
    return RCSMessage(
        from_='0316281500',
        to='01012341234',
        content=RCSContent(
            standalone=RCSStandAlone(
                text='text'
            ),
        ),
        format_id='formatId',
        ref='',
        fallback=RCSFallBack(
            type= RCSFallBackType.SMS,
            text='fallback text'
        ),
        brand_key='brandKey'
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
    