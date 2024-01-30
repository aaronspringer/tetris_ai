# tetris_env.py
import time

import gym
from gym import spaces
import numpy as np
import pyautogui
from PIL import ImageGrab


class TetrisEnv(gym.Env):
    def __init__(self):
        super(TetrisEnv, self).__init__()
        self.action_space = spaces.Discrete(4)  # Define your actions here
        self.observation_space = spaces.Box(low=0, high=1, shape=(20, 10, 1), dtype=np.uint8)
        self.top_left = (55, 215)  # Update with actual values
        self.bottom_right = (430, 1009)  # Update with actual values
        self.next_block_pos = (520, 320)  # Update with actual values
        self.board_width = 10
        self.board_height = 20
        self.pieces = {
            29: "J",
            53: "T",
            75: "S",
            76: "Z",
            173: "L",
            179: "I",
            226: "O",
        }

    def seed(self, seed=None):
        pass

    def start_game(self):
        # Click the "Play" or "Start" button
        play_button_x, play_button_y = 69, 1055  # Update with actual coordinates
        pyautogui.click(play_button_x, play_button_y)

        # Add a delay to allow the game to start
        time.sleep(2)

    def reset(self):
        self.start_game()
        return self._get_observation()

    def step(self, action):
        self.perform_action(action)
        observation = self._get_observation()
        reward = 0  # Calculate reward
        done = False  # Determine if the game is over
        return observation, reward, done, {}

    def render(self, mode='human'):
        pass

    def close(self):
        pass

    def _get_observation(self):
        screenshot = ImageGrab.grab().convert('L')
        board, next_block = self.update_board(screenshot)

        # Convert the board and next block to the observation format.
        # This could be a flattened array, one-hot encoding, etc., depending on your model's needs.
        # Here's a simple example where we convert the board to a binary array (empty or not).
        observation = np.zeros((self.board_height, self.board_width, 1), dtype=np.uint8)
        for y in range(self.board_height):
            for x in range(self.board_width):
                if board[y][x] != "_":
                    observation[y, x, 0] = 1

        return observation

    def update_board(self, screenshot):
        total_width = self.bottom_right[0] - self.top_left[0]
        total_height = self.bottom_right[1] - self.top_left[1]
        square_width = round(total_width / (self.board_width - 1))
        square_height = round(total_height / (self.board_height - 1))

        board = [["_" for _ in range(self.board_width)] for _ in range(self.board_height)]

        for y in range(self.board_height):
            for x in range(self.board_width):
                square_x = round(self.top_left[0] + x * square_width)
                square_y = round(self.top_left[1] + y * square_height)
                gray_value = screenshot.getpixel((square_x, square_y))
                piece = self.pieces.get(gray_value, "_")
                board[y][x] = piece

        next_block_gray_value = screenshot.getpixel((self.next_block_pos[0], self.next_block_pos[1]))
        next_block = self.pieces.get(next_block_gray_value, "Unknown")
        print("Next Block:", next_block)
        for row in board:
            print(" ".join(row))
        print("\n")
        return board, next_block

    def perform_action(self, action):
        if action == 0:  # Move left
            pyautogui.press('leftarrow')
        elif action == 1:  # Move right
            pyautogui.press('rightarrow')
        elif action == 2:  # Rotate
            pyautogui.press('uparrow')
        elif action == 3:  # Drop
            pyautogui.press('space')

