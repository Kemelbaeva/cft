import sqlite3


class DBWorker:
    """
    This class work with data base sqlite3
    """
    def __init__(self, db_name):
        self.connection = sqlite3.connect('resources/' + db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        CREATE TABLE if not exists Car (id INTEGER PRIMARY KEY AUTOINCREMENT, year INTEGER, model TEXT, producer TEXT, 
        car_class TEXT, car_body TEXT);
        """)
        self.connection.commit()

    def add_car(self, car):
        querry = "INSERT INTO Car (year, model, producer, car_class, car_body) VALUES ({}, '{}', '{}', '{}', '{}');"\
            .format(car.year, car.model, car.producer, car.car_class, car.car_body)

        try:
            self.cursor.execute(querry)
            self.connection.commit()
        except Exception:
            print('Invalid data for input')

    def get_all_data(self):
        return self.cursor.execute('SELECT * from Car;')

    def change_car_info(self, params, car_id):
        querry = "UPDATE Car SET {} = {} WHERE id  = {};"

        for key, value in params.items():
            try:
                self.cursor.execute(querry.format(key, value, car_id))
                self.connection.commit()
            except Exception as e:
                print(e)
                print('Invalid key or value. Field {} and value {} not inputed'.format(key, value))

    def delete_car(self, car_id):
        querry = 'DELETE from Car WHERE id = {};'

        self.cursor.execute(querry.format(car_id))
        self.connection.commit()