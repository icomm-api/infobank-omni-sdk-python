from pydantic import(
    Field
)
from typing import (
    List,
    Optional,
)
from typing_extensions import(
    Literal
)
from infobank.core.models import (
    CamelCaseModel,
    RequsetMessage,
    _ResponseApi
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
    _AlimTalkMessage,
    _FriendTalkMessage,
    _FriendTalkMessageType,
)
from infobank.core.models import(
    _BrandMessage,
    _BrandMessageSendType,
)
from infobank.omni.exceptions import(
    InfobankException
)

class SMSMessage(_SMSMessage):
    """통합 발송 MessageFlow SMS는 아래 페이지에서 확인 가능합니다.

    https://infobank-guide.gitbook.io/omni_api/api-reference/send/omni#sms
    """
    ttl :Optional[str]

class MMSMessage(_MMSMessage):
    """통합 발송 MessageFlow MMS는 아래 페이지에서 확인 가능합니다.

    https://infobank-guide.gitbook.io/omni_api/api-reference/send/omni#mms
    """
    ttl :Optional[str]


class RCSButtonType(_RCSButtonType):
    pass
    
class RCSButton(_RCSButton):
    """RCS 버튼는 아래 페이지에서 확인 가능합니다.

    https://infobank-guide.gitbook.io/omni_api/api-reference/send/rcs#rcs-button
    
    아래 정의된 함수를 사용하면 보다 편하게 작성이 가능합니다.
    
    from infobank.omni.models import (\n
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

class RCSContent(_RCSContent):
    pass

class RCSMessage(_RCSMessage):    
    """통합 발송 MessageFlow RCS는 아래 페이지에서 확인 가능합니다.

    https://infobank-guide.gitbook.io/omni_api/api-reference/send/omni#rcs
    """
    content: RCSContent
    agency_id :str
    copy_allowed :Optional[str]
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
 
    from infobank.omni.models import (\n
        make_alimtalk_al_button,\n
        make_alimtalk_bc_button,\n
        make_alimtalk_bk_button,\n
        make_alimtalk_bt_button,\n
        make_alimtalk_ds_button,\n
        make_alimtalk_md_button,\n
        make_alimtalk_wl_button,\n
        make_alimtalk_ac_button\n
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
    
    def __init__(
        self,
        list :List[AlimTalkAttachMentItemList] = None,
        summary :Optional[AlimTalkAttachMentItemSummary] = None
    ):
        if list is None or len(list) <= 0:
            raise InfobankException('list is not set.')
        
        super().__init__(
            list = list,
            summary = summary
        )

class AlimTalkAttachMent(RequsetMessage):
    button :Optional[List[AlimTalkButton]]
    item :Optional[AlimTalkAttachMentItem]
    item_highlight :Optional[AlimTalkAttachMentItemHighlight]

class AlimTalkSupplement(RequsetMessage):
    quick_reply: Optional[List[AlimTalkButton]]
    
class AlimTalkMessage(_AlimTalkMessage):
    """통합 발송 MessageFlow 알림톡는 아래 페이지에서 확인 가능합니다.

    https://infobank-guide.gitbook.io/omni_api/api-reference/send/omni#alimtalk
    """
    template_code :str
    title :Optional[str]
    header :Optional[str] = Field(
        max_length=50
    )
    attachment :Optional[AlimTalkAttachMent]
    supplement :Optional[AlimTalkSupplement]
    price :Optional[str]
    currency_type :Optional[str]

class FriendTalkButtonType(_AlimTalkButtonType):
    pass

class FriendTalkMessageType(_FriendTalkMessageType):
    FC="FC"
    FL="FL"
    FM="FM"
    FA="FA"
    FP="FP"
    pass

class FriendTalkButton(_AlimTalkButton):
    """친구톡 버튼는 아래 페이지에서 확인 가능합니다.

    https://omniapi.gitbook.io/omni_api/api-reference/send/kakao#button
    
    아래 정의된 함수를 사용하면 보다 편하게 버튼을 작성할 수 있습니다.
 
    from infobank.omni.models import (\n
        make_friendtalk_al_button,\n
        make_friendtalk_bc_button,\n
        make_friendtalk_bk_button,\n
        make_friendtalk_bt_button,\n
        make_friendtalk_ds_button,\n
        make_friendtalk_md_button,\n
        make_friendtalk_wl_button,\n
    )
    """
    pass

class FriendTalkAttachMentItemList(RequsetMessage):
    title :str
    img_url :str
    scheme_android :Optional[str]
    scheme_ios :Optional[str]
    url_mobile :str
    url_pc :Optional[str]
    

class FriendTalkAttachMentItemSummary(RequsetMessage):
    title :str
    description :str


class FriendTalkAttachMentItem(RequsetMessage):
    list :List[FriendTalkAttachMentItemList]
    summary :Optional[FriendTalkAttachMentItemSummary]

class FriendTalkAttachMentImage(RequsetMessage):
    img_url :str
    img_link :Optional[str]

class FriendTalkAttachMentCoupon(RequsetMessage):
    title :str
    description :str
    url_pc :Optional[str]
    url_mobile :Optional[str]
    scheme_android :Optional[str]
    scheme_ios :Optional[str]

class FriendTalkAttachMentCommerce(RequsetMessage):
    title :str
    regular_price :int
    discount_price :Optional[int]
    discount_rate :Optional[int]
    discount_fixed :Optional[int]

class FriendTalkAttachMentVideo(RequsetMessage):
    video_url :str
    thumbnail_url :Optional[str]
    
class FriendTalkAttachMent(RequsetMessage):
    button :Optional[List[FriendTalkButton]]
    item :Optional[FriendTalkAttachMentItem]
    image :Optional[FriendTalkAttachMentImage]
    coupon :Optional[FriendTalkAttachMentCoupon]
    commerce :Optional[FriendTalkAttachMentCommerce]
    video :Optional[FriendTalkAttachMentVideo]

class FriendTalkCarouselHead(RequsetMessage):
    header :str = Field(
        max_length=20
    )
    content :str = Field(
        max_length=50
    )
    image_url :Optional[str]
    url_mobile :Optional[str]
    url_pc :Optional[str]
    scheme_android :Optional[str]
    scheme_ios: Optional[str]


class FriendTalkCarouselList(RequsetMessage):
    header :Optional[str] = Field(
        max_length=20
    )
    message :Optional[str] = Field(
        max_length=180
    )
    additional_content :Optional[str] = Field(
        max_length=34
    )
    attachment :Optional[FriendTalkAttachMent]

class FriendTalkCarouselTail(RequsetMessage):
    url_pc :Optional[str]
    url_mobile :str
    scheme_ios :Optional[str]
    scheme_android :Optional[str]

class FriendTalkCarousel(RequsetMessage):
    head :Optional[FriendTalkCarouselHead]
    list :List[FriendTalkCarouselList]
    tail :Optional[FriendTalkCarouselTail]

class FriendTalkMessage(_FriendTalkMessage):
    """통합 발송 MessageFlow 친구톡는 아래 페이지에서 확인 가능합니다.

    https://omniapi.gitbook.io/omni_api/api-reference/send/omni#friendtalk
    """
    text :Optional[str]
    header :Optional[str]
    carousel :Optional[FriendTalkCarousel]
    attachment :Optional[FriendTalkAttachMent]
    additional_content :Optional[str]
    ad_flag :Optional[Literal['Y','N']] = Field(
        description="This field can only be 'Y' or 'N'"
    )
    adult :Optional[Literal['Y','N']] = Field(
        description="This field can only be 'Y' or 'N'"
    )
    group_tag_key :Optional[str] = Field(
        max_length=40
    )
    push_alarm :Optional[Literal['Y','N']] = Field(
        description="This field can only be 'Y' or 'N'"
    )


class BrandMessageMessageType(FriendTalkMessageType):
    pass

class BrandMessageSendType(_BrandMessageSendType):
    pass

class BrandMessageCarouselHead(FriendTalkCarouselHead):
    pass

class BrandMessageCarouselList(FriendTalkCarouselList):
    pass

class BrandMessageCarouselTail(FriendTalkCarouselTail):
    pass
class BrandMessageButtonType(_AlimTalkButtonType):
    pass

class BrandMessageButton(_AlimTalkButton):
    pass

class BrandMessageAttachMentItemList(FriendTalkAttachMentItemList):
    pass

class BrandMessageAttachMentItemSummary(FriendTalkAttachMentItemSummary):
    pass

class BrandMessageAttachMentItem(RequsetMessage):
    list :List[BrandMessageAttachMentItemList]
    summary :Optional[BrandMessageAttachMentItemSummary]
    
class BrandMessageAttachMentImage(FriendTalkAttachMentImage):
    pass

class BrandMessageAttachMentCoupon(FriendTalkAttachMentCoupon):
    pass

class BrandMessageAttachMentCommerce(FriendTalkAttachMentCommerce):
    pass

class BrandMessageAttachMentVideo(FriendTalkAttachMentVideo):
    pass
class BrandMessageAttachMent(RequsetMessage):
    button :Optional[List[BrandMessageButton]]
    item :Optional[BrandMessageAttachMentItem]
    image :Optional[BrandMessageAttachMentImage]
    coupon :Optional[BrandMessageAttachMentCoupon]
    commerce :Optional[BrandMessageAttachMentCommerce]
    video :Optional[BrandMessageAttachMentVideo]

class BrandMessageCarousel(RequsetMessage):
    head :Optional[BrandMessageCarouselHead]
    list :List[BrandMessageCarouselList]
    tail :Optional[FriendTalkCarouselTail]

class BrandMessage(_BrandMessage):
    text :Optional[str]
    carousel :Optional[BrandMessageCarousel]
    attachment :Optional[BrandMessageAttachMent]
    header :Optional[str]
    targeting :Optional[str] = Field(
        max_length=1
    )
    template_code: Optional[str]
    additional_content :Optional[str]
    ad_flag :Optional[Literal['Y','N']] = Field(
        description="This field can only be 'Y' or 'N'"
    )
    adult :Optional[Literal['Y','N']] = Field(
        description="This field can only be 'Y' or 'N'"
    )
    group_tag_key :Optional[str] = Field(
        max_length=40
    )
    push_alarm :Optional[Literal['Y','N']] = Field(
        description="This field can only be 'Y' or 'N'"
    )
    message_variable :Optional[dict]
    button_variable :Optional[dict]
    coupon_variable: Optional[dict]
    image_variable: Optional[dict]
    video_variable: Optional[dict]
    commerce_variable: Optional[dict]
    carousel_variable: Optional[dict]
    origin_cid :Optional[str] = Field(
        alias='originCID',
        max_length=9
    )
    unsubscribe_phone_number: Optional[str]
    unsubscribe_auth_number: Optional[str]
    

class MessageFlow(RequsetMessage):
    sms :Optional[SMSMessage]
    mms :Optional[MMSMessage]
    rcs :Optional[RCSMessage]
    alimtalk :Optional[AlimTalkMessage]
    friendtalk :Optional[FriendTalkMessage]
    brandmessage: Optional[BrandMessage]
    
    def __init__(
        self,
        sms: Optional[SMSMessage] = None,
        mms: Optional[MMSMessage] = None,
        rcs: Optional[RCSMessage] = None,
        alimtalk: Optional[AlimTalkMessage] = None,
        friendtalk: Optional[FriendTalkMessage] = None,
        brandmessage: Optional[BrandMessage] = None
    ):
        """sms / mms / rcs / alimtalk  중 하나만 세팅 가능합니다.
    
        통합 발송 MessageFlow는 아래 페이지에서 확인 가능합니다.

        https://infobank-guide.gitbook.io/omni_api/api-reference/send/omni#messageflow

        Args:
            sms (Optional[SMSMessage], optional): SMS 메시지 정보. Defaults to None.\n
            mms (Optional[MMSMessage], optional): MMS 메시지 정보. Defaults to None.\n
            rcs (Optional[RCSMessage], optional): RCS 메시지 정보. Defaults to None.\n
            alimtalk (Optional[AlimTalkMessage], optional): 카카오 알림톡 메시지 정보. Defaults to None.\n

        Raises:
            InfobankException:
        """
        # if sms is None and mms is None and rcs is None and alimtalk is None:
        #     raise InfobankException('At least one of sms, mms, rcs, or alimtalk must be set.')
        
        if sum(bool(x) for x in [sms, mms, rcs, alimtalk, friendtalk, brandmessage]) > 1:
            raise InfobankException('Only one of sms, mms, rcs, alimtalk or friendtalk can be set.')
        
        super().__init__(
            sms = sms,
            mms = mms,
            rcs = rcs,
            alimtalk = alimtalk,
            friendtalk = friendtalk,
            brandmessage = brandmessage
        )
        
class Destinations(RequsetMessage):
    to :str
    msg_key :Optional[str]
    code :Optional[str]
    result :Optional[str]
    
class OmniMessage(RequsetMessage):
    message_flow :List[MessageFlow] = None
    destinations :List[Destinations]
    message_form :Optional[str]
    payment_code :Optional[str]
    ref :Optional[str]
    
    def __init__(
        self,
        destinations :List[Destinations],
        message_flow :List[MessageFlow] = None,
        message_form :Optional[str] = None,
        payment_code :Optional[str] = None,
        ref :Optional[str] = None
    ):
        """통합 발송는 아래 페이지에서 확인 가능합니다.

        https://infobank-guide.gitbook.io/omni_api/api-reference/send/omni#request

        Args:
            destinations (List[Destinations]): 수신 정보 리스트(최대 10개)\n
            message_flow (List[MessageFlow], optional): 메시지 정보 리스트. Defaults to None.\n
            message_form (Optional[str], optional): 메시지 폼 ID. Defaults to None.\n
            payment_code (Optional[str], optional): 정산용 부서코드. Defaults to None.\n
            ref (Optional[str], optional): 참조필드. Defaults to None.\n

        Raises:
            InfobankException: 
        """
        if message_flow is None or len(message_flow) <= 0:
            raise InfobankException('message_flow is not set')
        if len(destinations) <= 0:
            raise InfobankException('destinations is not set')
        
        super().__init__(
            message_flow = message_flow,
            destinations = destinations,
            message_form = message_form,
            payment_code = payment_code,
            ref = ref
        )
        
class Data(CamelCaseModel):
    destinations:Optional[List[Destinations]]

class ResponseApi(_ResponseApi):
    data :Optional[Data] = None
    ref :Optional[str] = None
    
    
def make_rcs_url_button(
    name :str,
    url :str = None
) -> RCSButton:
    """URL 연결
    
    Web page 또는 App으로 이동할 수 있습니다.

    Args:
        name (str): 버튼 명\n
        url (str, optional): 웹브라우저로 연결할 URL주소\n

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
        name (str): 버튼 명\n
        label (str, optional): 지도 App에 표시될 라벨명\n
        latitude (str, optional): 위도 값 (예)37.4001971\n
        longitude (str, optional): 경도 값 (예)127.1071718\n
        fallback_url (str, optional): 지도 App동작이 안 될 경우 대처할 URL\n

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

