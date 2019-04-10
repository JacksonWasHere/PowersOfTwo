from datetime import datetime
def pow_count(num):
    count = 0
    list = {'1','2','4','8'}
    for c in str(num):
        if c in list:
            return 1
    return 0

def find_powers():
    t=datetime.now()
    last = t
    k=584_000
    num=2**k
    while k<10_000_000:
        num*=16
        count=pow_count(num)
        if not count:
            print("2^"+str(k)+"="+str(num))
        if(k%1000==0):
            print("At k="+str(k)+"\tTime = "+str(datetime.now()-t)+"\tdTime = "+str(datetime.now()-last))
            last = datetime.now()
        k+=4
find_powers()
