initial_state=".......OX"
next_symbol="O"
free_space=7
state_dict={}

# 0 1 2 
# 3 4 5
# 6 7 8

# print(initial_state)

def ended(state):
    empty_square=state.find(".")
    if (empty_square == -1):
        return True
    state=list(state)
    # check rows
    if (state[0] != '.' and state[1] != '.' and state[2] != '.'):
        if (state[0] == state[1] and state[0]== state[2]):
            return True
    if (state[3] != '.' and state[4] != '.' and state[5] != '.'):
        if (state[3] == state[4] and state[3]== state[5]):
            return True
    if (state[6] != '.' and state[7] != '.' and state[8] != '.'):
        if (state[6] == state[7] and state[6]== state[8]):
            return True

    # check columns
    if (state[0] != '.' and state[3] != '.' and state[6] != '.'):
        if (state[0] == state[3] and state[0]== state[6]):
            return True
    if (state[1] != '.' and state[4] != '.' and state[7] != '.'):
        if (state[1] == state[4] and state[1]== state[7]):
            return True
    if (state[2] != '.' and state[5] != '.' and state[8] != '.'):
        if (state[2] == state[5] and state[2]== state[8]):
            return True

    # check diagonals
    if (state[0] != '.' and state[4] != '.' and state[8] != '.'):
        if (state[0] == state[4] and state[4]== state[8]):
            return True
    if (state[2] != '.' and state[4] != '.' and state[6] != '.'):
        if (state[2] == state[4] and state[4]== state[6]):
            return True
    return False

def change_symbol(symbol):
    if (symbol == "O"):
        symbol = "X"
    elif (symbol == "X"):
        symbol = "O"
    return symbol

def generate_next_states(state, next_symbol, free_space):
    states = []
    state=list(state)
    for j in range(free_space):
        new_state=state[:]
        char = state[j]
        if (char == "."):
            new_state[j]=next_symbol
            new_state=''.join(new_state)
            states.append(new_state)
    return states

def play(state_dict, state, next_symbol, free_space):
    new_states=generate_next_states(state, next_symbol, free_space)
    if (state in state_dict.keys()):
        state_dict[state]+=new_states
        state_dict[state]=list(set(state_dict[state]))
    else:
        state_dict[state]=new_states
    next_symbol=change_symbol(next_symbol)
    for each in new_states:
        if (not (ended(each))):
            play(state_dict, each, next_symbol, free_space)


def print_dict(state_dict):
    for key, states in state_dict.iteritems():
        print(key, states)

def print_dot(state_dict):
    print("digraph {")
    for key, states in state_dict.iteritems():
        for each in states:
            print '"' + key + '"' + " -> " + '"'  + each + '"'
    print("}")
# 
# if (ended(initial_state)):
#     print("Algorithm is just wrong!")
# states=generate_next_states(initial_state, next_symbol, free_space)
# state_dict[initial_state]=states
# print(state_dict)
# next_symbol=change_symbol(next_symbol)
# for i in range(len(states)):
#     if (ended(states[i])):
#         print("Algorithm is just wrong!")
#     generate_next_states(states[i], next_symbol, free_space)
play(state_dict, initial_state, next_symbol, free_space)
# print(state_dict)
# print_dict(state_dict)
print_dot(state_dict)
