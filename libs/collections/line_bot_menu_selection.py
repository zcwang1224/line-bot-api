# -*- coding:utf-8 -*-
from collections import namedtuple

from libs.collections.area import Area
from .base import Base


LineBotMenuSelectionNamedTuple = namedtuple('LineBotMenuSelectionNamedTuple', ['code', 'description', 'description_en', 'columns'])

class LineBotMenuSelection(Base):
    Exhibit = LineBotMenuSelectionNamedTuple(1, "找展演", "Exhibit", None)
    Event = LineBotMenuSelectionNamedTuple(2, "找活動", "Event", None)
    Location = LineBotMenuSelectionNamedTuple(3, "找附近", "Location", None)
    
    
    

 
 
 
 
 
 
 
 
 
 
 
 