```python
class Battery:
	def __init__(self, battery_size=40):
		self.battery_size = battery_size
	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kWh battery.")
		
class ElectricCar(Car):
"""Represent aspects of a car, specific to electric vehic
les."""
	def __init__(self, make, model, year):
	"""
	Initialize attributes of the parent class.
	Then initialize attributes specific to an electric ca
	r.
	"""
		super().__init__(make, model, year)
		self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()

```