def make_friendtalk_wl_button(
    name :str,
    url_mobile :str,
    url_pc :str = None
) -> FriendTalkButton:
    """웹 링크
    
    버튼 클릭 시 이동할 pc/mobile환경별 web url

    Args:
        name (str): 버튼 명
        url_mobile (str): 모바일 환경에서 버튼 클릭 시 이동할 URL
        url_pc (str, optional): PC 환경에서 버튼 클릭시 이동할 URL

    Returns:
        FriendTalkButton: 프랜드 톡 버튼 인스턴트
    """
    return FriendTalkButton(
        type=FriendTalkButtonType.WL,
        name=name,
        url_mobile=url_mobile,
        url_pc=url_pc
    )
    
def make_friendtalk_al_button(
    name :str,
    scheme_android :str = None,
    scheme_ios :str = None,
    url_mobile :str = None,
    url_pc :str = None
) -> FriendTalkButton:
    """앱 링크
    
    scheme_ios, scheme_android, url_mobile 중 2가지 필수 입력 

    Args:
        name (str): 버튼 명
        scheme_android (str, optional): Android 환경에서 버튼클릭 시 실행 할 application custom scheme
        scheme_ios (str, optional): iOS 환경에서 버튼클릭 시 실행할 application custom scheme
        url_mobile (str, optional): 모바일 환경에서 버튼 클릭 시 이동할 URL
        url_pc (str, optional): PC 환경에서 버튼 클릭시 이동할 URL

    Returns:
        FriendTalkButton: 프랜드 톡 버튼 인스턴트
    """
    return FriendTalkButton(
        type=FriendTalkButtonType.AL,
        name=name,
        scheme_android=scheme_android,
        scheme_ios=scheme_ios,
        url_mobile=url_mobile,
        url_pc=url_pc
    )
    
