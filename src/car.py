import sqlite3

class Car:
    def __init__(self, year, model, producer, car_class, car_body, id=None):
        self.id = id
        self.model = model
        self.year = year
        self.producer = producer
        self.car_class = car_class
        self.car_body = car_body

