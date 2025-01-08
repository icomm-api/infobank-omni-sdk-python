from infobank.sms.models import (
    SMSMessage
)

def get_mandantory_validate_message(

) -> SMSMessage:
    return SMSMessage(
        from_='1234',
        to='12341234'
    )

def get_sms_message(
    
) -> SMSMessage:
    return SMSMessage(
        from_='0316281500',
        to='01012341234',
        text='text'
    )