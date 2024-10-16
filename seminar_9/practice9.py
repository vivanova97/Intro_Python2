from time import time
from typing import Callable
from functools import wraps


"""Create a decorator that times how long a function takes to execute and prints the time taken.
Problem: Write a decorator timer that logs the execution time of a function. Use time.time() or time.perf_counter() 
to track the time before and after the function call.
"""

def run_time_check(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        run_time = time() - start_time
        print(f"Function '{func.__name__}' took {run_time:.4f} seconds to run.")
        return result
    return wrapper


"""
2. Logging Function Calls
Create a decorator that logs every time a function is called, including the arguments passed and the result returned.
Problem: Write a decorator log_calls that prints out the function name, the arguments passed to it, and the result it 
returns.
"""

from typing import Callable


def log_calls(func: Callable):
    def wrapper(*args, **kwargs):
        args_str = ", ".join(map(str, args))  # Convert args to string for logging
        kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())  # Convert kwargs to string

        # Construct the final argument representation
        if args_str and kwargs_str:
            log_args = f"{args_str}, {kwargs_str}"
        elif args_str:
            log_args = args_str
        else:
            log_args = kwargs_str

        print(f"Calling {func.__name__}({log_args})")  # Log the function call with args and kwargs
        result = func(*args, **kwargs)  # Call the original function
        print(f"{func.__name__} returned {result}")  # Log the result of the function
        return result  # Return the original function's result

    return wrapper


"""3. Memoization (Caching Results)
Create a decorator that caches the results of expensive function calls so that future calls with the same arguments 
return instantly.
Problem: Write a decorator memoize that stores results of function calls and returns the cached result when the 
same inputs occur again."""

def cache_(func: Callable):
    results_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key by combining args and kwargs (use frozenset for immutability)
        key = (args, frozenset(kwargs.items()))
        if key in results_dict:
            return results_dict[key]  # Return cached result
        else:
            result = func(*args, **kwargs)  # Compute and store result
            results_dict[key] = result
            return result

    return wrapper


"""4. Access Control (Authorization Decorator)
Create a decorator that restricts access to a function based on user roles.

Problem: Write a decorator requires_role(role) that checks if the user has a certain role before allowing 
access to the function."""


def requires_role(allowed_roles):
    """
    Decorator to restrict access based on user roles.

    :param allowed_roles: List of roles allowed to access the function
    """
    def deco(func: Callable):
        @wraps(func)
        def wrapper(user_role, *args, **kwargs):
            if user_role in allowed_roles:
                return func(*args, **kwargs)
            else:
                print(f"Access denied. User role '{user_role}' is not authorized.")
                return None
        return wrapper
    return deco


@requires_role(['manager', 'supervisor'])
def view_dashboard(user_role):
    print("Welcome to the dashboard!")

@requires_role(['admin'])
def access_admin_panel(user_role):
    print("Accessing admin panel...")


"""
5. Retry on Failure
Create a decorator that retries a function if it fails (throws an exception).

Problem: Write a decorator retry(times) that will automatically retry a function if it raises an exception, 
up to a specified number of retries.
"""

def retry(times: int):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            attempts = times
            while attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts -= 1
                    print(f"Error: {e} {'Trying again...' if attempts != 0 else 'No more tries left.'}")
            raise Exception(f"Failed after {times} retries.")
        return wrapper
    return deco

"""
6. Input Validation
Create a decorator that checks if the input to a function matches certain conditions (e.g., type or range).

Problem: Write a decorator validate_input that ensures the function is only called with valid inputs. 
If the inputs are invalid, the decorator should raise an error.
"""


def validate_input(*arg_types, **kwarg_types):
    """
    Decorator to validate the input types of a function.
    :param arg_types: Expected types for positional arguments
    :param kwarg_types: Expected types for keyword arguments
    """
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check positional arguments
            for i, (arg, expected_type) in enumerate(zip(args, arg_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {i+1} is not of type {expected_type.__name__}")

            # Check keyword arguments
            for key, expected_type in kwarg_types.items():
                if key in kwargs and not isinstance(kwargs[key], expected_type):
                    raise TypeError(f"Keyword argument '{key}' is not of type {expected_type.__name__}")

            return func(*args, **kwargs)
        return wrapper
    return deco

@validate_input(int, int)  # Expect two integers
def add(a, b):
    return a + b

@validate_input(str, age=int)  # Expect a string and an 'age' keyword argument of type int
def greet(name, age=None):
    return f"Hello, {name}. You are {age} years old."

# Incorrect input (second argument is not an int)
try:
    print(add(5, "3"))
except TypeError as e:
    print(e)  # Output: Argument 2 is not of type int

# Correct inputs with keyword argument validation
print(greet("Alice", age=25))  # Output: Hello, Alice. You are 25 years old.

# Incorrect keyword argument type
try:
    print(greet("Alice", age="twenty-five"))
except TypeError as e:
    print(e)  # Output: Keyword argument 'age' is not of type int






# @cache_
# @run_time_check
# @log_calls
@retry(3)
def sum_(*args, **kwargs):
    summ = 0
    for key, value in kwargs.items():
        summ += key
    return summ

if __name__ == '__main__':
    division('hi',0)
    sum_(hi=1,bye=2,tie=3,shy=4,why=23,sly=124,rye=235,cry=345)
    delete_user(123 )