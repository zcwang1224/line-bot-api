# -*- coding:utf-8 -*-
from collections import namedtuple

from libs.collections.area import Area
from .base import Base


CityNamedTuple = namedtuple('CityNamedTuple', ['code', 'description', 'description_en', 'columns'])

class City(Base):
    Keelung = CityNamedTuple(1, "基隆", "Keelung", None)
    Taipei = CityNamedTuple(2, "台北", "Taipei", None)
    New_Taipei = CityNamedTuple(3, "新北", "New Taipei", None)    
    Taoyuan = CityNamedTuple(4, "桃園", "Taoyuan", None)
    Hsinchu = CityNamedTuple(5, "新竹", "Hsinchu", None)
    Miaoli = CityNamedTuple(6, "苗栗", "Miaoli", None)
    Taichung = CityNamedTuple(7, "台中", "Taichung", None)
    Changhua = CityNamedTuple(8, "彰化", "Changhua", None)
    Nantou = CityNamedTuple(9, "南投", "Nantou", None)
    Yunlin = CityNamedTuple(10, "雲林", "Yunlin", None)
    Chiayi = CityNamedTuple(11, "嘉義", "Chiayi", None)
    Tainan = CityNamedTuple(12, "台南", "Tainan", None)
    Kaohsiung = CityNamedTuple(13, "高雄", "Kaohsiung", None)
    Pingtung = CityNamedTuple(14, "屏東", "Pingtung", None)
    Yilan = CityNamedTuple(15, "宜蘭", "Yilan", None)
    Hualien = CityNamedTuple(16, "花蓮", "Hualien", None)
    Taitung = CityNamedTuple(17, "台東", "Taitung", None)
    
    @classmethod
    def getItems(cls, excludes = []):
        items = [cls.__getattr__(attr) for attr in dir(cls) if (attr.startswith('__') == False and cls.__getattr__(attr) not in excludes) ]
        return sorted(items, key=lambda x: x.value.code)
    
    @classmethod
    def getItemByArea(cls, area: Area):
        match (area):
            case (Area.Northern):
                return [
                    City.Keelung,
                    City.Taipei,
                    City.New_Taipei,
                    City.Taoyuan,
                    City.Hsinchu,
                    City.Yilan,
                ]
            case (Area.Central):
                return [
                    City.Miaoli,
                    City.Taichung,
                    City.Changhua,
                    City.Nantou,
                    City.Yunlin,
                ]   
            case (Area.Southern):
                return [
                    City.Chiayi,
                    City.Tainan,
                    City.Kaohsiung,
                    City.Pingtung,
                ]   
            case (Area.Eastern):
                return [
                    City.Hualien,
                    City.Taitung,
                ]                                    
            case _:
                return None
 
 
 
 
 
 
 
 
 
 
 
 
 
 