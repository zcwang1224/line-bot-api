from linebot.models import PostbackAction
ex1 = {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://res.klook.com/image/upload/x_107,y_0,w_1786,h_2500,c_crop/c_scale,w_424/v1744773505/events_admin/hld1qkjki0kvakx5b3b3.jpg",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "label": "Line",
        "uri": "https://linecorp.com/"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "QWER台北演唱會2025｜【1, 2, QWER! in TAIPEI】The First QWER Fan Concert in TAIPEI｜Zepp New Taipei",
          "weight": "bold",
          "size": "xl",
          "contents": []
        },
        {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "margin": "lg",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "地址",
                  "size": "sm",
                  "color": "#AAAAAA",
                  "flex": 1,
                  "contents": []
                },
                {
                  "type": "text",
                  "text": "新北市新莊區新北大道四段3號8樓",
                  "size": "sm",
                  "color": "#666666",
                  "flex": 5,
                  "wrap": True,
                  "contents": []
                }
              ]
            }]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "flex": 0,
      "spacing": "sm",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "postback",
            "label":'找美食',
            "data":'找美食',
            # "data": json.dumps({"city": "台北市", "search_type": "找餐廳"}, ensure_ascii=False)
          },
          "height": "sm",
          "style": "link"
        },
        
        # PostbackAction(
        #     label='postback',
        #     data='發送 postback'
        # ),         
        
        {
          "type": "button",
          "action": {
            "type": "postback",
            "label": "找住宿",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "找景點",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "前往網站",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },                
      #   {
      #     "type": "spacer",
      #     "size": "sm"
      #   }
      ]
    }
}   

ex2 = {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://res.klook.com/image/upload/x_0,y_2,w_326,h_456,c_crop/v1744167676/events_admin/iuawb06hok6wfzywztoj.jpg",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "label": "Line",
        "uri": "https://linecorp.com/"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "QWER台北演唱會2025｜【1, 2, QWER! in TAIPEI】The First QWER Fan Concert in TAIPEI｜Zepp New Taipei",
          "weight": "bold",
          "size": "xl",
          "contents": []
        },
        {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "margin": "lg",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "地址",
                  "size": "sm",
                  "color": "#AAAAAA",
                  "flex": 1,
                  "contents": []
                },
                {
                  "type": "text",
                  "text": "新北市新莊區新北大道四段3號8樓",
                  "size": "sm",
                  "color": "#666666",
                  "flex": 5,
                  "wrap": True,
                  "contents": []
                }
              ]
            }]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "flex": 0,
      "spacing": "sm",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "message",
            "label": "找美食",
            "text": "0911234567"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "找住宿",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "找景點",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "前往網站",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },                
      #   {
      #     "type": "spacer",
      #     "size": "sm"
      #   }
      ]
    }
}      

ex3 = {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://res.klook.com/image/upload/x_0,y_2,w_326,h_456,c_crop/v1743561861/events_admin/j6dkkildp5v1ajw86xz2.jpg",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "label": "Line",
        "uri": "https://linecorp.com/"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "QWER台北演唱會2025｜【1, 2, QWER! in TAIPEI】The First QWER Fan Concert in TAIPEI｜Zepp New Taipei",
          "weight": "bold",
          "size": "xl",
          "contents": []
        },
        {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "margin": "lg",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "地址",
                  "size": "sm",
                  "color": "#AAAAAA",
                  "flex": 1,
                  "contents": []
                },
                {
                  "type": "text",
                  "text": "新北市新莊區新北大道四段3號8樓",
                  "size": "sm",
                  "color": "#666666",
                  "flex": 5,
                  "wrap": True,
                  "contents": []
                }
              ]
            }]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "flex": 0,
      "spacing": "sm",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "message",
            "label": "找美食",
            "text": "0911234567"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "找住宿",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "找景點",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "前往網站",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },                
      #   {
      #     "type": "spacer",
      #     "size": "sm"
      #   }
      ]
    }
}      

ex4 = {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://res.klook.com/image/upload/x_58,y_0,w_964,h_1350,c_crop/v1743998489/events_admin/pjfjoooovkxv2hcjq5ny.jpg",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "label": "Line",
        "uri": "https://linecorp.com/"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "QWER台北演唱會2025｜【1, 2, QWER! in TAIPEI】The First QWER Fan Concert in TAIPEI｜Zepp New Taipei",
          "weight": "bold",
          "size": "xl",
          "contents": []
        },
        {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "margin": "lg",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "地址",
                  "size": "sm",
                  "color": "#AAAAAA",
                  "flex": 1,
                  "contents": []
                },
                {
                  "type": "text",
                  "text": "新北市新莊區新北大道四段3號8樓",
                  "size": "sm",
                  "color": "#666666",
                  "flex": 5,
                  "wrap": True,
                  "contents": []
                }
              ]
            }]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "flex": 0,
      "spacing": "sm",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "message",
            "label": "找美食",
            "text": "0911234567"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "找住宿",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "找景點",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "前往網站",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },                
      #   {
      #     "type": "spacer",
      #     "size": "sm"
      #   }
      ]
    }
}      

