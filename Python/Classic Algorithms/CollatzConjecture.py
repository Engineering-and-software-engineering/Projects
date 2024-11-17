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

def collatzIterative(n):
    assert n>1
    num_steps = 0
    while n!=1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        num_steps = num_steps + 1
    return num_steps

def collatzRecursively(n,num_steps=0):
    if n==1:
        return num_steps
    else:
        if n%2==0:
            return collatzRecursively(n/2,num_steps+1)
        else:
            return collatzRecursively((3*n)+1,num_steps+1)            

assert collatzIterative(6) == 8
assert collatzIterative(27) == 111
assert collatzIterative(6) == collatzRecursively(6)
assert collatzIterative(27) == collatzRecursively(27)
