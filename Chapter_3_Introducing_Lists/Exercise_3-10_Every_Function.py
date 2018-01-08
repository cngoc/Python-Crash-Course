print("Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you'd like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.\n")

teton_trail_passes = ['mount meek pass', 'hurricane pass', 'paintbrush divide', 'fox creek pass']

#functions instroduced in the chapter, sorted(), and len()

#sorted() stores the alphabetical sort temporarily, it can be more complicated when all the values are not in lowercase.
print("The array temporarily sorted " sorted(teton_trail_passes))

#len() returns the length of an array
print("The length of an array "len(teton_trail_passes))
