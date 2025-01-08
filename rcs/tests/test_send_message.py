#-*-coding:utf-8-*-
import pytest
import json

from pydantic import (
    ValidationError
)
from infobank.rcs.exceptions import(
    InfobankException
)
from infobank.infobank_client import (
    InfobankClient
)
from infobank.client import (
    Client
)

from infobank.rcs.tests.make_message import(
    get_mandantory_validate_message,
    get_content_not_set_message,
    get_content_validate_message,
    get_rcs_standalone_message,
    get_rcs_carousel_message,
    get_rcs_template_message,
    get_rcs_cell_message,
    get_fallback_message,
    get_rcs_carousel,
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

api = InfobankClient(
    api_url=Client.api_url,
    client_id=Client.client_id,
    client_passwd=Client.client_passwd
)

def test_validate_mandatory_value(
    
):
    with pytest.raises(ValidationError):
        get_mandantory_validate_message(
            
        )

def test_content_not_set_validation(
    
):
    with pytest.raises(InfobankException):
        get_content_not_set_message(
            
        )

def test_content_validation(
    
):
    with pytest.raises(InfobankException):
        get_content_validate_message(
            
        )


@pytest.mark.parametrize(
    'buttons',
    [
        (),
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
def test_standalone_message(
    buttons
):    
    message=get_rcs_standalone_message(
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
def test_carousel_message(
    buttons
):   
    message=get_rcs_carousel_message(
        get_rcs_carousel(
            buttons=buttons
        ),
        get_rcs_carousel(
            buttons=buttons
        ),
        get_rcs_carousel(
            buttons=buttons
        )
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
   
def test_template_message():
    message=get_rcs_template_message()
    
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
    
def test_cell_message():
    message=get_rcs_cell_message()
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
    
def test_fallback_message():
    message=get_fallback_message()
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