"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
  if x <= 1:
    return x
  else:
    ra = foo(x - 1)
    rb = foo(x - 2)
    return ra + rb

def longest_run(mylist, key):
  max_count = 0  # Sets maximum count to 0
  current_count = 0  # Sets current count to 0

  for num in mylist:
    if num == key:
      current_count += 1
      max_count = max(max_count, current_count)  # Update the maximum count
    else:
      current_count = 0  # Reset the current count if/when the sequential key stops

  return max_count


class Result:
    """ done """
    def __init__(self, left, right, longest, entire_range):
        self.left = left               # run on left side of input
        self.right = right            # run on right side of input
        self.longest = longest         # longest run in input
        self.entire_range = entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest, self.left, self.right, self.entire_range))
    
    
def longest_run_recursive(mylist, key):
  if not mylist:
    return 0

  def find_longest(start, end):
    if start == end:
      return 1 if mylist[start] == key else 0

    mid = (start + end) // 2

    left_length = find_longest(start, mid)
    right_length = find_longest(mid + 1, end)

    if mylist[mid] == key and mylist[mid + 1] == key:
      # If there's a run spanning both halves, we add both halves.
      left_run = 0
      right_run = 0

      i = mid
      while i >= start and mylist[i] == key:
        left_run += 1
        i -= 1

      i = mid + 1
      while i <= end and mylist[i] == key:
        right_run += 1
        i += 1

      return max(left_length, right_length, left_run + right_run)

    return max(left_length, right_length)

  return find_longest(0, len(mylist) - 1)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
