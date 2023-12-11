top_num=4000000

def calculations(top_num):
    num_list=[]
    num1 = 0
    num2 = 1
    next_number = num2  
    count = 1
    while next_number <= top_num:
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
        if next_number%2==0:
            num_list.append(next_number)
    total = sum(num_list)
    print(total)
    
calculations(top_num)



