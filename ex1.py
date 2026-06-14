# a)

a = 0; b = 1; c = 2
init_state = [1,4,3] # a,b,c

class ClockMachine:
  def __init__(self, state: list[int]):
    self.state = state
    
  def send_message(self, sender: int):
    # increment sender's clock
    self.state[sender] += 1
    return self.state[sender]
  
  def receive_message(self, sender_clk: int, receiver: int):
    # update receiver's clock
    self.state[receiver] = max(sender_clk, self.state[receiver]) + 1
  
  def print_state(self):
    print(f"a: {self.state[a]}, b: {self.state[b]}, c: {self.state[c]}")

cm = ClockMachine(init_state)
m1 = cm.send_message(sender=b) # b sends message to a
m2 = cm.send_message(sender=b) # b sends message to a again
cm.receive_message(sender_clk=m1, receiver=a) # a receives message from b
m3 = cm.send_message(sender=a) # a sends message to c
cm.receive_message(sender_clk=m3, receiver=c) # c receives message from a
cm.receive_message(sender_clk=m2, receiver=a) # a receives message from b again

cm.print_state() # print final state

m4 = cm.send_message(sender=a) # a sends message to b
m5 = cm.send_message(sender=c) # c sends message to b
cm.receive_message(sender_clk=m4, receiver=b) # b receives message from a
cm.receive_message(sender_clk=m5, receiver=b) # b receives message from c

cm.print_state() # print final state

