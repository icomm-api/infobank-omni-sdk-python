from typing import (
    List,
    Optional
)
from pydantic import (
    Field
)
from infobank.core.models import (
    _AlimTalkButtonType,
    _AlimTalkButton,
    _AlimTalkMessageType,
    _AlimTalkMessage,
    _FallBackType,
    _FallBack,
    _ResponseApi,
    _FriendTalkMessage,
    _FriendTalkMessageType,
    _BrandMessage,
    _BrandMessageSendType,
)
from infobank.core.models import (
    _ResponseApi,
    _FallBackType,
    _FallBack
)

class AlimTalkButtonType(_AlimTalkButtonType):
    pass

class AlimTalkMessageType(_AlimTalkMessageType):
    pass

class AlimTalkButton(_AlimTalkButton):
    """알림톡 버튼는 아래 페이지에서 확인 가능합니다.

    https://infobank-guide.gitbook.io/omni_api/api-reference/send/kakao#button
    
    아래 정의된 함수를 사용하면 보다 편하게 버튼을 작성할 수 있습니다.
 
    from infobank.kkoalimtalk.models import (\n
        make_alimtalk_al_button,\n
        make_alimtalk_bc_button,\n
        make_alimtalk_bk_button,\n
        make_alimtalk_bt_button,\n
        make_alimtalk_ds_button,\n
        make_alimtalk_md_button,\n
        make_alimtalk_wl_button\n
    )
    """
    pass

class AlimTalkFallBackType(_FallBackType):
    pass

class AlimTalkFallBack(_FallBack):
    """알림톡 fallback는 아래 페이지에서 확인 가능합니다.

    https://infobank-guide.gitbook.io/omni_api/api-reference/send/kakao#fallback    
    
    fallback 메시지는 SMS/MMS만 가능합니다.
    """
    from_ :str = Field(
        alias='from'
    )

class AlimTalkMessage(_AlimTalkMessage):
    """알림톡는 아래 페이지에서 확인 가능합니다.

    https://infobank-guide.gitbook.io/omni_api/api-reference/send/kakao#request
    """
    to :str
    template_code :str
    title :Optional[str] = Field(
        max_length=50
    )
    header :Optional[str]
    button :Optional[List[AlimTalkButton]] = Field(
        max_items=5
    )
    fallback :Optional[AlimTalkFallBack]
    ref :Optional[str] = Field(
        max_length= 200,
    )
 
class FriendTalkButtonType(_AlimTalkButtonType):
    pass

class FriendTalkMessageType(_FriendTalkMessageType):
    pass

class FriendTalkButton(_AlimTalkButton):
    """친구톡 버튼는 아래 페이지에서 확인 가능합니다.

    https://omniapi.gitbook.io/omni_api/api-reference/send/kakao#button
    
    아래 정의된 함수를 사용하면 보다 편하게 버튼을 작성할 수 있습니다.
 
    from infobank.kkofriendtalk.models import (\n
        make_friendtalk_al_button,\n
        make_friendtalk_bc_button,\n
        make_friendtalk_bk_button,\n
        make_friendtalk_bt_button,\n
        make_friendtalk_ds_button,\n
        make_friendtalk_md_button,\n
        make_friendtalk_wl_button\n
    )
    """
    pass

class FriendTalkFallBackType(_FallBackType):
    pass

class FriendTalkFallBack(_FallBack):
    """친구톡 fallback는 아래 페이지에서 확인 가능합니다.
    
    https://omniapi.gitbook.io/omni_api/api-reference/send/kakao#fallback
    
    fallback 메시지는 SMS/MMS만 가능합니다.    
    """
    from_ :str = Field(
        alias='from'
    )

class FriendTalkMessage(_FriendTalkMessage):
    """친구톡는 아래 페이지에서 확인 가능합니다.

    https://omniapi.gitbook.io/omni_api/api-reference/send/kakao#request-1
    """
    to :str
    text :str
    img_url :Optional[str]
    button :Optional[List[FriendTalkButton]] = Field(
        max_items=5
    )
    fallback :Optional[FriendTalkFallBack]
    ref :Optional[str] = Field(
        max_length= 200,
    )


class BrandMessageButtonType(_AlimTalkButtonType):
    pass

class BrandMessageMessageType(_FriendTalkMessageType):
    pass

class BrandMessageSendType(_BrandMessageSendType):
    pass
class BrandMessageButton(_AlimTalkButton):
    pass

class BrandMessageFallBackType(_FallBackType):
    pass

class BrandMessageFallBack(FriendTalkFallBack):
    pass

class BrandMessage(_BrandMessage):
    to :str
    text :Optional[str]
    img_url :Optional[str]
    targeting :Optional[str] = Field(
        max_length=1
    )
    template_code :Optional[str]
    button :Optional[List[BrandMessageButton]] = Field(
        max_items=5
    )
    fallback :Optional[BrandMessageFallBack]
    group_tag_key :Optional[str] = Field(
        max_length=40
    )
    message_variable :Optional[dict]
    button_variable :Optional[dict]
    coupon_variable: Optional[dict]
    image_variable: Optional[list]
    video_variable: Optional[dict]
    commerce_variable: Optional[dict]
    carousel_variable: Optional[dict]
    origin_cid :Optional[str] = Field(
        alias='originCID',
        max_length=9
    )
    unsubscribe_phone_number: Optional[str]
    unsubscribe_auth_number: Optional[str]
    ref :Optional[str]
    
class ResponseApi(_ResponseApi):
    msg_key :Optional[str]
    ref :Optional[str]


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

class ResponseApi(_ResponseApi):
    msg_key :Optional[str]
    ref :Optional[str]
    pass
