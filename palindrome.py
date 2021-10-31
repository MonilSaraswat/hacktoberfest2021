textValue = input("Enter a Value")
words = []
if textValue.isnumeric():
    for word in textValue:
        words.append(word)
    if (words[:] == words[::-1]):
        print("The Number is Palindrome")
    else:
        print("The Number is not Palindrome")
else:
    for word in textValue:
        words.append(word)
    if(words[:] == words[::-1]):
        print("The String is Palindrome")
    else:
        print("The String is not Palindrome")



