import json
import numpy as np

def hello(event, context):
    a = np.arange(15).reshape(3, 5)
    print("Your numpy array:")
    print(a)
    print("completed!!")

if __name__ == "__main__":
    hello('', '')
