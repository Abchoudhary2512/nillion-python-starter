from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")

    my_str = SecretString(Input(name="my_str", party=party1))

    # Step 1: Reverse the string
    reversed_str = my_str[::-1]

    # Step 2: Check if the original string is equal to the reversed string
    is_palindrome = (my_str == reversed_str)

    # Output the result to party1
    return [Output(is_palindrome, "is_palindrome", party1)]
