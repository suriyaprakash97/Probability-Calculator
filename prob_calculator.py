import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**balls):
    self.hat1 = []
    self.y = 0
    for i in balls:
      ball_count = balls.get(i)
      while self.y<ball_count:
        self.hat1.append(i)
        self.y+=1
        if self.y == ball_count:
          self.y = 0
          break
    self.contents = copy.copy(self.hat1)

  def draw(self,draw_numbers):
    self.contents=copy.copy(self.hat1)
    if draw_numbers >= len(self.contents):
      return (self.hat1)
    else:
      self.result = (random.sample(self.hat1,k=draw_numbers))
      for x in self.result:
        self.contents.remove(x)
      return (self.result)
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  experiment_number = 0
  m = 0
  match = 0
  while experiment_number < num_experiments:
    ex_match = copy.copy(match)
    experiment_number += 1
    result_list = (hat.draw(num_balls_drawn)) 
    result_to_check = {i: result_list.count(i) for i in result_list}
    for k, v in expected_balls.items():
      if k in result_to_check and v <= result_to_check.get(k):
        ex_match += 1
      if ex_match == len(expected_balls):
        m += 1
  return (m / num_experiments)