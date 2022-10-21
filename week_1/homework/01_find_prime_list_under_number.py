input = 20


def find_prime_list_under_number(number):
    prime_num = []
    
    for n in range(2, number + 1):
        for i in prime_num:
            if n % i == 0 and i * i < n:
                break
        else:
            prime_num.append(n)
            
    return prime_num
        

result = find_prime_list_under_number(input)
print(result)