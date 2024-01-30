# tetris_ai.py
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from tetris_env import TetrisEnv

env = make_vec_env(lambda: TetrisEnv(), n_envs=1)

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)
model.save("tetris_ppo_model")
