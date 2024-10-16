"""Problem 3: Time Management System
Objective: Create an abstract class called Time with the following:

Abstract methods:
__eq__(self, other) - to check if two times are equal.
__le__(self, other) - to check if one time is less than or equal to another.
__ge__(self, other) - to check if one time is greater than or equal to another.
Create a subclass called Time24 that implements the methods above.
Implement __init__ to take hours and minutes, ensuring valid time entries.
Implement __new__ to restrict the creation of Time24 instances if the time is invalid.
Use __setattr__ to restrict hours to a range of 0-23 and minutes to a range of 0-59."""

from abc import ABC, abstractmethod

class Time(ABC):
    @abstractmethod
    def __eq__(self, other):
        """Checks if two times are equal."""
        pass

    @abstractmethod
    def __le__(self, other):
        """Checks if one time is less than or equal to another."""
        pass

    @abstractmethod
    def __ge__(self, other):
        """Checks if one time is greater than or equal to another."""
        pass

class Time24(Time):
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __new__(cls, hours, minutes):
        max_hours = 23
        max_min = 59
        min_hours = min_minutes = 0
        if (isinstance(hours, int) and isinstance(minutes,int) and min_hours <= hours <= max_hours and
                min_minutes <= minutes <= max_min):
            return super().__new__(cls)
        else:
            raise ValueError(f"Error hours should be between {min_hours}-{max_hours} and minutes should be between"
                          f"{min_minutes}-{max_min} ")

    def __eq__(self, other):
        if not isinstance(other,Time24):
            raise TypeError(f"Error! Can't compare {type(other)} to {type(self)}")
        return self.hours == other.hours and self.minutes == other.minutes


    def __le__(self, other):
        if not isinstance(other,Time24):
            raise TypeError(f"Error! Can't compare {type(other)} to {type(self)}")
        elif self.hours < other.hours:
            return True
        elif self.hours == other.hours:
            return self.minutes < other.minutes or self.minutes == other.minutes

    def __ge__(self, other):
        if not isinstance(other,Time24):
            raise TypeError(f"Error! Can't compare {type(other)} to {type(self)}")
        elif self.hours > other.hours:
            return True
        elif self.hours == other.hours:
            return self.minutes > other.minutes or self.minutes == other.minutes

    def __setattr__(self, key, value):
        max_hours = 23
        max_min = 59
        min_hours = min_minutes = 0
        if key == 'hours':
            if not isinstance(value, int) or not (min_hours <= value <= max_hours):
                raise ValueError(f"Error hours should be between {min_hours}-{max_hours}")
        elif key == 'minutes':
            if not isinstance(value, int) or not (min_minutes <= value <= max_min):
                raise ValueError(f"Error minutes should be between {min_minutes}-{min_hours}")
        object.__setattr__(self,key,value)


time1 = Time24(23,10)
time2 =  Time24(23, 22)
time3 = 23.44

if __name__ == '__main__':
    print(time1.__le__(time2))
    # print(time1.__eq__(time3))

