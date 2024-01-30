# import pyautogui
# from PIL import ImageGrab
# import time
#
#
# def get_position(prompt):
#     print(prompt)
#     input("Press Enter after moving the cursor to the desired position...")
#     return pyautogui.position()
#
#
# def update_board(screenshot, top_left, bottom_right, next_block_pos, board_width, board_height):
#     total_width = bottom_right[0] - top_left[0]
#     total_height = bottom_right[1] - top_left[1]
#     square_width = round(total_width / (board_width - 1))
#     square_height = round(total_height / (board_height - 1))
#
#     board = [["_" for _ in range(board_width)] for _ in range(board_height)]
#
#     for y in range(board_height):
#         for x in range(board_width):
#             square_x = round(top_left[0] + x * square_width)
#             square_y = round(top_left[1] + y * square_height)
#             gray_value = screenshot.getpixel((square_x, square_y))
#             piece = pieces.get(gray_value, "_")
#             board[y][x] = piece
#
#     # Get next block
#     next_block_gray_value = screenshot.getpixel((next_block_pos[0], next_block_pos[1]))
#     next_block = pieces.get(next_block_gray_value, "Unknown")
#
#     return board, next_block
#
#
# def print_board(board, next_block):
#     print("Next Block:", next_block)
#     for row in board:
#         print(" ".join(row))
#     print("\n")
#
#
# def press_space_every_half_second(start_time):
#     if time.time() - start_time >= 0.5:
#         pyautogui.press(' ')
#         return time.time()
#     return start_time
#
#
# if __name__ == '__main__':
#     pieces = {
#         29: "J",
#         53: "T",
#         75: "S",
#         76: "Z",
#         173: "L",
#         179: "I",
#         226: "O",
#     }
#
#     top_left = get_position("Move to the top-left corner of the Tetris grid")
#     bottom_right = get_position("Move to the bottom-right corner of the Tetris grid")
#     next_block_pos = get_position("Move to the position where the next block is displayed")
#     board_width, board_height = 10, 20  # Adjust based on the game
#
#     last_space_press_time = time.time()
#     while True:
#         screenshot = ImageGrab.grab().convert('L')
#         board, next_block = update_board(screenshot, top_left, bottom_right, next_block_pos, board_width, board_height)
#
#         print_board(board, next_block)
#         last_space_press_time = press_space_every_half_second(last_space_press_time)
#         time.sleep(0.1)
