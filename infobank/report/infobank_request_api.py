from infobank.core.infobank_request_api import (
    _InfobankApi,
)
from infobank.report.models import(
    ResponseApi
)
class ReportApi (_InfobankApi):
    @classmethod
    def request_reports(
        cls
    ) -> ResponseApi:
        """리포트 조회는 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/report/polling#get

        Returns:
            class ResponseApi(
                *,
                status_code: int | None = None,
                response: Response | None = None,
                code: str,
                result: str,
                data: ReportData | None
            )
        """
        response = cls.http_client.request_reports_to_api(
            
        )
        return ResponseApi(
            **response.json(),
            status_code=response.status_code,
            response=response
        )
    
    @classmethod
    def delete_reports(
        cls,
        report_id :str
    ) -> ResponseApi:
        """리포트 삭제는 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/report/polling#delete

        Args:
            report_id (str): 조회 시 받은 report Id

        Returns:
            class ResponseApi(
                *,
                status_code: int | None = None,
                response: Response | None = None,
                code: str,
                result: str,
                data: ReportData | None
            )
        """
        response = cls.http_client.delete_result_to_api(
            report_id= report_id
        )
        
        return ResponseApi(
            **response.json(),
            status_code=response.status_code,
            response=response
        )
        
    @classmethod
    def inquiry_report(
        cls,
        report_id: str
    )-> ResponseApi:
        """메시지키를 기준으로 리포트를 조회합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/report/inquiry

        Args:
            report_id (str): 메시지 키

        Returns:
            class ResponseApi(
                *,
                status_code: int | None = None,
                response: Response | None = None,
                code: str,
                result: str,
                data: ReportData | None
            )
        """
        response = cls.http_client.inquiry_report(
            report_id=report_id
        )
        
        return ResponseApi(
            **response.json(),
            status_code=response.status_code,
            response=response
        )
        