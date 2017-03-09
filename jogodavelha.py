initial_state=".......OX"
next_symbol="O"
free_space=7
state_dict={}

print(initial_state)

def ended(state):
    state=list(state)



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

states=generate_next_states(initial_state, next_symbol, free_space)
state_dict[initial_state]=states
print(state_dict)
next_symbol=change_symbol(next_symbol)
for i in range(len(states)):
    generate_next_states(states[i], next_symbol, free_space)

