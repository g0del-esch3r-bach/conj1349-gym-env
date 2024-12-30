import gymnasium as gym # type: ignore
from gymnasium.spaces import Box # type: ignore
import numpy as np # type: ignore


class RelativePosition(gym.ObservationWrapper):
    def __init__(self, env):
        super().__init__(env)
        self.observation_space = Box(shape=(2,), low=-np.inf, high=np.inf)

    def observation(self, obs):
        return obs["target"] - obs["agent"]
