from person import Person
from enrollment import Enroll


class Student(Person):
	def __init__(self, first, last, dob, phone, international=False):
		super().__init__(first, last, dob, phone)
		self.international = international
		self.enrollments = []

	def add_enrollment(self, enroll):
		if not isinstance(enroll, Enroll):
			raise TypeError("Invalid Enroll...")

		self.enrollments.append(enroll)

	def is_on_probation(self):
		return self

	def is_part_time(self):
		return len(self.enrollments) <= 3
