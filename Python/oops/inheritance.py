# class car:
#     def __init__(self , brand , model):
#         self.brand = brand 
#         self.model = model 

#     def type_of_car(self):
#         return "fantastic car to enjoy life"


# class Electric(car):                                  Single inheritance
#     def __init__(self , brand , model , battery):
#         super().__init__(brand , model)
#         self.battery = battery
    


# class Pagani(car , Electric):
#     def __init__(self,brand , model , battery , engine ):
#         super().__init__(brand , model , battery )
#         self.engine   = engine

# tesla = Electric("Tesla" , "Model S " , "80 Kwj")
# print(tesla.brand)
# print(tesla.model)
# print(tesla.battery)
# print(tesla.type_of_car())


class Car:
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model 

    def type_of_car(self):
        return "fantastic car to enjoy life"


class Electric(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)  # Corrected super() usage
        self.battery = battery
        

class Pagani(Electric):  # Multiple inheritance
    def __init__(self, brand, model, battery, engine):
        super().__init__(brand, model, battery)  # Corrected super() usage
        self.engine = engine


Pag = Pagani("Pagani", "Model S", "otherworldly-Lightning", "Ultimate")
print(Pag.brand)
print(Pag.model)
print(Pag.battery)
print(Pag.engine)

Pag = Pagani("Pagani", "Model S", "otherworldly-Lightning", "Ultimate")
print(Pag.brand)
print(Pag.model)
print(Pag.battery)
print(Pag.engine)
