string methods
link to questions
https://towardsdatascience.com/41-questions-to-test-your-knowledge-of-python-strings-9eb473aa8fe8

1.check whether string contain specific substring or not
Done using in operator
message = "Hello ali how are you"
print("ali" in message)
print("Dev" in "Dev is an IDE used to compile C++")

---------------------------------------------------------------------------------------
2.Check whether every word of sentence start with capital letter or not
Done using istitle() method
message2 = "Hello How Are You Ali ?"
print(message2.istitle())
print("Hello ali how are you".istitle())

---------------------------------------------------------------------------------------
3.Check whether particular substring exist ,if exist return its index
Done using find and index method
message3="Dev is an IDE used to compile C++"
print(message3.find("Dev"))
print(message3.index("e"))
print("Find will return -1 if value not found".find("ali"))
print("Index will return value error(substring not found) if string no found".index("ali"))

---------------------------------------------------------------------------------------
4.Count the total number of character in string
Done using len
print(len("We ant to calculate characters here"))

---------------------------------------------------------------------------------------
5.Count the number of specific character in a string
message5 = "Here wwe want to count number of e's "
print(message5.count('e'))

---------------------------------------------------------------------------------------
6.Capitalize the first charcter of string
message6= "this is lowecase and we want to capital its first charcter "
print(message6.capitalize())

---------------------------------------------------------------------------------------
7.Using f string in place of format
name="Ali"
profession="Developer"
print(f"Hello my name is {name} and my profession is {profession} ")

---------------------------------------------------------------------------------------
8. Searchig specific portion of string for substring
message8 = "Hello how are you and i hope everyone will be fine how is it going"
print(message8.index("how",7))
print(message8.find("how",7))

---------------------------------------------------------------------------------------
9. f-string and format. format is less user friendly as variables are passed at the end
name="Ali"
profession="Developer"
print("Hello my name is {} and i am {} by profession".format(name,profession))
print(f"Hello my name is {name} and i am {profession} by profession")

---------------------------------------------------------------------------------------
10.Cheking is string contain all numeric or not
print("12345678".isnumeric())
print("1234   5678".isnumeric()) #space is not count as numeric so will return false
print("123.45678".isnumeric())  #punctuation marks are not count as character

---------------------------------------------------------------------------------------
11. Spliting a string on a specific character
message11="Hello how are you guys"
print(message11.split(" "))

---------------------------------------------------------------------------------------
12 check whether all charcter of string is lowercase or uppercase
message12 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent lobortis, eros dui suscipit erat,"
print(message12.islower())
print("here all lower case letter".islower())
print("HERE ALL UPPERCASE".isupper())

---------------------------------------------------------------------------------------
13. Checkng whether is character is lowecase or not
print("lOWER"[0].islower())

---------------------------------------------------------------------------------------
14.Reverse a string
message14=list("Hello Ali")
message14.reverse()
print(''.join(message14))

---------------------------------------------------------------------------------------
15. Making a string from list separated by hypen
message15 = list("Hello joiya there")
print(message15)
print('-'.join(message15))

---------------------------------------------------------------------------------------
16.Uppercase first and last character of a string
message16 = "hello how are you"
print(message16[0].upper())
print(message16[-1].upper())
print(message16[1:-1])
print(message16[0].upper()+message16[1:-1]+message16[-1].upper())

---------------------------------------------------------------------------------------
17.checking if all string is upper or not
message17 = "HELLO WH"
print(message17.isupper())

---------------------------------------------------------------------------------------
18.using splitlines
message18="1st line\n 2nd line \n 3rd line "
print(message18.splitlines())

---------------------------------------------------------------------------------------
19.Check if a string contains only characters of the alphabet
print("alijoiya".isalpha())
print("1343".isalpha())

---------------------------------------------------------------------------------------
20.Replacing all particular substring with a specific substring
print("PHP is a good language PHP is used for backend".replace("PHP","Python"))

---------------------------------------------------------------------------------------
21.Returning min character is a string i,e character which comes first in alphabetic order
print(min("alifdfdhgd"))

---------------------------------------------------------------------------------------
22.Checking whether string startswith or endswith a specific substring
print("ali joiya".startswith("ali"))
print("rimaan ".endswith(" "))

---------------------------------------------------------------------------------------
23.Encoding a string
print("abli".encode('ascii'))

---------------------------------------------------------------------------------------
24 Checking whether all characters are white spaces or not
print(''.isspace())
print('   '.isspace())
print('   v'.isspace())

---------------------------------------------------------------------------------------
24. Multiplying a string means concatinnatin that string that time
print("message-"*10)

---------------------------------------------------------------------------------------
25. Strings are not mutable
Once a string object has been created, it cannot be changed.
“Modifying” that string creates a whole new object in memory.

message25 = "Hello how are you"
print(id(message25))
message25 = message25 + " ali"
print(id(message25))

---------------------------------------------------------------------------------------
26. if two different strings have same vaalue then
only one memmory location will be assign to that variables
animal = 'Dog'
print(id(animal))
pet = 'Dog'
print(id(pet))

---------------------------------------------------------------------------------------
27
maketrans() creates a mapping from characters to other characters.
translate() then applies that mapping to translate a string.

mapping = str.maketrans('abc','123')
print("abc ukfsd s df ff sd baB".translate(mapping))