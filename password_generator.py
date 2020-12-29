import random


#common ASCII characters used in passwords
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '/', '.', '|', ':', '~', '<', '>', '?', '=']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = [letter.upper() for letter in lowercase]
combined = digits + symbols + lowercase + uppercase

needPassword = True

while needPassword:
    #get input length from user, stop if length is 0
    length = input("Choose Password Length\n")
    if int(length) < 4:
        print("password must be an appropriate length")
        continue

    #ensure password has one of each type of character
    result = random.choice(digits) + random.choice(symbols) + random.choice(lowercase) + random.choice(uppercase)

    #for remaining characters, choose any type, shuffle each time
    for x in range(int(length) - 4):
        result += random.choice(combined)
        result = ''.join(random.sample(result,len(result)))

    #print result
    print('Password:', result, end="\n")

    #ask if user would like a new password. A new length will be permitted
    choice = input("Would you like a new password? If so, type 'y'\n")
    needPassword = (choice == 'y')

print('Thank you for using this password generator')



#CONDENSED VERSION
# import random
# import string
# allCharacters = string.punctuation + string.ascii_letters + string.digits
# length = 15
# result = "".join(random.sample(allCharacters,length))

# print(result)