# Select Footer Accumo Spot Food Template

import copy
from models.postback_data import PostbackDataModel
from libs.collections.postback_trigger_type import PostbackTriggerType

footer_asf_template = {
    "type": "box",
    "layout": "horizontal",
    "flex": 1,
    "contents": [
        {
            "type": "box",
            "layout": "horizontal",
            "contents": []
        }
    ]
}

def generate_footer_asf_template(postback_data: PostbackDataModel):
    new_template = copy.deepcopy(footer_asf_template)
    
    for index, main_type in enumerate(PostbackTriggerType.getMainTypeList()):
        new_postback_data = copy.deepcopy(postback_data)
        new_postback_data.trigger_type = main_type.value.code
        new_postback_data.main_type = main_type.value.code
        new_template["contents"][0]["contents"].append(
            {
                "type": "button",
                "action": {
                    "type": "postback",
                    "label": main_type.value.description,
                    "data": new_postback_data.model_dump_json()
                }
            },            
        )
    
    return new_template