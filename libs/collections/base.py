# -*- coding:utf-8 -*-
from enum import Enum
class Base(Enum):

    @property
    def code(self):
        return self.value.code

    @property
    def description(self):
        return self.value.description

    @property
    def description_en(self):
        return self.value.description_en

    @property
    def columns(self):
        return self.value.columns

    @classmethod
    def getItems(cls, excludes = []):
        return [cls.__getattr__(attr) for attr in dir(cls) if (attr.startswith('__') == False and cls.__getattr__(attr) not in excludes) ]

    @classmethod
    def getItemByCode(cls, code: int):
        items = cls.getItems()
        # item = [item for item in items if int(item.value.code) == int(code)]
        item = [item for item in items if item.value.code == code]
        try:
            if len(item) == 0:
                return None

            return item[0]
        except IndexError as e:
            print(e)
            return None
        
    @classmethod
    def getItemByDescription(cls, desc: str):
        items = cls.getItems()
        # item = [item for item in items if int(item.value.code) == int(code)]
        item = [item for item in items if item.value.description == desc]
        try:
            if len(item) == 0:
                return None

            return item[0]
        except IndexError as e:
            print(e)
            return None        

    @classmethod
    def getCodeByDescription(cls, description):
        items = cls.getItems()
        item = [item.value.code for item in items if item.value.description == description]
        try:
            return item[0]
        except IndexError as e:
            print(e)
            return None

    @classmethod
    def getCodeList(cls, excludes=[]):
        items = cls.getItems(excludes=excludes)
        return [item.value.code for item in items]

    @classmethod
    def getDescriptionList(cls, excludes=[]):
        items = cls.getItems(excludes=excludes)
        return [item.value.description for item in items]

    @classmethod
    def getDescriptionEnList(cls, excludes=[]):
        items = cls.getItems(excludes=excludes)
        return [item.value.description_en for item in items]

    @classmethod
    def getDescriptionEnByCode(cls, code):
        items = cls.getItems()
        item = [item.value.description_en for item in items if item.value.code == code]
        try:
            return item[0]
        except IndexError as e:
            print(e)
            return None   
        
    @classmethod
    def getDescriptionByCode(cls, code):
        items = cls.getItems()
        item = [item.value.description for item in items if item.value.code == code]
        try:
            return item[0]
        except IndexError as e:
            print(e)
            return None           
