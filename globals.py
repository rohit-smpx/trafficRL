def init():
    global N, E, alpha, gamma, age, pre, preAction, numActions
    N = 6
    E = 0.05
    gamma = 0.8
    age = 0
    numActions = 1
    pre = 6*[0]
    preAction = 0
    alpha = 0.5