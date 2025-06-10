from typing import (
    Optional,
    List,
)
from infobank.rcs.exceptions import(
    InfobankException
)
from infobank.core.models import(
    _ResponseApi,
    _RCSButtonType,
    _RCSButton,
    _RCSSubContent,
    _RCSStandAlone,
    _RCSCarousel,
    _RCSTemplate,
    _RCSContent,
    _RCSMessage,
    _FallBackType,
    _FallBack
)


class RCSButtonType(_RCSButtonType):
    pass
    
class RCSButton(_RCSButton):
    """RCS 버튼는 아래 페이지에서 확인 가능합니다.

    https://infobank-guide.gitbook.io/omni_api/api-reference/send/rcs#rcs-button
    
    아래 정의된 함수를 사용하면 보다 편하게 작성이 가능합니다.
    
    from infobank.rcs.models import (\n
        make_rcs_dial_button,\n
        make_rcs_calendar_button,\n
        make_rcs_com_t_button,\n
        make_rcs_com_v_button,\n
        make_rcs_copy_button,\n
        make_rcs_map_loc_button,\n
        make_rcs_map_qry_button,\n
        make_rcs_map_send_button,\n
        make_rcs_url_button\n
    )
        
    """
    pass

class RCSSubContent(_RCSSubContent):
    """RCS subContent는 아래 페이지에서 확인 가능합니다.

    https://infobank-guide.gitbook.io/omni_api/api-reference/send/rcs#subcontent
    """
    pass

class RCSStandAlone(_RCSStandAlone):
    pass

class RCSCarousel(_RCSCarousel):
    pass

class RCSTemplate(_RCSTemplate):
    pass

class RCSFallBackType(_FallBackType):
    pass

class RCSFallBack(_FallBack):
    """RCS fallback는 아래 페이지에서 확인 가능합니다.

    https://infobank-guide.gitbook.io/omni_api/api-reference/send/rcs#fallback
        
    fallback 메시지는 SMS/MMS만 가능합니다.

    """
    pass

class RCSContent(_RCSContent):
    pass
    
class RCSMessage(_RCSMessage):
    """RCS는 아래 페이지에서 확인 가능합니다.

    https://infobank-guide.gitbook.io/omni_api/api-reference/send/rcs#request
    """
    to :str
    content :Optional[RCSContent]
    fallback :Optional[RCSFallBack]
    ref :Optional[str]
    

class ResponseApi(_ResponseApi):
    msg_key :Optional[str]
    ref :Optional[str]
    
    
def make_rcs_url_button(
    name :str,
    url :str = None
) -> RCSButton:
    """URL 연결
    
    Web page 또는 App으로 이동할 수 있습니다.

    Args:
        name (str): 버튼 명
        url (str, optional): 웹브라우저로 연결할 URL주소

    Returns:
        RCSButton: RCS 버튼 인스턴트
    """
    return RCSButton(
        type=RCSButtonType.URL,
        name=name,
        url=url
    )

def make_rcs_map_loc_button(
    name :str,
    label :str = None,
    latitude :str = None,
    longitude :str = None,
    fallback_url :str = None
) -> RCSButton:
    """지도 보여주기
    
    지정된 좌표로 설정된 지도 App을 실행합니다.

    Args:
        name (str): 버튼 명
        label (str, optional): 지도 App에 표시될 라벨명
        latitude (str, optional): 위도 값 (예)37.4001971
        longitude (str, optional): 경도 값 (예)127.1071718
        fallback_url (str, optional): 지도 App동작이 안 될 경우 대처할 URL

    Returns:
        RCSButton: RCS 버튼 인스턴트
    """
    return RCSButton(
        type = RCSButtonType.MAP_LOC,
        name = name,
        label= label,
        latitude=latitude,
        longitude=longitude,
        fallback_url=fallback_url
    )

def make_rcs_map_qry_button(
    name :str,
    query :str = None,
    fallback_url :str = None
) -> RCSButton:
    """지도 검색
    
    검색어를 통해 조회된 지도 App을 실행합니다.

    Args:
        name (str): 버튼 명
        query (str, optional): 지도 App에서 검색할 구문
        fallback_url (str, optional): 지도 App동작이 안 될 경우 대처할 URL

    Returns:
        RCSButton: RCS 버튼 인스턴트
    """
    return RCSButton(
        type = RCSButtonType.MAP_QRY,
        name = name,
        query= query,
        fallback_url=fallback_url
    )

def make_rcs_map_send_button(
    name :str
) -> RCSButton:
    """위치 전송
    
    휴대폰의 현재 위치 정보를 전송합니다.

    Args:
        name (str): 버튼 명

    Returns:
        RCSButton: RCS 버튼 인스턴트
    """
    return RCSButton(
        type = RCSButtonType.MAP_SEND,
        name = name
    )
    
def make_rcs_calendar_button(
    name :str,
    start_time :str = None,
    end_time :str = None,
    title :str = None,
    description :str = None
) -> RCSButton:
    """일정 등록
    
    정해진 일자와 내용으로 일정을 등록합니다.

    Args:
        name (str): 버튼 명
        start_time (str, optional): 시작 일정(yyyy-MM-dd'T'HH:mm:ssXXX)
        end_time (str, optional): 종료 일정(yyyy-MM-dd'T'HH:mm:ssXXX)
        title (str, optional): 일정 제목
        description (str, optional): 일정 내용

    Returns:
        RCSButton: RCS 버튼 인스턴트
    """
    return RCSButton(
        type = RCSButtonType.CALENDAR,
        name = name,
        start_time=start_time,
        end_time=end_time,
        title=title,
        description=description
    )
    
def make_rcs_copy_button(
    name :str,
    text :str = None
) -> RCSButton:
    """복사하기
    
    지정된 내용을 클립보드로 복사합니다.

    Args:
        name (str): 버튼 명
        text (str, optional): 클립보드로 복사될 내용

    Returns:
        RCSButton: RCS 버튼 인스턴트
    """
    return RCSButton(
        type= RCSButtonType.COPY,
        name= name,
        text= text
    )
    
def make_rcs_com_t_button(
    name :str,
    phone_number :str = None,
    text :str = None
) -> RCSButton:
    """대화방 열기 (문자)
    
    메시지 App을 실행합니다.

    Args:
        name (str): 버튼 명
        phone_number (str, optional): 대화방의 수신자 번호
        text (str, optional): 내용

    Returns:
        RCSButton: RCS 버튼 인스턴트
    """
    return RCSButton(
        type = RCSButtonType.COM_T,
        name = name,
        phone_number=phone_number,
        text=text
    )
    
def make_rcs_com_v_button(
    name :str,
    phone_number :str = None
) -> RCSButton:
    """대화방 열기 (음성, 영상)
    
    메시지 App을 실행합니다.

    Args:
        name (str): 버튼 명
        phone_number (str, optional): 대화방의 수신자 번호

    Returns:
        RCSButton: RCS 버튼 인스턴트
    """
    return RCSButton(
        type = RCSButtonType.COM_V,
        name = name,
        phone_number = phone_number
    )

def make_rcs_dial_button(
    name :str,
    phone_number :str = None
) -> RCSButton:
    """전화 연결
    
    특정 전화번호로 전화를 걸 수 있습니다.

    Args:
        name (str): 버튼 명
        phone_number (str, optional): 전화 연결 할 수신자 번호

    Returns:
        RCSButton: RCS 버튼 인스턴트
    """
    return RCSButton(
        type = RCSButtonType.DIAL,
        name = name,
        phone_number = phone_number
    )