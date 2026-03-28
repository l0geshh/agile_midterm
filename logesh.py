import sys


if len(sys.argv) < 2:
    print("Error: No word provided.")
    sys.exit(1)

word = sys.argv[1].lower().replace(" ", "")


if word == word[::-1]:
    print(f"Success: '{word}' is a palindrome!")
    sys.exit(0)
else:
    print(f"Fail: '{word}' is not a palindrome.")
    sys.exit(1)
    # Final Midterm Test for Lab TechkaksksdafwsjjdsjASDASDAASDAS