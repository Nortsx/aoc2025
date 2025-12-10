import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

joltages = []
buttons = []
with open('input.txt', 'r') as f:
    lines = [line.strip().split(' ') for line in f.readlines()]
    for line in lines:
        joltages.append([int(x) for x in line[-1].strip('{}').split(',')])
        tmp_buttons = []
        for button in line[1:-1]:
            tmp_buttons.append([int(x) for x in button.strip('()').split(',')])
        buttons.append(tmp_buttons)

def solve_joltage_milp(targets, buttons):
    n_counters = len(targets)
    n_buttons = len(buttons)

    A_eq = np.zeros((n_counters, n_buttons))
    for button_idx, button in enumerate(buttons):
        for counter_idx in button:
            if counter_idx < n_counters:
                A_eq[counter_idx][button_idx] = 1


    c = np.ones(n_buttons)

    b_eq = np.array(targets)
    constraints = [LinearConstraint(A_eq, lb=b_eq, ub=b_eq)]

    # Bounds: each button can be pressed 0 or more times
    bounds = Bounds(lb=0, ub=np.inf)

    # Specify that all variables are integers
    integrality = np.ones(n_buttons)  # 1 means integer variable

    # Solve the MILP
    result = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)

    if result.success:
        solution = np.round(result.x).astype(int)
        return int(sum(solution))
    else:
        return None

solution_sum = 0
for i in range(len(joltages)):
    solution_sum += solve_joltage_milp(joltages[i], buttons[i])

print(solution_sum)