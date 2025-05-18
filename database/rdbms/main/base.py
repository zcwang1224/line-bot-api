from sqlalchemy import not_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Query

from libs.collections.filter_match_mode import FilterMatchMode
Base = declarative_base()

class BaseUtil:
    def __init__(self) -> None:
        pass
    
    # region 欄位篩選
    @classmethod
    def customFilter(cls, query: Query, filters=None):
        """欄位篩選

        """
        # 篩選 
        # filters = {
        #     "bid.name": {
        #         "value": "BBBCCC",
        #         "matchMode": FilterMatchMode.EQUALS.value
        #     }
        # }
        
        
        if filters is None:
            return query
        
        for field_name in filters:
            if hasattr(cls, field_name) is True:
                query = cls.setQueryFilter(cls, query, field_name, filters[field_name])
                
                         
            # field_name_list = field_name.split(".")
            # classes = field_name_list[0: -1]
            # field_name_last = field_name_list[-1]
            
            # print(classes)
            # print(field_name_last)
            # for class_ in classes:
            #     if hasattr(cls, class_):
            #         cls = getattr(cls, class_).__class__()
            #         pass
            #     else:
            #         break
            
            # if filters.count(".") > 0:
            #     attrs = filters.split(".")
            #     for attr in attrs[0: -1]:
            #         if hasattr(cls, attr):
            #             cls = getattr(cls, attr)
            
            # if len(classes) == 0:
            #     if hasattr(cls, field_name_last) is True:
            #         query = cls.setQueryFilter(cls, query, field_name_last, filters[field_name_last])
            # else:
            #     # print(hasattr(cls, field_name_last))
            #     # if hasattr(cls, field_name_last) is True:
            #     query = cls.setQueryRelationalFilter(cls, query, field_name_last, filters[field_name])                
        return query
    # endregion
    
    # region 欄位排序
    @classmethod
    def customSort(cls, query: Query, sorts=[]):
        """欄位排序

        """
        # 排序
        if sorts is not None:
            for sort_order in dict(sorted(sorts.items())):
                field_name = sorts[sort_order]['field']
                order = sorts[sort_order]['order']

                if hasattr(cls, field_name) is True:
                    if order == -1:
                        query = query.order_by(getattr(cls, field_name).desc())
                    elif order == 1:
                        query = query.order_by(getattr(cls, field_name).asc())
            
        return query
    # endregion    
    
    # region 設定欄位篩選
    def setQueryFilter(class_, query: Query, field_name:str, filter) -> Query:

        if filter['value'] == None or filter['value'] == "":
            return query
        
        match filter['matchMode']:
            # str
            case FilterMatchMode.STARTS_WITH.value:
                return query.filter(getattr(class_, field_name).startswith(filter['value']))
            case FilterMatchMode.NOT_STARTS_WITH.value:
                return query.filter(not_(getattr(class_, field_name).startswith(filter['value'])))
            case FilterMatchMode.CONTAINS.value:
                return query.filter(getattr(class_, field_name).contains(filter['value']))
            case FilterMatchMode.NOT_CONTAINS.value:
                return query.filter(not_(getattr(class_, field_name).contains(filter['value'])))
            case FilterMatchMode.ENDS_WITH.value:
                return query.filter(getattr(class_, field_name).endswith(filter['value']))
            case FilterMatchMode.NOT_ENDS_WITH.value:
                return query.filter(not_(getattr(class_, field_name).endswith(filter['value'])))
            case FilterMatchMode.EQUALS.value:
                return query.filter(getattr(class_, field_name) == filter['value'])  
            case FilterMatchMode.NOT_EQUALS.value:
                return query.filter(getattr(class_, field_name) != filter['value'])
            
            # list
            case FilterMatchMode.IN_LIST.value:
                return query.filter(getattr(class_, field_name).in_(filter['value']))
            case FilterMatchMode.NOT_IN_LIST.value:
                return query.filter(~getattr(class_, field_name).in_(filter['value']))            
            
            # date
            case FilterMatchMode.DATE_IS.value:
                return query.filter(getattr(class_, field_name).__eq__(filter['value']))
            case FilterMatchMode.DATE_IS_NOT.value:
                return query.filter(~getattr(class_, field_name).__eq__(filter['value']))
            case FilterMatchMode.DATE_BEFORE.value:
                return query.filter(getattr(class_, field_name).__lt__(filter['value']))
            case FilterMatchMode.DATE_AFTER.value:
                return query.filter(getattr(class_, field_name).__gt__(filter['value']))
            case FilterMatchMode.DATE_BETWEEN.value:
                return query\
                        .filter(getattr(class_, field_name).__gt__(filter['value'][0]))\
                        .filter(getattr(class_, field_name).__lt__(filter['value'][1]))            
            case _:
                return query
    # endregion
    
    # region 設定關聯欄位篩選
    def setQueryRelationalFilter(class_, query: Query, field_name:str, filter) -> Query:

        if filter['value'] == None or filter['value'] == "":
            return query
        
        match filter['matchMode']:
            # str
            case FilterMatchMode.STARTS_WITH.value:
                return query.filter(getattr(class_, field_name).startswith(filter['value']))
            case FilterMatchMode.NOT_STARTS_WITH.value:
                return query.filter(not_(getattr(class_, field_name).startswith(filter['value'])))
            case FilterMatchMode.CONTAINS.value:
                return query.filter(getattr(class_, field_name).contains(filter['value']))
            case FilterMatchMode.NOT_CONTAINS.value:
                return query.filter(not_(getattr(class_, field_name).contains(filter['value'])))
            case FilterMatchMode.ENDS_WITH.value:
                return query.filter(getattr(class_, field_name).endswith(filter['value']))
            case FilterMatchMode.NOT_ENDS_WITH.value:
                return query.filter(not_(getattr(class_, field_name).endswith(filter['value'])))
            case FilterMatchMode.EQUALS.value:
                return query.filter(getattr(class_, field_name).has(bid_number=filter['value']))  
            case FilterMatchMode.NOT_EQUALS.value:
                return query.filter(getattr(class_, field_name) != filter['value'])
            
            # list
            case FilterMatchMode.IN_LIST.value:
                return query.filter(getattr(class_, field_name).in_(filter['value']))
            case FilterMatchMode.NOT_IN_LIST.value:
                return query.filter(~getattr(class_, field_name).in_(filter['value']))            
            
            # date
            case FilterMatchMode.DATE_IS.value:
                return query.filter(getattr(class_, field_name).__eq__(filter['value']))
            case FilterMatchMode.DATE_IS_NOT.value:
                return query.filter(~getattr(class_, field_name).__eq__(filter['value']))
            case FilterMatchMode.DATE_BEFORE.value:
                return query.filter(getattr(class_, field_name).__lt__(filter['value']))
            case FilterMatchMode.DATE_AFTER.value:
                return query.filter(getattr(class_, field_name).__gt__(filter['value']))
            case _:
                return query
    # endregion    