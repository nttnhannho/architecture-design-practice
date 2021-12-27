from address import Address


class Person:
	def __init__(self, first, last, dob, phone):
		self.first_name = first
		self.last_name = last
		self.date_of_birth = dob
		self.phone = phone
		self.addresses = []

	def add_address(self, address):
		if not isinstance(address, Address):
			raise TypeError("Invalid Address...")

		self.addresses.append(address)
