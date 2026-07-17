from enum import Enum


class Color(Enum):
    Red=1
    Blue=2




c1=Color.Red
c2=Color.Red

c3=Color.Blue

print(c1.__dict__)

print(c2.__dict__)

print(c1 is c3)