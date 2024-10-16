"""Problem 2: Custom String Class
Objective: Create a class called CustomString that behaves like a string but includes additional features:

Implement __init__ to initialize the string.
Implement __add__ to concatenate two CustomString instances.
Implement __sub__ to remove all occurrences of a substring from the string.
Implement __eq__ to compare two CustomString instances.
Implement __len__ to return the length of the string.
Implement __getattribute__ to restrict access to certain methods, such as upper() and lower()."""

class CustomString(str):
    def __new__(cls, value):
        return super().__new__(cls, value)

    def __init__(self, value):
        pass

    def __add__(self, other):
        if isinstance(other, (CustomString,str)):
            return CustomString(super().__add__(other))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other,str):
            return CustomString(self.replace(other,''))
        raise TypeError("Subtraction only works with strings.")

    def __eq__(self, other):
        if isinstance(other, (CustomString, str)):
            return super().__eq__(other)
        return NotImplemented

    def __len__(self):
        return super().__len__()

    def __getattribute__(self, item):
        if item in ("upper", "lower"):
            raise AttributeError(f"Access Denied. Cannot access attribute {item}.")
        object.__getattribute__(self,item)


if __name__ == '__main__':
    # string = CustomString('hi,')
    # string2 = CustomString('how are you?')
    # print(type(string))
    # string3 = string + string2
    # print(string3)
    # print(type(string3))

    # string = CustomString('how')
    # string2 = CustomString('Hi, how are you?')
    #
    # print(string2-string)
    #
    # string5 = CustomString('Hi')
    # print(type(string5))
    # # string6 = 'hi'
    # # print(string5 == string6)
    #
    # print(string5.lower())




    