#Ex1: Simple Math
print(2 + 2)

#Ex2: Expressions
print(2)

#Ex3: Order of Operations
print(2 + 3 * 6)
print((2 + 3) * 6)
print(48565878 * 578453)
print(2 ** 8)
print(23 / 7)
print(23 // 7)
print(23 % 7)
print(2    +           2)
print((5 - 1) * ((7 + 1) / (3 - 1)))
#Evaluates to one decimal place after calculating "(8/2)" -> "4.0"

#Table 1-2: Common Data Types
print('Integers:',-2,-1,0,1,2,3,4,5)
print('Floating-point numbers:',-1.25,-1.0,--0.5,0.0,0.5,1.0,1.25)
print('a','aa','aaa','Hello!','11 cats')

#Ex5: String Concatenation and Replication
print('Alice' + 'Bob')
print('Alice' * 5)

#Ex6: Variables
spam = 42
print('The variable spam now has the integer value',spam,'in it.')
spam = 40
print(spam)
eggs = 2
print(spam + eggs + spam)
spam = spam + 2
print(spam)

#Ex7: Overwriting the Variable
spam = 'Hello'
print(spam)
spam = 'Goodbye'
print(spam)

#Ex8: First Program

# This program says hello and asks for my name.
print('Hello world!')
print('What is your name?')	# ask for their name
myName = input()
print('It is good to meet you, ' + myName + '.')
print('The length of your name is:')
print(len(myName))
print('What is your age?')	# ask for their name
myAge = input()
print(myName + ', you will be ' + str(int(myAge) + 1) + ' in a year.')