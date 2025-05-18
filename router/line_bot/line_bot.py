import datetime
import json
from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from pydantic import ValidationError
from shapely import wkb
from pymongo import MongoClient

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage
from linebot.models import (StickerMessage, FlexSendMessage)

from database.rdbms import *
from models.postback_data import PostbackDataModel
from template.carousel_accomo import generate_carousel_accomo_template
from template.carousel_activity import generate_carousel_event_template
from template.carousel_exhibition import generate_carousel_exhibit_template
from template.carousel_food import generate_carousel_food_template
from template.carousel_spot import generate_carousel_spot_template
from template.select_accomo_subtype_template import generate_accomo_subtype_template
from template.select_area_template import generate_area_template
from template.select_asf_template import generate_asf_template
from template.select_city_template import generate_county_template
from template.select_distrct_template import generate_district_template
from template.select_food_subtype_template import generate_food_subtype_template
from template.select_location_template import generate_location_template
from template.select_spot_subtype_template import generate_spot_subtype_template
from libs.collections.line_bot_menu_selection import LineBotMenuSelection
from libs.collections.postback_trigger_type import PostbackTriggerType
from libs.collections.area import Area
from libs.collections.city import City
from libs.collections.district import District
from libs.collections.filter_match_mode import FilterMatchMode

router = APIRouter()


def print_postback_data(postback_data: PostbackDataModel):
    print(" ========================= Postback Data ========================= ")
    from libs.collections.area import Area
    from libs.collections.city import City
    
    log_menu_type_str = LineBotMenuSelection.getDescriptionByCode(postback_data.menu_type) if postback_data.menu_type else None
    log_area_str = Area.getDescriptionByCode(postback_data.area) if postback_data.area else None
    log_county_str = City.getDescriptionByCode(postback_data.county) if postback_data.county else None
    log_district_str = District.getDescriptionByCode(postback_data.district) if postback_data.district else None
    log_main_type_str = PostbackTriggerType.getDescriptionByCode(postback_data.main_type) if postback_data.main_type else None
    log_sub_type_str = PostbackTriggerType.getDescriptionByCode(postback_data.sub_type) if postback_data.sub_type else None
    log_trigger_type_str = PostbackTriggerType.getDescriptionByCode(postback_data.trigger_type) if postback_data.trigger_type else None
    
    
    print(f"\t menu_type: {postback_data.menu_type} - {log_menu_type_str}")
    print(f"\t area: {postback_data.area} - {log_area_str}")
    print(f"\t county: {postback_data.county} - {log_county_str}")
    print(f"\t district: {postback_data.district} - {log_district_str}")
    print(f"\t main_type: {postback_data.main_type} - {log_main_type_str}")
    print(f"\t lat: {postback_data.lat}")
    print(f"\t lng: {postback_data.lng}")
    print(f"\t sub_type: {postback_data.sub_type} - {log_sub_type_str}")
    print(f"\t trigger_type: {postback_data.trigger_type} - {log_trigger_type_str}")
    
    print(" ------------------------- Postback Data ------------------------- ")

# region receive_message_handler
def receive_message_handler(data, line_bot_api: LineBotApi, db_main_session: Session):
    message_type = data['events'][0]['message']['type']     # 取得 LINe 收到的訊息類型 
    match(message_type):
        # region Text
        case "text":
            receive_text_message_handler(data, line_bot_api)
        # endregion Text            
        
        # region Image
        case "image":
            # 取得回傳訊息的 Token
            tk = data['events'][0]['replyToken']                
            reply = '你傳的是圖片'
            line_bot_api.reply_message(tk, TextSendMessage(reply))
        # endregion Image                
        
        # region Video
        case "video":
            # 取得回傳訊息的 Token
            tk = data['events'][0]['replyToken']                
            reply = '你傳的是影片'
            line_bot_api.reply_message(tk, TextSendMessage(reply))
        # endregion Video
        
        # region Sticker
        case "sticker":
            receive_sticker_message_handler(data, line_bot_api)
        # endregion Sticker
        
        # region Location
        case "location":
            # 取得回傳訊息的 Token
            tk = data['events'][0]['replyToken']
            
            # 取得 UserId
            user_id = data['events'][0]["source"]["userId"]
            
            # 取得地理位置資訊
            print(data['events'][0]['message'])
            lat = data['events'][0]['message']["latitude"]
            lng = data['events'][0]['message']["longitude"]
            address = data['events'][0]['message']["address"]
            
            postback_data = PostbackDataModel(
                menu_type=LineBotMenuSelection.Location.value.code,
                lat=lat,
                lng=lng,
                trigger_type=PostbackTriggerType.SelectGeoLocation.value.code,
                address=address
            )
            
            contents = generate_asf_template(postback_data)
            message = FlexSendMessage(alt_text="選擇美食、景點、住宿", contents=contents)
            line_bot_api.reply_message(tk, message)

        # endregion
            
        case _:
            pass    
# endregion receive_message_handler

