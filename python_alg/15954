import math
def average(doll): # 평균
    sum = 0
    avg = 0
    for i in range(len(doll)):
        sum += doll[i]
    avg = sum / len(doll)
    return avg

def variance(select,mean): # 분산
    vsum = 0
    for val in select:
        vsum = vsum + (val - mean) ** 2
    variance = vsum / len(select)
    return variance

N,K = map(int,input().split())
doll = []
select = []
std = 0
stdmin = 100

doll = list(map(int,input().split()))
for i in range(N-K+1):
    select = doll[i:i+3]
    mean = average(select)
    var = variance(select,mean)
    std = math.sqrt(var)# 표준편차 결과
    if std <  stdmin:
        stdmin = std

print(stdmin) 