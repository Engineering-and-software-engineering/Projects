##This program is free software: you can redistribute it and/or modify
##it under the terms of the GNU General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##This program is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU General Public License for more details.
##
##You should have received a copy of the GNU General Public License
##along with this program.  If not, see <http://www.gnu.org/licenses/>.

def merge_sort(array):
	def split_list(list):
		half = len(list)/2
		return list[:half],list[half:]

	def merge_lists(array_1,array_2):
		if len(array_1) == 0:
			return array_2
		elif len(array_2) == 0:
			return array_1
		else:
			if array_1[0] < array_2[0]:
				return [array_1[0]] + merge_lists(array_1[1:],array_2)
			else:
				return [array_2[0]] + merge_lists(array_1,array_2[1:])

	assert(isinstance(array,list))
	if len(array) <= 1:
		return array
	else:
		array_1,array_2 = split_list(array)
		return merge_lists(merge_sort(array_1),merge_sort(array_2))

def bubble_sort(array):
	def swap(array,pos_1,pos_2):
		array[pos_1],array[pos_2] = array[pos_2],array[pos_1]

	assert(isinstance(array,list))
	swaped = True
	while swaped:
		swaped = False
		for i in xrange(len(array)-1):
			if array [i] > array[i+1]:
				swaped = True
				swap(array,i,i+1)
	return array

assert merge_sort([1,2,3]) == [1,2,3]
assert merge_sort([1]) == [1]
assert merge_sort([]) == []
assert merge_sort([5,4,3,2,1,0]) == [0,1,2,3,4,5]
assert merge_sort(["a","zs","bt"]) == ["a","bt","zs"]

assert bubble_sort([1,2,3]) == [1,2,3]
assert bubble_sort([1]) == [1]
assert bubble_sort([]) == []
assert bubble_sort([5,4,3,2,1,0]) == [0,1,2,3,4,5]
assert bubble_sort(["a","zs","bt"]) == ["a","bt","zs"]