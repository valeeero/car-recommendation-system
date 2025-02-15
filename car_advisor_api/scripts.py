import json

from car_advisor_api.models import Brand

def add_brands():
    with open('db_resources/brands.json') as f:
        brands_data = json.load(f)

    for brand in brands_data:
        try:
            Brand.objects.create(name=brand['name'])
            print(f'Brand - {brand['name']}, with id - {brand['id']} added!')
            continue
        except:
            print(f'Brand - {brand['name']}, with id - {brand['id']} already exists!')

