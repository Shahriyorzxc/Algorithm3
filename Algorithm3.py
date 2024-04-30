def check(lst, number):
    return number in lst

print(check([1,2,3,4,5], 3)) #True
print(check([1,1,2,1,1,],3)) #False
print(check([5,5,5,6], 5)) #True
check([],5) #False

def list_less_than_100(lst):
    sum = 0
    for number in lst:
        sum += number
    return sum < 100

print(list_less_than_100([5, 57])) #True
print(list_less_than_100([77,30])) #False
print(list_less_than_100([0])) #True

def max_total(lst):
    lst.sort(reverse=True)
    max_amount = 0
    for i in range(5):
        max_amount += lst[i]
        return max_amount

print([1,1,0,1,3,10,10,10,10,1]) #43
print([0,0,0,0,0,0,0,0,0,10]) #100
print([1,2,3,4,5,6,7,8,9,10]) #40


















