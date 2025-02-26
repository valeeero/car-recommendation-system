from django.apps import AppConfig


class CarAdvisorApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'car_advisor_api'

    def ready(self):
        from car_advisor_api.scripts import add_brands, add_cars
        add_brands()
        add_cars()