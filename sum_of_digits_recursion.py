
def sum_of_dgt(num):
    if num <= 10:
        return num  
    else:
        return (num%10 + sum_of_dgt(int(num/10)))

num = int(input())
result = sum_of_dgt(num)
print(result)