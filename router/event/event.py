from datetime import timedelta
import json
from typing import Annotated, Any
from fastapi import APIRouter, Depends, Request
from pydantic import ValidationError
from database.rdbms import *
from libs.collections.filter_match_mode import FilterMatchMode
from libs.collections.redis_key import RedisKey
from libs.redis_client import redis_client
from libs.collections.respcode import RespCode
from constant import Constant
from models.activity import EventCreateModel
from models.line_user import LineUserCreateModel
from models.sample_code import SampleCodeRedisAddModel, SampleLocationAddModel
from router import Response
router = APIRouter()

# ------------------- API ----------------------------

# region 新增event資料
@router.post("")
async def create(
    request: Request,
    db_main_session: Session = Depends(db.get_main_session),    
):
    resp_code: RespCode = RespCode.OK
    
    body = await request.body()
    try:
        data = EventCreateModel.model_validate_json(body.decode(encoding='utf-8'))
    except ValidationError as e:
        print(str(e))
        return Response(RespCode.ArgumentDataTypeError)
    
    print("================================================")
    print(data.ev_name)
    print("----------------------------------------------")
    
    new_event = Event(
        ev_name=data.ev_name,
        lng=data.lng,
        lat=data.lat,
        address=data.address,
        accu_url=data.accu_url,
        s_time=data.s_time,
        e_time=data.e_time,
        county=data.county,
        pic_url=data.pic_url,
    )
    
    try:
        db_main_session.add(new_event)
        db_main_session.commit()
    
    except Exception as e:
        print(str(e))
        db_main_session.rollback()
        return Response(RespCode.DatabaseError)
    
    return resp_code

# endregion 新增exhibit資料

# region 取得計算距離列表
@router.get("")
async def get_list(
    request: Request,
    lng: float,    
    lat: float,
    db_main_session: Session = Depends(db.get_main_session),
):
    resp_code: RespCode = RespCode.OK
    
    data, resp_code = await Exhibit.cal_distance(db_main_session, lng, lat)
    print(data)
    return Response(resp_code)    
# endregion

