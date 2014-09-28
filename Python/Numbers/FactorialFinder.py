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

def factIter(num):
	"""
	Calculates the factorial of a given natural number interactively.

    Keyword arguments:
    num -- the natural number
    """
	
	if num == 0 :
		return 1

	result = 1
	for i in range(1 , num+1):
		result = result * i

	return result

assert factIter(0) == 1
assert factIter(1) == 1
assert factIter(5) == 120
assert factIter(15) == 1307674368000
