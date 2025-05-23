import copy
import math
from database.rdbms.main.spot import Spot
from libs.collections.district import District
from models.postback_data import PostbackDataModel
from system_global import global_setting
import urllib.parse

carousel_root_template = {
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

spot_template = {
	"type": "bubble",
	"hero": {
		"type": "image",
		"url": "",
		"size": "full",
		"aspectRatio": "20:13",
		"aspectMode": "cover",
		"action": {
			"type": "uri",
			"label": "Action",
			"uri": ""
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
	}
}
    
rate_template = {
	"type": "box",
	"layout": "baseline",
	"margin": "md",
	"contents": [
	]
}
  
rate_icon_template = {
	"type": "icon",
	"url": "",
	"size": "sm"
}

rate_text_template = {
	"type": "text",
	"text": "",
	"size": "sm",
	"color": "#999999",
	"flex": 0,
	"margin": "md",
	"contents": []	
}
  
def generate_spot_title_template(title: str):
    """
		{
			"type": "text",
			"text": "",
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
  
def generate_spot_detail_template(title: str, value: str):
    new_template = copy.deepcopy(body_content_detail_template)
    new_template["contents"][0]["text"] = title
    new_template["contents"][1]["text"] = value
    
    return new_template

def generate_rate_text_template(score: float, comm: str):
    new_template = copy.deepcopy(rate_text_template)
    new_template["text"] = f"{str(score)} ({comm:,})"
    return new_template

def generate_rate_icon_template(url):
    new_template = copy.deepcopy(rate_icon_template)
    new_template["url"] = url
    return new_template

def generate_rate_template(score: float, comm: str):
    new_template = copy.deepcopy(rate_template)
    
    full_star_image_url = "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
    half_star_image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzdikfDI9FSkeTT5QslMs2PQOwrRNV9neesw&s"
    empty_star_image_url = "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
    
    decimal_part, integer_part = math.modf(score)
    full_count = int(integer_part)
    half_count = 1 if decimal_part > 0 else 0
    empty_count = int(5 - (full_count + half_count))
    
    for i in range(full_count):
        new_template["contents"].append(
			generate_rate_icon_template(full_star_image_url)
		)
        
    for i in range(half_count):
        new_template["contents"].append(
			generate_rate_icon_template(half_star_image_url)
		)
        
    for i in range(empty_count):
        new_template["contents"].append(
			generate_rate_icon_template(empty_star_image_url)
		)
        
    new_template["contents"].append(
		generate_rate_text_template(score, comm)
	)
    
    return new_template         
    
    

def generate_spot_template(spot: Spot, postback_data: PostbackDataModel, user_id: str):
    new_template = copy.deepcopy(spot_template)

    # region Point 轉換成經緯度
    # point = wkb.loads(bytes(spot.geo_loc.data))  # 轉為 shapely.geometry.Point 物件
    # lat = point.y  # 緯度 (Latitude)
    # lng = point.x  # 經度 (Longitude)
    # postback_data.lat = lng
    # postback_data.lng = lat
    # endregion Point 轉換成經緯度
    
    new_template["hero"]["url"] = spot.pic_url
    
    link = f"{global_setting.ngrok_url}/line_bot/redirect/{user_id}?main_type={postback_data.main_type}&item_id={spot.spot_id}&redirect_url={urllib.parse.quote(spot.gmaps_url)}"

    new_template["hero"]["action"]["uri"] = link
    new_template["body"]["contents"][0]["text"] = spot.s_name
    new_template["body"]["contents"][0] = generate_spot_title_template(spot.s_name)
    
    if spot.rate:
        new_template["body"]["contents"][1]["contents"].append(
			generate_rate_template(spot.rate, spot.comm)
		)
    
    if spot.address:
        new_template["body"]["contents"][1]["contents"].append(
         	generate_spot_detail_template("地址", spot.address)
        )  

    if spot.b_hours:
        new_template["body"]["contents"][1]["contents"].append(
         	generate_spot_detail_template("營業時間", spot.b_hours)
        )            

    return new_template
 
def generate_carousel_spot_template(spots: list[Spot], postback_data: PostbackDataModel, user_id: str):
    
    new_template = copy.deepcopy(carousel_root_template)
    booking_search = postback_data.address if postback_data.address else District.getDescriptionByCode(postback_data.district)
    
    for spot in spots:
        
        new_spot_template = generate_spot_template(spot, postback_data, user_id)
        new_template["contents"].append(
            new_spot_template
        )
        
        
    new_template["contents"].append(
		{
			"type": "bubble",
			"hero": {
				"type": "image",
				"url": "https://i.ytimg.com/vi/ZG4JQX4BO9A/maxresdefault.jpg",
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
							"uri": f"https://www.google.com.tw/maps/place/{urllib.parse.quote(booking_search)}"
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