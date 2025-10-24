import numpy as np
import os
import time

frame = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

def add_padding(frame):
    size = len(frame)
    padded = [[0] * (size + 2) for _ in range(size + 2)]
    for i in range(size):
        for j in range(size):
            padded[i+1][j+1] = frame[i][j]
    return padded

def count_neighbors(padded, i, j):
    count = 0
    for x in range(i, i+3):
        for y in range(j, j+3):
            if x != i+1 or y != j+1:
                count += padded[x][y]
    return count

def next_generation(frame):
    padded = add_padding(frame)
    size = len(frame)
    new_frame = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            neighbors = count_neighbors(padded, i, j)
            if frame[i][j] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_frame[i][j] = 1
                else:
                    new_frame[i][j] = 0
            else:
                if neighbors == 3:
                    new_frame[i][j] = 1
                else:
                    new_frame[i][j] = 0
    return new_frame

while True:
    for row in frame:
        print(' '.join(str(cell) for cell in row))
    print()
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    frame = next_generation(frame)
