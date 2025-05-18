# -*- coding:utf-8 -*-
import sys
from collections import namedtuple
from .base import Base


RespCodeNamedTuple = namedtuple('RespCodeNamedTuple', ['code', 'description', 'description_en', 'columns'])

class RespCode(Base):
    
    NotImplemented = RespCodeNamedTuple(123456, "尚未實作", "Not Implemented Yet", None)

    # 21X
    OK = RespCodeNamedTuple(200, "OK", "OK", None)
    
    # 5XX
    DatabaseError = RespCodeNamedTuple(500, "資料庫錯誤", "Database Error Occur", None)
    ArgumentError = RespCodeNamedTuple(504, "參數錯誤", "Argument Error", None)
    ArgumentDataTypeError = RespCodeNamedTuple(507, "參數資料型態錯誤", "Argument Data Type Error", None)
    SystemError = RespCodeNamedTuple(510, "系統錯誤", "Database Error Occur", None)
    
    # 10XX
    LineUserIdIsEmpty = RespCodeNamedTuple(1001, "Line使用者ID - 資料為空", "Line UserId Is Empty", None)
    LineUserIdDataTypeError = RespCodeNamedTuple(1004, "Line使用者ID - 資料型別錯誤", "Line UserId Data Type Error", None)
    LineUserIdMaxLengthError = RespCodeNamedTuple(1007, "Line使用者ID - 資料長度超過限制", "Line UserId - Max Length Error", None)
    LineUserExist = RespCodeNamedTuple(1007, "Line使用者 - 資料已存在", "Line UserId - Data Exist", None)
    
    