from fastapi import APIRouter, Depends, Request
from pydantic import ValidationError
from router import Response
from database.rdbms import *
from libs.collections.respcode import RespCode
from models.spot import SpotCreateModel

router = APIRouter()

# ------------------- API ----------------------------

# region 新增spot資料
@router.post("")
async def create(
    request: Request,
    db_main_session: Session = Depends(db.get_main_session),    
):
    resp_code: RespCode = RespCode.OK
    
    body = await request.body()
    try:
        data = SpotCreateModel.model_validate_json(body.decode(encoding='utf-8'))
    except ValidationError as e:
        print(str(e))
        return Response(RespCode.ArgumentDataTypeError)
    
    new_spot = Spot(
        s_name=data.s_name,
        lng=data.lng,
        lat=data.lat,
        address=data.address,
        gmaps_url=data.gmaps_url,
        b_hours=data.b_hours,
        county=data.county,
        pic_url=data.pic_url,
        s_type=data.s_type,
        rate=data.rate,
        comm=data.comm,
        area=data.area
    )
    
    try:
        db_main_session.add(new_spot)
        db_main_session.commit()
    
    except Exception as e:
        print(str(e))
        db_main_session.rollback()
        return Response(RespCode.DatabaseError)
    
    return resp_code

# endregion 新增spot資料

# region 取得計算距離列表
@router.get("")
async def get_list(
    request: Request,
    lng: float,    
    lat: float,
    db_main_session: Session = Depends(db.get_main_session),
):
    resp_code: RespCode = RespCode.OK
    
    data, resp_code = await Spot.getListByDistanceAsync(db_main_session, lng, lat)
    print(data)
    return Response(resp_code)    
# endregion

