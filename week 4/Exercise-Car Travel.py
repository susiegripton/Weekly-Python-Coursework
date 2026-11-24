from random import randint, choice
import matplotlib.pyplot as plt
cars=[]
next_car_number=1
entry_points=[0,30,60]
exit_points=[40,70,100]
class Car:
    def __init__(self,make,colour,start,destination):
        self.make=make
        self.colour=colour
        self.location=start
        self.destination=destination
        self.join()
    def join(self):
        global cars
        cars.append(self)
    def move(self):
        next_location=self.location+1
        for car in cars:
            if car!=self and car.location==next_location:
                return
        self.location+=1
        if self.location>=self.destination:
            self.leave()
    def leave(self):
        global cars
        cars.remove(self)
        print(f"{self.make}({self.colour}) left at junction {self.destination}")
    def report(self):
        print(f"{self.make} ({self.colour}) at {self.location}, heading for {self.destination}")
colours=["blue","red","yellow","green","silver","orange","purple"]
makes=["Vauxhall","Citroen","Audi","Ford","Honda","Toyota","Peugeot","Renault","Volkswagen","Hyundai","Jaguar","Kia","Lexus","Mazda","Mercedez-Benz","Nissan","Alfa Romeo","BMW","Fiat"]
def add_car():
    global next_car_number
    start=choice(entry_points)
    if any(car.location==start for car in cars):
        return
    possible_exits=[x for x in exit_points if x >start]
    if not possible_exits:
        return
    destination=choice(possible_exits)
    make=choice(makes)
    colour=choice(colours)
    Car(make,colour,start,destination)
    next_car_number+=1
    print(f"A {make}({colour}) joined at juntion {start}")
number_of_cars=20
total_car_limit=50
def plot_simulation():
    ax.clear()
    for car in cars:
        ax.scatter(car.location,1,color=car.colour,s=150,edgecolors="black",zorder=3)
        ax.text(car.location,1.15,f"{car.make}({car.colour})" ,fontsize=7,ha="center",rotation=90)
    for entry in entry_points:
        ax.axvline(entry,color="green",linestyle="--",alpha=0.6)
    for exit in exit_points:
        ax.axvline(exit,color="red",linestyle="--",alpha=0.6)
    ax.set_xlim(-5,105)
    ax.set_ylim(0,2.5)
    ax.set_xlabel("Position along the road")
    ax.set_yticks([])
    ax.set_title("Traffic Simulation - \n" f"Cars currently on the road:{len(cars)}")
    ax.grid(axis="x",alpha=0.3)
    fig.canvas.draw_idle()
    plt.pause(0.2)
for i in range(min(number_of_cars,total_car_limit)):
    if not add_car():
        break
plt.ion()
fig,ax=plt.subplots(figsize=(12,5))
plt.show(block=False)
simulation_step=0
while cars or next_car_number<=total_car_limit:
    if not plt.fignum_exists(fig.number):
        break
    simulation_step+=1
    for car in sorted(cars[:],key=lambda car:car.location,reverse=True):
        car.move()
    if next_car_number<=total_car_limit:
        if randint(1,3)==1:
            add_car()
    for car in cars:
        car.report()
    print(f"\nCars currently on the road:{len(cars)}")
    plot_simulation()
#    if cars or next_car_number<=total_car_limit:
#        input("\nPress Enter to continue their journey...")
print("\nAll cars have reached their destinations!")
plt.ioff()
plt.show()





        
