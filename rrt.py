import numpy as np
from numpy.linalg import norm

class Node(object):
  def __init__(self, point, children=()):
    self.children = list(children)
    self.point = np.array(point)

class Tree(object):
  """ Rapidly-expanding random tree implementation.

  Usage:
   
    >>> import numpy as np
    >>> from rrt import Tree
    >>> tree = Tree((0, 0))
    >>> for i in xrange(100):
    ...   x = np.random.uniform(0, 1, 2)
    ...   x0, x1 = tree.grow(x)
    ...
    >>> for x0, x1 in tree.lines():
    ...   print x0, "connects to", x1
  """

  def __init__(self, x):
    self.nodes = [Node(x)]

  def grow(self, x, ds=None):
    """ Grow the tree toward the given point.

    Parameters:
      x -- (float) the point to grow toward
      ds -- (float or None) the maximum step to take

    Returns 2-tuple of (parent point, child point) for the new point added.
    """
    nn = min(self.nodes, key=lambda n: norm(n.point-x, 2))
    u = x - nn.point
    step = ds if ds is not None else norm(u, 2)
    u = u / norm(u, 2)
    xp = nn.point + u * step
    node = Node(xp)
    nn.children.append(node)
    self.nodes.append(node)
    return nn.point, xp

  def lines(self):
    """ Returns 2-tuple of (parent point, child point) in arbitrary order.
    """
    for parent in self.nodes:
      for child in parent.children:
        yield parent.point, child.point
