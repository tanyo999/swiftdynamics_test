num = [1,2,1,3,5,6,4]
count_max = num[0]
count_min = num[0]

for i in range(len(num)):
    if(num[i] > count_max):
        count_max = num[i]
    elif(num[i]< count_min):
        count_min = num[i]

print("Max : ",count_max)
print("Min : ",count_min)
