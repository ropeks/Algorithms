#!/usr/bin/python

import sys

'''
1. Understand the problem:
  possible answers: r / p / s
  given the number n create list of lists with length of n
  that contain all possible permutations of possible answers

'''

r = 'rock'
p = 'paper'
s = 'scissors'

def rock_paper_scissors(n):
  possible_sols = [[r], [p], [s]]
  combinations = []
  if n <= 0:
        combinations.append([])
        return combinations
  if n == 1:
        combinations.extend(possible_sols)
        return combinations
  if n > 1:
        rec = rock_paper_scissors(n-1)
        for round in rec:
              for sol in possible_sols:
                    new_round = round + sol
                    combinations.append(new_round)
        return combinations


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')