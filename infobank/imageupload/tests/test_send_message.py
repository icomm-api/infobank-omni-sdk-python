#-*-coding:utf-8-*-
import pytest

from pydantic import (
    ValidationError
)
from infobank.infobank_client import (
    InfobankClient
)
from infobank.imageupload.tests.make_message import (
    get_mandantory_validate_message,
    get_mms_image_file,
    get_rcs_image_file
)
from infobank.client import (
    Client
)

api = InfobankClient(
    api_url=Client.api_url,
    client_id=Client.client_id,
    client_passwd=Client.client_passwd
)

def test_validate_mandatory_value(
    
):
    with pytest.raises(ValidationError):
        get_mandantory_validate_message()
   

def test_mms_image_file_upload(

):
    response = api.request_image_upload(
        image_file=get_mms_image_file(
            
        )
    )
    
    data = response.data
    
    assert response.status_code == 200, "(status_code:{status_code}, {response})".format(
        status_code = response.status_code,
        response = response
    )
    assert response.code == 'A000', response
    assert len(data.file_key) > 0, response
    

def test_rcs_image_file_upload(
    
):
    response = api.request_image_upload(
        image_file=get_rcs_image_file(
            
        )
    )
    
    data = response.data
    
    assert response.status_code == 200, "(status_code:{status_code}, {response})".format(
        status_code = response.status_code,
        response = response
    )
    assert response.code == 'A000', response
    assert len(data.media) > 0, response