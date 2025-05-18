search_hotel_template = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://hips.hearstapps.com/hmg-prod/images/jcagh-p1502-pool-layout-4x3-658ea2f16d734.jpg?crop=1xw:1xh;center,top&resize=980:*",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        # "action": {
        #   "type": "uri",
        #   "label": "Line",
        #   "uri": "https://linecorp.com/"
        # }
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
              "label": "住飯店",
              "data": "住飯店"
            },
            "height": "sm",
            "style": "link"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://cdn2.ettoday.net/images/1264/d1264747.jpg",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        # "action": {
        #   "type": "uri",
        #   "label": "Line",
        #   "uri": "https://linecorp.com/"
        # }
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
              "label": "住青旅",
              "data": "住青旅"
            },
            "height": "sm",
            "style": "link"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://cdn.hk01.com/di/media/images/3115678/org/dc08557cb357fa831fa5f6b348839902.jpg/GE5SaXz4uaRSsK89ypUqidA5rC4OubktEfxfdBH8X3Q?v=w1280r16_9",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        # "action": {
        #   "type": "uri",
        #   "label": "Line",
        #   "uri": "https://linecorp.com/"
        # }
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
              "label": "住民宿",
              "data": "住民宿"
            },
            "height": "sm",
            "style": "link"
          }
        ]
      }
    }
  ]
}