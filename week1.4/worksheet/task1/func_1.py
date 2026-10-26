
def func_1(lst_value): 
    ''' 
    code takes in a list and returns its average
    
    ''' 

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
        sum = sum + value 
    return sum/num_of_value 
    
print(func_1([2,5,6]))