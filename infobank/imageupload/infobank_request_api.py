from infobank.core.infobank_request_api import (
    _InfobankApi
)


class ImageUploadApi(_InfobankApi):
    from infobank.imageupload.models import (
        ImageFile,
        ResponseApi
    )
    @classmethod
    def request_image_file(
        cls,
        image_file :ImageFile
    ) -> ResponseApi:
        """이미지 업로드는 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/management/file
        
        응답 결과 json 포맷은 아래 페이지에서 확인 가능합니다.
        
        https://infobank-guide.gitbook.io/omni_api/api-reference/management/file#response
        
        Args:
            message (ImageFile): 

        Returns:
            class ResponseApi(
                *,
                status_code: int | None = None,
                response: Response | None = None,
                code: str,
                result: str,
                data: Data | None
            )
        """
        response = cls.http_client.request_image_file_to_api(
            image_file = image_file
        )
        
        from infobank.imageupload.models import (
        ResponseApi
    )
        
        return ResponseApi(
            **response.json(),
            status_code=response.status_code,
            response=response
        )

