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
