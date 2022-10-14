input = [3, 5, 6, 1, 2, 4]

def is_number_exist(number, array):
    for number in array: # array 길이 만큼 아래 연산 실행
        if number == number: # 비교 연산 1번 실행
            return True # N * 1 = N 만큼
    return False
result = is_number_exist(10, input)
print(result)