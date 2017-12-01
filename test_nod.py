import pytest
import nod

def factory(a, b, c):
	def abstract_test():
		assert nod.nod(a, b) == c
	return abstract_test


test_1 = factory(123, 12, 3)
test_2 = factory(10, 5, 5)
test_3 = factory(0, 5, 1)
test_4 = factory(5, 0, 1)