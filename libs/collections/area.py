# -*- coding:utf-8 -*-
from collections import namedtuple
from .base import Base


AreaNamedTuple = namedtuple('AreaNamedTuple', ['code', 'description', 'description_en', 'columns'])

class Area(Base):
    Northern = AreaNamedTuple(1, "北部", "Northern", None)
    Central = AreaNamedTuple(2, "中部", "Central", None)
    Southern = AreaNamedTuple(3, "南部", "Southern", None)
    Eastern = AreaNamedTuple(4, "東部", "Eastern", None)

