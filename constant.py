class Constant:
    # URI PREFIX
    URI_PREFIX = ""

    REDIS_KEY_PREFIX = "SERVER"    # 系統存放REDIS Key的Prefix
    REDIS_USER_INFO_KEEP_SECOND = 86400 # 系統保存個人資訊一天
    # Common

    # Line User
    LINE_USER_ID_MAX_LENGTH = 100   # Line UserId Max Length

    # Geo Distance filter
    GEO_DISTANCE_LIMIT = 5000 # 五公里
    
    EXCLUDE_RECOMMAND_HOUR = 1 # 排除n個小時內推薦過的項目