ex5 = {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://res.klook.com/image/upload/x_0,y_77,w_1408,h_1971,c_crop/v1741318365/events_admin/lvzn3tbkb9poeedvgdee.jpg",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "label": "Line",
        "uri": "https://linecorp.com/"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "QWER台北演唱會2025｜【1, 2, QWER! in TAIPEI】The First QWER Fan Concert in TAIPEI｜Zepp New Taipei",
          "weight": "bold",
          "size": "xl",
          "contents": []
        },
        {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "margin": "lg",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "地址",
                  "size": "sm",
                  "color": "#AAAAAA",
                  "flex": 1,
                  "contents": []
                },
                {
                  "type": "text",
                  "text": "新北市新莊區新北大道四段3號8樓",
                  "size": "sm",
                  "color": "#666666",
                  "flex": 5,
                  "wrap": True,
                  "contents": []
                }
              ]
            }]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "flex": 0,
      "spacing": "sm",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "message",
            "label": "找美食",
            "text": "0911234567"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "找住宿",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "找景點",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "前往網站",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },                
      #   {
      #     "type": "spacer",
      #     "size": "sm"
      #   }
      ]
    }
}      

ex6 = {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://res.klook.com/image/upload/x_0,y_2,w_326,h_456,c_crop/v1737696936/events_admin/mwduf6sxvvfprhe5o3hz.jpg",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "label": "Line",
        "uri": "https://linecorp.com/"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "QWER台北演唱會2025｜【1, 2, QWER! in TAIPEI】The First QWER Fan Concert in TAIPEI｜Zepp New Taipei",
          "weight": "bold",
          "size": "xl",
          "contents": []
        },
        {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "margin": "lg",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "地址",
                  "size": "sm",
                  "color": "#AAAAAA",
                  "flex": 1,
                  "contents": []
                },
                {
                  "type": "text",
                  "text": "新北市新莊區新北大道四段3號8樓",
                  "size": "sm",
                  "color": "#666666",
                  "flex": 5,
                  "wrap": True,
                  "contents": []
                }
              ]
            }]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "flex": 0,
      "spacing": "sm",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "message",
            "label": "找美食",
            "text": "0911234567"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "找住宿",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "找景點",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "前往網站",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },                
      #   {
      #     "type": "spacer",
      #     "size": "sm"
      #   }
      ]
    }
}      

ex7 = {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://res.klook.com/image/upload/x_5,y_0,w_834,h_1167,c_crop/v1739340591/events_admin/v6ibtfdx42gqawl6awr0.jpg",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "label": "Line",
        "uri": "https://linecorp.com/"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "QWER台北演唱會2025｜【1, 2, QWER! in TAIPEI】The First QWER Fan Concert in TAIPEI｜Zepp New Taipei",
          "weight": "bold",
          "size": "xl",
          "contents": []
        },
        {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "margin": "lg",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "地址",
                  "size": "sm",
                  "color": "#AAAAAA",
                  "flex": 1,
                  "contents": []
                },
                {
                  "type": "text",
                  "text": "新北市新莊區新北大道四段3號8樓",
                  "size": "sm",
                  "color": "#666666",
                  "flex": 5,
                  "wrap": True,
                  "contents": []
                }
              ]
            }]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "flex": 0,
      "spacing": "sm",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "message",
            "label": "找美食",
            "text": "0911234567"
          },
          "height": "sm",
          "style": "link"
        },
       
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "找住宿",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "找景點",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "前往網站",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },                
      #   {
      #     "type": "spacer",
      #     "size": "sm"
      #   }
      ]
    }
}      

ex8 = {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://res.klook.com/image/upload/x_0,y_10,w_1448,h_2027,c_crop/v1734417037/events_admin/d73tqwtfdmfpclanghav.jpg",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "label": "Line",
        "uri": "https://linecorp.com/"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "QWER台北演唱會2025｜【1, 2, QWER! in TAIPEI】The First QWER Fan Concert in TAIPEI｜Zepp New Taipei",
          "weight": "bold",
          "size": "xl",
          "contents": []
        },
        {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "margin": "lg",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "地址",
                  "size": "sm",
                  "color": "#AAAAAA",
                  "flex": 1,
                  "contents": []
                },
                {
                  "type": "text",
                  "text": "新北市新莊區新北大道四段3號8樓",
                  "size": "sm",
                  "color": "#666666",
                  "flex": 5,
                  "wrap": True,
                  "contents": []
                }
              ]
            }]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "flex": 0,
      "spacing": "sm",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "message",
            "label": "找美食",
            "text": "0911234567"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "找住宿",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "找景點",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "前往網站",
            "uri": "https://guide.michelin.com/tw/zh_TW/taipei-region/taipei/restaurant/sinchao-rice-shoppe"
          },
          "height": "sm",
          "style": "link"
        },                
      #   {
      #     "type": "spacer",
      #     "size": "sm"
      #   }
      ]
    }
}      


