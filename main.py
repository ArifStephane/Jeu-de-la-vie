import numpy as np
import os
import time

frame = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])

def compute_number_of_neighbors(paded_frame, index_row, index_column):
    neighborhood = paded_frame[index_row:index_row+3, index_column:index_column+3]
    return np.sum(neighborhood) - paded_frame[index_row+1, index_column+1]

def compute_next_frame(frame):
    paded_frame = np.pad(frame, 1, mode='constant')
    new_frame = np.zeros_like(frame)
    for i in range(frame.shape[0]):
        for j in range(frame.shape[1]):
            neighbors = compute_number_of_neighbors(paded_frame, i, j)
            if frame[i, j] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_frame[i, j] = 1
                else:
                    new_frame[i, j] = 0
            else:
                if neighbors == 3:
                    new_frame[i, j] = 1
                else:
                    new_frame[i, j] = 0
    return new_frame

while True:
    print(frame)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    frame = compute_next_frame(frame)

