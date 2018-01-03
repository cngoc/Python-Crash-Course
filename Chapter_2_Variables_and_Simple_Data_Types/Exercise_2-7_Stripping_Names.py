print("Store a person\'s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, \"\\t\" and \"\\n\", at least once. \nPrint the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().")

name = " Fluffy "
print("A poem of a name repeating in space.")
print(name + "\n" + name.lstrip() + "\n" + name.rstrip() + name.strip() + "\n\t" + name)
