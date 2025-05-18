import json
from typing import Annotated, Any
from fastapi import APIRouter, Depends, Request
from database.rdbms import *
from libs.collections.filter_match_mode import FilterMatchMode
from libs.redis_client import redis_client
from libs.collections.respcode import RespCode
from constant import Constant
from models.line_user import LineUserCreateModel
from router import Response
router = APIRouter()

# ------------------- API ----------------------------

# region 取得Line User列表
@router.post("/list")
async def get_list(
    request: Request,
    db_main_session: Session = Depends(db.get_main_session),
):
    resp_code: RespCode = RespCode.OK

    # region ========== 取得列表資料 ==========
    
    areas, resp_code = await LineUser.getListAsync(
        db_main_session,
    )
    
    if resp_code != RespCode.OK:
        # 資料庫錯誤
        return Response(resp_code)
    
    # endregion ========== 取得列表資料 ==========

    schema = LineUserSchema(many=True)
    JsonDataString = schema.dumps(areas)
    JsonDataObject = json.loads(JsonDataString)
    data = {
        'line_users': JsonDataObject,
    }
    
    return Response(RespCode.OK, data = data)

# endregion 取得Line User列表

# region 新增Line User
@router.post("")
async def create_area(
    request: Request,
    body: LineUserCreateModel|None = None,
    db_main_session: Session = Depends(db.get_main_session),
):
    resp_code: RespCode = RespCode.OK
    
    # region ========== 檢查資料正確 ==========
    
    # 檢查Body
    if body is None:
        return Response(RespCode.ArgumentError)    

    
    # region 檢查line_user_id(Required, str, Max Length)
    
    if body.line_user_id is None:
        return Response(RespCode.LineUserIdIsEmpty)
    
    if isinstance(body.line_user_id, str) is False:
        return Response(RespCode.LineUserIdDataTypeError) 
    
    body.line_user_id = body.line_user_id.strip()
    
    if body.line_user_id.strip() == "":
        return Response(RespCode.LineUserIdIsEmpty)
    
    # 限制名稱長度
    if len(body.line_user_id) > Constant.LINE_USER_ID_MAX_LENGTH:
        return Response(RespCode.LineUserIdMaxLengthError)
    
    # endregion 檢查名稱 name (Required, str, Max Length)

    # endregion -------------------- 檢查資料正確 --------------------

    # region ========== 檢查資料重複 ==========
    
    # region 檢查名稱重複
    
    # 設定Filter
    filter = {
        "name": {
            "value": body.line_user_id,
            "matchMode": FilterMatchMode.EQUALS.value
        }
    }
    
    count_line_user_id, resp_code = await LineUser.countAsync(db_main_session, filters=filter)
    
    if resp_code != RespCode.OK:
        return Response(resp_code)
    
    if count_line_user_id > 0:
        return Response(RespCode.LineUserExist)
    
    # endregion 檢查名稱重複

    # endregion -------------------- 檢查資料重複 --------------------
    
    # region ========== 更新DB ==========
    
    new_line_user = LineUser(
        line_user_id=body.line_user_id,
    )

    try:
        db_main_session.add(new_line_user)
        db_main_session.commit()
        db_main_session.refresh(new_line_user)
            
    except Exception as e:
        print(str(e))
        db_main_session.rollback()
        return Response(RespCode.DatabaseError)
    
    # endregion -------------------- 更新DB --------------------
    
    data = {
        "id": new_line_user.id,
        "line_user_id": new_line_user.line_user_id
    }
    
    return Response(resp_code, data=data)
# endregion 新增Line User