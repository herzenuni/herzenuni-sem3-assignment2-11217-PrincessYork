import sort
import pytest
import hypothesis.strategies as st
from hypothesis import given

@given(st.lists(st.integers()))
def test_bsort(lst):
	assert sort.bsort(lst) == sorted(lst)

@given(st.lists(st.integers()))
def test_qsort(lst):
	assert sort.qsort(lst) == sorted(lst)

def test_param_bsort():
	arr = [5,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1]
	assert sort.bsort(arr) == sorted(arr)

def test_param_qsort():
	arr = [5,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1,3,7,9,2,1]
	assert sort.bsort(arr) == sorted(arr)