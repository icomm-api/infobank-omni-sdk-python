from pydantic import(
    Field
)
from typing import (
    List,
    Dict,
    Optional
)
from infobank.core.models import (
    CamelCaseModel,
    RequsetMessage,
    _ResponseApi,
)
from infobank.core.models import (
    _SMSMessage
)
from infobank.core.models import (
    _MMSMessage
)
from infobank.core.models import(
    _RCSContent,
    _RCSButtonType,
    _RCSButton,
    _RCSSubContent,
    _RCSStandAlone,
    _RCSCarousel,
    _RCSTemplate,
    _RCSMessage
)
from infobank.core.models import (
    _AlimTalkButtonType,
    _AlimTalkButton,
    _AlimTalkMessageType,
    _AlimTalkMessage
)
from infobank.messageform.exceptions import (
    InfobankException
)

class SMSMessage(_SMSMessage):
    """메시지 폼 등록 MessageFlow SMS는 아래 페이지에서 확인 가능합니다.

    https://infobank-guide.gitbook.io/omni_api/api-reference/send/omni#sms
    """
    ttl :Optional[str]

class MMSMessage(_MMSMessage):
    """메시지 폼 등록 MessageFlow MMS는 아래 페이지에서 확인 가능합니다.

    https://infobank-guide.gitbook.io/omni_api/api-reference/send/omni#mms
    """
    ttl :Optional[str]


class RCSButtonType(_RCSButtonType):
    pass
    
