# 서비스 소개

---------------------------------------
## 개요
인포뱅크 OMNI API는 간편하게 연동 할 수 있는 통합메시지 API 입니다.

다양한 채널의 메시지 ( SMS, MMS, 국제메시지, RCS, 카카오 비즈메시지, PUSH 등 ) 발송 및 리포트 결과, 메시지 간 Fallback 기능을 제공합니다.


## 설치방법
infobank python sdk 설치를 위해서는 아래 명령어를 실행해야 합니다.

sdk는 python3.6이상부터 사용가능합니다.
```shell
python3 setup.py install
```


## 사용법

sdk 사용을 위해서는 [인포뱅크 비즈플러스](https://www.ibizplus.co.kr/main)를 통해 계정 발급 후 사용할 수 있습니다.

Api 인스턴트 생성 후 발송을 진행 할 수 있습니다.
```python
from infobank.infobank_client import (
    InfobankClient
)

api = InfobankClient(
    api_url= <api_url>,
    client_id = <client_id>,
    client_passwd = <client_passwd>
)
```

SMS 발송 예제 소스 입니다.
```python
from infobank.sms.models import (
    SMSMessage
)

message = SMSMessage(
    from_='0316281500',
    to='01012341234',
    text='안녕하세요. SMS 테스트 메시지입니다.'
)
```
message 생성후 아래 api 인스턴트로 발송할 수 있습니다.
```python
response = api.send_message(
    message=message
)
```
response 응답 결과는 ResponseApi Object로 내려갑니다.
```python

class ResponseApi(
    *,
    status_code: int | None = None,
    response: Response | None = None,
    code: str,
    result: str,
    msg_key: str | None,
    ref: str | None
)

status_code=200 response=<requests.Response [200]> code='A000' result='Success' msg_key='<msgKey>' ref=<ref>
```

## 레포트 수신

레포트는 polling 방식으로 제공되며 아래와 같이 수신 받을 수 있습니다.

InfobankClient 인스턴트를 생성합니다.
```python
from infobank.infobank_client import (
    InfobankClient
)

api = InfobankClient(
    api_url= <api_url>,
    client_id = <client_id>,
    client_passwd = <client_code>
)
```

request_results() 함수를 호출하여 레포트를 수신합니다.
```python
response = api.request_reports()
```

레포트는 List형태로 아래와 같이 수신됩니다.
```python
status_code=200 response=<Response [200]> code='A000' result='Success' data=ReportData(report_id='20230713100013607R1000002607', report=[Report(msg_key='20230711231841908DEVR1RC00043700', service_type='RCS', msg_type='', report_type='0', report_code='10000', report_text=None, report_time='2023-07-12T08:18:41+09:00', carrier='10000', res_cnt=None, ref='ref')]
```

레포트 수신 확인 후 reportId로 delete method를 호출해야 다음 레포트를 받을 수 있습니다.

```python
api.delete_reports(
    report_id = response.data.report_id
)
```


자세한 규격 및 결과코드는 [Omni Api Specification](https://infobank-guide.gitbook.io/omni_api) 에서 확인 할 수 있습니다.


## Docker 사용예제
omni_sdk_python 디렉토리 경로에서 아래 명령어로 이미지 생성을 합니다.
```shell
docker build . -t infobank-omni-sdk-python:latest
```

이미지 생성 후 아래 명령어로 컨테이너를 생성 후 컨테이너에 진입합니다.
```shell
docker run -it --name infobank-omni-sdk-python infobank-omni-sdk-python:latest 
docker run -it infobank-omni-sdk-python python
````

위 사용법을 참고하여 발송이 가능합니다.