# region recieve_postback_handler
async def recieve_postback_handler(data, line_bot_api: LineBotApi, db_main_session: Session):
    # 取得回傳訊息的 Token
    tk = data['events'][0]['replyToken']
    
    # 取得 UserId
    user_id = data['events'][0]["source"]["userId"]
    
    # 取得 LINE Postback Data
    try:
        postback_data = PostbackDataModel.model_validate_json(data['events'][0]['postback']['data'])
    except ValidationError as e:
        return
    
    print_postback_data(postback_data)
    
    match(postback_data.trigger_type):
        
        # region 選擇位置
        case PostbackTriggerType.SelectLocation.value.code:
            postback_data = PostbackDataModel(
                trigger_type=PostbackTriggerType.SelectArea.value.code,
                menu_type = LineBotMenuSelection.Location.value.code
            )
            contents = generate_area_template(postback_data)
            message = FlexSendMessage(alt_text=LineBotMenuSelection.Location.value.description, contents=contents)
            line_bot_api.reply_message(tk, message)
        # endregion 選擇位置
        
        # region 選擇區域
        case PostbackTriggerType.SelectArea.value.code:
            contents = generate_county_template(postback_data)
            message = FlexSendMessage(alt_text=PostbackTriggerType.SelectArea.value.description, contents=contents)
            line_bot_api.reply_message(tk, message)
        # endregion 選擇區域 
        
        # region 選擇縣市
        case PostbackTriggerType.SelectCounty.value.code:
            
            match(postback_data.menu_type):
                # region 展演
                case LineBotMenuSelection.Exhibit.value.code:
                    exclude_count = 0
                    exclude_ids = []
                    
                    county: City = City.getItemByCode(postback_data.county)
                    
                    if not county:
                        return
                    
                    # region 取得指定時間內推薦過的exhibit_id
                    with MongoClient(system_config.mongodb_uri) as client:
                        db = client.user_db_2
                        collection = db.user
                        
                        datetime_threshold = datetime.datetime.now() - datetime.timedelta(hours=Constant.EXCLUDE_RECOMMAND_HOUR)
                        result = collection.aggregate([
                            {
                                "$match": {
                                    "users_id": user_id,
                                    "s_type": "找展演",
                                    "c_time": {"$gt": datetime_threshold},
                                }
                            },
                            {
                                "$group": {
                                    "_id": "$record_id"
                                }
                            },
                            {
                                "$project": {
                                    "_id": 0,
                                    "record_id": "$_id"
                                }
                            },        
                            # {
                            #     "$count" : "total_rows"
                            # }            
                        ])                
                                    
                        for record in result:
                            exclude_ids.append(record["record_id"])                    
                    # endregion 取得指定時間內推薦過的exhibit_id
                    
                    # region 設定Filter
                    filters = {
                        "county": {
                            "value": county.value.description,
                            "matchMode": FilterMatchMode.CONTAINS.value
                        },
                        "e_time": {
                            "value": datetime.datetime.now() + datetime.timedelta(days=1),
                            "matchMode": FilterMatchMode.DATE_AFTER.value
                        },
                        "exhibit_id": {
                            "value": exclude_ids,
                            "matchMode": FilterMatchMode.NOT_IN_LIST.value
                        }
                    }
                    # endregion 設定Filter
                    
                    # region 取得資料筆數
                    
                    count, resp_code = await Exhibit.countAsync(
                        db_main_session,
                        filters=filters,                   
                    )
                    
                    if resp_code != RespCode.OK:
                        return
                    
                    # endregion 取得資料筆數                    
                    
                    if count == 0:
                        # 隨機取得
                        filters = {
                            "county": {
                                "value": county.value.description,
                                "matchMode": FilterMatchMode.CONTAINS.value
                            },
                            "e_time": {
                                "value": datetime.datetime.now() + datetime.timedelta(days=1),
                                "matchMode": FilterMatchMode.DATE_AFTER.value
                            }
                        } 
                        
                        exhibits, resp_code = await Exhibit.getListRandomAsync(
                            db_main_session, 
                            filters=filters,
                            row_per_page=7)                        
                                               
                    else:
                        # region 設定Sorts
                        sorts={
                            "1": { 
                                "field": "s_time",
                                "order": 1
                            }   
                        }                    
                        # endregion 設定Sorts
                      
                        exhibits, resp_code = await Exhibit.getListAsync(
                            db_main_session, 
                            filters=filters, 
                            sorts=sorts, 
                            row_per_page=7)                

                    # region 回傳Line Bot
                    if len(exhibits) > 0:
                        contents = generate_carousel_exhibit_template(exhibits, postback_data)

                        message = FlexSendMessage(alt_text=LineBotMenuSelection.Exhibit.value.description, contents=contents)
                        line_bot_api.reply_message(tk, message) 
                                
                    else:
                        line_bot_api.reply_message(tk, messages=TextSendMessage(text="查詢無資料"))
                        return 
                    
                    # endregion 回傳Line Bot

                    # region 將搜尋結果紀錄至MongoDB
                    mongodb_user_results_list = []
                    
                    for exhibit in exhibits:
                        mongodb_user_results_list.append(
                            {
                                "users_id": user_id,
                                "area": Area.getDescriptionByCode(postback_data.area) if postback_data.area else None,
                                "county": City.getDescriptionByCode(postback_data.county) if postback_data.county else None,
                                "c_time": datetime.datetime.now(),
                                "s_type": LineBotMenuSelection.getDescriptionByCode(postback_data.menu_type),
                                "record_id": exhibit.exhibit_id,
                            }
                        )
                    
                    with MongoClient(system_config.mongodb_uri) as client:
                        db = client.user_db_2
                        collection = db.user
                        collection.insert_many(mongodb_user_results_list)

                    
                    # endregion 將搜尋結果紀錄至MongoDB
                    
                # endregion 展演
                
                # region 活動
                case LineBotMenuSelection.Event.value.code:
                    
                    exclude_ids = []                    
                    county: City = City.getItemByCode(postback_data.county)
                    
                    if not county:
                        return
                        
                    
                    # region 取得指定時間內推薦過的event_id
                    with MongoClient(system_config.mongodb_uri) as client:
                        db = client.user_db_2
                        collection = db.user
                        
                        datetime_threshold = datetime.datetime.now() - datetime.timedelta(hours=Constant.EXCLUDE_RECOMMAND_HOUR)
                        result = collection.aggregate([
                            {
                                "$match": {
                                    "users_id": user_id,
                                    "s_type": "找活動",
                                    "c_time": {"$gt": datetime_threshold},
                                }
                            },
                            {
                                "$group": {
                                    "_id": "$record_id"
                                }
                            },
                            {
                                "$project": {
                                    "_id": 0,
                                    "record_id": "$_id"
                                }
                            },        
                            # {
                            #     "$count" : "total_rows"
                            # }            
                        ])                
                                    
                        for record in result:
                            exclude_ids.append(record["record_id"])                    
                    # endregion 取得指定時間內推薦過的event_id
                                                
                    # region 設定Filter
                    filters = {
                        "county": {
                            "value": county.value.description,
                            "matchMode": FilterMatchMode.CONTAINS.value
                        },
                        "e_time": {
                            "value": datetime.datetime.now() + datetime.timedelta(days=1),
                            "matchMode": FilterMatchMode.DATE_AFTER.value
                        },
                        "events_id": {
                            "value": exclude_ids,
                            "matchMode": FilterMatchMode.NOT_IN_LIST.value
                        }
                    }
                    # endregion 設定Filter
    
                    # region 取得資料筆數
                    
                    count, resp_code = await Event.countAsync(
                        db_main_session,
                        filters=filters,                   
                    )
                    
                    if resp_code != RespCode.OK:
                        return
                    
                    # endregion 取得資料筆數                      
                    
                    if count == 0:
                        # 隨機取得
                        filters = {
                            "county": {
                                "value": county.value.description,
                                "matchMode": FilterMatchMode.CONTAINS.value
                            },
                            "e_time": {
                                "value": datetime.datetime.now() + datetime.timedelta(days=1),
                                "matchMode": FilterMatchMode.DATE_AFTER.value
                            }
                        } 
                        
                        events, resp_code = await Event.getListRandomAsync(
                            db_main_session, 
                            filters=filters,
                            row_per_page=7)                        
                                               
                    else:
                        # region 設定Sorts
                        sorts={
                            "1": { 
                                "field": "s_time",
                                "order": 1
                            }   
                        }                    
                        # endregion 設定Sorts
                      
                        events, resp_code = await Event.getListAsync(
                            db_main_session, 
                            filters=filters, 
                            sorts=sorts, 
                            row_per_page=7)                

                    # region 回傳Line Bot
                    if len(events) > 0:
                        contents = generate_carousel_event_template(events, postback_data)

                        message = FlexSendMessage(alt_text=LineBotMenuSelection.Event.value.description, contents=contents)
                        line_bot_api.reply_message(tk, message) 
                                
                    else:
                        line_bot_api.reply_message(tk, messages=TextSendMessage(text="查詢無資料"))
                        return 
                    
                    # endregion 回傳Line Bot

                    # region 將搜尋結果紀錄至MongoDB
                    mongodb_user_results_list = []
                    
                    for event in events:
                        mongodb_user_results_list.append(
                            {
                                "users_id": user_id,
                                "area": Area.getDescriptionByCode(postback_data.area) if postback_data.area else None,
                                "county": City.getDescriptionByCode(postback_data.county) if postback_data.county else None,
                                "c_time": datetime.datetime.now(),
                                "s_type": LineBotMenuSelection.getDescriptionByCode(postback_data.menu_type),
                                "record_id": event.events_id,
                            }
                        )
                    
                    with MongoClient(system_config.mongodb_uri) as client:
                        db = client.user_db_2
                        collection = db.user
                        collection.insert_many(mongodb_user_results_list)

                    
                    # endregion 將搜尋結果紀錄至MongoDB
                                           
                
                # endregion 活動
                
                # region 找附近
                case LineBotMenuSelection.Location.value.code:
                    # 選擇Distrct
                    contents = generate_district_template(postback_data)
                    message = FlexSendMessage(alt_text=PostbackTriggerType.SelectDistrict.value.description, contents=contents)
                    line_bot_api.reply_message(tk, message)                    
                    pass
                
                # endregion 找附近
                case _:
                    pass 
        # endregion 選擇縣市
        
        # region 選擇鄉鎮區
        case PostbackTriggerType.SelectDistrict.value.code:
            contents = generate_asf_template(postback_data)
            message = FlexSendMessage(alt_text="選擇美食、景點、住宿", contents=contents)
            line_bot_api.reply_message(tk, message)                    

        # endregion 選擇鄉鎮區

        # region 找美食
        case PostbackTriggerType.SelectFood.value.code:
            contents = generate_food_subtype_template(postback_data)
            message = FlexSendMessage(alt_text=PostbackTriggerType.SelectFood.value.description, contents=contents)
            line_bot_api.reply_message(tk, message)
        # endregion 找美食
        
        # region 找餐廳 | 找咖啡廳
        case PostbackTriggerType.SelectResturant.value.code | PostbackTriggerType.SelectCoffee.value.code:
            exclude_count = 0
            exclude_ids = []
            
            # region 取得指定時間內推薦過的food_id
            with MongoClient(system_config.mongodb_uri) as client:
                db = client.user_db_2
                collection = db.user
                
                datetime_threshold = datetime.datetime.now() - datetime.timedelta(hours=Constant.EXCLUDE_RECOMMAND_HOUR)
                result = collection.aggregate([
                    {
                        "$match": {
                            "users_id": user_id,
                            "s_cate": "找美食",
                            "c_time": {"$gt": datetime_threshold},
                        }
                    },
                    {
                        "$group": {
                            "_id": "$record_id"
                        }
                    },
                    {
                        "$project": {
                            "_id": 0,
                            "record_id": "$_id"
                        }
                    },        
                    # {
                    #     "$count" : "total_rows"
                    # }            
                ])                
                              
                for record in result:
                    exclude_ids.append(record["record_id"])
            # endregion 取得指定時間內推薦過的food_id
            
            # region 設定filter f_type
            type_value = ""
            match(postback_data.trigger_type):
                case PostbackTriggerType.SelectResturant.value.code:
                    type_value = "餐廳"
                case PostbackTriggerType.SelectCoffee.value.code:
                    type_value = "咖啡廳"
                case _:
                    return
            # endregion 設定filter s_type
            
            # region 分享位置(座標定位)
            if postback_data.lat is not None and postback_data.lng is not None:
                filters = {
                    "f_type": {
                        "value": type_value,
                        "matchMode": FilterMatchMode.EQUALS.value
                    },
                    "food_id": {
                        "value": exclude_ids,
                        "matchMode": FilterMatchMode.NOT_IN_LIST.value
                    }                    
                }
                
                # region 取得資料筆數
                
                count, resp_code = await Food.countByDistanceAsync(
                    db_main_session,
                    lng=postback_data.lng,
                    lat=postback_data.lat,
                    filters=filters,                   
                )
                
                if resp_code != RespCode.OK:
                    return
                
                # endregion 取得資料筆數
                
                if count == 0:
                    # 隨機取得
                    
                    filters = {
                        "f_type": {
                            "value": type_value,
                            "matchMode": FilterMatchMode.EQUALS.value
                        }                  
                    }                    
                    
                    foods, _ = await Food.getListByDistanceRandomAsync(
                        db_main_session,
                        lng=postback_data.lng,
                        lat=postback_data.lat,
                        filters=filters, 
                        row_per_page=7)                    
                    
                else:
                    foods, _ = await Food.getListByDistanceAsync(
                        db_main_session,
                        lng=postback_data.lng,
                        lat=postback_data.lat,
                        filters=filters, 
                        row_per_page=7)
                
                foods = [food for (food, distance) in foods]
                
                

            # endregion 分享位置(座標定位)
            
            # region 所在位置     
            elif postback_data.district is not None:
                # 設定Filter
                filters = {
                    "area": {
                        "value": District.getDescriptionByCode(postback_data.district),
                        "matchMode": FilterMatchMode.CONTAINS.value
                    },
                    "f_type": {
                        "value": type_value,
                        "matchMode": FilterMatchMode.EQUALS.value
                    },
                    "food_id": {
                        "value": exclude_ids,
                        "matchMode": FilterMatchMode.NOT_IN_LIST.value
                    }
                }
                
                # region 取得資料筆數
                
                count, resp_code = await Food.countAsync(
                    db_main_session,
                    filters=filters,                   
                )
                
                if resp_code != RespCode.OK:
                    return
                
                # endregion 取得資料筆數                
                
                if count == 0:
                    # 隨機取得
                    
                    filters = {
                        "area": {
                            "value": District.getDescriptionByCode(postback_data.district),
                            "matchMode": FilterMatchMode.CONTAINS.value
                        },
                        "f_type": {
                            "value": type_value,
                            "matchMode": FilterMatchMode.EQUALS.value
                        },                                        
                    }                    
                    
                    foods, _ = await Food.getListRandomAsync(
                        db_main_session,
                        filters=filters, 
                        row_per_page=7)                    
                    
                else:
                    foods, _ = await Food.getListAsync(
                        db_main_session,
                        filters=filters, 
                        row_per_page=7)                
                
                               

            # endregion 所在位置
            
            # region 回傳Line Bot
            if len(foods) > 0:
                contents = generate_carousel_food_template(foods, postback_data, user_id)

                message = FlexSendMessage(alt_text=PostbackTriggerType.getDescriptionByCode(postback_data.trigger_type), contents=contents)
                line_bot_api.reply_message(tk, message)
                           
            else:
                line_bot_api.reply_message(tk, messages=TextSendMessage(text="查詢無資料"))
                return            
            
            # endregion 回傳Line Bot
            
            # region 將搜尋結果紀錄至MongoDB
            mongodb_user_results_list = []
            
            for food in foods:
                
                # region Point 轉換成經緯度
                point = wkb.loads(bytes(food.geo_loc.data))  # 轉為 shapely.geometry.Point 物件
                lat = point.y  # 緯度 (Latitude)
                lng = point.x  # 經度 (Longitude)
                # endregion Point 轉換成經緯度                    
                
                mongodb_user_results_list.append(
                    {
                        "users_id": user_id,
                        "area": Area.getDescriptionByCode(postback_data.area) if postback_data.area else None,
                        "county": City.getDescriptionByCode(postback_data.county) if postback_data.county else None,
                        "township": District.getDescriptionByCode(postback_data.district) if postback_data.district else None,
                        "c_time": datetime.datetime.now(),
                        "s_type": LineBotMenuSelection.getDescriptionByCode(postback_data.menu_type),
                        "s_cate": PostbackTriggerType.getDescriptionByCode(postback_data.main_type),
                        "s_detail": PostbackTriggerType.getDescriptionByCode(postback_data.sub_type),
                        "s_type_url": "",
                        "s_detail_url": "",
                        "record_id": food.food_id,
                        "lat": lat,
                        "lng": lng,
                    }
                )
            
            with MongoClient(system_config.mongodb_uri) as client:
                db = client.user_db_2
                collection = db.user
                collection.insert_many(mongodb_user_results_list)

            # endregion 將搜尋結果紀錄至MongoDB             

        # endregion 找餐廳 | 找咖啡廳
        
        # region 找景點
        case PostbackTriggerType.SelectSpot.value.code:
            contents = generate_spot_subtype_template(postback_data)
            message = FlexSendMessage(alt_text=PostbackTriggerType.SelectSpot.value.description, contents=contents)
            line_bot_api.reply_message(tk, message)
        # endregion 找景點

        # region 想去室內 | 戶外
        case PostbackTriggerType.SelectIndoor.value.code | PostbackTriggerType.SelectOutdoor.value.code:
            
            exclude_count = 0
            exclude_ids = []
            
            # region 取得指定時間內推薦過的spot_id
            with MongoClient(system_config.mongodb_uri) as client:
                db = client.user_db_2
                collection = db.user
                
                datetime_threshold = datetime.datetime.now() - datetime.timedelta(hours=Constant.EXCLUDE_RECOMMAND_HOUR)
                result = collection.aggregate([
                    {
                        "$match": {
                            "users_id": user_id,
                            "s_cate": "找景點",
                            "c_time": {"$gt": datetime_threshold},
                        }
                    },
                    {
                        "$group": {
                            "_id": "$record_id"
                        }
                    },
                    {
                        "$project": {
                            "_id": 0,
                            "record_id": "$_id"
                        }
                    },        
                    # {
                    #     "$count" : "total_rows"
                    # }            
                ])                
                              
                for record in result:
                    exclude_ids.append(record["record_id"])
            # endregion 取得推薦過的spot_id
            
            # region 設定filter s_type
            type_value = ""
            match(postback_data.trigger_type):
                case PostbackTriggerType.SelectIndoor.value.code:
                    type_value = "室內"
                case PostbackTriggerType.SelectOutdoor.value.code:
                    type_value = "戶外"
                case _:
                    return
            # endregion 設定filter s_type
            
            # region 分享位置(座標定位)
            if postback_data.lat is not None and postback_data.lng is not None:
                filters = {
                    "s_type": {
                        "value": type_value,
                        "matchMode": FilterMatchMode.EQUALS.value
                    },
                    "spot_id": {
                        "value": exclude_ids,
                        "matchMode": FilterMatchMode.NOT_IN_LIST.value
                    }                    
                }
                
                # region 取得資料筆數
                
                count, resp_code = await Spot.countByDistanceAsync(
                    db_main_session,
                    lng=postback_data.lng,
                    lat=postback_data.lat,
                    filters=filters,                   
                )
                
                if resp_code != RespCode.OK:
                    return
                
                # endregion 取得資料筆數
                
                if count == 0:
                    # 隨機取得
                    
                    filters = {
                        "s_type": {
                            "value": type_value,
                            "matchMode": FilterMatchMode.EQUALS.value
                        }                  
                    }                    
                    
                    spots, _ = await Spot.getListByDistanceRandomAsync(
                        db_main_session,
                        lng=postback_data.lng,
                        lat=postback_data.lat,
                        filters=filters, 
                        row_per_page=7)                    
                    
                else:
                    spots, _ = await Spot.getListByDistanceAsync(
                        db_main_session,
                        lng=postback_data.lng,
                        lat=postback_data.lat,
                        filters=filters, 
                        row_per_page=7)
                
                spots = [spot for (spot, distance) in spots]
                
                

            # endregion 分享位置(座標定位)
            
            # region 所在位置     
            elif postback_data.district is not None:
                # 設定Filter
                filters = {
                    "area": {
                        "value": District.getDescriptionByCode(postback_data.district),
                        "matchMode": FilterMatchMode.CONTAINS.value
                    },
                    "s_type": {
                        "value": type_value,
                        "matchMode": FilterMatchMode.EQUALS.value
                    },
                    "spot_id": {
                        "value": exclude_ids,
                        "matchMode": FilterMatchMode.NOT_IN_LIST.value
                    }
                }
                
                # region 取得資料筆數
                
                count, resp_code = await Spot.countAsync(
                    db_main_session,
                    filters=filters,                   
                )
                
                if resp_code != RespCode.OK:
                    return
                
                # endregion 取得資料筆數                
                
                if count == 0:
                    # 隨機取得
                    
                    filters = {
                        "area": {
                            "value": District.getDescriptionByCode(postback_data.district),
                            "matchMode": FilterMatchMode.CONTAINS.value
                        },
                        "s_type": {
                            "value": type_value,
                            "matchMode": FilterMatchMode.EQUALS.value
                        },                                        
                    }                    
                    
                    spots, _ = await Spot.getListRandomAsync(
                        db_main_session,
                        filters=filters, 
                        row_per_page=7)                    
                    
                else:
                    spots, _ = await Spot.getListAsync(
                        db_main_session,
                        filters=filters, 
                        row_per_page=7)                
                
                               

            # endregion 所在位置
            
            # region 回傳Line Bot
            if len(spots) > 0:
                contents = generate_carousel_spot_template(spots, postback_data, user_id)

                message = FlexSendMessage(alt_text=PostbackTriggerType.getDescriptionByCode(postback_data.trigger_type), contents=contents)
                line_bot_api.reply_message(tk, message)
                           
            else:
                line_bot_api.reply_message(tk, messages=TextSendMessage(text="查詢無資料"))
                return            
            
            # endregion 回傳Line Bot
            
            # region 將搜尋結果紀錄至MongoDB
            mongodb_user_results_list = []
            
            for spot in spots:
                
                # region Point 轉換成經緯度
                point = wkb.loads(bytes(spot.geo_loc.data))  # 轉為 shapely.geometry.Point 物件
                lat = point.y  # 緯度 (Latitude)
                lng = point.x  # 經度 (Longitude)
                # endregion Point 轉換成經緯度                    
                
                mongodb_user_results_list.append(
                    {
                        "users_id": user_id,
                        "area": Area.getDescriptionByCode(postback_data.area) if postback_data.area else None,
                        "county": City.getDescriptionByCode(postback_data.county) if postback_data.county else None,
                        "township": District.getDescriptionByCode(postback_data.district) if postback_data.district else None,
                        "c_time": datetime.datetime.now(),
                        "s_type": LineBotMenuSelection.getDescriptionByCode(postback_data.menu_type),
                        "s_cate": PostbackTriggerType.getDescriptionByCode(postback_data.main_type),
                        "s_detail": PostbackTriggerType.getDescriptionByCode(postback_data.sub_type),
                        "s_type_url": "",
                        "s_detail_url": "",
                        "record_id": spot.spot_id,
                        "lat": lat,
                        "lng": lng,
                    }
                )
            
            with MongoClient(system_config.mongodb_uri) as client:
                db = client.user_db_2
                collection = db.user
                collection.insert_many(mongodb_user_results_list)

            # endregion 將搜尋結果紀錄至MongoDB             

                
        # endregion 想去室內 | 戶外

        # region 找住宿
        case PostbackTriggerType.SelectAccomo.value.code:
            contents = generate_accomo_subtype_template(postback_data)
            message = FlexSendMessage(alt_text=PostbackTriggerType.SelectAccomo.value.description, contents=contents)
            line_bot_api.reply_message(tk, message)
        # endregion 找住宿

        # region 住飯店 | 住民宿 | 住青旅
        case PostbackTriggerType.SelectHotel.value.code | PostbackTriggerType.SelectBandB.value.code | PostbackTriggerType.SelectHostel.value.code:
            
            exclude_count = 0
            exclude_ids = []            
            
            # region 取得指定時間內推薦過的accomo_id
            with MongoClient(system_config.mongodb_uri) as client:
                db = client.user_db_2
                collection = db.user
                
                datetime_threshold = datetime.datetime.now() - datetime.timedelta(hours=Constant.EXCLUDE_RECOMMAND_HOUR)
                result = collection.aggregate([
                    {
                        "$match": {
                            "users_id": user_id,
                            "s_cate": "找住宿",
                            "c_time": {"$gt": datetime_threshold},
                        }
                    },
                    {
                        "$group": {
                            "_id": "$record_id"
                        }
                    },
                    {
                        "$project": {
                            "_id": 0,
                            "record_id": "$_id"
                        }
                    },        
                    # {
                    #     "$count" : "total_rows"
                    # }            
                ])                
                              
                for record in result:
                    exclude_ids.append(record["record_id"])
            # endregion 取得推薦過的spot_id            
            
            # region 設定filter s_type
            type_value = ""
            match(postback_data.trigger_type):
                case PostbackTriggerType.SelectHotel.value.code:
                    type_value = "飯店"
                case PostbackTriggerType.SelectBandB.value.code:
                    type_value = "民宿"
                case PostbackTriggerType.SelectHostel.value.code:
                    type_value = "青旅"
                case _:
                    return
            # endregion 設定filter s_type
            
            # region 分享位置(座標定位)
            if postback_data.lat is not None and postback_data.lng is not None:
                filters = {
                    "ac_type": {
                        "value": type_value,
                        "matchMode": FilterMatchMode.EQUALS.value
                    },
                    "accomo_id": {
                        "value": exclude_ids,
                        "matchMode": FilterMatchMode.NOT_IN_LIST.value
                    }                     
                }     
                
                # region 取得資料筆數
                
                count, resp_code = await Accomo.countByDistanceAsync(
                    db_main_session,
                    lng=postback_data.lng,
                    lat=postback_data.lat,
                    filters=filters,                   
                )
                
                if resp_code != RespCode.OK:
                    return
                
                # endregion 取得資料筆數                
                
                if count == 0:
                    # 隨機取得
                    
                    filters = {
                        "ac_type": {
                            "value": type_value,
                            "matchMode": FilterMatchMode.EQUALS.value
                        }                  
                    }                    
                    
                    accomos, _ = await Accomo.getListByDistanceRandomAsync(
                        db_main_session,
                        lng=postback_data.lng,
                        lat=postback_data.lat,
                        filters=filters, 
                        row_per_page=7)   
                else:
                    accomos, _ = await Accomo.getListByDistanceAsync(
                        db_main_session,
                        lng=postback_data.lng,
                        lat=postback_data.lat,
                        filters=filters, 
                        row_per_page=7)
                
                accomos = [accomo for (accomo, distance) in accomos]                    
                    
                # endregion 分享位置(座標定位)
                    
            # region 所在位置     
            elif postback_data.district is not None:
                # 設定Filter
                filters = {
                    "area": {
                        "value": District.getDescriptionByCode(postback_data.district),
                        "matchMode": FilterMatchMode.CONTAINS.value
                    },
                    "ac_type": {
                        "value": type_value,
                        "matchMode": FilterMatchMode.EQUALS.value
                    },
                    "accomo_id": {
                        "value": exclude_ids,
                        "matchMode": FilterMatchMode.NOT_IN_LIST.value
                    }
                }
                
                # region 取得資料筆數
                
                count, resp_code = await Accomo.countAsync(
                    db_main_session,
                    filters=filters,                   
                )
                
                if resp_code != RespCode.OK:
                    return
                
                # endregion 取得資料筆數                
                
                if count == 0:
                    # 隨機取得
                    
                    filters = {
                        "area": {
                            "value": District.getDescriptionByCode(postback_data.district),
                            "matchMode": FilterMatchMode.CONTAINS.value
                        },
                        "ac_type": {
                            "value": type_value,
                            "matchMode": FilterMatchMode.EQUALS.value
                        },                                        
                    }                    
                    
                    accomos, _ = await Accomo.getListRandomAsync(
                        db_main_session,
                        filters=filters, 
                        row_per_page=7)                    
                    
                else:
                    accomos, _ = await Accomo.getListAsync(
                        db_main_session,
                        filters=filters, 
                        row_per_page=7)                
                
            # endregion 所在位置            

            # region 回傳Line Bot
            if len(accomos) > 0:
                contents = generate_carousel_accomo_template(accomos, postback_data, user_id)

                message = FlexSendMessage(alt_text=PostbackTriggerType.getDescriptionByCode(postback_data.trigger_type), contents=contents)
                line_bot_api.reply_message(tk, message)
                           
            else:
                line_bot_api.reply_message(tk, messages=TextSendMessage(text="查詢無資料"))
                return            
            
            # endregion 回傳Line Bot                               
            
            # region 將搜尋結果紀錄至MongoDB
            mongodb_user_results_list = []
            
            for accomo in accomos:
                
                # region Point 轉換成經緯度
                point = wkb.loads(bytes(accomo.geo_loc.data))  # 轉為 shapely.geometry.Point 物件
                lat = point.y  # 緯度 (Latitude)
                lng = point.x  # 經度 (Longitude)
                # endregion Point 轉換成經緯度                    
                
                mongodb_user_results_list.append(
                    {
                        "users_id": user_id,
                        "area": Area.getDescriptionByCode(postback_data.area) if postback_data.area else None,
                        "county": City.getDescriptionByCode(postback_data.county) if postback_data.county else None,
                        "township": District.getDescriptionByCode(postback_data.district) if postback_data.district else None,
                        "c_time": datetime.datetime.now(),
                        "s_type": LineBotMenuSelection.getDescriptionByCode(postback_data.menu_type),
                        "s_cate": PostbackTriggerType.getDescriptionByCode(postback_data.main_type),
                        "s_detail": PostbackTriggerType.getDescriptionByCode(postback_data.sub_type),
                        "s_type_url": "",
                        "s_detail_url": "",
                        "record_id": accomo.accomo_id,
                        "lat": lat,
                        "lng": lng,
                    }
                )
            
            with MongoClient(system_config.mongodb_uri) as client:
                db = client.user_db_2
                collection = db.user
                collection.insert_many(mongodb_user_results_list)

            # endregion 將搜尋結果紀錄至MongoDB             
                               
             
        # endregion 住飯店 | 住民宿 | 住青旅
               
        case _:
            pass                        
            
