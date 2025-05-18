# -*- coding:utf-8 -*-
from collections import namedtuple

from libs.collections.city import City
from .base import Base


DistrictNamedTuple = namedtuple('DistrictNamedTuple', ['code', 'description', 'description_en', 'columns'])

class District(Base):
    # region 基隆10XX
    Keelung_RenAi = DistrictNamedTuple(1001, "仁愛區", "Ren'ai District", None)
    Keelung_Zhongzheng = DistrictNamedTuple(1002, "中正區", "Zhongzheng District", None)
    Keelung_Xinyi = DistrictNamedTuple(1003, "信義區", "Xinyi District", None)
    Keelung_Zhongshan = DistrictNamedTuple(1004, "中山區", "Zhongshan District", None)
    Keelung_Anle = DistrictNamedTuple(1005, "安樂區", "Anle District", None)
    Keelung_Nuannuan = DistrictNamedTuple(1006, "暖暖區", "Nuannuan District", None)
    Keelung_Qidu = DistrictNamedTuple(1007, "七堵區", "Qidu District", None)
    # endregion
    
    # region 台北 11XX
    Taipei_Zhongzheng = DistrictNamedTuple(1101, "中正區", "Zhongzheng District", None)
    Taipei_Datong = DistrictNamedTuple(1102, "大同區", "Datong District", None)
    Taipei_Zhongshan = DistrictNamedTuple(1103, "中山區", "Zhongshan District", None)
    Taipei_Wanhua = DistrictNamedTuple(1104, "萬華區", "Wanhua District", None)
    Taipei_Xinyi = DistrictNamedTuple(1105, "信義區", "Xinyi District", None)
    Taipei_Songshan = DistrictNamedTuple(1106, "松山區", "Songshan District", None)
    Taipei_Da = DistrictNamedTuple(1107, "大安區", "Da'an District", None)
    Taipei_Nangang = DistrictNamedTuple(1108, "南港區", "Nangang District", None)
    Taipei_Beitou = DistrictNamedTuple(1109, "北投區", "Beitou District", None)
    Taipei_Neihu = DistrictNamedTuple(1110, "內湖區", "Neihu District", None)
    Taipei_Shilin = DistrictNamedTuple(1111, "士林區", "Shilin District", None)
    Taipei_Wenshan = DistrictNamedTuple(1112, "文山區", "Wenshan District", None)
    # endregion 台北
    
    # region 新北 12XX
    New_Taipei_Banqiao = DistrictNamedTuple(1201, "板橋區", "Banqiao District", None)
    New_Taipei_Xinzhuang = DistrictNamedTuple(1202, "新莊區", "Xinzhuang District", None)
    New_Taipei_Taishan = DistrictNamedTuple(1203, "泰山區", "Taishan District", None)
    New_Taipei_Linkou = DistrictNamedTuple(1204, "林口區", "Linkou District", None)
    New_Taipei_Tamsui = DistrictNamedTuple(1205, "淡水區", "Tamsui District", None)
    New_Taipei_Jinshan = DistrictNamedTuple(1206, "金山區", "Jinshan District", None)
    New_Taipei_Bali = DistrictNamedTuple(1207, "八里區", "Bali District", None)
    New_Taipei_Wanli = DistrictNamedTuple(1208, "萬里區", "Wanli District", None)
    New_Taipei_Shimen = DistrictNamedTuple(1209, "石門區", "Shimen District", None)
    New_Taipei_Sanzhi = DistrictNamedTuple(1210, "三芝區", "Sanzhi District", None)
    New_Taipei_Ruifang = DistrictNamedTuple(1211, "瑞芳區", "Ruifang District", None)
    New_Taipei_Xizhi = DistrictNamedTuple(1212, "汐止區", "Xizhi District", None)
    New_Taipei_Pingxi = DistrictNamedTuple(1213, "平溪區", "Pingxi District", None)
    New_Taipei_Gongliao = DistrictNamedTuple(1214, "貢寮區", "Gongliao District", None)
    New_Taipei_Shuangxi = DistrictNamedTuple(1215, "雙溪區", "Shuangxi District", None)
    New_Taipei_Shenkeng = DistrictNamedTuple(1216, "深坑區", "Shenkeng District", None)
    New_Taipei_Shiding = DistrictNamedTuple(1217, "石碇區", "Shiding District", None)
    New_Taipei_Xindian = DistrictNamedTuple(1218, "新店區", "Xindian District", None)
    New_Taipei_Pinglin = DistrictNamedTuple(1219, "坪林區", "Pinglin District", None)
    New_Taipei_Wulai = DistrictNamedTuple(1220, "烏來區", "Wulai District", None)
    New_Taipei_Zhonghe = DistrictNamedTuple(1221, "中和區", "Zhonghe District", None)
    New_Taipei_Yonghe = DistrictNamedTuple(1222, "永和區", "Yonghe District", None)
    New_Taipei_Tucheng = DistrictNamedTuple(1223, "土城區", "Tucheng District", None)
    New_Taipei_Sanxia = DistrictNamedTuple(1224, "三峽區", "Sanxia District", None)
    New_Taipei_Shulin = DistrictNamedTuple(1225, "樹林區", "Shulin District", None)
    New_Taipei_Yingge = DistrictNamedTuple(1226, "鶯歌區", "Yingge District", None)
    New_Taipei_Sanchong = DistrictNamedTuple(1227, "三重區", "Sanchong District", None)
    New_Taipei_Luzhou = DistrictNamedTuple(1228, "蘆洲區", "Luzhou District", None)
    New_Taipei_Wugu = DistrictNamedTuple(1229, "五股區", "Wugu District", None)    
    # endregion 新北
    
    # region 桃園 13XX
    Taoyuan_Taoyuan = DistrictNamedTuple(1300, "桃園區", "Taoyuan District", None)
    Taoyuan_Zhongli = DistrictNamedTuple(1301, "中壢區", "Zhongli District", None)
    Taoyuan_Pingzhen = DistrictNamedTuple(1302, "平鎮區", "Pingzhen District", None)
    Taoyuan_Bade = DistrictNamedTuple(1303, "八德區", "Bade District", None)
    Taoyuan_Yangmei = DistrictNamedTuple(1304, "楊梅區", "Yangmei District", None)
    Taoyuan_Luzhu = DistrictNamedTuple(1305, "蘆竹區", "Luzhu District", None)
    Taoyuan_Guishan = DistrictNamedTuple(1306, "龜山區", "Guishan District", None)
    Taoyuan_Longtan = DistrictNamedTuple(1307, "龍潭區", "Longtan District", None)
    Taoyuan_Daxi = DistrictNamedTuple(1308, "大溪區", "Daxi District", None)
    Taoyuan_Dayuan = DistrictNamedTuple(1309, "大園區", "Dayuan District", None)
    Taoyuan_Guanyin = DistrictNamedTuple(1310, "觀音區", "Guanyin District", None)
    Taoyuan_Xinwu = DistrictNamedTuple(1311, "新屋區", "Xinwu District", None)
    Taoyuan_Fuxing = DistrictNamedTuple(1312, "復興區", "Fuxing District", None)
    # endregion 桃園
    
    # region 新竹 14XX
    Hsinchu_Zhubei = DistrictNamedTuple(1400, "竹北市",  "Zhubei City", None)
    Hsinchu_ZhuDong = DistrictNamedTuple(1401, "竹東鎮",  "Zhu Dong Township", None)
    Hsinchu_Xinpu = DistrictNamedTuple(1402, "新埔鎮",  "Xinpu Township", None)
    Hsinchu_Guanxi = DistrictNamedTuple(1403, "關西鎮",  "Guanxi Township", None)
    Hsinchu_Emei = DistrictNamedTuple(1404, "峨眉鄉",  "Emei Township", None)
    Hsinchu_Baoshan = DistrictNamedTuple(1405, "寶山鄉",  "Baoshan Township", None)
    Hsinchu_Beipu = DistrictNamedTuple(1406, "北埔鄉",  "Beipu Township", None)
    Hsinchu_Hengshan = DistrictNamedTuple(1407, "橫山鄉",  "Hengshan Township", None)
    Hsinchu_Xianglin = DistrictNamedTuple(1408, "芎林鄉",  "Xianglin Township", None)
    Hsinchu_Hukou = DistrictNamedTuple(1409, "湖口鄉",  "Hukou Township", None)
    Hsinchu_Xinfeng = DistrictNamedTuple(1410, "新豐鄉",  "Xinfeng Township", None)
    Hsinchu_JianShi = DistrictNamedTuple(1411, "尖石鄉",  "Jian Shi Township", None)
    Hsinchu_Wufeng = DistrictNamedTuple(1412, "五峰鄉",  "Wufeng Township", None)
    Hsinchu_East = DistrictNamedTuple(1413, "東區",  "East District", None)
    Hsinchu_North = DistrictNamedTuple(1414, "北區",  "North District", None)
    Hsinchu_Xiangshan = DistrictNamedTuple(1415, "香山區",  "Xiangshan District", None)
    # endregion 新竹
    
    # region 苗栗 15XX
    Miaoli_Miaoli = DistrictNamedTuple(1500, "苗栗市", "Miaoli City", None)
    Miaoli_Tongxiao = DistrictNamedTuple(1501, "通霄鎮", "Tongxiao Township", None)
    Miaoli_Yuanli = DistrictNamedTuple(1502, "苑裡鎮", "Yuanli Township", None)
    Miaoli_Zhunan = DistrictNamedTuple(1503, "竹南鎮", "Zhunan Township", None)
    Miaoli_Toufen = DistrictNamedTuple(1504, "頭份鎮", "Toufen Township", None)
    Miaoli_Holo = DistrictNamedTuple(1505, "後龍鎮", "Holo Township", None)
    Miaoli_Zhuolan = DistrictNamedTuple(1506, "卓蘭鎮", "Zhuolan Township", None)
    Miaoli_Xihu = DistrictNamedTuple(1507, "西湖鄉", "Xihu Township", None)
    Miaoli_Touwu = DistrictNamedTuple(1508, "頭屋鄉", "Touwu Township", None)
    Miaoli_Gongguan = DistrictNamedTuple(1509, "公館鄉", "Gongguan Township", None)
    Miaoli_Tongluo = DistrictNamedTuple(1510, "銅鑼鄉", "Tongluo Township", None)
    Miaoli_Sanyi = DistrictNamedTuple(1511, "三義鄉", "Sanyi Township", None)
    Miaoli_Zaoqiao = DistrictNamedTuple(1512, "造橋鄉", "Zaoqiao Township", None)
    Miaoli_Sanwan = DistrictNamedTuple(1513, "三灣鄉", "Sanwan Township", None)
    Miaoli_Nanzhuang = DistrictNamedTuple(1514, "南庄鄉", "Nanzhuang Township", None)
    Miaoli_Dahu = DistrictNamedTuple(1515, "大湖鄉", "Dahu Township", None)
    Miaoli_Shitan = DistrictNamedTuple(1516, "獅潭鄉", "Shitan Township", None)
    Miaoli_Taian = DistrictNamedTuple(1517, "泰安鄉", "Taian Township", None)
    # endregion 苗栗
    
    # region 台中 16XX
    Taichung_Central = DistrictNamedTuple(1600, "中區", "Central District", None)
    Taichung_East = DistrictNamedTuple(1601, "東區", "East District", None)
    Taichung_South = DistrictNamedTuple(1602, "南區", "South District", None)
    Taichung_West = DistrictNamedTuple(1603, "西區", "West District", None)
    Taichung_North = DistrictNamedTuple(1604, "北區", "North District", None)
    Taichung_Beitun = DistrictNamedTuple(1605, "北屯區", "Beitun District", None)
    Taichung_Xitun = DistrictNamedTuple(1606, "西屯區", "Xitun District", None)
    Taichung_Nantun = DistrictNamedTuple(1607, "南屯區", "Nantun District", None)
    Taichung_Taiping = DistrictNamedTuple(1608, "太平區", "Taiping District", None)
    Taichung_Dali = DistrictNamedTuple(1609, "大里區", "Dali District", None)
    Taichung_Wufeng = DistrictNamedTuple(1610, "霧峰區", "Wufeng District", None)
    Taichung_Wuri = DistrictNamedTuple(1611, "烏日區", "Wuri District", None)
    Taichung_Fengyuan = DistrictNamedTuple(1612, "豐原區", "Fengyuan District", None)
    Taichung_Houli = DistrictNamedTuple(1613, "后里區", "Houli District", None)
    Taichung_Dongshi = DistrictNamedTuple(1614, "東勢區", "Dongshi District", None)
    Taichung_Shigang = DistrictNamedTuple(1615, "石岡區", "Shigang District", None)
    Taichung_Xinshe = DistrictNamedTuple(1616, "新社區", "Xinshe District", None)
    Taichung_Heping = DistrictNamedTuple(1617, "和平區", "Heping District", None)
    Taichung_Shengang = DistrictNamedTuple(1618, "神岡區", "Shengang District", None)
    Taichung_Tanzi = DistrictNamedTuple(1619, "潭子區", "Tanzi District", None)
    Taichung_Daya = DistrictNamedTuple(1620, "大雅區", "Daya District", None)
    Taichung_Dadu = DistrictNamedTuple(1621, "大肚區", "Dadu District", None)
    Taichung_Longjing = DistrictNamedTuple(1622, "龍井區", "Longjing District", None)
    Taichung_Shalu = DistrictNamedTuple(1623, "沙鹿區", "Shalu District", None)
    Taichung_Wuqi = DistrictNamedTuple(1624, "梧棲區", "Wuqi District", None)
    Taichung_Qingshui = DistrictNamedTuple(1625, "清水區", "Qingshui District", None)
    Taichung_Dajia = DistrictNamedTuple(1626, "大甲區", "Dajia District", None)
    Taichung_Waipu = DistrictNamedTuple(1627, "外埔區", "Waipu District", None)
    Taichung_DaAn = DistrictNamedTuple(1628, "大安區", "Da'an District", None)
    # endregion 台中
    
    # region 南投 17XX
    Nantou_Nantou = DistrictNamedTuple(1701, "南投市", "Nantou City", None)
    Nantou_Puli = DistrictNamedTuple(1702, "埔里鎮", "Puli Township", None)
    Nantou_Caotun = DistrictNamedTuple(1703, "草屯鎮", "Caotun Township", None)
    Nantou_Zhushan = DistrictNamedTuple(1704, "竹山鎮", "Zhushan Township", None)
    Nantou_Jiji = DistrictNamedTuple(1705, "集集鎮", "Jiji Township", None)
    Nantou_Mingjian = DistrictNamedTuple(1706, "名間鄉", "Mingjian Township", None)
    Nantou_Lugu = DistrictNamedTuple(1707, "鹿谷鄉", "Lugu Township", None)
    Nantou_Zhongliao = DistrictNamedTuple(1708, "中寮鄉", "Zhongliao Township", None)
    Nantou_Yuchi = DistrictNamedTuple(1709, "魚池鄉", "Yuchi Township", None)
    Nantou_Guoxing = DistrictNamedTuple(1710, "國姓鄉", "Guoxing Township", None)
    Nantou_Shuili = DistrictNamedTuple(1711, "水里鄉", "Shuili Township", None)
    Nantou_Xinyi = DistrictNamedTuple(1712, "信義鄉", "Xinyi Township", None)
    Nantou_RenAi = DistrictNamedTuple(1713, "仁愛鄉", "Ren'ai Township", None)
    
    # endregion 南投
    
    # region 彰化 18XX
    Changhua_Changhua = DistrictNamedTuple(1800, "彰化市", "Changhua City", None)
    Changhua_Yuanlin = DistrictNamedTuple(1801, "員林鎮", "Yuanlin Township", None)
    Changhua_Hemei = DistrictNamedTuple(1802, "和美鎮", "Hemei Township", None)
    Changhua_Lugang = DistrictNamedTuple(1803, "鹿港鎮", "Lugang Township", None)
    Changhua_Xihu = DistrictNamedTuple(1804, "溪湖鎮", "Xihu Township", None)
    Changhua_Erlin = DistrictNamedTuple(1805, "二林鎮", "Erlin Township", None)
    Changhua_Tianzhong = DistrictNamedTuple(1806, "田中鎮", "Tianzhong Township", None)
    Changhua_Beidou = DistrictNamedTuple(1807, "北斗鎮", "Beidou Township", None)
    Changhua_Huatan = DistrictNamedTuple(1808, "花壇鄉", "Huatan Township", None)
    Changhua_Fenyuan = DistrictNamedTuple(1809, "芬園鄉", "Fenyuan Township", None)
    Changhua_Dacun = DistrictNamedTuple(1810, "大村鄉", "Dacun Township", None)
    Changhua_Yongjing = DistrictNamedTuple(1811, "永靖鄉", "Yongjing Township", None)
    Changhua_Shengang = DistrictNamedTuple(1812, "伸港鄉", "Shengang Township", None)
    Changhua_Xianxi = DistrictNamedTuple(1813, "線西鄉", "Xianxi Township", None)
    Changhua_Fuxing = DistrictNamedTuple(1814, "福興鄉", "Fuxing Township", None)
    Changhua_Xiushui = DistrictNamedTuple(1815, "秀水鄉", "Xiushui Township", None)
    Changhua_Puxin = DistrictNamedTuple(1816, "埔心鄉", "Puxin Township", None)
    Changhua_Puyan = DistrictNamedTuple(1817, "埔鹽鄉", "Puyan Township", None)
    Changhua_Dacheng = DistrictNamedTuple(1818, "大城鄉", "Dacheng Township", None)
    Changhua_Fangyuan = DistrictNamedTuple(1819, "芳苑鄉", "Fangyuan Township", None)
    Changhua_Zhutang = DistrictNamedTuple(1820, "竹塘鄉", "Zhutang Township", None)
    Changhua_Shetou = DistrictNamedTuple(1821, "社頭鄉", "Shetou Township", None)
    Changhua_Ershui = DistrictNamedTuple(1822, "二水鄉", "Ershui Township", None)
    Changhua_Tianwei = DistrictNamedTuple(1823, "田尾鄉", "Tianwei Township", None)
    Changhua_Pitou = DistrictNamedTuple(1824, "埤頭鄉", "Pitou Township", None)
    Changhua_Xizhou = DistrictNamedTuple(1825, "溪州鄉", "Xizhou Township", None)
    
    # endregion 彰化
    
    # region 雲林 19XX
    Yunlin_Douliu = DistrictNamedTuple(1900,  "斗六市", "Douliu City", None)
    Yunlin_Dounan = DistrictNamedTuple(1901,  "斗南鎮", "Dounan Township", None)
    Yunlin_Huwei = DistrictNamedTuple(1902,  "虎尾鎮", "Huwei Township", None)
    Yunlin_Xiluo = DistrictNamedTuple(1903,  "西螺鎮", "Xiluo Township", None)
    Yunlin_Tukang = DistrictNamedTuple(1904,  "土庫鎮", "Tukang Township", None)
    Yunlin_Beigang = DistrictNamedTuple(1905,  "北港鎮", "Beigang Township", None)
    Yunlin_Cihu = DistrictNamedTuple(1906,  "莿桐鄉", "Cihu Township", None)
    Yunlin_Linnei = DistrictNamedTuple(1907,  "林內鄉", "Linnei Township", None)
    Yunlin_Gukeng = DistrictNamedTuple(1908,  "古坑鄉", "Gukeng Township", None)
    Yunlin_Dapi = DistrictNamedTuple(1909,  "大埤鄉", "Dapi Township", None)
    Yunlin_Lunbei = DistrictNamedTuple(1910,  "崙背鄉", "Lunbei Township", None)
    Yunlin_Erlun = DistrictNamedTuple(1911,  "二崙鄉", "Erlun Township", None)
    Yunlin_Mailiao = DistrictNamedTuple(1912,  "麥寮鄉", "Mailiao Township", None)
    Yunlin_Taixi = DistrictNamedTuple(1913,  "臺西鄉", "Taixi Township", None)
    Yunlin_Dongshi = DistrictNamedTuple(1914,  "東勢鄉", "Dongshi Township", None)
    Yunlin_Baozhong = DistrictNamedTuple(1915,  "褒忠鄉", "Baozhong Township", None)
    Yunlin_Sihu = DistrictNamedTuple(1916,  "四湖鄉", "Sihu Township", None)
    Yunlin_Kouhu = DistrictNamedTuple(1917,  "口湖鄉", "Kouhu Township", None)
    Yunlin_Shuilin = DistrictNamedTuple(1918,  "水林鄉", "Shuilin Township", None)
    Yunlin_Yuanchang = DistrictNamedTuple(1919,  "元長鄉", "Yuanchang Township", None)
    
    # endregion 雲林   
    
    # region 嘉義 20XX
    Chiayi_Taibao = DistrictNamedTuple(2000, "太保市", "Taibao City", None)
    Chiayi_Puzi = DistrictNamedTuple(2001, "朴子市", "Puzi City", None)
    Chiayi_Budai = DistrictNamedTuple(2002, "布袋鎮", "Budai Township", None)
    Chiayi_Dalin = DistrictNamedTuple(2003, "大林鎮", "Dalin Township", None)
    Chiayi_Minxiong = DistrictNamedTuple(2004, "民雄鄉", "Minxiong Township", None)
    Chiayi_Xikou = DistrictNamedTuple(2005, "溪口鄉", "Xikou Township", None)
    Chiayi_Xingang = DistrictNamedTuple(2006, "新港鄉", "Xingang Township", None)
    Chiayi_Liujiao = DistrictNamedTuple(2007, "六腳鄉", "Liujiao Township", None)
    Chiayi_Dongshi = DistrictNamedTuple(2008, "東石鄉", "Dongshi Township", None)
    Chiayi_Yizhu = DistrictNamedTuple(2009, "義竹鄉", "Yizhu Township", None)
    Chiayi_Lucao = DistrictNamedTuple(2010, "鹿草鄉", "Lucao Township", None)
    Chiayi_Shuishang = DistrictNamedTuple(2011, "水上鄉", "Shuishang Township", None)
    Chiayi_Zhongpu = DistrictNamedTuple(2012, "中埔鄉", "Zhongpu Township", None)
    Chiayi_Zhuzhi = DistrictNamedTuple(2013, "竹崎鄉", "Zhuzhi Township", None)
    Chiayi_Meishan = DistrictNamedTuple(2014, "梅山鄉", "Meishan Township", None)
    Chiayi_Fanlu = DistrictNamedTuple(2015, "番路鄉", "Fanlu Township", None)
    Chiayi_Dapu = DistrictNamedTuple(2016, "大埔鄉", "Dapu Township", None)
    Chiayi_Alishan = DistrictNamedTuple(2017, "阿里山鄉", "Alishan Township", None)
    Chiayi_East = DistrictNamedTuple(2018, "東區", "East District", None)
    Chiayi_West = DistrictNamedTuple(2019, "西區", "West District", None)
    
    # endregion 嘉義

    # region 臺南 21XX
    Tainan_CentralWestern = DistrictNamedTuple(2100, "中西區", "Central and Western District", None)
    Tainan_East = DistrictNamedTuple(2101, "東區", "East District", None)
    Tainan_South = DistrictNamedTuple(2102, "南區", "South District", None)
    Tainan_North = DistrictNamedTuple(2103, "北區", "North District", None)
    Tainan_Anping = DistrictNamedTuple(2104, "安平區", "Anping District", None)
    Tainan_Annan = DistrictNamedTuple(2105, "安南區", "Annan District", None)
    Tainan_Yongkang = DistrictNamedTuple(2106, "永康區", "Yongkang District", None)
    Tainan_Guiren = DistrictNamedTuple(2107, "歸仁區", "Guiren District", None)
    Tainan_Xinhua = DistrictNamedTuple(2108, "新化區", "Xinhua District", None)
    Tainan_Zuojhen = DistrictNamedTuple(2109, "左鎮區", "Zuojhen District", None)
    Tainan_Yujing = DistrictNamedTuple(2110, "玉井區", "Yujing District", None)
    Tainan_Nanshi = DistrictNamedTuple(2111, "楠西區", "Nanshi District", None)
    Tainan_Nanhua = DistrictNamedTuple(2112, "南化區", "Nanhua District", None)
    Tainan_Rende = DistrictNamedTuple(2113, "仁德區", "Rende District", None)
    Tainan_Guanmiao = DistrictNamedTuple(2114, "關廟區", "Guanmiao District", None)
    Tainan_Longqi = DistrictNamedTuple(2115, "龍崎區", "Longqi District", None)
    Tainan_Guantian = DistrictNamedTuple(2116, "官田區", "Guantian District", None)
    Tainan_Madou = DistrictNamedTuple(2117, "麻豆區", "Madou District", None)
    Tainan_Jiali = DistrictNamedTuple(2118, "佳里區", "Jiali District", None)
    Tainan_Xigang = DistrictNamedTuple(2119, "西港區", "Xigang District", None)
    Tainan_Qigu = DistrictNamedTuple(2120, "七股區", "Qigu District", None)
    Tainan_Jiangjun = DistrictNamedTuple(2121, "將軍區", "Jiangjun District", None)
    Tainan_Xuejia = DistrictNamedTuple(2122, "學甲區", "Xuejia District", None)
    Tainan_Beimen = DistrictNamedTuple(2123, "北門區", "Beimen District", None)
    Tainan_Xinying = DistrictNamedTuple(2124, "新營區", "Xinying District", None)
    Tainan_Houbi = DistrictNamedTuple(2125, "後壁區", "Houbi District", None)
    Tainan_Baihe = DistrictNamedTuple(2126, "白河區", "Baihe District", None)
    Tainan_Dongshan = DistrictNamedTuple(2127, "東山區", "Dongshan District", None)
    Tainan_Liujia = DistrictNamedTuple(2128, "六甲區", "Liujia District", None)
    Tainan_Xiaying = DistrictNamedTuple(2129, "下營區", "Xiaying District", None)
    Tainan_Liuying = DistrictNamedTuple(2130, "柳營區", "Liuying District", None)
    Tainan_Yanshui = DistrictNamedTuple(2131, "鹽水區", "Yanshui District", None)
    Tainan_Shanhua = DistrictNamedTuple(2132, "善化區", "Shanhua District", None)
    Tainan_Danei = DistrictNamedTuple(2133, "大內區", "Danei District", None)
    Tainan_Shanshang = DistrictNamedTuple(2134, "山上區", "Shanshang District", None)
    Tainan_Xinshi = DistrictNamedTuple(2135, "新市區", "Xinshi District", None)
    Tainan_Anding = DistrictNamedTuple(2136, "安定區", "Anding District", None)
    
    # endregion 臺南
    
    # region 高雄 22XX
    Kaohsiung_Nanzih = DistrictNamedTuple(2200, "楠梓區", "Nanzih District", None)
    Kaohsiung_Zuoying = DistrictNamedTuple(2201, "左營區", "Zuoying District", None)
    Kaohsiung_Gushan = DistrictNamedTuple(2202, "鼓山區", "Gushan District", None)
    Kaohsiung_Sanmin = DistrictNamedTuple(2203, "三民區", "Sanmin District", None)
    Kaohsiung_Yancheng = DistrictNamedTuple(2204, "鹽埕區", "Yancheng District", None)
    Kaohsiung_Qianjin = DistrictNamedTuple(2205, "前金區", "Qianjin District", None)
    Kaohsiung_Xinxing = DistrictNamedTuple(2206, "新興區", "Xinxing District", None)
    Kaohsiung_Lingya = DistrictNamedTuple(2207, "苓雅區", "Lingya District", None)
    Kaohsiung_Qianzhen = DistrictNamedTuple(2208, "前鎮區", "Qianzhen District", None)
    Kaohsiung_Xiaogang = DistrictNamedTuple(2209, "小港區", "Xiaogang District", None)
    Kaohsiung_Qijin = DistrictNamedTuple(2210, "旗津區", "Qijin District", None)
    Kaohsiung_Fengshan = DistrictNamedTuple(2211, "鳳山區", "Fengshan District", None)
    Kaohsiung_Daliao = DistrictNamedTuple(2212, "大寮區", "Daliao District", None)
    Kaohsiung_Niaosong = DistrictNamedTuple(2213, "鳥松區", "Niaosong District", None)
    Kaohsiung_Linyuan = DistrictNamedTuple(2214, "林園區", "Linyuan District", None)
    Kaohsiung_Renwu = DistrictNamedTuple(2215, "仁武區", "Renwu District", None)
    Kaohsiung_Dashu = DistrictNamedTuple(2216, "大樹區", "Dashu District", None)
    Kaohsiung_Dasha = DistrictNamedTuple(2217, "大社區", "Dasha District", None)
    Kaohsiung_Gangshan = DistrictNamedTuple(2218, "岡山區", "Gangshan District", None)
    Kaohsiung_Luzhu = DistrictNamedTuple(2219, "路竹區", "Luzhu District", None)
    Kaohsiung_Qiaotou = DistrictNamedTuple(2220, "橋頭區", "Qiaotou District", None)
    Kaohsiung_Ziguan = DistrictNamedTuple(2221, "梓官區", "Ziguan District", None)
    Kaohsiung_Mituo = DistrictNamedTuple(2222, "彌陀區", "Mituo District", None)
    Kaohsiung_YongAn = DistrictNamedTuple(2223, "永安區", "Yong'an District", None)
    Kaohsiung_Yanchao = DistrictNamedTuple(2224, "燕巢區", "Yanchao District", None)
    Kaohsiung_Tianliao = DistrictNamedTuple(2225, "田寮區", "Tianliao District", None)
    Kaohsiung_Alian = DistrictNamedTuple(2226, "阿蓮區", "Alian District", None)
    Kaohsiung_Ciaotou = DistrictNamedTuple(2227, "茄萣區", "Ciaotou District", None)
    Kaohsiung_Hunei = DistrictNamedTuple(2228, "湖內區", "Hunei District", None)
    Kaohsiung_Qishan = DistrictNamedTuple(2229, "旗山區", "Qishan District", None)
    Kaohsiung_Meinong = DistrictNamedTuple(2230, "美濃區", "Meinong District", None)
    Kaohsiung_Neimen = DistrictNamedTuple(2231, "內門區", "Neimen District", None)
    Kaohsiung_Shanlin = DistrictNamedTuple(2232, "杉林區", "Shanlin District", None)
    Kaohsiung_Jiasian = DistrictNamedTuple(2233, "甲仙區", "Jiasian District", None)
    Kaohsiung_Liugui = DistrictNamedTuple(2234, "六龜區", "Liugui District", None)
    Kaohsiung_Maolin = DistrictNamedTuple(2235, "茂林區", "Maolin District", None)
    Kaohsiung_Taoyuan = DistrictNamedTuple(2236, "桃源區", "Taoyuan District", None)
    Kaohsiung_Namasiya = DistrictNamedTuple(2237, "那瑪夏區", "Namasiya District", None)
    

    # endregion 高雄
    
    # region 屏東 23XX
    Pingtung_Pingtung = DistrictNamedTuple(2300, "屏東市", "Pingtung City", None)
    Pingtung_Chaozhou = DistrictNamedTuple(2301, "潮州鎮", "Chaozhou Township", None)
    Pingtung_Donggang = DistrictNamedTuple(2302, "東港鎮", "Donggang Township", None)
    Pingtung_Hengchun = DistrictNamedTuple(2303, "恆春鎮", "Hengchun Township", None)
    Pingtung_Wanduan = DistrictNamedTuple(2304, "萬丹鄉", "Wanduan Township", None)
    Pingtung_Changzhi = DistrictNamedTuple(2305, "長治鄉", "Changzhi Township", None)
    Pingtung_Linluo = DistrictNamedTuple(2306, "麟洛鄉", "Linluo Township", None)
    Pingtung_Jiuru = DistrictNamedTuple(2307, "九如鄉", "Jiuru Township", None)
    Pingtung_Ligang = DistrictNamedTuple(2308, "里港鄉", "Ligang Township", None)
    Pingtung_Yanpu = DistrictNamedTuple(2309, "鹽埔鄉", "Yanpu Township", None)
    Pingtung_Gaoshu = DistrictNamedTuple(2310, "高樹鄉", "Gaoshu Township", None)
    Pingtung_Wanluan = DistrictNamedTuple(2311, "萬巒鄉", "Wanluan Township", None)
    Pingtung_Neipu = DistrictNamedTuple(2312, "內埔鄉", "Neipu Township", None)
    Pingtung_Zhudian = DistrictNamedTuple(2313, "竹田鄉", "Zhudian Township", None)
    Pingtung_Xinpi = DistrictNamedTuple(2314, "新埤鄉", "Xinpi Township", None)
    Pingtung_Fangliao = DistrictNamedTuple(2315, "枋寮鄉", "Fangliao Township", None)
    Pingtung_Xinyuan = DistrictNamedTuple(2316, "新園鄉", "Xinyuan Township", None)
    Pingtung_Kanding = DistrictNamedTuple(2317, "崁頂鄉", "Kanding Township", None)
    Pingtung_Linbian = DistrictNamedTuple(2318, "林邊鄉", "Linbian Township", None)
    Pingtung_Nanzhou = DistrictNamedTuple(2319, "南州鄉", "Nanzhou Township", None)
    Pingtung_Jiadong = DistrictNamedTuple(2320, "佳冬鄉", "Jiadong Township", None)
    Pingtung_Liuqiu = DistrictNamedTuple(2321, "琉球鄉", "Liuqiu Township", None)
    Pingtung_Checheng = DistrictNamedTuple(2322, "車城鄉", "Checheng Township", None)
    Pingtung_Manzhou = DistrictNamedTuple(2323, "滿州鄉", "Manzhou Township", None)
    Pingtung_Fangshan = DistrictNamedTuple(2324, "枋山鄉", "Fangshan Township", None)
    Pingtung_Wutai = DistrictNamedTuple(2325, "霧台鄉", "Wutai Township", None)
    Pingtung_Maja = DistrictNamedTuple(2326, "瑪家鄉", "Maja Township", None)
    Pingtung_Taiwu = DistrictNamedTuple(2327, "泰武鄉", "Taiwu Township", None)
    Pingtung_Laiyi = DistrictNamedTuple(2328, "來義鄉", "Laiyi Township", None)
    Pingtung_Chunri = DistrictNamedTuple(2329, "春日鄉", "Chunri Township", None)
    Pingtung_Shizi = DistrictNamedTuple(2330, "獅子鄉", "Shizi Township", None)
    Pingtung_Mudan = DistrictNamedTuple(2331, "牡丹鄉", "Mudan Township", None)
    Pingtung_Sandimen = DistrictNamedTuple(2332, "三地門鄉", "Sandimen Township", None)
    
    
    # endregion 屏東
    
    # region 宜蘭 24XX
    Yilan_Yilan = DistrictNamedTuple(2400, "宜蘭市", "Yilan City", None)
    Yilan_Luodong = DistrictNamedTuple(2401, "羅東鎮", "Luodong Township", None)
    Yilan_SuAo = DistrictNamedTuple(2402, "蘇澳鎮", "Su'ao Township", None)
    Yilan_Toucheng = DistrictNamedTuple(2403, "頭城鎮", "Toucheng Township", None)
    Yilan_Jiaoxi = DistrictNamedTuple(2404, "礁溪鄉", "Jiaoxi Township", None)
    Yilan_Zhuangwei = DistrictNamedTuple(2405, "壯圍鄉", "Zhuangwei Township", None)
    Yilan_Yuanshan = DistrictNamedTuple(2406, "員山鄉", "Yuanshan Township", None)
    Yilan_Dongshan = DistrictNamedTuple(2407, "冬山鄉", "Dongshan Township", None)
    Yilan_Wujie = DistrictNamedTuple(2408, "五結鄉", "Wujie Township", None)
    Yilan_Sanxing = DistrictNamedTuple(2409, "三星鄉", "Sanxing Township", None)
    Yilan_Datong = DistrictNamedTuple(2410, "大同鄉", "Datong Township", None)
    Yilan_Nanao = DistrictNamedTuple(2411, "南澳鄉", "Nanao Township", None)
    
    # endregion 宜蘭
    
    # region 花蓮 25XX
    Hualien_Hualien = DistrictNamedTuple(2500, "花蓮市", "Hualien City", None)
    Hualien_Fenglin = DistrictNamedTuple(2501, "鳳林鎮", "Fenglin Township", None)
    Hualien_Yuli = DistrictNamedTuple(2502, "玉里鎮", "Yuli Township", None)
    Hualien_Xincheng = DistrictNamedTuple(2503, "新城鄉", "Xincheng Township", None)
    Hualien_JiAn = DistrictNamedTuple(2504, "吉安鄉", "Ji'an Township", None)
    Hualien_Shoufeng = DistrictNamedTuple(2505, "壽豐鄉", "Shoufeng Township", None)
    Hualien_Xiulin = DistrictNamedTuple(2506, "秀林鄉", "Xiulin Township", None)
    Hualien_Guangfu = DistrictNamedTuple(2507, "光復鄉", "Guangfu Township", None)
    Hualien_Fengbin = DistrictNamedTuple(2508, "豐濱鄉", "Fengbin Township", None)
    Hualien_Ruifeng = DistrictNamedTuple(2509, "瑞穗鄉", "Ruifeng Township", None)
    Hualien_Wanrong = DistrictNamedTuple(2510, "萬榮鄉", "Wanrong Township", None)
    Hualien_Fuli = DistrictNamedTuple(2511, "富里鄉", "Fuli Township", None)
    Hualien_Zhuoxi = DistrictNamedTuple(2512, "卓溪鄉", "Zhuoxi Township", None)
    
    # endregion 花蓮
    
    # region 臺東 26XX
    Taitung_Taitung = DistrictNamedTuple(2600, "臺東市", "Taitung City", None)
    Taitung_Chenggong = DistrictNamedTuple(2601, "成功鎮", "Chenggong Township", None)
    Taitung_Guanshan = DistrictNamedTuple(2602, "關山鎮", "Guanshan Township", None)
    Taitung_Changbin = DistrictNamedTuple(2603, "長濱鄉", "Changbin Township", None)
    Taitung_Haiduan = DistrictNamedTuple(2604, "海端鄉", "Haiduan Township", None)
    Taitung_Chishang = DistrictNamedTuple(2605, "池上鄉", "Chishang Township", None)
    Taitung_Donghe = DistrictNamedTuple(2606, "東河鄉", "Donghe Township", None)
    Taitung_Luye = DistrictNamedTuple(2607, "鹿野鄉", "Luye Township", None)
    Taitung_Yanping = DistrictNamedTuple(2608, "延平鄉", "Yanping Township", None)
    Taitung_Beinan = DistrictNamedTuple(2609, "卑南鄉", "Beinan Township", None)
    Taitung_Jinpeng = DistrictNamedTuple(2610, "金峰鄉", "Jinpeng Township", None)
    Taitung_Dawu = DistrictNamedTuple(2611, "大武鄉", "Dawu Township", None)
    Taitung_Darin = DistrictNamedTuple(2612, "達仁鄉", "Darin Township", None)
    Taitung_GreenIsland = DistrictNamedTuple(2613, "綠島鄉", "Green Island Township", None)
    Taitung_Lanyu = DistrictNamedTuple(2614, "蘭嶼鄉", "Lanyu Township", None)
    Taitung_Taimali = DistrictNamedTuple(2615, "太麻里鄉", "Taimali Township", None)
    
    # endregion 臺東
    
    @classmethod
    def getItemByCity(cls, city: City):
        match (city):
            # region 基隆
            case (City.Keelung):
                return [
                    District.Keelung_RenAi,
                    District.Keelung_Zhongzheng,
                    District.Keelung_Xinyi,
                    District.Keelung_Zhongshan,
                    District.Keelung_Anle,
                    District.Keelung_Nuannuan,
                    District.Keelung_Qidu,
                ]
            # endregion 基隆
            
            # region 台北
            case (City.Taipei):
                return [
                    District.Taipei_Zhongzheng,
                    District.Taipei_Datong,
                    District.Taipei_Zhongshan,
                    District.Taipei_Wanhua,
                    District.Taipei_Xinyi,
                    District.Taipei_Songshan,
                    District.Taipei_Da,
                    District.Taipei_Nangang,
                    District.Taipei_Beitou,
                    District.Taipei_Neihu,
                    District.Taipei_Shilin,
                    District.Taipei_Wenshan,
                ]
            # endregion 台北
            
            # region 新北
            case (City.New_Taipei):
                return [
                    District.New_Taipei_Banqiao,
                    District.New_Taipei_Xinzhuang,
                    District.New_Taipei_Taishan,
                    District.New_Taipei_Linkou,
                    District.New_Taipei_Tamsui,
                    District.New_Taipei_Jinshan,
                    District.New_Taipei_Bali,
                    District.New_Taipei_Wanli,
                    District.New_Taipei_Shimen,
                    District.New_Taipei_Sanzhi,
                    District.New_Taipei_Ruifang,
                    District.New_Taipei_Xizhi,
                    District.New_Taipei_Pingxi,
                    District.New_Taipei_Gongliao,
                    District.New_Taipei_Shuangxi,
                    District.New_Taipei_Shenkeng,
                    District.New_Taipei_Shiding,
                    District.New_Taipei_Xindian,
                    District.New_Taipei_Pinglin,
                    District.New_Taipei_Wulai,
                    District.New_Taipei_Zhonghe,
                    District.New_Taipei_Yonghe,
                    District.New_Taipei_Tucheng,
                    District.New_Taipei_Sanxia,
                    District.New_Taipei_Shulin,
                    District.New_Taipei_Yingge,
                    District.New_Taipei_Sanchong,
                    District.New_Taipei_Luzhou,
                    District.New_Taipei_Wugu,
                ]
            # endregion 新北
            
            # region 桃園
            case (City.Taoyuan):
                return [
                    District.Taoyuan_Taoyuan,
                    District.Taoyuan_Zhongli,
                    District.Taoyuan_Pingzhen,
                    District.Taoyuan_Bade,
                    District.Taoyuan_Yangmei,
                    District.Taoyuan_Luzhu,
                    District.Taoyuan_Guishan,
                    District.Taoyuan_Longtan,
                    District.Taoyuan_Daxi,
                    District.Taoyuan_Dayuan,
                    District.Taoyuan_Guanyin,
                    District.Taoyuan_Xinwu,
                    District.Taoyuan_Fuxing,
                ]
            # endregion  桃園
            
            # region 新竹
            case (City.Hsinchu):
                return [
                    District.Hsinchu_Zhubei,
                    District.Hsinchu_ZhuDong,
                    District.Hsinchu_Xinpu,
                    District.Hsinchu_Guanxi,
                    District.Hsinchu_Emei,
                    District.Hsinchu_Baoshan,
                    District.Hsinchu_Beipu,
                    District.Hsinchu_Hengshan,
                    District.Hsinchu_Xianglin,
                    District.Hsinchu_Hukou,
                    District.Hsinchu_Xinfeng,
                    District.Hsinchu_JianShi,
                    District.Hsinchu_Wufeng,
                    District.Hsinchu_East,
                    District.Hsinchu_North,
                    District.Hsinchu_Xiangshan,
                ]
            # endregion 新竹
            
            # region 苗栗
            case (City.Miaoli):
                return [
                    District.Miaoli_Miaoli,
                    District.Miaoli_Tongxiao,
                    District.Miaoli_Yuanli,
                    District.Miaoli_Zhunan,
                    District.Miaoli_Toufen,
                    District.Miaoli_Holo,
                    District.Miaoli_Zhuolan,
                    District.Miaoli_Xihu,
                    District.Miaoli_Touwu,
                    District.Miaoli_Gongguan,
                    District.Miaoli_Tongluo,
                    District.Miaoli_Sanyi,
                    District.Miaoli_Zaoqiao,
                    District.Miaoli_Sanwan,
                    District.Miaoli_Nanzhuang,
                    District.Miaoli_Dahu,
                    District.Miaoli_Shitan,
                    District.Miaoli_Taian,
                ]
            # endregion 苗栗
            
            # region 台中
            case (City.Taichung):
                return [
                    District.Taichung_Central,
                    District.Taichung_East,
                    District.Taichung_South,
                    District.Taichung_West,
                    District.Taichung_North,
                    District.Taichung_Beitun,
                    District.Taichung_Xitun,
                    District.Taichung_Nantun,
                    District.Taichung_Taiping,
                    District.Taichung_Dali,
                    District.Taichung_Wufeng,
                    District.Taichung_Wuri,
                    District.Taichung_Fengyuan,
                    District.Taichung_Houli,
                    District.Taichung_Dongshi,
                    District.Taichung_Shigang,
                    District.Taichung_Xinshe,
                    District.Taichung_Heping,
                    District.Taichung_Shengang,
                    District.Taichung_Tanzi,
                    District.Taichung_Daya,
                    District.Taichung_Dadu,
                    District.Taichung_Longjing,
                    District.Taichung_Shalu,
                    District.Taichung_Wuqi,
                    District.Taichung_Qingshui,
                    District.Taichung_Dajia,
                    District.Taichung_Waipu,
                    District.Taichung_DaAn,
                ]
            # endregion  台中
            
            # region 南投
            case (City.Nantou):
                return [
                    District.Nantou_Nantou,
                    District.Nantou_Puli,
                    District.Nantou_Caotun,
                    District.Nantou_Zhushan,
                    District.Nantou_Jiji,
                    District.Nantou_Mingjian,
                    District.Nantou_Lugu,
                    District.Nantou_Zhongliao,
                    District.Nantou_Yuchi,
                    District.Nantou_Guoxing,
                    District.Nantou_Shuili,
                    District.Nantou_Xinyi,
                    District.Nantou_RenAi,
                ]
            # endregion 南投
            
            # region 彰化
            case (City.Changhua):
                return [
                    District.Changhua_Changhua,
                    District.Changhua_Yuanlin,
                    District.Changhua_Hemei,
                    District.Changhua_Lugang,
                    District.Changhua_Xihu,
                    District.Changhua_Erlin,
                    District.Changhua_Tianzhong,
                    District.Changhua_Beidou,
                    District.Changhua_Huatan,
                    District.Changhua_Fenyuan,
                    District.Changhua_Dacun,
                    District.Changhua_Yongjing,
                    District.Changhua_Shengang,
                    District.Changhua_Xianxi,
                    District.Changhua_Fuxing,
                    District.Changhua_Xiushui,
                    District.Changhua_Puxin,
                    District.Changhua_Puyan,
                    District.Changhua_Dacheng,
                    District.Changhua_Fangyuan,
                    District.Changhua_Zhutang,
                    District.Changhua_Shetou,
                    District.Changhua_Ershui,
                    District.Changhua_Tianwei,
                    District.Changhua_Pitou,
                    District.Changhua_Xizhou,
                ]
            # endregion 彰化
            
            # region 雲林
            case (City.Yunlin):
                return [
                    District.Yunlin_Douliu,
                    District.Yunlin_Dounan,
                    District.Yunlin_Huwei,
                    District.Yunlin_Xiluo,
                    District.Yunlin_Tukang,
                    District.Yunlin_Beigang,
                    District.Yunlin_Cihu,
                    District.Yunlin_Linnei,
                    District.Yunlin_Gukeng,
                    District.Yunlin_Dapi,
                    District.Yunlin_Lunbei,
                    District.Yunlin_Erlun,
                    District.Yunlin_Mailiao,
                    District.Yunlin_Taixi,
                    District.Yunlin_Dongshi,
                    District.Yunlin_Baozhong,
                    District.Yunlin_Sihu,
                    District.Yunlin_Kouhu,
                    District.Yunlin_Shuilin,
                    District.Yunlin_Yuanchang,
                ]
            # endregion 雲林
            
            # region 嘉義
            case (City.Chiayi):
                return [
                    District.Chiayi_Taibao,
                    District.Chiayi_Puzi,
                    District.Chiayi_Budai,
                    District.Chiayi_Dalin,
                    District.Chiayi_Minxiong,
                    District.Chiayi_Xikou,
                    District.Chiayi_Xingang,
                    District.Chiayi_Liujiao,
                    District.Chiayi_Dongshi,
                    District.Chiayi_Yizhu,
                    District.Chiayi_Lucao,
                    District.Chiayi_Shuishang,
                    District.Chiayi_Zhongpu,
                    District.Chiayi_Zhuzhi,
                    District.Chiayi_Meishan,
                    District.Chiayi_Fanlu,
                    District.Chiayi_Dapu,
                    District.Chiayi_Alishan,
                    District.Chiayi_East,
                    District.Chiayi_West,
                ]
            # endregion 嘉義
            
            # region 臺南
            case (City.Tainan):
                return [
                    District.Tainan_CentralWestern,
                    District.Tainan_East,
                    District.Tainan_South,
                    District.Tainan_North,
                    District.Tainan_Anping,
                    District.Tainan_Annan,
                    District.Tainan_Yongkang,
                    District.Tainan_Guiren,
                    District.Tainan_Xinhua,
                    District.Tainan_Zuojhen,
                    District.Tainan_Yujing,
                    District.Tainan_Nanshi,
                    District.Tainan_Nanhua,
                    District.Tainan_Rende,
                    District.Tainan_Guanmiao,
                    District.Tainan_Longqi,
                    District.Tainan_Guantian,
                    District.Tainan_Madou,
                    District.Tainan_Jiali,
                    District.Tainan_Xigang,
                    District.Tainan_Qigu,
                    District.Tainan_Jiangjun,
                    District.Tainan_Xuejia,
                    District.Tainan_Beimen,
                    District.Tainan_Xinying,
                    District.Tainan_Houbi,
                    District.Tainan_Baihe,
                    District.Tainan_Dongshan,
                    District.Tainan_Liujia,
                    District.Tainan_Xiaying,
                    District.Tainan_Liuying,
                    District.Tainan_Yanshui,
                    District.Tainan_Shanhua,
                    District.Tainan_Danei,
                    District.Tainan_Shanshang,
                    District.Tainan_Xinshi,
                    District.Tainan_Anding,
                ]
            # endregion 臺南
            
            # region 高雄
            case (City.Kaohsiung):
                return [
                    District.Kaohsiung_Nanzih,
                    District.Kaohsiung_Zuoying,
                    District.Kaohsiung_Gushan,
                    District.Kaohsiung_Sanmin,
                    District.Kaohsiung_Yancheng,
                    District.Kaohsiung_Qianjin,
                    District.Kaohsiung_Xinxing,
                    District.Kaohsiung_Lingya,
                    District.Kaohsiung_Qianzhen,
                    District.Kaohsiung_Xiaogang,
                    District.Kaohsiung_Qijin,
                    District.Kaohsiung_Fengshan,
                    District.Kaohsiung_Daliao,
                    District.Kaohsiung_Niaosong,
                    District.Kaohsiung_Linyuan,
                    District.Kaohsiung_Renwu,
                    District.Kaohsiung_Dashu,
                    District.Kaohsiung_Dasha,
                    District.Kaohsiung_Gangshan,
                    District.Kaohsiung_Luzhu,
                    District.Kaohsiung_Qiaotou,
                    District.Kaohsiung_Ziguan,
                    District.Kaohsiung_Mituo,
                    District.Kaohsiung_YongAn,
                    District.Kaohsiung_Yanchao,
                    District.Kaohsiung_Tianliao,
                    District.Kaohsiung_Alian,
                    District.Kaohsiung_Ciaotou,
                    District.Kaohsiung_Hunei,
                    District.Kaohsiung_Qishan,
                    District.Kaohsiung_Meinong,
                    District.Kaohsiung_Neimen,
                    District.Kaohsiung_Shanlin,
                    District.Kaohsiung_Jiasian,
                    District.Kaohsiung_Liugui,
                    District.Kaohsiung_Maolin,
                    District.Kaohsiung_Taoyuan,
                    District.Kaohsiung_Namasiya,
                ]
            # endregion 高雄
            
            # region 屏東
            case (City.Pingtung):
                return [
                    District.Pingtung_Pingtung,
                    District.Pingtung_Chaozhou,
                    District.Pingtung_Donggang,
                    District.Pingtung_Hengchun,
                    District.Pingtung_Wanduan,
                    District.Pingtung_Changzhi,
                    District.Pingtung_Linluo,
                    District.Pingtung_Jiuru,
                    District.Pingtung_Ligang,
                    District.Pingtung_Yanpu,
                    District.Pingtung_Gaoshu,
                    District.Pingtung_Wanluan,
                    District.Pingtung_Neipu,
                    District.Pingtung_Zhudian,
                    District.Pingtung_Xinpi,
                    District.Pingtung_Fangliao,
                    District.Pingtung_Xinyuan,
                    District.Pingtung_Kanding,
                    District.Pingtung_Linbian,
                    District.Pingtung_Nanzhou,
                    District.Pingtung_Jiadong,
                    District.Pingtung_Liuqiu,
                    District.Pingtung_Checheng,
                    District.Pingtung_Manzhou,
                    District.Pingtung_Fangshan,
                    District.Pingtung_Wutai,
                    District.Pingtung_Maja,
                    District.Pingtung_Taiwu,
                    District.Pingtung_Laiyi,
                    District.Pingtung_Chunri,
                    District.Pingtung_Shizi,
                    District.Pingtung_Mudan,
                    District.Pingtung_Sandimen,
                ]
            # endregion 屏東
            
            # region 宜蘭
            case (City.Yilan):
                return [
                    District.Yilan_Yilan,
                    District.Yilan_Luodong,
                    District.Yilan_SuAo,
                    District.Yilan_Toucheng,
                    District.Yilan_Jiaoxi,
                    District.Yilan_Zhuangwei,
                    District.Yilan_Yuanshan,
                    District.Yilan_Dongshan,
                    District.Yilan_Wujie,
                    District.Yilan_Sanxing,
                    District.Yilan_Datong,
                    District.Yilan_Nanao,
                ]
            # endregion 宜蘭
            
            # region 花蓮
            case (City.Hualien):
                return [
                    District.Hualien_Hualien,
                    District.Hualien_Fenglin,
                    District.Hualien_Yuli,
                    District.Hualien_Xincheng,
                    District.Hualien_JiAn,
                    District.Hualien_Shoufeng,
                    District.Hualien_Xiulin,
                    District.Hualien_Guangfu,
                    District.Hualien_Fengbin,
                    District.Hualien_Ruifeng,
                    District.Hualien_Wanrong,
                    District.Hualien_Fuli,
                    District.Hualien_Zhuoxi,
                ]
            # endregion 花蓮
            
            # region 臺東
            case (City.Taitung):
                return [
                    District.Taitung_Taitung,
                    District.Taitung_Chenggong,
                    District.Taitung_Guanshan,
                    District.Taitung_Changbin,
                    District.Taitung_Haiduan,
                    District.Taitung_Chishang,
                    District.Taitung_Donghe,
                    District.Taitung_Luye,
                    District.Taitung_Yanping,
                    District.Taitung_Beinan,
                    District.Taitung_Jinpeng,
                    District.Taitung_Dawu,
                    District.Taitung_Darin,
                    District.Taitung_GreenIsland,
                    District.Taitung_Lanyu,
                    District.Taitung_Taimali,
                ]
            # endregion 臺東                                                                                               
                                                                                            
            case _:
                return None
# area_data = {












    

            