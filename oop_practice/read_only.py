"""2. ReadOnly Descriptor
Problem: Create a ReadOnly descriptor that allows reading an attribute but does not allow it to be set or deleted after
its initial assignment in __init__. Raise an AttributeError if an attempt is made to set or delete the attribute after
initialization.
Practice: Use this descriptor in a Configuration class where version is a read-only attribute.
Extra Challenge: Add a __str__ method to Configuration that returns a string representation of the class instance."""

class ReadOnly:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if hasattr(instance, self.param_name):
            raise AttributeError(f"Cannot set {self.param_name} because attribute has already been set.")
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f"Cannot delete {self.param_name} because it is read-only.")



class Configuration:
    version = ReadOnly()

    def __init__(self, version):
        self.version = version

    def __str__(self):
        return f"Configuration(version={self.version})"


if __name__ == "__main__":
    config = Configuration(3)
    # del config.version
    print(config)


