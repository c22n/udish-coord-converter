import numpy as np
from typing import List

def calculate_rotation(ref1: List[int],
                       ref2: List[int]):
  theta = (np.arctan2(ref1[1], ref1[0]) -
           np.arctan2(ref2[1], ref2[0]))
  return theta


def rotate_pt(pt: List[int],
              theta: float):
  magnitude = np.linalg.norm(pt)
  alpha = np.arctan2(pt[1],pt[0]) - theta
  new_pt = ([
    magnitude*np.cos(alpha),
    magnitude*np.sin(alpha)
  ])
  return new_pt
