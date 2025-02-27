import json

from car_advisor_api.models import Brand, Car


def check_brand(brand_name):
    try:
        brand = Brand.objects.get(name=brand_name)
        return brand.id
    except Exception:
        return None


def add_brands():
    print('\nIn to car_advisor_api/scripts.py (add_brands)\n')
    with open('db_resources/brands.json') as f:
        brands_data = json.load(f)

    for brand in brands_data:
        try:
            Brand.objects.create(name=brand['name'])
            print(f'Brand - {brand['name']}, with id - {brand['id']} added!')
            continue
        except Exception:
            print(
                f'''Brand - {brand['name']}, with id - {brand['id']} already exists!''')


def add_cars():
    print('\nExcept in to car_advisor_api/scripts.py (add_cars)\n')
    with open('db_resources/cars.json') as f:
        cars_data = json.load(f)

    for car in cars_data:
        is_valid_brand = check_brand(car['brand_name'])
        is_valid_car = Car.objects.filter(
            model_name=car['model'],
            price=car['price']
        ).exists()

        if not is_valid_brand:
            print(f'Invalid brand: {car["brand_name"]}')
            continue

        if is_valid_car:
            print(
                f'Car - {car["brand_name"]}, model - {car["model"]}, with id - {car["id"]} already exists!')
            continue

        try:
            Car.objects.create(
                model_name=car['model'],
                brand_id=Brand.objects.get(id=check_brand(car['brand_name'])),
                price=car['price']
            )
            print(f'Car - {car["brand_name"]}, model - {car["model"]} added!')

        except Exception:
            print(
                f'Car - {car["brand_name"]}, model - {car["model"]} could not be added!')
