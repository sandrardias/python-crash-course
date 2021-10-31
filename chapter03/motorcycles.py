motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)


motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

motorcycles.insert(0,'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

first_owned = motorcycles.pop(0)
print(f"first owned = {first_owned.title()}")

motorcycles = ['honda', 'yamaha', 'suzuki','ducati'] 
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