def make_friendtalk_bk_button(
    name :str
) -> FriendTalkButton:
    """봇 키워드
    
    해당 버튼 텍스트 전송

    Args:
        name (str): 버튼 명

    Returns:
        FriendTalkButton: 프랜드 톡 버튼 인스턴트
    """
    return FriendTalkButton(
        type=FriendTalkButtonType.BK,
        name=name
    )
    
def make_friendtalk_md_button(
    name :str
) -> FriendTalkButton:
    """메시지 전달
    
    해당 버튼 텍스트 + 메시지 본문 전송

    Args:
        name (str): 버튼 명

    Returns:
        FriendTalkButton: 프랜드 톡 버튼 인스턴트
    """
    return FriendTalkButton(
        type=FriendTalkButtonType.MD,
        name=name
    )
    
def make_friendtalk_ds_button(
    name :str
) -> FriendTalkButton:
    """배송조회
    
    버튼 클릭 시 배송 조회 페이지로 이동

    Args:
        name (str): 버튼 명

    Returns:
        FriendTalkButton: 프랜드 톡 버튼 인스턴트
    """
    return FriendTalkButton(
        type=FriendTalkButtonType.DS,
        name=name
    )
    
def make_friendtalk_bc_button(
    name :str,
    chat_extra :str = None
) -> FriendTalkButton:
    """상담톡 전환

    상담톡을 이용하는 카카오톡 채널만 이용 가능
    
    Args:
        name (str): 버튼 명
        chat_extra (str, optional): 봇/상담톡전환 시 전달할 메타정보

    Returns:
        FriendTalkButton: 프랜드 톡 버튼 인스턴트
    """
    return FriendTalkButton(
        type=FriendTalkButtonType.BC,
        name=name,
        chat_extra=chat_extra
    )
    
