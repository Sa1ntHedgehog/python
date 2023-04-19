#Mixing two dictionaries
car1={"brand":"Honda","model":"Civic"}
car2={"brand":"Tesla","model":"X"}
car3={"brand":"Лада","model":"2104"}
cars=[]
cars.append(car1)
cars.append(car2)
cars.append(car3)
print(cars)
#Mixing two dictionaries
dict1={"Тип коробки":"Механика","Привод":"Задний"}
dict2={"Цвет":"Красный"}
dict3={"brand":"Лада","model":"2104"}
car={}
for settings in (dict1,dict2,dict3):
    car.update(settings)
print(car)
    

