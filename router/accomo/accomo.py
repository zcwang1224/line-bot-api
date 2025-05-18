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
from models.accomo import AccomoCreateModel
from models.line_user import LineUserCreateModel
from models.sample_code import SampleCodeRedisAddModel, SampleLocationAddModel
from router import Response
router = APIRouter()

# ------------------- API ----------------------------

# region 新增exhibit資料
@router.post("")
async def create(
    request: Request,
    db_main_session: Session = Depends(db.get_main_session),    
):
    resp_code: RespCode = RespCode.OK
    
    body = await request.body()
    try:
        data = AccomoCreateModel.model_validate_json(body.decode(encoding='utf-8'))
    except ValidationError as e:
        print(str(e))
        return Response(RespCode.ArgumentDataTypeError)
    
    new_accomo = Accomo(
        a_name=data.a_name,
        lng=data.lng,
        lat=data.lat,
        address=data.address,
        b_url=data.b_url,
        county=data.county,
        pic_url=data.pic_url,
        ac_type=data.ac_type,
        rate=data.rate,
        comm=data.comm,
        area=data.area
    )
    
    try:
        db_main_session.add(new_accomo)
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
    
    data, resp_code = await Accomo.cal_distance(db_main_session, lng, lat)
    print(data)
    return Response(resp_code)    
# endregion

