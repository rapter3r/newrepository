class Car:
    fuel = 20
    rate = 0.1
    traveled = 0

    def __int__(self, fuel=20, rate=0.1):
        self.fuel = fuel
        self.rate = rate

    def drive(self, distance):
        posible_to_travel = self.fuel / self.rate

        if posible_to_travel >= distance:
            self.traveled += distance
            self.fuel -= distance * self.rate

        else:
            self.traveled += posible_to_travel
            self.fuel = 0
            raise Exception('Бензин закончился!')

car1 = Car()
car1.drive(201)


