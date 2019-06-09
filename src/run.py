from src.car import Car
from src.db_worker import DBWorker


if __name__ == '__main__':
    commands = """
        1 - add car
        2 - delete car
        3 - change car
        4 - print all cars
        5 - show commands
        6 - exit
        
        Fields in database: year, model, producer, car_class, car_body 
    """
    worker = DBWorker('car_databse')

    print(commands)
    while True:
        cmd = input('Write command: ')
        if cmd == '1':
            print('Input car data in format: year, model, producer, car class, car body')
            car_data = input()
            car_data = car_data.split(', ')
            worker.add_car(Car(car_data[0], car_data[1], car_data[2], car_data[3], car_data[4]))

        if cmd == '2':
            car_id = input('Input car id to delete: ')
            worker.delete_car(car_id)

        if cmd == '3':
            car_id = input('Input car ID: ')
            value = ''
            field = ''
            result_changing_fields_and_values = dict()
            while True:
                print('Input car property and new value for it. If you ended changing your fields input "done"')
                field = input('Input changing field: ')

                if field == 'done':
                    break

                value = input('Input value for this field: ')
                if value == 'done':
                    break

                result_changing_fields_and_values[field] = value

            worker.change_car_info(result_changing_fields_and_values, car_id)

        if cmd == '4':
            for row in worker.get_all_data():
                print(row)
            print('\n')

        if cmd == '5':
            print(commands)

        if cmd == '6':
            print('Stop working...')
            exit(0)
