import copy
import math

from libs.collections.area import Area
from libs.collections.city import City
from libs.collections.district import District
from libs.collections.postback_trigger_type import PostbackTriggerType
from models.postback_data import PostbackDataModel


select_county_root_message = {
  "type": "bubble",
  "size": "mega",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "所在縣市",
        "size": "lg",
        "color": "#000000FF",
        "align": "center",
        "margin": "xl",
        "contents": []
      },
      {
        "type": "separator",
        "margin": "md"
      }
    ]
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": []
  }
}

def generate_district_template(postback_data: PostbackDataModel):
	return_message = copy.deepcopy(select_county_root_message)
	data = sorted(District.getItemByCity(City.getItemByCode(postback_data.county)), key=lambda district: district.code)
	len_col=3
 
	for index, district in enumerate(data):
		new_postback_data = copy.deepcopy(postback_data)
		new_postback_data.trigger_type = PostbackTriggerType.SelectDistrict.value.code
		new_postback_data.district = district.value.code
		index_outer = int(math.floor(index / len_col))
		index_inner = index % len_col
		outer_contents_len = len(return_message["body"]["contents"])
		is_create = False
		
		if outer_contents_len == 0:
			is_create = True
		elif index_inner == 0:
			is_create = True
		
		if is_create:
			return_message["body"]["contents"].append(
				{
					"type": "box",
					"layout": "horizontal",
					"contents": []
				}      
			)

		return_message["body"]["contents"][index_outer]["contents"].append(
			{
				"type": "button",
				"action": {
					"type": "postback",
					"label": district.description,
					"data": new_postback_data.model_dump_json()
				}
			}		
		)
	return return_message