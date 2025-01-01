def diff_color_balls(balls):
    
    count_b = balls.count('B')
    count_r = balls.count('R')
    count_g = balls.count('G')

    return ['B'] * count_b + ['R'] * count_r + ['G'] * count_g



balls = input("enter your balls:")

balls = list(balls.strip()) 

sort_color_balls = diff_color_balls(balls)

print("Separated balls:", sort_color_balls)