initial_state=".......OX"
next_symbol="O"
free_space=7

print(initial_state)


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
    print(states)
    return states

states=generate_next_states(initial_state, next_symbol, free_space)
next_symbol=change_symbol(next_symbol)
generate_next_states(states[0], next_symbol, free_space)

