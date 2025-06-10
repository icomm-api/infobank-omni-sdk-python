from infobank.international.models import (
    InterSMSMessage
)

def get_mandantory_validate_message(

) -> InterSMSMessage:
    return InterSMSMessage(
        from_='1234',
        to='12341234'
    )
    
def get_validate_to_message(
    
) -> InterSMSMessage:
    return InterSMSMessage(
        from_='0316281500',
        to='01012341234',
        text='text'
    )
    
def get_international_sms_message(
    
) -> InterSMSMessage:
    return InterSMSMessage(
        from_='0316281500',
        to='+841012341234',
        text='text'
    )