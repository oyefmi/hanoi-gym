import gym
import hanoi_gym
from collections import deque

import keras
from keras import Sequential
from keras.layers.core import Dense
from keras.optimizers import Adam

import numpy as np
import random


class Agent:

    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.5    # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.1
        self.model = self.neural_net

    def neural_net(self):
        model = Sequential()

        model.add(Dense(27, input_dim = self.state_size, activation = 'relu'))
        model.add(Dense(27, activation = 'relu'))
        model.add(Dense(self.action_size, activation = 'linear'))
        model.compile(loss = 'mse', optimizer = Adam(learn = self.learning_rate))
    
    # function to keep track of the previous experiences of the agent at a given state
    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))
    
    # decides how the agent will act based on the epsilon greedy policy
    def act(self, state):
        if np.random.rand() < self.epsilon:
            return random.randrange(len(self.action_size))

        act_values = self.model.predict(state)

        return np.argmax(act_values[0])  # returns action
    
    # takes samples to train the neural net based on past experiences
    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)

        for state, action, reward, next_state, done in minibatch:
            target = reward

        if not done:
            target = (reward + self.gamma *
                      np.amax(self.model.predict(next_state)[0]))
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)

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
        num_moves = 0 #the total number of moves it takes to solve the puzzle
        done = False

    #for i in range(episodes):
        num_moves += 1
        state = env.reset()
        while not done:
            action = dqn_hanoi.act(state)
            next_state, reward, done = env.step(action)
            dqn_hanoi.remember(state, action, reward, next_state, done)
            state = next_state

        print("Number of moves to solve: " + num_moves)

        if len(dqn_agent.memory) > batch_size:
            dqn_hanoi.replay(batch_size)
