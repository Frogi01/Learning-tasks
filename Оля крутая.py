class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("The car is started")

    def stop(self):
        print("The car is stopped")

    def year_of_car(self, year):
        self.year = year

    def type_of_car(self, type):
        self.type = type

    def color_of_car(self, color):
        self.color = color

car = Car("blue","BMW",2018)
car.start()
car.stop()
car.year_of_car(2022)
car.type_of_car("Mercedes")
car.color_of_car("black")