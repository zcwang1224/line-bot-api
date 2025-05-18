import copy
import math
from libs.collections.postback_trigger_type import PostbackTriggerType
from models.postback_data import PostbackDataModel


select_food_subtype_template = {
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


food_subtype_images = {
	PostbackTriggerType.SelectCoffee.value.code: "https://cdn.vox-cdn.com/thumbor/6kLvmWfhU4h64EhC0S6tsn714fI=/0x0:4032x3024/1200x900/filters:focal(1694x1190:2338x1834)/cdn.vox-cdn.com/uploads/chorus_image/image/59740845/IMG_1503.42.jpg",
	PostbackTriggerType.SelectResturant.value.code: "https://images.ctfassets.net/nwbqij9m1jag/1u1hCw0a5IjEBDPkSPnTaM/b18741a8d84943484fbc94b4832abf18/Clarion_Hotel__stersund___NOR___Round_table_with_food_and_wine_261_100?fm=webp&q=80&w=1280",
}

def generate_food_subtype_template(postback_data: PostbackDataModel):
	return_message = copy.deepcopy(select_food_subtype_template)
	data = sorted(PostbackTriggerType.getFoodSubtypeList(), key=lambda x: x.code)
 
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
					"url": food_subtype_images[sub_type.value.code],
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
