import math

def find_min_rate(apples, h):
    def time_takes(rate):
        time = 0
        for i in range(len(apples)):
            time += (apples[i] + rate - 1) // rate 
        return time
    
    rate = 1
    while time_takes(rate) > h:
        rate += 1
    return rate

apples = [4, 7, 9, 12]
h = 6
print(find_min_rate(apples, h))