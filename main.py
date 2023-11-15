<<<<<<< HEAD
def add_numbers(a, b):
    """두 수의 합을 반환하는 함수"""
    result = a + b
    return result

# 함수 호출 예시
num1 = 5
num2 = 7
sum_result = add_numbers(num1, num2)

print(f"{num1}와 {num2}의 합은 {sum_result}입니다.")
=======
# main.py

def convert_to_uppercase(string):
    """
    Converts a given string to uppercase.
    
    Parameters:
    string (str): The string to convert.

    Returns:
    str: The converted uppercase string.
    """
    return string.upper()

# 이 함수를 사용하는 예시
if __name__ == "__main__":
    input_string = "Hello, World!"
    uppercase_string = convert_to_uppercase(input_string)
    print(uppercase_string)
>>>>>>> origin/main
