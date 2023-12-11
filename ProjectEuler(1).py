num_count = 0
top_num = 1000

def calculations(num_count,top_num):
    numbers = []
    while num_count != 1000:
        if num_count%3==0 or num_count%5==0:
            number_append = num_count
            numbers.append(number_append)
            num_count = num_count + 1
        else:
            num_count = num_count + 1
    total = sum(numbers)
    return total

print(calculations(num_count,top_num))
