input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabets = ['a','b','c','d','e','f','g','h','j','k','l','m','o','p','q','r','s',
                't','u','v','w','x','y','z']

    max_num = 0
    max_alphabet = alphabets[0]

    for alphabet in alphabets:
        num = 0
        for char in string:
            if char == alphabet:
                num += 1
        if num > max_num:
            max_num = num
            max_alphabet = alphabet
        
    return max_alphabet

result = find_max_occurred_alphabet(input)
print(result)