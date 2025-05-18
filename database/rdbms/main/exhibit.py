from typing import Any
import uuid
from sqlalchemy import Column, DateTime, Index, String, Text, text
from sqlalchemy.sql import func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, Query
from geoalchemy2 import Geometry
from geoalchemy2.shape import from_shape
from shapely.geometry import Point
from loguru import logger

from libs.collections.respcode import RespCode
from .base import Base, BaseUtil


class Exhibit(Base, BaseUtil):
    __tablename__ = 'EXHIBIT'
    __table_args__ = {
        'mysql_engine':'InnoDB',
        'mysql_charset': 'utf8', 	
        'mysql_collate': 'utf8_general_ci' 
        }
    

    # id = Column(Integer, primary_key=True)
    exhibit_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    ex_name = Column(String(100), nullable=False, comment="展演名稱")
    county = Column(String(3), comment="縣市")
    address = Column(String(100), comment="地址")
    geo_loc = Column(Geometry(geometry_type='POINT', nullable=False, spatial_index=True, srid=4326))
    pic_url = Column(Text, comment="圖片URL")
    klook_url = Column(Text, comment="KLOOK 連結")
    s_time = Column(DateTime, comment="開始時間")
    e_time = Column(DateTime, comment="結束時間")
    create_time = Column(DateTime, nullable=False, server_default=func.now())
    update_time = Column(DateTime, server_default=text('NULL ON UPDATE CURRENT_TIMESTAMP'))
        

    __table_args__ = (
        Index('idx_geo_loc', geo_loc, mysql_prefix='SPATIAL'),
    )    
    
    def __init__(
        self,
        ex_name,
        lng=None, # [-180.000000, 180.000000]
        lat=None, # [-90.000000, 90.000000]
        address=None,
        klook_url=None,        
        s_time=None,
        e_time=None,
        county=None,
        pic_url=None,
        
    ):
        self.ex_name = ex_name
        self.geo_loc = from_shape(Point(lat, lng), srid=4326) if lat not in (None, "") and lng not in (None, "") else None 
        self.address = address
        self.klook_url = klook_url
        self.s_time = s_time
        self.e_time = e_time
        self.county = county
        self.pic_url = pic_url
        
        
        
    def __repr__(self):
        return "<%s(id=%s, name=%s)>" % (self.__class__.__name__, self.exhibit_id, self.ex_name)
    
    # region ========== 取得指定一筆資料 ==========
    @classmethod
    async def getOneAsync(
        cls, 
        session: Session, 
        filters=None,
        columns: list[str]|None = None
    ):
        """根據filter取得指定一筆資料
        
        """
        try:
            query = session.query(cls) if columns is None else session.query()
                            
            if hasattr(cls, "deleted_at"):
                query = query.filter(cls.deleted_at.is_(None))

            # 欄位篩選
            query = cls.customFilter(query, filters)

            # 設定 SELECT 欄位
            if columns is not None:
                for column in columns:
                    query = query.add_entity(getattr(cls, column))

            return query.one_or_none(), RespCode.OK
            
        except SQLAlchemyError as e:
            logger.error(str(e))
            return None, RespCode.DatabaseError
        except Exception as e:
            logger.error(str(e))
            return None, RespCode.SystemError
        
    # endregion -------------------- 取得指定一筆資料 --------------------
    
    # region ========== 取得列表 ==========
    @classmethod
    async def getListAsync(
        cls, 
        session: Session,
        row_per_page: int|None = None, 
        offset: int|None = 0, 
        filters: dict|None = None, 
        sorts: dict|None = None,
        columns: list[str]|None = None            
    ) -> tuple[Any, RespCode]:
        limit = row_per_page
        try:
            
            query = session.query(cls) if columns is None else session.query()
            
            if hasattr(cls, "deleted_at"):
                query = query.filter(cls.deleted_at.is_(None))
 
            # 欄位篩選
            query = cls.customFilter(query, filters)
            # 欄位排序
            query = cls.customSort(query, sorts)

            if limit != None:
                query = query.limit(limit)
            if offset != 0:
                query = query.offset(offset)
            
            # 設定 SELECT 欄位
            if columns is not None:
                for column in columns:
                    if hasattr(cls, column) is True:
                        query = query.add_entity(getattr(cls, column))            
            
            data = query.all()
            
            return data, RespCode.OK
        except SQLAlchemyError as e:
            logger.error(str(e))
            return None, RespCode.DatabaseError
        except Exception as e:
            logger.error(str(e))
            return None, RespCode.SystemError         
        
    # endregion -------------------- 取得列表 --------------------
    
    # region ========== 取得列表(隨機排序) ==========
    @classmethod
    async def getListRandomAsync(
        cls, 
        session: Session,
        row_per_page: int|None = None, 
        offset: int|None = 0, 
        filters: dict|None = None, 
        columns: list[str]|None = None            
    ) -> tuple[Any, RespCode]:
        limit = row_per_page
        try:
            
            query = session.query(cls) if columns is None else session.query()
            
            if hasattr(cls, "deleted_at"):
                query = query.filter(cls.deleted_at.is_(None))
 
            # 欄位篩選
            query = cls.customFilter(query, filters)

            # 隨機排序
            query = query.order_by(func.rand())

            if limit != None:
                query = query.limit(limit)
            if offset != 0:
                query = query.offset(offset)
            
            # 設定 SELECT 欄位
            if columns is not None:
                for column in columns:
                    if hasattr(cls, column) is True:
                        query = query.add_entity(getattr(cls, column))            
            
            data = query.all()
            
            return data, RespCode.OK
        except SQLAlchemyError as e:
            logger.error(str(e))
            return None, RespCode.DatabaseError
        except Exception as e:
            logger.error(str(e))
            return None, RespCode.SystemError         
        
    # endregion -------------------- 取得列表 --------------------    
    
    # region 計算資料筆數
    @classmethod
    async def countAsync(
        cls, 
        session: Session, 
        filters = None
    ) -> tuple[int|None, RespCode]:
        """計算資料筆數
        """
        try:
            query: Query = session.query(cls)
            
            if hasattr(cls, "deleted_at"):
                query = query.filter(cls.deleted_at.is_(None))

            # 欄位篩選
            query = cls.customFilter(query, filters)

            data = query.count()

            return data, RespCode.OK
            
        except SQLAlchemyError as e:
            logger.error(str(e))
            return None, RespCode.DatabaseError
        except Exception as e:
            logger.error(str(e))
            return None, RespCode.SystemError        
    # endregion    

    # region 計算距離
    @classmethod
    async def cal_distance(
        cls, 
        session: Session, 
        lng: float,
        lat: float,
        filters = None
    ) -> tuple[int|None, RespCode]:
        """計算距離
        """
        try:
            # query: Query = session.query(cls)
            # ST_Distance_Sphere
            distance_expr = func.ST_Distance(
                cls.geo_loc,
                func.ST_GeomFromText(f'POINT({lat} {lng})', 4326)
            )

            # query = session.query(cls, distance_expr.label('distance'))
            query = (
                session.query(cls, distance_expr.label('distance'))
                # .filter(distance_expr <= 5000)  # 只拿5公里內
                .order_by(distance_expr.asc())  # 最近的排前面
            )
            data = query.all()
            return data, RespCode.OK
            
        except SQLAlchemyError as e:
            logger.error(str(e))
            return None, RespCode.DatabaseError
        except Exception as e:
            logger.error(str(e))
            return None, RespCode.SystemError      
    # endregion    
    
if __name__ == "__main__":
    pass               