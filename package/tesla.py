class Tesla:
    # WRITE YOUR CODE HERE
    def __init__(self, model: str, color: str, autopilot = False):
        self.__model = model
        self.__color = color
        self.__battery_charge = 99.9
        self.__is_locked = True
        self.__seats_count = 5
        self.__autopilot = autopilot
        self.__obstacle = ""
        self.__efficiency = 0.3
        
    def welcome(self):
        raise NotImplementedError
    
    @property
    def color(self):
        return self.__color
    
    def autopilot(self, obstacle):
        self.__obstacle = obstacle
        if self.__autopilot:
            return f"Tesla model {self.__model} avoids {self.__obstacle}"
        else:
            return "Autopilot is not available"
    
    @property
    def seats_count(self):
        return self.__seats_count
    
    @seats_count.setter
    def seats_count(self, new_count: int):
        """ Change the original number of seats in the car which has to be higher or equal to 2 """
        if new_count >= 2:
            self.__seats_count = new_count
    
    def unlock(self):
        """ Unlocks the car """
        self.__is_locked = False
    
    def open_doors(self):
        """ If the car is unlocked, opens the doors """
        if self.__is_locked == False:
            return "Doors opens sideways"
        else:
            return "Car is locked!"
    
    def check_battery_level(self) -> str:
        return f"Battery charge level is {self.__battery_charge}%"

    def charge_battery(self):
        # COMPLETE THE FUNCTION
        self.__battery_charge = 100
        # BATTERY LEVEL SHOULD BE SET TO 100
        self.check_battery_level()
    
    def drive(self, travel_range: float):
        battery_discharge_percent = travel_range * self.__efficiency
        # COMPLETE THE FUNCTION
        if self.__battery_charge - battery_discharge_percent >= 0:
            self.__battery_charge -= battery_discharge_percent
            return self.check_battery_level()
        else:
            return self.check_battery_level()
