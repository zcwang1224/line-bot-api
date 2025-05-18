
# region LOCATION_ROOT_TEMPLATE
LOCATION_ROOT_TEMPLATE = {
    "type":"bubble",
    "size":"kilo",
    "direction":"ltr",
    "header": {
        "type":"box",
        "layout":"vertical",
        "contents": [
            {
                "type": "text",
                "text": "所在區域",
                "size": "lg",
                "color": "#000000FF",
                "align": "center",
                "margin": "xl",
                "contents": [],
            },
            {
                "type":"separator",
                "margin":"md"
            }
        ]
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [],
    }
}

# endregion

class LineBotTemplate:
    
    @staticmethod
    def select_area_template():
        pass
    
    @classmethod
    def select_city_template():
        pass