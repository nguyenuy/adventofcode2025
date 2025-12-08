from dataclasses import dataclass
from functools import reduce
import re
from typing import Dict, Literal, Match, Optional, Tuple

from util.advent_reader import read_problem_file


def get_new_position(current_index, steps, list_length):
    new_index = (current_index + steps) % list_length
    return new_index

def count_crossings(current_index, steps, list_length):
    absolute_index = current_index + steps
    if steps > 0:
        if (absolute_index % list_length) == 0:
            crossings = absolute_index // list_length - 1
        else:
           crossings = absolute_index // list_length   
    else:
        crossings = abs(steps) // list_length
        remainder = abs(steps) % list_length
        if ((current_index - remainder) < 0) & (current_index != 0):
            crossings += 1
    
    return crossings

def run_problem_one(prob_input: list[str]) -> int:
    dial_position = 50
    dial_numbers = list(range(100))
    password = 0

    for i in prob_input:
        direction = i[0]
        num_rotations = int(i[1:])
        if direction == 'L':
            num_rotations = num_rotations*-1

        dial_position = get_new_position(dial_position, num_rotations, len(dial_numbers))
        if dial_position == 0:
            password = password + 1

    return password

def run_problem_two(prob_input: list[str]) -> int:
    dial_position = 50
    dial_numbers = list(range(100))
    password = 0

    for i in prob_input:
        direction = i[0]
        num_rotations = int(i[1:])
        if direction == 'L':
            num_rotations = num_rotations*-1
        
        password = password + count_crossings(dial_position, num_rotations, len(dial_numbers))
        dial_position = get_new_position(dial_position, num_rotations, len(dial_numbers))
        if dial_position == 0:
            password = password + 1
        
    
    return password

if __name__ == "__main__":
    day = '01'
    test_input = read_problem_file('day/day01-part01-example.txt')
    print(run_problem_one(test_input))

    prob_01_input = read_problem_file('day/day01-part01-input.txt')
    print(run_problem_one(prob_01_input))

    testcase = read_problem_file('day/day01-part01-testcase.txt')
    print(run_problem_two(test_input))
    print(run_problem_two(prob_01_input))
    
