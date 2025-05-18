import copy
import math
from libs.collections.postback_trigger_type import PostbackTriggerType
from models.postback_data import PostbackDataModel


select_asf_template = {
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
# 		"url": "https://media.istockphoto.com/id/1316145932/photo/table-top-view-of-spicy-food.jpg?s=612x612&w=0&k=20&c=eaKRSIAoRGHMibSfahMyQS6iFADyVy1pnPdy1O5rZ98=",
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


asf_images = {
	PostbackTriggerType.SelectAccomo.value.code: "https://cdn2.ettoday.net/images/5861/d5861534.jpg",
	PostbackTriggerType.SelectFood.value.code: "https://www.gomaji.com/blog/wp-content/uploads/2020/04/Da-Tung-Food-Banner-e1588216225724.jpg",
 	PostbackTriggerType.SelectSpot.value.code: "https://goldcard.nat.gov.tw/cms-uploads/national-chiang-kai-shek-memorial-hall.jpg",
}

def generate_asf_template(postback_data: PostbackDataModel):
	return_message = copy.deepcopy(select_asf_template)
	data = sorted(PostbackTriggerType.getMainTypeList(), key=lambda x: x.code)
	len_col=3
 
	for index, main_type in enumerate(data):
		new_postback_data = copy.deepcopy(postback_data)
		new_postback_data.trigger_type = main_type.value.code
		new_postback_data.main_type = main_type.value.code

		return_message["contents"].append(
			{
				"type": "bubble",
				"size": "micro",
				"hero": {
					"type": "image",
					"url": asf_images[main_type.value.code],
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
								"label": main_type.value.description,
								"data": new_postback_data.model_dump_json()
							}
						}
					]
				}
			}			
		)
	return return_message