def make_friendtalk_bt_button(
    name :str,
    chat_extra :str = None,
    chat_event :str = None
) -> FriendTalkButton:
    """챗봇 전환
    
    카카오 I 오픈빌더의 챗봇을 사용하는 카카오톡 채널만 이용가능

    Args:
        name (str): 버튼 명
        chat_extra (str, optional): 봇/상담톡전환 시 전달할 메타정보
        chat_event (str, optional): 봇/상담톡 전환 시 연결할 이벤트 명

    Returns:
        FriendTalkButton: 프랜드 톡 버튼 인스턴트
    """
    return FriendTalkButton(
        type=FriendTalkButtonType.BC,
        name=name,
        chat_extra=chat_extra,
        chat_event=chat_event
    )
    
    
def make_friendtalk_bf_button(
    name :str,
    biz_form_key :str,
    biz_form_id : str
) -> FriendTalkButton:
    """비즈폼
    
    카카오 비즈니스에서 생성한 비즈니스폼 ID

    Args:
        name (str): 버튼 명
        biz_form_key (str): 비즈폼 키
        biz_form_id (str): 비즈폼 ID

    Returns:
        FriendTalkButton: 프랜드 톡 버튼 인스턴트
    """
    return FriendTalkButton(
        type=FriendTalkButtonType.BC,
        name=name,
        biz_form_key=biz_form_key,
        biz_form_id=biz_form_id
    )
    
