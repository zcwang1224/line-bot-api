import json
from linebot.models import (PostbackAction,TemplateSendMessage, ButtonsTemplate, 
                            LocationAction)

from libs.collections.line_bot_menu_selection import LineBotMenuSelection
from libs.collections.postback_trigger_type import PostbackTriggerType
from models.postback_data import PostbackDataModel

# region location_template
def generate_location_template():
    postback_data = PostbackDataModel(
		menu_type=LineBotMenuSelection.Location.value.code,
		trigger_type=PostbackTriggerType.SelectLocation.value.code
	)
    return TemplateSendMessage(
                alt_text=LineBotMenuSelection.Location.value.description,
                template=ButtonsTemplate(
                    # thumbnail_image_url='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
                    # title='找附近',
                    text=LineBotMenuSelection.Location.value.description,
                    actions=[
                        PostbackAction(
                            label=PostbackTriggerType.SelectLocation.value.description,
                            data=postback_data.model_dump_json()
                        ),
                        LocationAction(
                            label=PostbackTriggerType.SelectGeoLocation.value.description
                        )
                    ]
                )
            )    
# endregion location_template