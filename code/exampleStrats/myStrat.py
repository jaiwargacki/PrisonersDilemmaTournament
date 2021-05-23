__author__ = "Jai Wargacki"


def strategy(history, memory):
    length = history.shape[1]

    if length == 1:
        return 0, None
    elif length < 3:
        return 1, [0, 1]
    elif length == 3:
        for i in range(0, 3):
            if history[1][i] == 1:
                break
            elif i == 2:
                return 0, [3, 1]

    if memory[0] == 3:
        memory[1] += 1
        return 0, memory

    last = history[1][-1]
    if memory[0] == 0:
        if last == 1:
            memory[1] += 1
            return 0, memory
        return 1, [1, 1]
    elif memory[0] == 1:
        if memory[1] == 1:
            memory[1] += 1
            return 1, memory
        if last == 1:
            memory = [2, 1]
            return 1, memory
        memory = [3, 1]
        return 0, memory
    memory[1] += 1
    if (memory[1] > 5 and last == 0) or memory[0] != 2:
        memory = [0, 1]
    return 1, memory
