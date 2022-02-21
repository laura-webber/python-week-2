# 1) word = ‘Hello World’# did you get an error? How would you fix this?
# Hint you can use both double and single quotes in Python as long as you are consistent.

word = 'Hello World'
print(word)

# 2) another word = ', I Love Python'

another_word = ', I Love Python'
print(another_word)

# 3) print(word[0])
print(word[0])

# 4) print(word[1:5])
print(word[1:5])

# 5) print(word[-1]
print(word[-1])

# 6) print(word[-5])
print(word[-5])

# 7) print(word[-5:len(word)])
print(word[-5:len(word)])

# 8)    print(word[-5:]) # ---------- I forgot to show this in the demo, but it will produce the #same result as
# print(word[-5:len(word)]) and it’s more “pythonic”
print(word[-5:])

# 9)    Using a combination of concatenation and string splicing (you learned last week) make the console print the
# word, yellow, from the variables, word and another word, using the lower() string function where appropriate.
first = another_word[10]
# print(first)
mid = word[1:5]
print(mid)
print(first + mid)
last = word[6].lower()
print(first + mid + last)

# 10) Create a new variable called sen using the sentence "The quick brown fox jumped over the lazy dog"
sen = "The quick brown fox jumped over the lazy dog"

# 11) print(sen)
print(sen)

# 12) print(type(sen)) #<---This will print the datatype of the variable, sen, you should get '<class 'str'>' return
# to the console. Use this whenever you are unsure of a variable’s datatype (rather, the object’s datatype to which
# the variable is referring)
print(type(sen))

# 13) Using the new variable, sen, and parse out each word in the sentence and assign them their own variable.
# Example (a = "The", b = "quick", c = "brown", etc.)
a = sen[0:3]
b = sen[4:9]
c = sen[10:15]
d = sen[16:20]
e = sen[20:26]
f = sen[27:32]
g = sen[32:36]
h = sen[36:40]
i = sen[41:45]

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)

# 14) lst1 = [a, b, c, d, e, f, g, h, i]
lst1 = [a, b, c, d, e, f, g, h, i]

# 15) print(lst1)
print(lst1)

# 16) print(type(lst1))
print(type(lst1))

# 17) STRETCH: Now create a second list, lst2, from the sen variable using the String split() function and print it
# to the console. #Hint: it should produce the same result as print(lst1).
lst2 = sen.split(" ")
print(lst2)

# 18) STRETCH: Next create a new variable, sen2, by using the String function, join() on lst2 then print it out. What
# is its type? #Hint: the result should be the same as print(sen).
sen2 = " ".join(lst2)
print(sen2)

# 19) EXTRA STRETCH: Create and assign new variables 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 'i2' by using
# the String split() function on the variable, sen, in one statement (i.e., one line of code) and print it out.

# 20) dict = {"hello": word, "love": another_word}
dict = {
    "hello": word,
    "love": another_word
}

# 21) print(dict)
print(dict)

# 22) e1 = dict["hello"]
e1 = dict["hello"]

# 23) print(e1)
print(e1)

# 24) print(dict["love"])
print(dict["love"])

# 25) STRETCH: Make the console print "Hell or Python" using String slicing and the dictionary you just created, dict.

# 26) dict2 = {'a3': a2, 'b3': b2, 'c3': c2, 'd3': d2, 'e3': e2, 'f3': f2, 'g3': g2, 'h3': h2, 'i3': i2}

# 27) print(dict2)

# 28) print(type(dict2))

# 29) EXTRA, EXTRA STRETCH: Using dict2, combine the values of each key to create one string for new variable, sen3.