# endregion recieve_postback_handler

# region receive_text_message_handler
def receive_text_message_handler(data, line_bot_api: LineBotApi):
    
    # 取得回傳訊息的 Token
    tk = data['events'][0]['replyToken']
    
    # 取得 LINE 收到的文字訊息
    message_text = data['events'][0]['message']['text']  
    user_id = data['events'][0]["source"]["userId"]

    match(message_text):
        # region 找展演
        case LineBotMenuSelection.Exhibit.value.description:
            postback_data = PostbackDataModel(
                menu_type=LineBotMenuSelection.Exhibit.value.code
            )
            contents = generate_area_template(postback_data)
            message = FlexSendMessage(alt_text=LineBotMenuSelection.Exhibit.value.description, contents=contents)
            line_bot_api.reply_message(tk, message)

        # endregion 找展演
        
        # region 找活動
        case LineBotMenuSelection.Event.value.description:
            postback_data = PostbackDataModel(
                menu_type=LineBotMenuSelection.Event.value.code
            )
            contents = generate_area_template(postback_data)            
            message = FlexSendMessage(alt_text=LineBotMenuSelection.Event.value.description, contents=contents)
            line_bot_api.reply_message(tk, message)  
            
        # endregion 找活動
        
        # region 找附近           
        case LineBotMenuSelection.Location.value.description:
            line_bot_api.reply_message(tk, generate_location_template())
            
        # endregion 找附近
        
        case _:
            pass 
    
