```python
class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()
	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles onit.")
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
			
# this is just the regular class created behold !!! below are what is really dose

class ElectricCar(Car):

	def __init__(self, make, model, year):
	# so yes you need the super__inti__() stuff to make it work 
		super().__init__(make, model, year)
		self.battery_size = 40
		# yes the attribute will be associated with the child class only 
		
	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kWh battery.")
		
	# and yes the child could fuck the dead what I mean is overriding the parent attributes and create one of its own
	def fill_gas_tank(self):
		print('The electric car has no gas tank')
	# for example lets say there is an attribute for gas_tank in parent but in child you coudl override it 
		
my_leaf = ElectricCar('nissan', 'leaf', 2024)		
print(my_leaf.get_descriptive_name())

```