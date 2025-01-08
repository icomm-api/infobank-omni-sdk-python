from infobank.infobank_client import (
    InfobankClient
)
from infobank.client import (
    Client
)

report_id=""
api = InfobankClient(
    api_url=Client.api_url,
    client_id=Client.client_id,
    client_passwd=Client.client_passwd
)

def test_get_reports(
    
):
    response = api.request_reports(
        
    )
    
    assert response.status_code == 200, "(status_code:{status_code}, {response})".format(
        status_code = response.status_code,
        response = response
    )
    assert response.code == 'A000', response
    
    report_id = response.data.report_id
    

""" def test_delete_reports(
    
):
    test_get_reports(
        
    )

    response = api.delete_reports(
        report_id= report_id
    )
    
    if (len(report_id) > 0 ):
        assert response.status_code == 200, "(status_code:{status_code} response:{response})".format(
            status_code = response.status_code,
            response = response
        )
        assert response.code == "A000", "(status_code:{status_code} response:{response})".format(
            status_code = response.status_code,
            response = response
            
        )
    else :
        assert response.status_code == 404, "(status_code:{status_code} response:{response})".format(
            status_code = response.status_code,
            response = response
        )
     """