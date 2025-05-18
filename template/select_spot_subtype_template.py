import copy
import math
from libs.collections.postback_trigger_type import PostbackTriggerType
from models.postback_data import PostbackDataModel


select_spot_subtype_template = {
  "type": "carousel",
  "contents": [
# 	{
# 	  "type": "bubble",
# 	  "size": "micro",
# 	  "hero": {
# 		"type": "image",
# 		"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLcZ2KQcoP0evOgz9TLy2yS2vw96AwOY8gsA&s",
# 		"size": "full",
# 		"aspectRatio": "20:13",
# 		"aspectMode": "cover"
# 	  },
# 	  "footer": {
# 		"type": "box",
# 		"layout": "vertical",
# 		"spacing": "sm",
# 		"contents": [
# 		  {
# 			"type": "button",
# 			"action": {
# 			  "type": "postback",
# 			  "label": "找咖啡廳",
# 			  "data": "找咖啡廳"
# 			}
# 		  }
# 		]
# 	  }
# 	},
# 	{
# 	  "type": "bubble",
# 	  "size": "micro",
# 	  "hero": {
# 		"type": "image",
# 		"url": "https://media.istockphoto.com/id/1316145932/photo/table-top-view-of-spicy-spot.jpg?s=612x612&w=0&k=20&c=eaKRSIAoRGHMibSfahMyQS6iFADyVy1pnPdy1O5rZ98=",
# 		"size": "full",
# 		"aspectRatio": "20:13",
# 		"aspectMode": "cover"
# 	  },
# 	  "footer": {
# 		"type": "box",
# 		"layout": "vertical",
# 		"spacing": "sm",
# 		"contents": [
# 		  {
# 			"type": "button",
# 			"action": {
# 			  "type": "postback",
# 			  "label": "找餐廳",
# 			  "data": "找餐廳"
# 			}
# 		  }
# 		]
# 	  }
# 	}
  ]
}


spot_subtype_images = {
	PostbackTriggerType.SelectIndoor.value.code: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKg4A9YzIlIZH00rOOYhxS97TMTufNJbMBDA&s",
	PostbackTriggerType.SelectOutdoor.value.code: "https://onetreeplanted.org/cdn/shop/files/Amazon-Rainforests-Amazonia-South-America.jpg?v=1739422746",
}

def generate_spot_subtype_template(postback_data: PostbackDataModel):
	return_message = copy.deepcopy(select_spot_subtype_template)
	data = sorted(PostbackTriggerType.getSpotSubtypeList(), key=lambda x: x.code)
 
	for index, sub_type in enumerate(data):
		new_postback_data = copy.deepcopy(postback_data)
		new_postback_data.trigger_type = sub_type.value.code
		new_postback_data.sub_type = sub_type.value.code

		return_message["contents"].append(
			{
				"type": "bubble",
				"size": "micro",
				"hero": {
					"type": "image",
					"url": spot_subtype_images[sub_type.value.code],
					"size": "full",
					"aspectRatio": "20:13",
					"aspectMode": "cover"
				},
				"footer": {
					"type": "box",
					"layout": "vertical",
					"spacing": "sm",
					"contents": [
						{
							"type": "button",
							"action": {
								"type": "postback",
								"label": sub_type.value.description,
								"data": new_postback_data.model_dump_json()
							}
						}
					]
				}
			}			
		)
	return return_message