def make_brandmessage_wl_button(
    name: str,
    url_mobile: str,
    url_pc: str = None
) -> BrandMessageButton:
    """웹 링크

    버튼 클릭 시 이동할 pc/mobile환경별 web url
    """
    return BrandMessageButton(
        type=BrandMessageButtonType.WL,
        name=name,
        url_mobile=url_mobile,
        url_pc=url_pc
    )

def make_brandmessage_al_button(
    name: str,
    scheme_android: str = None,
    scheme_ios: str = None,
    url_mobile: str = None,
    url_pc: str = None
) -> BrandMessageButton:
    """앱 링크

    scheme_ios, scheme_android, url_mobile 중 2가지 필수 입력
    """
    return BrandMessageButton(
        type=BrandMessageButtonType.AL,
        name=name,
        scheme_android=scheme_android,
        scheme_ios=scheme_ios,
        url_mobile=url_mobile,
        url_pc=url_pc
    )

def make_brandmessage_bk_button(
    name: str
) -> BrandMessageButton:
    """봇 키워드

    해당 버튼 텍스트 전송
    """
    return BrandMessageButton(
        type=BrandMessageButtonType.BK,
        name=name
    )

def make_brandmessage_md_button(
    name: str
) -> BrandMessageButton:
    """메시지 전달

    해당 버튼 텍스트 + 메시지 본문 전송
    """
    return BrandMessageButton(
        type=BrandMessageButtonType.MD,
        name=name
    )

