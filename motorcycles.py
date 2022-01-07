#modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[-1] = 'hyundai'
print(motorcycles)

# adding elements in a list - quickest way: appending elements to the last position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
# exercise
players = []
players.append('Cristiano Ronaldo')
players.append('Lionel Messi')
players.append('Neymar Junior')
players.append('Bruno Fernandes')
print(players)

#Inserting elements in a list - is adding an element in any position
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# removing elements using the del statement - use this when you know the position of an item
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

# removing elements through pop method
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
# this popped_motorcycle shows us that we still have access to the eliminated element
print(popped_motorcycle)
print(f"I don't like {popped_motorcycle}, at all")

# removing elements at any position using pop method
motorcycles = ['honda', 'yamaha', 'suzuki']
popped = motorcycles.pop(0)
print(motorcycles)

# remove items using remove method
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('honda')
print(motorcycles)


