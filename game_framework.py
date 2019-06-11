import time


class GameState:
    def __init__(self, state):
        self.enter = state.enter
        self.exit = state.exit
        self.pause = state.pause
        self.resume = state.resume

running = None
stack = None


def change_state(state):
    global stack
    pop_state()
    stack.append(state)
    state.run()



def push_state(state):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(state)
    state.enter()



def pop_state():
    global stack
    if (len(stack) > 0):
        # execute the current state's exit function
        stack[-1].exit()
        # remove the current state
        stack.pop()

    # execute resume function of the previous state
    if (len(stack) > 0):
        stack[-1].resume()



def quit():
    global running
    running = False


def run(start_state):
    global running, stack
    running = True
    stack = [start_state]
    start_state.enter()
    stack[-1].run()
#    current_time = time.clock()
#    while (running):
#        frame_time = time.clock() - current_time
#        current_time += frame_time
#        stack[-1].handle_events(frame_time)
#        stack[-1].update(frame_time)
#        stack[-1].draw(frame_time)
    # repeatedly delete the top of the stack
    while (len(stack) > 0):
        stack[-1].exit()
        stack.pop()


def reset_time():
    global current_time
    current_time = time.clock()

