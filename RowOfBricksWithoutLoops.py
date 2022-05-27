#This a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each).
#Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops.

def make_bricks(small, big, goal):
  div5 = goal // 5
  if div5 > big :
    remain = goal - big*5
    div1 = remain // 1
    if div1 <= small :
      return True
    return False
  else :
    remain = goal - div5*5
    div1 = remain // 1
    return (div1 <= small)

print(make_bricks(2, 1000000, 100003))
print(make_bricks(1000000, 1000, 1000100))
print(make_bricks(0, 2, 10))
print(make_bricks(3, 2, 10))

