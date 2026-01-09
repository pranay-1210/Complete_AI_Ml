#calculating Average:-

def calc_avg(num1, num2):  # with non-default parameters
    sum = num1 + num2
    avg = sum / 2
    return avg

avg = calc_avg(10, 20)
print("The average of 10 and 20 is", avg)


# Function with default parameters(Average of two numbers):-

def calc_avg(num1, num2 = 20):  # with default parameters
    sum = num1 + num2
    avg = sum / 2
    return avg

avg = calc_avg(10)
print("The average of 10 and 20 is", avg)