class RCSButton(_RCSButton):
    """RCS 버튼는 아래 페이지에서 확인 가능합니다.

    https://infobank-guide.gitbook.io/omni_api/api-reference/send/rcs#rcs-button
    
    아래 정의된 함수를 사용하면 보다 편하게 작성이 가능합니다.
    
    from infobank.messageform.models import (\n
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
    sub_content :Optional[List[RCSSubContent]]
    button :Optional[List[RCSButton]]

class RCSCarousel(_RCSCarousel):
    button :Optional[List[RCSButton]]

class RCSTemplate(_RCSTemplate):
    sub_content :Optional[List[RCSSubContent]]

class RCSContent(_RCSContent):
    standalone :Optional[RCSStandAlone]
    carousel :Optional[List[RCSCarousel]]
    template :Optional[RCSTemplate]
    
    def __init__(
        self,
        standalone :Optional[RCSStandAlone] = None,
        carousel :Optional[List[RCSCarousel]] = None,
        template :Optional[RCSTemplate] = None
    ):
        """RCS conetent는 아래 페이지에서 확인 가능합니다.

        https://infobank-guide.gitbook.io/omni_api/api-reference/send/rcs#content
        
        3개 필드 중 1개 필수(standalone, carousel, template)입니다.

        Args:
            standalone (Optional[RCSStandAlone], optional): standalone. Defaults to None.\n
            carousel (Optional[List[RCSCarousel]], optional): carousel. Defaults to None.\n
            template (Optional[RCSTemplate], optional): template. Defaults to None.\n

        Raises:
            InfobankException:
        """
        if standalone is None and carousel is None and template is None:
            raise InfobankException('At least one of standalone, carousel, or template must be set.')
        
        if sum(bool(x) for x in [standalone, carousel, template]) > 1:
            raise InfobankException('Only one of standalone, carousel or template can be set.')
        
        if carousel is not None and len(carousel) <= 0:
            raise InfobankException('carousel is not set')
        
        super().__init__(
            standalone = standalone,
            carousel = carousel,
            template = template
        )

class RCSMessage(_RCSMessage):    
    """메시지 폼 등록 MessageFlow RCS는 아래 페이지에서 확인 가능합니다.

    https://infobank-guide.gitbook.io/omni_api/api-reference/send/omni#rcs
    """
    content: RCSContent
    copy_allowed :Optional[str]
    brand_id :Optional[str]
    brand_key :Optional[str]
    agency_id :Optional[str]
    agency_key :Optional[str]
    group_id :Optional[str]
    ttl :Optional[str]


class AlimTalkButtonType(_AlimTalkButtonType):
    pass

class AlimTalkMessageType(_AlimTalkMessageType):
    pass

class AlimTalkButton(_AlimTalkButton):
    """알림톡 버튼는 아래 페이지에서 확인 가능합니다.

    https://infobank-guide.gitbook.io/omni_api/api-reference/send/kakao#button
    
    아래 정의된 함수를 사용하면 보다 편하게 버튼을 작성할 수 있습니다.
 
    from infobank.messageform.models import (\n
        make_alimtalk_al_button,\n
        make_alimtalk_bc_button,\n
        make_alimtalk_bk_button,\n
        make_alimtalk_bt_button,\n
        make_alimtalk_ds_button,\n
        make_alimtalk_ac_button,\n
        make_alimtalk_md_button,\n
        make_alimtalk_wl_button\n
    )
    """
    pass


class AlimTalkAttachMentItemList(RequsetMessage):
    title :str
    description :str

class AlimTalkAttachMentItemSummary(RequsetMessage):
    title :str
    description :str

class AlimTalkAttachMentItemHighlight(RequsetMessage):
    title :str
    description :str

class AlimTalkAttachMentItem(RequsetMessage):
    list :List[AlimTalkAttachMentItemList]
    summary :Optional[AlimTalkAttachMentItemSummary]

class AlimTalkAttachMent(RequsetMessage):
    button :Optional[List[AlimTalkButton]]
    item :Optional[AlimTalkAttachMentItem]
    item_highlight :Optional[AlimTalkAttachMentItemHighlight]

class AlimTalkSupplement(RequsetMessage):
    quick_reply: Optional[List[AlimTalkButton]]
    
class AlimTalkMessage(_AlimTalkMessage):
    """메시지 폼 등록 MessageFlow 알림톡는 아래 페이지에서 확인 가능합니다.

    https://infobank-guide.gitbook.io/omni_api/api-reference/send/omni#alimtalk
    """
    template_code :str
    title :Optional[str]
    attachment :Optional[AlimTalkAttachMent]
    supplement :Optional[AlimTalkSupplement]
    price :Optional[str]
    currency_type :Optional[str]


class MessageForm(RequsetMessage):
    sms :Optional[SMSMessage]
    mms :Optional[MMSMessage]
    rcs :Optional[RCSMessage]
    alimtalk :Optional[AlimTalkMessage]
    
    def __init__(
        self,
        sms: Optional[SMSMessage] = None,
        mms: Optional[MMSMessage] = None,
        rcs: Optional[RCSMessage] = None,
        alimtalk: Optional[AlimTalkMessage] = None,
    ):
        """메시지 폼 등록 MessageFlow는 아래 페이지에서 확인 가능합니다.

        https://infobank-guide.gitbook.io/omni_api/api-reference/management/form#messageform

        Args:
            sms (Optional[SMSMessage], optional): SMS 메시지 정보. Defaults to None.\n
            mms (Optional[MMSMessage], optional): MMS 메시지 정보. Defaults to None.\n
            rcs (Optional[RCSMessage], optional): RCS 메시지 정보. Defaults to None.\n
            alimtalk (Optional[AlimTalkMessage], optional): 카카오 알림톡 메시지 정보. Defaults to None.\n

        Raises:
            InfobankException:
        """
        if sms is None and mms is None and rcs is None and alimtalk is None:
            raise InfobankException('At least one of sms, mms, rcs, or alimtalk must be set.')
        
        if sum(bool(x) for x in [sms, mms, rcs, alimtalk]) > 1:
            raise InfobankException('Only one of sms, mms, rcs, or alimtalk can be set.')
        
        super().__init__(
            sms = sms,
            mms = mms,
            rcs = rcs,
            alimtalk = alimtalk
        )
        
class MessageFormMessage(RequsetMessage):
    message_form :List[MessageForm]
    
    def __init__(
        self,
        message_form :List[MessageForm] = None
    ):
        if message_form is None or len(message_form) <= 0:
            raise InfobankException('message_form is not set')
        
        super().__init__(
            message_form = message_form
        )
    
class Data(CamelCaseModel):
    form_id: Optional[str]
    message_form :Optional[List[MessageForm]]
    expired: Optional[str]
    
class ResponseApi(_ResponseApi):
    data :Optional[Data]
    
    
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
    
def make_alimtalk_wl_button(
    name :str,
    url_mobile :str,
    url_pc :str = None
) -> AlimTalkButton:
    """웹 링크
    
    버튼 클릭 시 이동할 pc/mobile환경별 web url

    Args:
        name (str): 버튼 명
        url_mobile (str): 모바일 환경에서 버튼 클릭 시 이동할 URL
        url_pc (str, optional): PC 환경에서 버튼 클릭시 이동할 URL

    Returns:
        AlimTalkButton: 알림톡 버튼 인스턴트
    """
    return AlimTalkButton(
        type=AlimTalkButtonType.WL,
        name=name,
        url_mobile=url_mobile,
        url_pc=url_pc
    )
    
def make_alimtalk_al_button(
    name :str,
    scheme_android :str = None,
    scheme_ios :str = None,
    url_mobile :str = None,
    url_pc :str = None
) -> AlimTalkButton:
    """앱 링크
    
    scheme_ios, scheme_android, url_mobile 중 2가지 필수 입력 

    Args:
        name (str): 버튼 명
        scheme_android (str, optional): Android 환경에서 버튼클릭 시 실행 할 application custom scheme
        scheme_ios (str, optional): iOS 환경에서 버튼클릭 시 실행할 application custom scheme
        url_mobile (str, optional): 모바일 환경에서 버튼 클릭 시 이동할 URL
        url_pc (str, optional): PC 환경에서 버튼 클릭시 이동할 URL

    Returns:
        AlimTalkButton: 알림톡 버튼 인스턴트
    """
    return AlimTalkButton(
        type=AlimTalkButtonType.AL,
        name=name,
        scheme_android=scheme_android,
        scheme_ios=scheme_ios,
        url_mobile=url_mobile,
        url_pc=url_pc
    )
    
def make_alimtalk_bk_button(
    name :str
) -> AlimTalkButton:
    """봇 키워드
    
    해당 버튼 텍스트 전송

    Args:
        name (str): 버튼 명

    Returns:
        AlimTalkButton: 알림톡 버튼 인스턴트
    """
    return AlimTalkButton(
        type=AlimTalkButtonType.BK,
        name=name
    )
    
def make_alimtalk_md_button(
    name :str
) -> AlimTalkButton:
    """메시지 전달
    
    해당 버튼 텍스트 + 메시지 본문 전송

    Args:
        name (str): 버튼 명

    Returns:
        AlimTalkButton: 알림톡 버튼 인스턴트
    """
    return AlimTalkButton(
        type=AlimTalkButtonType.MD,
        name=name
    )
    
def make_alimtalk_ds_button(
    name :str
) -> AlimTalkButton:
    """배송조회
    
    버튼 클릭 시 배송 조회 페이지로 이동

    Args:
        name (str): 버튼 명

    Returns:
        AlimTalkButton: 알림톡 버튼 인스턴트
    """
    return AlimTalkButton(
        type=AlimTalkButtonType.DS,
        name=name
    )


def make_alimtalk_bc_button(
    name :str,
    chat_extra :str = None
) -> AlimTalkButton:
    """상담톡 전환

    상담톡을 이용하는 카카오톡 채널만 이용 가능
    
    Args:
        name (str): 버튼 명
        chat_extra (str, optional): 봇/상담톡전환 시 전달할 메타정보

    Returns:
        AlimTalkButton: 알림톡 버튼 인스턴트
    """
    return AlimTalkButton(
        type=AlimTalkButtonType.BC,
        name=name,
        chat_extra=chat_extra
    )
    
def make_alimtalk_bt_button(
    name :str,
    chat_extra :str = None,
    chat_event :str = None
) -> AlimTalkButton:
    """챗봇 전환
    
    카카오 I 오픈빌더의 챗봇을 사용하는 카카오톡 채널만 이용가능

    Args:
        name (str): 버튼 명
        chat_extra (str, optional): 봇/상담톡전환 시 전달할 메타정보
        chat_event (str, optional): 봇/상담톡 전환 시 연결할 이벤트 명

    Returns:
        AlimTalkButton: 알림톡 버튼 인스턴트
    """
    return AlimTalkButton(
        type=AlimTalkButtonType.BT,
        name=name,
        chat_extra=chat_extra,
        chat_event=chat_event
    )

def make_alimtalk_ac_button(
    name :str
) -> AlimTalkButton:
    """채널 추가
    
    버튼 클릭 시 카카오톡 채널 추가

    Args:
        name (str): 버튼 명

    Returns:
        AlimTalkButtonType: 알림톡 버튼 인스턴트
    """
    return AlimTalkButton(
        type=AlimTalkButtonType.AC,
        name=name
    )
    
def make_alimtalk_bf_button(
    name :str,
    biz_form_key :str,
    biz_form_id : str
) -> AlimTalkButton:
    """비즈폼
    
    카카오 비즈니스에서 생성한 비즈니스폼 ID

    Args:
        name (str): 버튼 명
        biz_form_key (str): 비즈폼 키
        biz_form_id (str): 비즈폼 ID

    Returns:
        AlimTalkButtonType: 알림톡 톡 버튼 인스턴트
    """
    return AlimTalkButton(
        type=AlimTalkButtonType.BC,
        name=name,
        biz_form_key=biz_form_key,
        biz_form_id=biz_form_id
    )