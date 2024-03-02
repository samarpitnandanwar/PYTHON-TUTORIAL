myDict = {
    "fast" : "In a Quick Manner",
    "harry": "A Coder",
    "marks": [1,2,5],
    "anotherdict": {'harry' : 'Player'}
}

print(list(myDict.keys()))
print(myDict.values())
print(myDict.items())
print(myDict)

updateDict = {
    "Lovich" : "Friend",
    "harry": "A Dancer"
}
myDict.update(updateDict)
print(myDict)