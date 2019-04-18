import numpy as np
from typing import List

def calculate_rotation(ref1: List[float],
                       ref2: List[float]) -> float:
  theta = (np.arctan2(ref1[1], ref1[0]) -
           np.arctan2(ref2[1], ref2[0]))
  print('The dish has been rotated %.3f degrees' %
        np.rad2deg(theta))
  return theta


def rotate_pt(pt: List[float],
              theta: float) -> List[float]:
  magnitude = np.linalg.norm(pt)
  alpha = np.arctan2(pt[1],pt[0]) - theta
  new_pt = ([
    magnitude*np.cos(alpha),
    magnitude*np.sin(alpha)
  ])
  return new_pt

def transform_coords(locs: List[List[float]],
                     theta: float) -> List[List[float]]:
  locs1 = np.array(locs)
  locs2 = np.zeros(locs1.shape)
  for i, pt in enumerate(locs1):
    locs2[i,:] = rotate_pt(pt, theta)
  print('The transformed coordinates are:')
  print(locs2)
  return locs2
