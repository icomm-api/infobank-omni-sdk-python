import os

from infobank.imageupload.models import (
    ImageFile,
    ImageServiceType
)

def get_mandantory_validate_message(
    
) -> ImageFile:
    return ImageFile(
        
    )
    
def get_mms_image_file(

) -> ImageFile:
    file_full_path = os.getcwd()+'/infobank/imageupload/example/image.jpg'
    return ImageFile(
        service_type=ImageServiceType.MMS,
        file_path=file_full_path
    )
    
def get_rcs_image_file(
    
) -> ImageFile:
    file_full_path = os.getcwd()+'/infobank/imageupload/example/image.jpg'
    return ImageFile(
        service_type=ImageServiceType.RCS,
        file_path=file_full_path
    )