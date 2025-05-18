from constant import Constant
from contextlib import asynccontextmanager
import requests

import ngrok
from fastapi import FastAPI

from system_config import *
from libs.redis_client import redis_client
from router.exhibit import exhibit
from router.spot import spot
from router.accomo import accomo
from router.event import event
from router.line_bot import line_bot
from database.rdbms.manager import db
from router.line_user import line_user
from system_global import global_setting

@asynccontextmanager
async def lifespan(app: FastAPI):
    pass
    ngrok.set_auth_token(system_config.ngrok_auth_token)
    
    # 設定 MySQL DB
    await startup_db_setting()

    # 設定 Redis
    # await startup_redis_setting()    
    
    # region 設定Ngrok Forward
    tunnel = await ngrok.forward(
        addr=system_config.app_port
    )
    
    ngrok_forward_url = tunnel.url()
    print(ngrok_forward_url)
    with open("/tmp/ngrol_url.txt", "w+") as f:
        f.write(ngrok_forward_url)
        f.write("\n")
    
    global_setting.ngrok_url = ngrok_forward_url
    # endregion 設定Ngrok Forward    
    
    # 設定Line Bot Webhook URL
    await update_line_bot_webhook_url(ngrok_forward_url)
    
    yield
    pass
    # redis_client.deleteByKeys(redis_client.scan(f"{Constant.REDIS_KEY_PREFIX}:*"))
    ngrok.disconnect()


app = FastAPI(lifespan=lifespan)

# region 系統啟動預設 DB
async def startup_db_setting():
    '''系統啟動預設 DB
    Database 使用方式: 參考database/SQL/*.py
    主要參考檔案: manager.py
    '''
    db.add_database(f"{system_config.db_main_uri}{system_config.db_main_name}", debug=system_config.db_main_debug, key = system_config.db_main_name)

    # 第二個DB
    # db.add_database(f"{settings.DB_SUB_URI}{settings.DB_SUB_NAME}", debug=settings.DB_SUB_DEBUG, key = {settings.DB_SUB_NAME})

    #print(f"顯示目前所有連線的資料庫明名稱: {db.get_all_database_names()}")
# endregion 系統啟動預設 DB

# region 系統啟動預設 Redis
async def startup_redis_setting():
    ''' 系統啟動預設 Redis
    '''
    # region ========== REDIS 存放系統預設資料 ==========
    
    main_session = db.get_main_session().__next__()
    ret = redis_client.connection(system_config.redis_url)

    # 清除所有系統使用的Redis資料
    redis_client.deleteByKeys(redis_client.scan(f"{Constant.REDIS_KEY_PREFIX}:*"))
    
    try:
        pass
    except Exception as e:
        print(str(e))
    finally:
        main_session.close()
        
    # endregion -------------------- REDIS 存放系統預設資料 --------------------
# endregion 系統啟動預設 Redis

# region 設定Line Bot Webhook URL
async def update_line_bot_webhook_url(host:str):
    
    url = "https://api.line.me/v2/bot/channel/webhook/endpoint"
    
    headers = {
        'Authorization': f'Bearer {system_config.line_access_token}',
        'Content-Type': 'application/json'
    }

    payload = {
        'endpoint': f"{host}/line_bot/call"
    }

    requests.put(url, headers=headers, json=payload)
    
    return
    
# endregion 設定Line Bot Webhook URL

'''
API Routers
'''
# ----- Base System
app.include_router(line_bot.router, prefix=f"/line_bot", tags=["Line Bot"])
app.include_router(line_user.router, prefix=f"/line_user", tags=["Line User"])
app.include_router(exhibit.router, prefix=f"/exhibit", tags=["Exhibit"])
app.include_router(spot.router, prefix=f"/spot", tags=["Spot"])
app.include_router(accomo.router, prefix=f"/accomo", tags=["Accomo"])
app.include_router(event.router, prefix=f"/event", tags=["Event"])

# ----- sample code
# app.include_router(sample_code.router, prefix=f"/sample_code", tags=["Sample Code"])