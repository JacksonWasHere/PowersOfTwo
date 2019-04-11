from datetime import datetime
from multiprocessing import Pool
import math
def pow_count(num):
    list = {1,2,4,8}
    digits = int(math.log(num)/math.log(10)+1)
    for i in range(digits):
        if num%10 in list:
            return 1
        num//=10
    return 0

def power(num):
    num*=4
    if(num%5000==0):
        print(num,file=open("output.txt","a"))
        print(num)
    if not pow_count(2**num):
        print("2^"+str(num)+" is valid",file=open("output.txt","a"))
        print("FOUND")
        return 1
    return 0

if __name__ == '__main__':
    with Pool(96) as p:
        print("start",file=open("output.txt","w"))
        nums = p.map(power, range(100000000))
        print("done",file=open("output.txt","a"))
