from professor import Professor
from enrollment import Enroll


class Course:
	def __init__(self, name, code, max_, min_, professor):
		self.name = name
		self.code = code
		self.max = max_
		self.min = min_
		self.professors = []
		self.enrollments = []

		if isinstance(professor, Professor):
			self.professors.append(professor)
		elif isinstance(professor, list):
			for entry in professor:
				if not isinstance(entry, Professor):
					raise TypeError("Invalid professor...")

			self.professors = professor
		else:
			raise TypeError("Invalid professor...")

	def add_professor(self, professor):
		if not isinstance(professor, Professor):
			raise TypeError("Invalid professor...")

		self.professors.append(professor)

	def add_enrollment(self, enroll):
		if not isinstance(enroll, Enroll):
			raise TypeError("Invalid Enroll")

		if len(self.enrollments) == self.max:
			raise TypeError("Cannot enroll, course if full...")

		self.enrollments.append(enroll)

	def is_cancelled(self):
		return len(self.enrollments) < self.min
