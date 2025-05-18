from typing import Any
from marshmallow import Schema
from sqlalchemy import Column, DateTime, ForeignKey, Index, Integer, String, Time, not_, DATE
from sqlalchemy.sql import func, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, Query, relationship
from geoalchemy2 import Geometry
from geoalchemy2.shape import from_shape
from shapely.geometry import Point
from marshmallow import Schema, fields
from loguru import logger

from libs.collections.respcode import RespCode
from .base import Base, BaseUtil


class SampleLocation(Base, BaseUtil):
    __tablename__ = 'sample_location'
    __table_args__ = {
        'mysql_engine':'InnoDB',
        'mysql_charset': 'utf8', 	
        'mysql_collate': 'utf8_general_ci' 
        }
    

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, comment="名稱")
    location = Column(Geometry(geometry_type='POINT', nullable=False, spatial_index=True, srid=4326))
    
    __table_args__ = (
        Index('idx_location', location, mysql_prefix='SPATIAL'),
    )    
    
    def __init__(
        self,
        name,
        lng, # [-180.000000, 180.000000]
        lat, # [-90.000000, 90.000000]
    ):
        self.name = name
        # self.location = from_shape(Point(lng, lat), 4326)  # srid=4326：代表 WGS 84 標準座標系（Google Maps、GPS 用的那個）
        # self.location = func.ST_GeomFromText(f"POINT({lat} {lng})", 4326)
        self.location = from_shape(Point(lat, lng), srid=4326)
        # self.location = func.ST_SRID(Point(lng, lat), 4326)
    def __repr__(self):
        return "<%s(id=%d, name=%s)>" % (self.__class__.__name__, self.id, self.name)
    
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
                cls.location,
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

class SampleLocationSchema(Schema):
    
    id = fields.Integer()
    name = fields.String()
    
    
if __name__ == "__main__":
    pass               