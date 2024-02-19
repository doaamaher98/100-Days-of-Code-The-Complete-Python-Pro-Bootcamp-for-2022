
import math

def paint_calc(height, width, cover):
    num_of_cans = float((height * width) / cover)
    return num_of_cans


test_h = int(input("Height of wall :\n"))
test_w = int(input("Width of wall :\n"))
coverage = 5

cans = paint_calc(height=test_h, width=test_w, cover=coverage)

print(f"You'll need : {math.ceil(cans)} cans of paint")