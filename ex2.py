# a)

a = 0; b = 1; c = 2
init_state: list[list[int, int, int]] = [
  [3, 1, 2], # a
  [2, 4, 3], # b
  [5, 2, 1]  # c
]

class VectorClockMachine:
  def __init__(self, state: list[list[int, int, int]]):
    self.state = state
    
  def send_message(self, sender: int):
    # increment sender's clock (it is a vector clock, so we increment the sender's own component)
    self.state[sender][sender] += 1
    return self.state[sender]
  
  def receive_message(self, sender_clk: list[int, int, int], receiver: int):
    # pick maximum of each component of the sender's clock and the receiver's clock
    self.state[receiver] = list(max(sender_clk[i], self.state[receiver][i]) for i in range(3))
    # increment the receiver's own component
    self.state[receiver][receiver] += 1
  
  def print_state(self):
    for i, clock in enumerate(self.state):
      print(f"Process {i}: a: {clock[a]}, b: {clock[b]}, c: {clock[c]}")
    print()  # print a newline for better readability

cm = VectorClockMachine(init_state)
cm.print_state() # print initial state

m1 = cm.send_message(sender=b) # b sends message to c
cm.receive_message(sender_clk=m1, receiver=c) # c receives message from b
m2 = cm.send_message(sender=a) # a sends message to c
cm.receive_message(sender_clk=m2, receiver=c) # c receives message from a
m3 = cm.send_message(sender=c) # c sends message to a
cm.receive_message(sender_clk=m3, receiver=a) # a receives message from c

cm.print_state() # print final state

m4 = cm.send_message(sender=b) # b sends message to a
m5 = cm.send_message(sender=c) # c sends message to b
cm.receive_message(sender_clk=m4, receiver=a) # a receives message from b
cm.receive_message(sender_clk=m5, receiver=b) # b receives message from c

cm.print_state() # print final state
