import copy
import json
from database.rdbms.main.exhibit import Exhibit
from models.postback_data import PostbackDataModel
from template.select_footer_asf import generate_footer_asf_template
from shapely import wkb

from datetime import datetime

carousel_exhibit_root_template = {
  "type": "carousel",
  "contents": []
}

body_content_title_template = {
    "type": "text",
    "text": "",
    "weight": "bold",
    "size": "xl",
    "gravity": "center",
    "wrap": True,
    "contents": []
}

body_content_detail_template = {
	"type": "box",
	"layout": "baseline",
	"spacing": "sm",
	"contents": [
		{
			"type": "text",
			"text": "",
			"size": "sm",
			"color": "#AAAAAA",
			"flex": 2,
			"contents": []
		},
		{
			"type": "text",
			"text": "",
			"size": "sm",
			"color": "#666666",
			"flex": 4,
			"wrap": True,
			"contents": []
		}
	]
}

exhibit_template = {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://res.klook.com/image/upload/v1744167529/bqzzmmjux4v9ahw3xa5g.jpg",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com/"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "contents": [
          {
            "type": "text",
            "text": "",
            "weight": "bold",
            "size": "xl",
            "gravity": "center",
            "wrap": True,
            "contents": []
          },
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "margin": "lg",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "flex": 1,
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "postback",
                  "label": "找美食",
                  "data": "找美食"
                }
              },
              {
                "type": "button",
                "action": {
                  "type": "postback",
                  "label": "找景點",
                  "data": "找景點"
                }
              },
              {
                "type": "button",
                "action": {
                  "type": "postback",
                  "label": "找住宿",
                  "data": "找住宿"
                }
              }
            ]
          }
        ]
      }
    }

def generate_exhibit_title_template(title: str):
    """
		{
			"type": "text",
			"text": "Travis Japan演唱會2025台北站｜Travis Japan World Tour 2025 VIIsual｜Zepp New Taipei",
			"weight": "bold",
			"size": "xl",
			"gravity": "center",
			"wrap": True,
			"contents": []
		}    
    """
    new_template = copy.deepcopy(body_content_title_template)
    new_template["text"] = title
    
    return new_template
  
def generate_exhibit_detail_template(title: str, value: str):
    new_template = copy.deepcopy(body_content_detail_template)
    new_template["contents"][0]["text"] = title
    new_template["contents"][1]["text"] = value
    
    return new_template
    

def generate_exhibit_template(exhibit: Exhibit, postback_data: PostbackDataModel):
    new_template = copy.deepcopy(exhibit_template)
    
    # region Point 轉換成經緯度
    point = wkb.loads(bytes(exhibit.geo_loc.data))  # 轉為 shapely.geometry.Point 物件
    lat = point.y  # 緯度 (Latitude)
    lng = point.x  # 經度 (Longitude)
    postback_data.lat = lng
    postback_data.lng = lat
    postback_data.address = exhibit.address
    postback_data.s_type_record_id = exhibit.exhibit_id
    # postback_data.s_type_url = exhibit.klook_url
    # endregion Point 轉換成經緯度
    
    
    new_template["hero"]["url"] = exhibit.pic_url
    new_template["hero"]["action"]["uri"] = exhibit.klook_url
    new_template["body"]["contents"][0] = generate_exhibit_title_template(exhibit.ex_name)
    
    if exhibit.s_time:
        new_template["body"]["contents"][1]["contents"].append(
         	generate_exhibit_detail_template("開始時間", datetime.strftime(exhibit.s_time, "%Y/%m/%d"))
        )
        
    if exhibit.e_time:
        new_template["body"]["contents"][1]["contents"].append(
         	generate_exhibit_detail_template("結束時間", datetime.strftime(exhibit.e_time, "%Y/%m/%d"))
        )
        
    if exhibit.address:
        new_template["body"]["contents"][1]["contents"].append(
         	generate_exhibit_detail_template("展覽地點", exhibit.address)
        )                
    
    new_template["footer"] = generate_footer_asf_template(postback_data)
    
    return new_template
 
def generate_carousel_exhibit_template(exhibits: list[Exhibit], postback_data: PostbackDataModel):
    
    new_template = copy.deepcopy(carousel_exhibit_root_template)
    
    for exhibit in exhibits:
        
        new_exhibit_template = generate_exhibit_template(exhibit, postback_data)
        new_template["contents"].append(
            new_exhibit_template
        )
        
    new_template["contents"].append(
		{
			"type": "bubble",
			"hero": {
				"type": "image",
				"url": "https://res.klook.com/image/upload/q_auto,c_fill,w_1120,h_584/v1645439471/fyhpxzhcyqrzhpxnthoo.jpg",
				"size": "full",
				"aspectRatio": "20:13",
				"aspectMode": "cover",
				"action": {
					"type": "postback",
					"label": "Action",
					"data": "aaa"
				}
			},
			"body": {
				"type": "box",
				"layout": "horizontal",
				"spacing": "md",
				"contents": [
				{
					"type": "box",
					"layout": "vertical",
					"flex": 1,
					"backgroundColor": "#FFFFFFFF",
					"borderColor": "#FFFFFFFF",
					"contents": [
					{
						"type": "button",
						"action": {
						"type": "uri",
						"label": "想看更多",
						"uri": f"https://www.klook.com/zh-TW"
						},
      					"gravity": "center"
					}
					]
				}
				]
			}
		}		
	)       
        
    return new_template