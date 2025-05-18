from typing import Any
from marshmallow import Schema
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Time, not_, DATE
from sqlalchemy.sql import func, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, Query, relationship
from marshmallow import Schema, fields
from loguru import logger

from libs.collections.respcode import RespCode
from .base import Base, BaseUtil


class LineUser(Base, BaseUtil):
    __tablename__ = 'line_user'
    __table_args__ = {
        'mysql_engine':'InnoDB',
        'mysql_charset': 'utf8', 	
        'mysql_collate': 'utf8_general_ci' 
        }
    id = Column(Integer, primary_key=True)
    line_user_id = Column(String(100), nullable=False, comment="Line UserId")
    
    def __init__(
        self,
        line_user_id,
    ):
        self.line_user_id = line_user_id

    def __repr__(self):
        return "<%s(id=%d, line_user_id=%s)>" % (self.__class__.__name__, self.id, self.line_user_id)
    
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

class LineUserSchema(Schema):
    
    id = fields.Integer()
    line_user_id = fields.String()
    
if __name__ == "__main__":
    pass               