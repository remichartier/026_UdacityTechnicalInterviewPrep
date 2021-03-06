
"""
We're going to take a look at recursion with a famous example—the Fibonacci Sequence.
The Fibonacci Sequence follows one rule: get the next number in the sequence by adding the two previous numbers. Here is an example of the sequence:
0,1,1,2,3,5,8,13,21,34...
Step through each value. You start with 0 and 1. 0 + 1 = 1, so you add 1 to the sequence. 1 + 1 = 2, so 2 is added. 1 + 2 = 3, so 3. 2 + 3 = 5, et cetera.
You could represent these numbers as Python list, and it would look something like this:
fib_seq = []
fib_seq[0] = 0
fib_seq[1] = 1
fib_seq[2] = 1
fib_seq[3] = 2
fib_seq[4] = 3
fib_seq[5] = 5
fib_seq[6] = 8
fib_seq[7] = 13
fib_seq[8] = 21
fib_seq[9] = 34
We can generate this sequence using an iterative method (with loops):
function getFib(position) {
  if (position == 0) { return 0; }
  if (position == 1) { return 1; }
  var first = 0,
      second = 1,
      next = first + second;
  for (var i = 2; i < position; i++) {
    first = second;
    second = next;
    next = first + second;
  }
  return next;
}
In the quiz, you'll be implementing get_fib() in a recursive way.
"""

"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    return -1

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)
