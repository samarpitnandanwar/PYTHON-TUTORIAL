name = input("name: ")
date = input("date: ")
letter = '''Dear |name|, 
      You are selected!
      |date|'''

letter = letter.replace("|name|", name)
letter = letter.replace("|date|", date)
print(letter)