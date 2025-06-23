#Advanced concepts - Strings

message = ' Hello, World!'

#print(message[0])
#print(message[1])

#print(message[-1])

#print(len(message))

print(message.strip()) #Remove leading and trailing whitespace
print(message.lower()) #convert all characters to lower
print(message.split(',')) #split the string into a list based on the comma
print(message.upper()) #convert all characters to upper
print(message.replace("World","Erebus"))