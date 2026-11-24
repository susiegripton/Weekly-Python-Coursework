from random import randint
import matplotlib.pyplot as plt
import math

class power_generator:
    def __init__(self):
        self.output = 0

    def generate(self,day):
        global grid
        grid += round(50*(math.sin(2*math.pi/365*(day-81.75))+1)) + randint(0,250)
        
class power_user:
    def __init__(self,level):
        self.level = level

    def consume(self):
        global grid, stores

        if grid >= self.level:
            grid -= self.level
            return True
        else:
             target = self.level - grid
             grid =0
             for battery in stores:
                 if target > 0:
                     target -= battery.decharge(target)
             if target > 0:
                 print("Not enough power")
                 return False
             else:
                 return True
        
turbines = []
for i in range(0,5):
    turbines.append(power_generator())
solar_farms = []
for i in range(0,5):
    solar_farms.append(power_generator())

factory = power_user(300)
farms = []
for i in range(10):
    farms.append(power_user(100))
    
class power_store:
    def __init__(self,capacity):
        self.capacity = capacity
        self.level = 0

    def charge(self):
        global grid

        if grid > 0: 
            if (self.capacity - self.level) > grid: 
                self.level += grid
                grid = 0
            else:
                grid -= self.capacity - self.level
                self.level = self.capacity

    def decharge(self,amount):
        if self.level >= amount:
            self.level -= amount
            return amount
        else:
            power = self.level
            self.level = 0
            return power

stores = []
for i in range(10):
    stores.append(power_store(100))
    
days=[]
daily_production=[]
daily_storage=[]

brown_out_days=0


#this IS LOOP

for i in range(365):
    grid = 0
    days.append(i)
    for turbine in turbines:
        turbine.generate(i)
    for solar_farm in solar_farms:
        solar_farm.generate(i)
    print(f"Start day {i}. Grid power level: {grid}.")
    daily_production.append(grid)

    if factory.consume():
        for farm in farms:
            if not farm.consume():
                brown_out_days+=1
                break
    else:
        brown_out_days+=1
    print(f"End day {i}. Grid power level: {grid}.")
    
        
            
    for battery in stores:
        battery.charge()
        
    overall_storage = 0
    for battery in stores:
        overall_storage += battery.level
    print(f"Stored in batteries: {overall_storage}")
    daily_storage.append(overall_storage)

    if grid > 0:
        print(f"Unstored power: {grid}")

print(brown_out_days)

plt.plot(days,daily_production)
plt.plot(days,daily_storage)
plt.xlabel('Days')
plt.ylabel('Power')
plt.legend(['Production', 'Storage'])
plt.show()