def make_brandmessage_ds_button(
    name: str
) -> BrandMessageButton:
    """배송조회

    버튼 클릭 시 배송 조회 페이지로 이동
    """
    return BrandMessageButton(
        type=BrandMessageButtonType.DS,
        name=name
    )

def make_brandmessage_bc_button(
    name: str,
    chat_extra: str = None
) -> BrandMessageButton:
    """상담톡 전환

    상담톡을 이용하는 카카오톡 채널만 이용 가능
    """
    return BrandMessageButton(
        type=BrandMessageButtonType.BC,
        name=name,
        chat_extra=chat_extra
    )

def make_brandmessage_bt_button(
    name: str,
    chat_extra: str = None,
    chat_event: str = None
) -> BrandMessageButton:
    """챗봇 전환

    카카오 I 오픈빌더의 챗봇을 사용하는 카카오톡 채널만 이용가능
    """
    return BrandMessageButton(
        type=BrandMessageButtonType.BC,
        name=name,
        chat_extra=chat_extra,
        chat_event=chat_event
    )

def make_brandmessage_bf_button(
    name: str,
    biz_form_key: str,
    biz_form_id: str
) -> BrandMessageButton:
    """비즈폼

    카카오 비즈니스에서 생성한 비즈니스폼 ID
    """
    return BrandMessageButton(
        type=BrandMessageButtonType.BC,
        name=name,
        biz_form_key=biz_form_key,
        biz_form_id=biz_form_id
    )
