from enum import Enum

class FilterMatchMode(Enum):
    # str
    STARTS_WITH = "startsWith"
    NOT_STARTS_WITH = "notStartsWith"
    CONTAINS = "contains"
    NOT_CONTAINS = "notContains"
    ENDS_WITH = "endsWith"
    NOT_ENDS_WITH = "notEndsWith"
    EQUALS = "equals"
    NOT_EQUALS = "notEquals"

    # list
    IN_LIST = "inList"
    NOT_IN_LIST = "notInList"

    # date
    DATE_IS = "dateIs"
    DATE_IS_NOT = "dateIsNot"
    DATE_BEFORE = "dateBefore"
    DATE_AFTER = "dateAfter"
    DATE_BETWEEN = "dateBetween"
    # 
    PASS = "pass"
