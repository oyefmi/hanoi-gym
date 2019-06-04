import gym
import hanoi_gym
from collections import deque

from keras import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD

import numpy as np
import random


class Agent:

    def __init__(self, state_size, action_size):
        self.state_size = 3
        self.action_size = len(action_size)
        self.memory = deque(maxlen=2000)
        self.gamma = 0.8    # discount rate
        self.epsilon = .95  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.2
        self.tau = .075

        self.model = self._neural_net()
        self.target_model = self._neural_net()

    def _neural_net(self):
        model = Sequential()

        model.add(Dense(50, input_dim=1, activation='relu'))
        # model.add(Dense(80, activation='relu'))
        model.add(Dense(100, activation='relu'))
        model.add(Dense(25, activation='relu'))
        model.add(Dense(6, activation = 'linear'))
        model.compile(loss='mse', optimizer=SGD(lr=self.learning_rate))

        return model

    # function to keep track of the previous experiences of the agent at a given state
    def remember(self, state, action, reward, next_state, done):
        nxt = np.array(next_state)
        st = np.array(state)

        self.memory.append((st, action, reward, nxt, done))
    
    # decides how the agent will act based on the epsilon greedy policy
    def act(self, state):
        st = np.array(state)
        if np.random.rand() > self.epsilon:
            # exploit
            q_values = self.model.predict(st)
            return np.argmax(q_values[0])  # returns optimal action
        else:
            # explore
            return random.randrange(6)

    # ideal target based on updated weights
    def target_train(self):
        weights = self.model.get_weights()
        target_weights = self.target_model.get_weights()
        for i in range(len(target_weights)):
            target_weights[i] = weights[i] * self.tau + target_weights[i] * (1 - self.tau)
        self.target_model.set_weights(target_weights)

    def save_model(self, fn):
        self.model.save(fn)

    # takes samples of the agent's experience in order to update Q-values
    def replay(self):
        batch_size = 50
        if len(self.memory) < batch_size:
            return
        samples = random.sample(self.memory, batch_size)
        for sample in samples:
            state, action, reward, new_state, done = sample
            target = self.target_model.predict(state)
            if done:
                target[0][action] = reward
            else:
                q_future = max(
                    self.target_model.predict(new_state)[0])
                target[0][action] = reward + q_future * self.gamma
            self.model.fit(state, target, epochs=1, verbose=0)

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay


if __name__ == "__main__":
        env = gym.make('Hanoi-v0')
        action_size = env.observation_space
        state_size = env.action_space
        dqn_hanoi = Agent(state_size, action_size)
        num_moves = 0
        episodes = 100
        test = 15
        done = False
        training_list = []
        test_list = []

        # train model while iteratively updating q_values
        for t in range(episodes):
            num_moves = 0  # the total number of moves it takes to solve the puzzle
            state = env.reset()
            done = False

            while not done:
                num_moves += 1
                action = dqn_hanoi.act(state)
                next_state, reward, done = env.step(action)
                dqn_hanoi.remember(state, action, reward, next_state, done)
                state = next_state

                # update weights and values after each episode
                if done:
                    print("Number of moves to solve: " + str(num_moves))
                    training_list.append(num_moves)
                    dqn_hanoi.replay()
                    dqn_hanoi.target_train()

                if num_moves > 250:
                    if num_moves % 10 == 0:
                        dqn_hanoi.save_model("Episode-{}.model".format(t))
                else:
                    dqn_hanoi.save_model("success.model")

        training_average = sum(training_list) / episodes
        print("\n" + "Average number of moves for training model " + str(training_average)
              + "\n" + "\n")

        # test model performance
        for t in range(test):
            num_moves = 0  # the total number of moves it takes to solve the puzzle
            state = env.reset()
            done = False

            while not done:
                num_moves += 1
                action = dqn_hanoi.act(state)
                next_state, reward, done = env.step(action)
                dqn_hanoi.remember(state, action, reward, next_state, done)
                state = next_state

            if done:
                print("Number of moves to solve: " + str(num_moves))
                test_list.append(num_moves)

        test_average = sum(test_list) / test
        print("\n" + "Average number of moves for test model " + str(test_average)) 
