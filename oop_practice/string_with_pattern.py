"""4. StringWithPattern Descriptor
Problem: Create a StringWithPattern descriptor that accepts only strings matching a specified regular expression pattern.
If the string does not match the pattern, raise a ValueError.
Practice: Use this descriptor in an Account class where the username attribute should follow a specific pattern (e.g.,
only letters and numbers).
Extra Challenge: Add a change_username method that allows updating the username only if the new username matches the
required pattern."""

import re

class StringWithPattern:
    def __init__(self, pattern: str):
        self.pattern = pattern

    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def __set__(self, instance, value):
        match = re.fullmatch(self.pattern, value)

        if not match:
            raise ValueError(f"{self._param_name} doesn't match pattern.")

        setattr(instance, self._param_name, value)


class Account:
    username = StringWithPattern(r"[><?@+'`~^%&\*\[\]\{\}.!#|\\\"$';,:;=/\(\),\-\w\s+]{7,}")

    def __init__(self, username: str):
        self.username = username


if __name__ == "__main__":
    acct1 = Account('vadsasdf')
    print(acct1.username)










