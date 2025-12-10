panels = []
buttons = []
with open('input.txt', 'r') as f:
    lines = [line.strip().split(' ') for line in f.readlines()]
    for line in lines:
        panels.append(line[0].strip('[]'))
        tmp_buttons = []
        for button in line[1:-1]:
            tmp_buttons.append([int(x) for x in button.strip('()').split(',')])
        buttons.append(tmp_buttons)

def find_min_steps(panel, buttons):
    combinations = 2 ** len(buttons)
    target = [1 if c == '#' else 0 for c in panel]
    min_presses = float('inf')
    for to_press in range(combinations):
        lights = [0] * len(target)
        presses = 0

        for button_idx in range(len(buttons)):
            button_is_pressed = (to_press >> button_idx) & 1
            if button_is_pressed:
                presses += 1
                for light_idx in buttons[button_idx]:
                    lights[light_idx] ^= 1

        if lights == target:
            min_presses = min(min_presses, presses)

    return min_presses

sum = 0
for idx, panel in enumerate(panels):
    sum += find_min_steps(panel, buttons[idx])

print(sum)