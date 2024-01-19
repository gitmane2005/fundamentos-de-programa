dic = {'left' : (-1,0), 
        'right': (1,0), 
        'down': (0,-1), 
        'up': (0, 1)}
def find_treasure(pos, steps):
    if len(steps) == 1:
        x = pos[0] + (dic[steps[0]])[0]
        y = pos[1] + (dic[steps[0]])[1]
        return (x , y)
    else:
        x_value = pos[0] + find_treasure((0,0), [steps[0]])[0] + find_treasure((0,0), steps[1:])[0]
        y_value = pos[1] + find_treasure((0,0), [steps[0]])[1] + find_treasure((0,0), steps[1:])[1]
        return (x_value, y_value)
