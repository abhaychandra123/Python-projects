class Vehicle:
    def __init__(self,imodel,idriver_name,inum_seats,ihas_ac):
        self.model=imodel
        self.driver_name=idriver_name
        self.num_seats=inum_seats
        self.has_ac=ihas_ac
    def car_desc(self):
        print("The car " + self.model + ", is a " + str(self.num_seats) + " seater car. The driver of the car is " + self.driver_name + ".")
        if self.has_ac=="yes":
            print("It is also air conditioned.")
        elif self.has_ac=="no":
            print("Unfortunataly, it's not air conditioned.")
        else:
            quit("Enter yes/no, fool.")

car1=Vehicle("Renault","Ram",8,"yes")
print(car1.__dict__)
print()
car1.car_desc()
