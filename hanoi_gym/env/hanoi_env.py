import gym
from gym import error, spaces, utils
from gym.utils import seeding

import random
import numpy as np

class HanoiEnv(gym.Env):
  metadata = {'render.modes': ['human']}
  
  action_to_move = [(0, 1), (0, 2), (1, 0),
                  (1, 2), (2, 0), (2, 1)]
  
  def __init__(self):
    self.disk_num = 3
    self.action_space = spaces.Discrete(6)
    self.observation_space = spaces.Tuple(self.disk_num * (spaces.Discrete(3),))
    
    self.state = None
    self.goal = self.disk_num * (2,)
    self.finished = None
    
  def step(self, action):
    move = self.action_to_move[action]
    
    if self.move_allowed(move):
      disk_to_move = min(self.disks_on_peg(move[0]))
      next_state = list(self.state)
      next_state[disk_to_move] = move[1]
      self.state = tuple(next_state)
      
    if self.state == self.goal:
      reward = 100
      self.finished = True
      env.reset()
    else:
      reward = -1
      
    return self.state, reward, self.finished
  
  # method to check which disks, if any, disks are on a given peg
  def disks_on_peg(self, peg):
    return [disk for disk in range (self.disk_num) if self.state[disk] == peg]
  
  #checks if an action is allowed for the given state
  def move_allowed(self, move):
    disks_from = self.disks_on_peg(move[0]) 
    disks_to = self.disks_on_peg(move[1])
    
  def reset(self):
    self.state = self.disk_num * (0,)
    self.finished = False
    return self.state
  
  def set_env_parameters(self, disk_num):
    self.disk_num = disk_num
    self.observation_space = spaces.Tuple(self.disk_num * (spaces.Discrete(3),))
    self.goal = self.disk_num * (2,)
    
  """
  def render(self):
    return
  """
  
