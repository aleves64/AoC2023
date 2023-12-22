import os
from collections import deque
from math import lcm
from functools import reduce

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

class Module:
    def __init__(self, name, op):
        self.name = name
        self.op = op
        self.inputs = []
        self.outputs = []

    def initialize_state(self):
        if self.op == '&':
            self.state = [0]*len(self.inputs)
        else:
            self.state = 0

    def receive_input(self, src, val):
        if self.op == '&':
            src = self.inputs.index(src)
            self.state[src] = val
            if sum(self.state) == len(self.state):
                out_val = 0
            else:
                out_val = 1
            pulse_queue.append((self.name, out_val))
        elif self.op == '%':
            prev = self.state
            self.state = (self.state^val)^1
            if self.state != prev:
                pulse_queue.append((self.name, self.state))
        else:
            self.state = val
            pulse_queue.append((self.name, 0))

modules = {}
for line in myinput:
    name, destinations = line.split(" -> ")
    if name == "broadcaster":
        module = Module(name, "")
    else:
        op = name[0]
        name = name[1:]
        module = Module(name, op)
    module.outputs = destinations.split(", ")
    modules[name] = module
for name in modules:
    module = modules[name]
    for dest in module.outputs:
        if dest in modules:
            modules[dest].inputs.append(name)
        elif dest == "rx":
            rx_source = module
for name in modules:
    modules[name].initialize_state()

pulse_queue = deque()
def handle_pulse(cnt):
    src, val = pulse_queue.popleft()
    dsts = modules[src].outputs
    for dst in dsts:
        cnt[val] += 1
        if dst in modules:
            modules[dst].receive_input(src, val)
        for j in range(len(rx_source.state)):
            if rx_source.state[j] == 1 and cycle_lengths[j] == 0:
                cycle_lengths[j] = i

def push_button():
    bc = modules["broadcaster"]
    bc.receive_input("button", 0)
    cnt = [1,0]
    while pulse_queue:
        handle_pulse(cnt)
    return cnt

cycle_lengths = [0]*len(rx_source.state)
i = 0
while True:
    i += 1
    low_pulses, high_pulses = push_button()
    if not 0 in cycle_lengths:
        total = reduce(lcm, cycle_lengths)
        break
print(total)
