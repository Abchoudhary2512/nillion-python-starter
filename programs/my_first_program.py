from nada_dsl import *

def encrypt_string(secret_str):
    # Simulating encryption of the string
    return ''.join(chr(ord(char) + 1) for char in secret_str)

def decrypt_string(encrypted_str):
    # Simulating decryption of the string
    return ''.join(chr(ord(char) - 1) for char in encrypted_str)

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    try:
        my_str = SecretString(Input(name="my_str", party=party1))

        # Step 1: Encrypt the string
        encrypted_str = encrypt_string(my_str)

        # Step 2: Reverse the encrypted string
        reversed_encrypted_str = encrypted_str[::-1]

        # Step 3: Decrypt the reversed string
        reversed_str = decrypt_string(reversed_encrypted_str)

        # Step 4: Check if the original string is equal to the reversed string
        is_palindrome = (my_str == reversed_str)

        # Output the result to party1
        return [Output(is_palindrome, "is_palindrome", party1)]

    except Exception as e:
        # Handle any potential errors and output an error message to party2
        error_message = f"Error occurred: {str(e)}"
        return [Output(error_message, "error_message", party2)]

# Simulating a more complex use case with additional security features
def complex_palindrome_check(party1_str, party2_str):
    # Encrypt both strings
    encrypted_str1 = encrypt_string(party1_str)
    encrypted_str2 = encrypt_string(party2_str)

    # Reverse and decrypt both strings
    reversed_str1 = decrypt_string(encrypted_str1[::-1])
    reversed_str2 = decrypt_string(encrypted_str2[::-1])

    # Check if both reversed strings match their original counterparts
    is_palindrome1 = (party1_str == reversed_str1)
    is_palindrome2 = (party2_str == reversed_str2)

    return is_palindrome1, is_palindrome2

def nada_main_advanced():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    try:
        party1_str = SecretString(Input(name="party1_str", party=party1))
        party2_str = SecretString(Input(name="party2_str", party=party2))

        # Perform complex palindrome check
        is_palindrome1, is_palindrome2 = complex_palindrome_check(party1_str, party2_str)

        # Output the results to respective parties
        return [
            Output(is_palindrome1, "is_palindrome_party1", party1),
            Output(is_palindrome2, "is_palindrome_party2", party2)
        ]

    except Exception as e:
        # Handle any potential errors and output an error message to both parties
        error_message = f"Error occurred: {str(e)}"
        return [
            Output(error_message, "error_message_party1", party1),
            Output(error_message, "error_message_party2", party2)
        ]

# Test function to simulate inputs and outputs
def test_nada_main():
    party1 = Party(name="TestParty1")
    party2 = Party(name="TestParty2")

    try:
        # Simulating inputs
        test_str1 = "madam"
        test_str2 = "racecar"

        # Run the advanced main function with test inputs
        outputs = nada_main_advanced()

        # Print the outputs for testing purposes
        for output in outputs:
            print(f"Output for {output.party.name}: {output.name} = {output.value}")

    except Exception as e:
        print(f"Test error: {str(e)}")

test_nada_main()