# endregion

# region receive_sticker_message_handler
def receive_sticker_message_handler(data, line_bot_api: LineBotApi):
    # 取得回傳訊息的 Token
    tk = data['events'][0]['replyToken']                
    # reply = '你傳的是貼圖'
    # line_bot_api.reply_message(tk, TextSendMessage(reply))
    print(data)
    line_bot_api.reply_message(
        reply_token=tk, 
        messages=StickerMessage(
            package_id=11537,
            sticker_id=52002735
        ),
    )
# endregion


# ------------------- API ----------------------------

# region Line Bot API
@router.post("/call")
async def root(
    request: Request,
    db_main_session: Session = Depends(db.get_main_session),
):
    try:
        line_bot_api = LineBotApi(system_config.line_access_token)              # 確認 token 是否正確
        handler = WebhookHandler(system_config.line_secret)                     # 確認 secret 是否正確        
        
        # region 解析Line Event 訊息
        
        body = await request.body()
        json_data = json.loads(body.decode())

        signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
        handler.handle(body.decode(), signature)             # 綁定訊息回傳的相關資訊
        # print(json_data)
        
        event_type = json_data['events'][0]['type']
        
        match(event_type):
            case "postback":
                await recieve_postback_handler(json_data, line_bot_api, db_main_session)
            case "message":
                receive_message_handler(json_data, line_bot_api, db_main_session)
            case _:
                pass
        
        # endregion 解析Line Event 訊息

    except InvalidSignatureError as e:
        # TODO 紀錄Log
        print(str(e))
    except Exception as e:
        # TODO 紀錄Log
        print(str(e))

    return "OK" # 驗證 Webhook 使用，不能省略    
    
# endregion Line Bot API

# region Line Bot Click Link API
@router.get("/redirect/{userId}")
async def get_available_parent_list(
    userId: str,
    main_type: int,
    item_id: str,
    redirect_url: str,    
):
    """ 紀錄Link操作相關資訊至MongoDB，並回傳Redirect
    """
    new_data = {
        "user_id": userId,
        "click_url": redirect_url,
        "s_cate": PostbackTriggerType.getDescriptionByCode(main_type),
        "record_id": item_id,
        "s_time": datetime.datetime.now()
    }
    
    with MongoClient(system_config.mongodb_uri) as conn:
        db = conn.user_s_result_db_2
        collection = db.user_s_result
        NewData_id = collection.insert_one(new_data).inserted_id
        print(f"資料id:{NewData_id}")        
        
    return RedirectResponse(redirect_url)
# endregion Line Bot Click Link API
