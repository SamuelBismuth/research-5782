def safe_call(f, **args):
    for key, val in args.items():
        if key in f.__annotations__:
            if f.__annotations__[key] != val.__class__:
                raise Exception("Check the arguments.")
    # If everything is ok, call the function:
    print(f(**args))

def f(x:int, y:float, z):
    return x+y+z


'''
Tests
'''

# Here the call is working. Then, it prints 15.0
try:
    safe_call(f, x=5, y=7.0, z=3)
except Exception as ex:
    print(ex)

# Here the call is working despite the fact the z is a str since the function f doesn't annotate z.
# Then, the function call sends an error.
try:
    safe_call(f, x=5, y=7.0, z="3")
except Exception as ex:
    print(ex)

# Here the call is not working since y should be a float but it is a str.
# Then it prints "Check the arguments."
try:
    safe_call(f, x=5, y="abc", z=3)
except Exception as ex:
    print(ex)