import gym
from gym import error, spaces, utils
from gym.utils import seeding

import random
import numpy as np


class HanoiEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    """
    Available Actions
    
    {0 : "(0,1) - top disk of pole 0 to top of pole 1 ",
     1 : "(0,2) - top disk of pole 0 to top of pole 2 ",
     2 : "(1,0) - top disk of pole 1 to top of pole 0",
     3 : "(1,2) - top disk of pole 1 to top of pole 2",
     4 : "(2,0) - top disk of pole 2 to top of pole 0",
     5 : "(2,1) - top disk of pole 2 to top of pole 1"}  
    
    """

    action_list = [(0, 1), (0, 2), (1, 0),
                   (1, 2), (2, 0), (2, 1)]

    disk_index = [0, 1, 2]
    # dictionary that maps the disks to there corresponding state within the
    # state space representation
    disk_dict = {0: disk_index[2],
                 1: disk_index[1],
                 2: disk_index[0]}

    def __init__(self):
        self.disk_num = 3
        self.action_space = spaces.Discrete(6)
        self.observation_space = spaces.Tuple(self.disk_num * (spaces.Discrete(3),))  # state space

        self.state = None  # current state
        self.goal = self.disk_num * (2,)  # goal state
        self.finished = None

    # take next action if move is allowed
    def step(self, action):
        """
        * Inputs:
            - action: integer from 0 to 5
        * Outputs:
            - state: state after transition
            - reward: reward from transition
            - finished: episode state
        1. Transform action (0 to 5 integer) to tuple move
        2. Check if move is allowed
        3. If it is change corresponding entry | If not return same state
        4. Check if episode completed and return
        """

        info = {"invalid_action": False}

        move = self.action_list[action]

        if self.move_allowed(move):
            disks_from = self.disks_on_peg(move[0])
            disk_to_move = self.disk_index[disks_from[-1]] if disks_from else self.disk_index[self.state[-1]]
            next_state = list(self.state)
            next_state[disk_to_move] = move[1]
            self.state = tuple(next_state)
        else:
            info["invalid_action"] = True

        if self.state == self.goal:
            reward = 100
            self.finished = True
        else:
            reward = -1

        return self.state, reward, self.finished

    def disks_on_peg(self, peg):
        """
        * Inputs:
            - peg: pole to check how many/which disks are in it
        * Outputs:
            - list of disk numbers that are allocated on pole
        """
        return [disk for disk in range(self.disk_num) if self.state[disk] == peg]

    def move_allowed(self, move):
        """
        * Inputs:
            - move: tuple of state transition
        * Outputs:
            - boolean indicating whether action is allowed from state!
        move[0] - peg from which we want to move disk
        move[1] - peg we want to move disk to
        Allowed if:
            * disks_to is empty (no disc of peg) set to true
            * Smallest disk on target pole larger than smallest on previous one
        """
        disks_from = self.disks_on_peg(move[0])
        disks_to = self.disks_on_peg(move[1])

        if disks_from:
            return (min(disks_to) > min(disks_from)) if disks_to else True
        else:
            return False

    # reset environment
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
