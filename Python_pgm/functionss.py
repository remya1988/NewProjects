def multiply(a,b):
    result = a*b
    return result

#PALINDROME CHECKING

def is_palindrome(string):
    backword = string[::-1]
    return backword

ans = multiply(10,2)
print("10 * 2 = ",ans)

for i in range(10):
    an = multiply(i,2)
    print(i ,"* 2 = ",an)

str = input("Enter a string to check the plaindrome : \n")
back = is_palindrome(str)
if back.casefold() == str.casefold():
    print("{} is a palindrome string......".format(str))
else :
    print("The given string is not palindrome......")


def pal_sentence(string1):
    st = ""
    for char in string1:
        if char.isalnum():
            st += char
    bksen = st[::-1]
    if bksen.casefold() == st.casefold():
        return True
    else:
        return False


str = input("Enter a setence : \n")
res = pal_sentence(str)
if res == True:
    print("{} is a palindrome sentence....".format(str))
else :
    print("{} is not a palindrome sentence.......".format(str))