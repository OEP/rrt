#!/usr/bin/env python
""" Example script for RRT generation.

Invoke this script with an output file to write a randomly-generated RRT rooted
at (0,0) in the space [(0,0), (1,1)].

Examples:

  $> python growvis.py rrt.png
  $> python growvis.py -i 1000 -s 0.01 rrt-smallstep.png
"""

from rrt import Node, Tree
import numpy as np
from argparse import ArgumentParser
import matplotlib.pyplot as plt

def main():
  p = ArgumentParser()
  p.add_argument('output', type=str, help='output file')
  p.add_argument('--step', '-s', type=float, default=None,
                 help='maximum step size per iteration')
  p.add_argument('--iterations', '-i', type=int, default=100,
                 help='number of iterations')

  args = p.parse_args()
  tree = Tree((0,0))

  for i in xrange(args.iterations):
    x = np.random.uniform(0, 1, 2)
    tree.grow(x, args.step)

  for x0, x1 in tree.lines():
    plt.plot([x0[0], x1[0]], [x0[1], x1[1]], 'k-')

  plt.savefig(args.output, dpi=96)

if __name__ == "__main__":
  main()
