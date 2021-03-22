import json
import os

def load_data():
    """Load the data from the json file.
    """
    d = {}
    #input your location of json file and replace
    with open('C://Users//Lenovo//Downloads//challenge955336d//challenge//json//course.json') as json_file:
        data = json.load(json_file)
        for i in range(len(data)):
            d[data[i]['id']] = {'title': data[i]['title'],
                                "date_created": data[i]["date_created"],
                                "date_updated": data[i]["date_updated"],
                                "description": data[i]["description"],
                                "discount_price": data[i]["discount_price"],
                                "id": data[i]["id"],
                                "image_path": data[i]["image_path"],
                                "on_discount": data[i]["on_discount"],
                                "price": data[i]["price"]
                                }
    return d