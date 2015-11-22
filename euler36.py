import palindrome

def sum_double_base_palindrome(num):
    sum = 0
    for i in range(num+1):
        if palindrome.is_palindrome(i,10) and palindrome.is_palindrome(i,2):
           sum += i

    return sum
