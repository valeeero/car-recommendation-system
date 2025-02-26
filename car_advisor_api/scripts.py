import json

from car_advisor_api.models import Brand, Car


def add_brands():
    with open('db_resources/brands.json') as f:
        brands_data = json.load(f)

    for brand in brands_data:
        try:
            Brand.objects.create(name=brand['name'])
            print(f'Brand - {brand['name']}, with id - {brand['id']} added!')
            continue
        except:
            print(
                f'Brand - {brand['name']}, with id - {brand['id']} already exists!')


def check_brand(brand_name):
    try:
        brand = Brand.objects.get(name=brand_name)
        return brand.id
    except:
        return None


def check_car(car_name, car_price):
    try:
        Car.objects.get(model_name=car_name)
        Car.objects.get(price=car_price)
        return False
    except:
        return True


def add_cars():
    with open('db_resources/cars.json') as f:
        cars_data = json.load(f)

    for car in cars_data:
        if check_brand(car['brand_name']) and check_car(car_name=car['model'], car_price=car['price']) == False:
            try:
                Car.objects.create(
                    model_name=car['model'],
                    brand_id=Brand.objects.get(
                        id=check_brand(car['brand_name'])),
                    price=car['price']
                )
                print(
                    f'Car - {car['brand_name']}, with id - {car['id']} added!')
                continue

            except:
                print(
                    f'Car - {car['brand_name']}, with id - {car['id']} already exists!')
        else:
            print(f'Car - {car['brand_name']}, with id - {car['id']} already exists!')
            continue
