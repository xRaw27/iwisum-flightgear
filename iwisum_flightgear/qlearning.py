import math
import numpy as np
from iwisum_flightgear.config import OBSERVATION_SPACE, ACTION_SPACE

import jsbgym
import gymnasium as gym


class QLearner:
    def __init__(self, buckets_number=5, epsilon=0.1, alpha=0.1, gamma=0.99):
        self.environment = gym.make('C172-HeadingControlTask-Shaping.STANDARD-FG-v0', render_mode='flightgear')

        self.attempt_no = 1
        self.lower_bounds = [low for _, _, low, _ in OBSERVATION_SPACE]
        self.upper_bounds = [high for _, _, _, high in OBSERVATION_SPACE]
        self.buckets_number = tuple([buckets_number for _ in range(len(OBSERVATION_SPACE))])
        self.buckets = [
            np.linspace(
                self.lower_bounds[i], self.upper_bounds[i], self.buckets_number[i] + 1
            )[1:-1]
            for i in range(len(self.buckets_number))
        ]
        self.q_table = np.zeros(self.buckets_number + (len(ACTION_SPACE),))

        self.epsilon = epsilon  # Exploration rate
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor

    def learn(self, max_attempts):
        for _ in range(max_attempts):
            reward_sum = self.attempt()
            print(reward_sum)

    def attempt(self):
        observation, _ = self.environment.reset()
        observation = self.discretise(observation)
        done = False
        reward_sum = 0.0
        while not done:
            self.environment.render()
            action = self.pick_action(observation)
            new_observation, reward, done, truncated, info = self.environment.step(action)
            new_observation = self.discretise(new_observation)
            self.update_knowledge(action, observation, new_observation, reward)
            observation = new_observation
            reward_sum += reward
        self.attempt_no += 1
        return reward_sum

    def discretise(self, observation):
        assert len(observation) == len(self.buckets)
        return tuple(
            np.digitize(observation[i], self.buckets[i]) for i in range(len(observation))
        )

    def pick_action(self, observation):
        # if np.random.uniform(0, 1) < self.epsilon:
        return self.environment.action_space.sample()  # Explore
        # else:
        #     return np.argmax(self.q_table[observation])  # Exploit

    def update_knowledge(self, action, observation, new_observation, reward):
        pass
        # best_next_action = np.argmax(self.q_table[new_observation])
        # learned_value = (
        #         reward + self.gamma * self.q_table[new_observation][best_next_action]
        # )
        # old_value = self.q_table[observation][action]
        # self.q_table[observation][action] = (
        #         (1 - self.alpha) * old_value + self.alpha * learned_value
        # )
