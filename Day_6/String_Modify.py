Name = "My name is Anagha"
print(Name.lower())

print(Name.upper())

print(Name.strip())

print(Name.replace("Anagha", "Ubale"))

Sentence = Name.split(",")
print(Sentence)
print(type(Sentence))

#Concatination of string

str1 = "Anagha"
str2 = "Ubale"
result = str1 + str2 
print(result)

space = " "
result = str1 + space + str2
print(result)

#String format method

Name = "My name is Anagha. I am {} years old. I like {}. I am studying in  {}."
print(Name.format(17, "Music", "GPP"))

print(Name.capitalize())

#Boolean
print(bool())
print(bool("is this true"))
print(bool(1234))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(False))
print(bool(None))