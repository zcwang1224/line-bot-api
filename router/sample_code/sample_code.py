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
from models.line_user import LineUserCreateModel
from models.sample_code import SampleCodeRedisAddModel, SampleLocationAddModel
from router import Response
router = APIRouter()

# ------------------- API ----------------------------

# region test router
@router.get("/test_router")
async def test_router(
    request: Request,
):
    resp_code: RespCode = RespCode.OK
    return_data = {}
    return Response(resp_code, data = return_data)
# endregion test router

# region 取得Redis資料
@router.get("/redis/user_info/list")
async def get_redis_list(
    request: Request,
    db_main_session: Session = Depends(db.get_main_session),
):
    resp_code: RespCode = RespCode.OK
    user_info_key_list = redis_client.keys(f"{RedisKey.USER_INFO.value}:*")
    
    return_data = []
    
    for key in user_info_key_list:
        user_info = redis_client.get(key)
        data = json.loads(user_info) if user_info else {}
        return_data.append(data)
    return Response(RespCode.OK, data = return_data)

# endregion 取得Redis資料

# region 設定Redis資料
@router.post("/redis")
async def create_area(
    request: Request,
    db_main_session: Session = Depends(db.get_main_session),
):
    resp_code: RespCode = RespCode.OK
    
    body = await request.body()
    try:
        data = SampleCodeRedisAddModel.model_validate_json(body)
    except ValidationError as e:
        print(str(e))
        return Response(RespCode.ArgumentDataTypeError)    
    
    redis_client.set(
        f"{RedisKey.USER_INFO.value}:{data.line_user_id}", 
        body,
        ex=timedelta(seconds=Constant.REDIS_USER_INFO_KEEP_SECOND)
    )          
    
    return Response(resp_code)
# endregion 設定Redis資料

# region 新增sample location資料
@router.post("/sample_location")
async def create_sample_location(
    request: Request,
    db_main_session: Session = Depends(db.get_main_session),
):
    resp_code: RespCode = RespCode.OK
    
    body = await request.body()
    try:
        data = SampleLocationAddModel.model_validate_json(body)
    except ValidationError as e:
        print(str(e))
        return Response(RespCode.ArgumentDataTypeError)    
    
    try:
        sample_location = SampleLocation(data.name, data.lng, data.lat)
        db_main_session.add(sample_location)
        db_main_session.commit()
    except Exception as e:
        print(str(e))
        db_main_session.rollback()
        return Response(RespCode.DatabaseError)
    
    return Response(resp_code)    
# endregion 新增sample location資料

# region 取得計算距離列表
@router.get("/sample_location/distance")
async def create_sample_location(
    request: Request,
    lng: float,    
    lat: float,
    db_main_session: Session = Depends(db.get_main_session),
):
    resp_code: RespCode = RespCode.OK
    
    data, resp_code = await SampleLocation.cal_distance(db_main_session, lng, lat)
    print(data)
    return Response(resp_code)    
# endregion

