import gym
import numpy as np
import random
import pygame

env = gym.make('CartPole-v1', render_mode = 'human')   #simple environment: only 2 actions: left or right

episodes = 10
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0

    while not done:

        action = random.choice([0,1])
        n_state, reward, done, info = env.step(action)
        #_, reward, done,_ = env.step(action) # _ is the next state, reward is the reward for the action, done is a boolean to indicate if the episode is done, env.step(action) is the action to be taken
        score += reward
        env.render()
    print('Episode:{} Score:{}'.format(episode, score))

env.close()