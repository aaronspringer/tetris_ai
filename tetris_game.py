# tetris_game.py
import pyautogui
from PIL import ImageGrab
import time
from stable_baselines3 import PPO
from tetris_env import TetrisEnv

def main():
    model = PPO.load("tetris_ppo_model")
    env = TetrisEnv()

    while True:
        observation = env.reset()
        done = False
        while not done:
            action, _ = model.predict(observation, deterministic=True)
            observation, _, done, _ = env.step(action)
            env.render()
        time.sleep(0.1)

if __name__ == '__main__':
    main()
