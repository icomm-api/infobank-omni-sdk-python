from infobank.mms.models import (
    MMSMessage
)

def get_mandantory_validate_message(

) -> MMSMessage:
    return MMSMessage(
        from_='1234',
        to='12341234'
    )

def get_mms_message(
    
) -> MMSMessage:
    return MMSMessage(
        from_='0316281500',
        to='01012341234',
        title='title',
        text='text',
        file_key=[
            'fileKey1',
            'fileKey2',
            'fileKey3'
        ],
        ref='ref'
    )