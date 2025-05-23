from typing import Any
import uuid
from sqlalchemy import Column, DateTime, Index, String, Text, DECIMAL, Integer, text
from sqlalchemy.sql import func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, Query
from geoalchemy2 import Geometry
from geoalchemy2.shape import from_shape
from shapely.geometry import Point
from loguru import logger

from libs.collections.respcode import RespCode
from .base import Base, BaseUtil
from constant import Constant

class Accomo(Base, BaseUtil):
    __tablename__ = 'ACCOMO'
    __table_args__ = {
        'mysql_engine':'InnoDB',
        'mysql_charset': 'utf8', 	
        'mysql_collate': 'utf8_general_ci' 
        }
    
    accomo_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    a_name = Column(String(100), nullable=False, comment="店家名")
    county = Column(String(3), comment="縣市")
    address = Column(String(100), comment="地址")
    rate = Column(DECIMAL(2, 1), comment="評分")
    geo_loc = Column(Geometry(geometry_type='POINT', nullable=False, spatial_index=True, srid=4326))
    pic_url = Column(Text, comment="圖片URL")    
    b_url = Column(Text, comment="BOOKING 連結")
    ac_type = Column(String(3), comment="類型")
    comm = Column(Integer, comment="評論數")
    area = Column(String(3), comment="鄉鎮區")
    fac = Column(String(100), comment="設施")
    create_time = Column(DateTime, nullable=False, server_default=func.now())
    update_time = Column(DateTime, server_default=text('NULL ON UPDATE CURRENT_TIMESTAMP'))
    
    __table_args__ = (
        Index('idx_geo_loc', geo_loc, mysql_prefix='SPATIAL'),
    )    
    
    def __init__(
        self,
        a_name,
        lng, # [-180.000000, 180.000000]
        lat, # [-90.000000, 90.000000]        
        county=None,
        address=None,
        rate=None,
        pic_url=None,
        b_url=None,
        ac_type=None,
        comm=None,
        area=None,
    ):
        self.a_name = a_name
        self.geo_loc = from_shape(Point(lat, lng), srid=4326) if lat not in (None, "") and lng not in (None, "") else None 
        self.county = county
        self.address = address
        self.rate = rate
        self.pic_url = pic_url
        self.b_url = b_url
        self.ac_type = ac_type
        self.comm = comm
        self.area = area
        
    def __repr__(self):
        return "<%s(id=%s, name=%s)>" % (self.__class__.__name__, self.accomo_id, self.a_name)
    
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
        
    # endregion -------------------- 取得列表(隨機排序) --------------------    
    
    
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
    
    # region 根據距離取得資料列表
    @classmethod
    async def getListByDistanceAsync(
        cls, 
        session: Session, 
        lng: float,
        lat: float,
        row_per_page: int|None = None, 
        offset: int|None = 0,         
        filters = None
    ) -> tuple[int|None, RespCode]:
        """計算距離
        """
        try:
            limit = row_per_page
            # query: Query = session.query(cls)
            # ST_Distance_Sphere
            distance_expr = func.ST_Distance(
                cls.geo_loc,
                func.ST_GeomFromText(f'POINT({lat} {lng})', 4326)
            )

            # query = session.query(cls, distance_expr.label('distance'))
            query = (
                session.query(cls, distance_expr.label('distance'))
                .filter(distance_expr <= Constant.GEO_DISTANCE_LIMIT)  # 只拿GEO_DISTANCE_LIMIT公里內
                .order_by(cls.rate.desc(), cls.comm.desc())  # 評分最高的排前面
            )
            
            # 欄位篩選
            query = cls.customFilter(query, filters)            
            
            if limit != None:
                query = query.limit(limit)
            if offset != 0:
                query = query.offset(offset)            
            
            data = query.all()
            # print(data)
            return data, RespCode.OK
            
        except SQLAlchemyError as e:
            logger.error(str(e))
            return None, RespCode.DatabaseError
        except Exception as e:
            logger.error(str(e))
            return None, RespCode.SystemError      
    # endregion  根據距離取得資料列表
    
    
    # region 根據距離取得資料列表(隨機排序)
    @classmethod
    async def getListByDistanceRandomAsync(
        cls, 
        session: Session, 
        lng: float,
        lat: float,
        row_per_page: int|None = None, 
        offset: int|None = 0,         
        filters = None
    ) -> tuple[int|None, RespCode]:
        """計算距離
        """
        try:
            limit = row_per_page
            # query: Query = session.query(cls)
            # ST_Distance_Sphere
            distance_expr = func.ST_Distance(
                cls.geo_loc,
                func.ST_GeomFromText(f'POINT({lat} {lng})', 4326)
            )

            # query = session.query(cls, distance_expr.label('distance'))
            query = (
                session.query(cls, distance_expr.label('distance'))
                .filter(distance_expr <= Constant.GEO_DISTANCE_LIMIT)  # 只拿GEO_DISTANCE_LIMIT公里內
                .order_by(func.rand()) # 最近的排前面
            )
            
            # 欄位篩選
            query = cls.customFilter(query, filters)            
            
            if limit != None:
                query = query.limit(limit)
            if offset != 0:
                query = query.offset(offset)            
            
            data = query.all()
            # print(data)
            return data, RespCode.OK
            
        except SQLAlchemyError as e:
            logger.error(str(e))
            return None, RespCode.DatabaseError
        except Exception as e:
            logger.error(str(e))
            return None, RespCode.SystemError      
    # endregion  根據距離取得資料列表(隨機排序)
        
    
    # region 根據距離取得資料筆數
    @classmethod
    async def countByDistanceAsync(
        cls, 
        session: Session, 
        lng: float,
        lat: float,     
        filters = None
    ) -> tuple[int|None, RespCode]:
        """根據距離取得資料筆數
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
                .filter(distance_expr <= Constant.GEO_DISTANCE_LIMIT)  # 只拿GEO_DISTANCE_LIMIT公里內
                .order_by(distance_expr.asc())  # 最近的排前面
            )
            
            # 欄位篩選
            query = cls.customFilter(query, filters)            

            count = query.count()
            # print(data)
            return count, RespCode.OK
            
        except SQLAlchemyError as e:
            logger.error(str(e))
            return None, RespCode.DatabaseError
        except Exception as e:
            logger.error(str(e))
            return None, RespCode.SystemError      
    # endregion 根據距離取得資料筆數
    
if __name__ == "__main__":
    pass               