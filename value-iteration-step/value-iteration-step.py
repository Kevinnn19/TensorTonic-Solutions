def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    newval = []
    numst = len(values)
    for s in range(numst) :
        best = float('-inf')
        for a in range(len(transitions[s])) :
            future = 0.0
            for nextst in range(numst) :
                future += transitions[s][a][nextst] * values[nextst]
            q = rewards[s][a] + gamma * future
            best = max(best, q)
        newval.append(float(best))
    return newval