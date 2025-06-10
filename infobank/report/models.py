from typing import (
    List,
    Optional
)
from infobank.core.models import (
    CamelCaseModel,
    RequsetMessage,
    _ResponseApi
)

class Report(CamelCaseModel):
    msg_key :str
    service_type :str
    msg_type :str
    report_type :str
    report_code :str
    report_text :Optional[str]
    report_time :str
    carrier :Optional[str]
    res_cnt :Optional[str]
    user_type: Optional[str]
    ref :Optional[str]

class ReportData(RequsetMessage):
    report_id :Optional[str]
    report :Optional[List[Report]]
    
class ResponseApi(_ResponseApi):
    data :Optional[ReportData]
