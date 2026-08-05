


try:
    # raise  Exception
    print("Try block code execution without any exception")
except:
    print("Error Occurred,flow come when exception is raised")
else:
    print("No Exception present, Flow come when there is no exception")
finally:
    print("Finally block is always executed")