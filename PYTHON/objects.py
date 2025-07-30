# class superbikes:
#     def __init__( self , companies , bike , specifications , modify , topspeed , torque , horsepower , design , fuelcapacity , price ):
#         self.companies=companies 
#         self.bike=bike
#         self.specifiactions=specifications
#         self.companies=modify
#         self.topspeed=topspeed
#         self.torque=torque
#         self.horsepower=horsepower
#         self.design=design
#         self.price=price
#         self.fuelcapacity=fuelcapacity


#         def __superbikes_info(self):
#             print(f"bikes : {self.companies} {self.bike} {self.specifications} {self.modofy} {self.topspeed} {self.torque} {self.horsepower} {self.design} {self.price}")
            
# bike1 = superbikes("KAWASAKI","ninja h2","998cc,liqued cooled,inline 4 cylinder with supercharger dual channel abs with full of electronic feachers like lunch control etc, ","with fully loaded carbon body and sc project excust","209 mph(335 km/h)","141.7nm @ 11000 rpm","231 ps @ 11500 rpm","fully aro dynamic","17L","35.35 lakh - 88.52 lakh")
# bike2 = superbikes("B M W","s1000rr","999cc,water/oil cooled, inline 4 cylinder, 4 stroke, four titanium valves per cylinder, dual channel abs with full bluetooth features etc","with puig pro and arrow excust","225 mph(303 km/h)","113nm @11000 rpm","206.66 ps @ 13750 rpm","totally aro dynamic","16.5L","20.75 lakh - 25.25 lakh")
# bike3=bike3(DUCATI)

# bike1.superbikes_info()
# bike2.superbikes_info()





class Superbikes:
    def __init__(self, companies, bike, specifications, modify, topspeed, torque, horsepower, design, fuelcapacity, price):
        self.companies = companies
        self.bike = bike
        self.specifications = specifications  
        self.modify = modify  
        self.topspeed = topspeed
        self.torque = torque
        self.horsepower = horsepower
        self.design = design
        self.fuelcapacity = fuelcapacity
        self.price = price

    def superbikes_info(self): 
        print(f"Bike: {self.companies} {self.bike}\n"
              f"Specifications: {self.specifications}\n"
              f"Modifications: {self.modify}\n"
              f"Top Speed: {self.topspeed}\n"
              f"Torque: {self.torque}\n"
              f"Horsepower: {self.horsepower}\n"
              f"Design: {self.design}\n"
              f"Fuel Capacity: {self.fuelcapacity}\n"
              f"Price: {self.price}\n")


bike1 = Superbikes(
    "KAWASAKI", "Ninja H2", 
    "998cc, liquid-cooled, inline 4-cylinder with supercharger, dual-channel ABS with full electronic features like launch control, etc.",
    "Fully loaded carbon body and SC Project exhaust",
    "209 mph (335 km/h)", "141.7 Nm @ 11000 rpm", "231 PS @ 11500 rpm", 
    "Fully aerodynamic", "17L", "35.35 lakh - 88.52 lakh"
)

bike2 = Superbikes(
    "BMW", "S1000RR", 
    "999cc, water/oil-cooled, inline 4-cylinder, 4-stroke, four titanium valves per cylinder, dual-channel ABS with full Bluetooth features, etc.",
    "With Puig Pro and Arrow exhaust",
    "225 mph (303 km/h)", "113 Nm @ 11000 rpm", "206.66 PS @ 13750 rpm", 
    "Totally aerodynamic", "16.5L", "20.75 lakh - 25.25 lakh"
)


bike1.superbikes_info()
bike2.superbikes_info()
