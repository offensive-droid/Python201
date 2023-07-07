from datetime import datetime
import time

def logger(func):
    def wrapper():
        print("-"*50)
        print("Executed started at: ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        func()
        print("Executed finished at: ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print("-"*50)
    return wrapper

#call
@logger
def display():
    time.sleep(1)
    print("Decorators are pythonic!")
    time.sleep(1)
display()
