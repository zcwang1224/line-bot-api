# -*- coding:utf-8 -*-
from collections import namedtuple

from libs.collections.area import Area
from .base import Base


PostbackTriggerTypeNamedTuple = namedtuple('PostbackTriggerTypeNamedTuple', ['code', 'description', 'description_en', 'columns'])

class PostbackTriggerType(Base):
    
    SelectArea = PostbackTriggerTypeNamedTuple(1, "所在區域", "Area", None)
    SelectCounty = PostbackTriggerTypeNamedTuple(2, "所在縣市", "County", None)
    SelectDistrict = PostbackTriggerTypeNamedTuple(3, "所在鄉鎮區", "District", None)
    SelectLocation = PostbackTriggerTypeNamedTuple(4, "所在位置", "Location", None)
    SelectGeoLocation = PostbackTriggerTypeNamedTuple(5, "分享位置", "Geo Location", None)
    
    SelectFood = PostbackTriggerTypeNamedTuple(11, "找美食", "Food", None)
    SelectSpot = PostbackTriggerTypeNamedTuple(12, "找景點", "Spot", None)
    SelectAccomo = PostbackTriggerTypeNamedTuple(13, "找住宿", "Accomo", None)

    SelectResturant = PostbackTriggerTypeNamedTuple(21, "找餐廳", "Resturant", None)
    SelectCoffee = PostbackTriggerTypeNamedTuple(22, "找咖啡廳", "Coffee", None)
    
    
    SelectIndoor = PostbackTriggerTypeNamedTuple(31, "想去室內", "Indoor", None)
    SelectOutdoor = PostbackTriggerTypeNamedTuple(32, "想去室外", "Outdoor", None)
    
    SelectHotel = PostbackTriggerTypeNamedTuple(41, "住飯店", "Hotel", None)
    SelectBandB = PostbackTriggerTypeNamedTuple(42, "住民宿", "B&B", None)
    SelectHostel = PostbackTriggerTypeNamedTuple(43, "住青旅", "Hostel", None)
    
    
    @staticmethod
    def getMainTypeList():
        return [
            PostbackTriggerType.SelectFood,
            PostbackTriggerType.SelectSpot,            
            PostbackTriggerType.SelectAccomo,
        ]
        
    @staticmethod
    def getFoodSubtypeList():
        return [
            PostbackTriggerType.SelectResturant, 
            PostbackTriggerType.SelectCoffee,
        ]
        
    @staticmethod
    def getSpotSubtypeList():
        return [
            PostbackTriggerType.SelectIndoor, 
            PostbackTriggerType.SelectOutdoor,            
        ]
        
    @staticmethod
    def getAccomoSubtypeList():
        return [
            PostbackTriggerType.SelectHotel,
            PostbackTriggerType.SelectBandB,
            PostbackTriggerType.SelectHostel,
        ]        