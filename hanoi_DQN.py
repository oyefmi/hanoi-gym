import gym
import hanoi_gym
from collections import deque

from keras import Sequential
from keras.layers.core import Dense
from keras.optimizers import Adam

import numpy as np
from numpy import array
import random


class Agent:

    def __init__(self, state_size, action_size):
        self.state_size = 3
        self.action_size = len(action_size)
        self.memory = deque(maxlen=2000)
        self.gamma = 0.5    # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.1
        self.model = self._neural_net()

    def _neural_net(self):
        model = Sequential()

        model.add(Dense(27, input_dim = 1, activation = 'relu'))
        model.add(Dense(27, activation = 'relu'))
        model.add(Dense(6, activation = 'linear'))
        model.compile(loss = 'mse', optimizer = Adam(lr = self.learning_rate))

        return model

    # function to keep track of the previous experiences of the agent at a given state
    def remember(self, state, action, reward, next_state, done):
        nxt = array(next_state)
        st = array(state)
        nxt_st = nxt.T
        curr_st = st.T
        self.memory.append((curr_st, action, reward, nxt_st, done))
    
    # decides how the agent will act based on the epsilon greedy policy
    def act(self, state):
        st = array(state)
        curr_st = st.T
        if np.random.rand() < self.epsilon:
            # explore
            return random.randrange(6)
        else:
            # exploit
            act_values = self.model.predict(curr_st)
            return np.argmax(act_values[0])  # returns action
    
    # takes samples to train the neural net based on past experiences
    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)

        for curr_st, action, reward, nxt_st, done in minibatch:
            target = reward

            if not done:
                target = (reward + self.gamma *
                          max(self.model.predict(nxt_st)[0]))
                target_f = self.model.predict(curr_st)
                target_f[0][action] = target
                self.model.fit(curr_st, target_f, epochs=1, verbose=0)

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay


if __name__ == "__main__":
        env = gym.make('Hanoi-v0')
        action_size = env.observation_space
        state_size = env.action_space
        dqn_hanoi = Agent(state_size, action_size)
        num_moves = 0 
        batch_size = 30
        episodes = 500
        test = 25
        num_moves = 0 # the total number of moves it takes to solve the puzzle
        done = False

        # train model
        for t in range(episodes):
            state = env.reset()
            num_moves += 1
            action = dqn_hanoi.act(state)
            next_state, reward, done = env.step(action)
            dqn_hanoi.remember(state, action, reward, next_state, done)
            state = next_state

            if done:
                print("Number of moves to solve: " + str(num_moves))

        # test of model
        for i in range(25):

            dqn_hanoi.replay(batch_size)
