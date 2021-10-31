def describe_pet(pet_name, animal_type='dog'):
	"""Display information about a pet"""
	print(f"\nI have an animal {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='willie', animal_type='dog')
describe_pet('july','dog')
describe_pet('jimmy')