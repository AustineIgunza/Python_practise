#this function helps us to reverse a string and its read backwards

def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

#example case use for the function to reverse the sentence hello world
print(reverse_string("hello world"))
