import pyautogui
import threading
import keyboard
import os

from directions import DirectionsEnum

def _exit_listener():
    """
    При нажатии кнопки Ecsape программа завершается
    """
    keyboard.wait("esc")
    os._exit(1)


def start_mouse_walk(collisions: int = 5):
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 0

    screen_size = pyautogui.size()
    current_direction = DirectionsEnum.right_bottom

    step = 60
    duration = 0.2
    border_indent = 10  # Отступ от границ экрана
    for _ in range(0, collisions):
        while True:
            pos = pyautogui.position()

            # Вправо вниз
            if (current_direction == DirectionsEnum.right_bottom):
                if (pos.x >= screen_size.width - border_indent):
                    current_direction = DirectionsEnum.left_bottom
                    break
                if (pos.y >= screen_size.height - border_indent):
                    current_direction = DirectionsEnum.right_top
                    break
                pyautogui.moveRel(step, step, duration=duration)

            # Вправо вверх
            elif (current_direction == DirectionsEnum.right_top):
                if (pos.x >= screen_size.width - border_indent):
                    current_direction = DirectionsEnum.left_top
                    break
                if (pos.y <= border_indent):
                    current_direction = DirectionsEnum.right_bottom
                    break
                pyautogui.moveRel(step, -step, duration=duration)

            # Влево вверх
            elif (current_direction == DirectionsEnum.left_top):
                if (pos.x <= border_indent):
                    current_direction = DirectionsEnum.right_top
                    break
                if (pos.y <= border_indent):
                    current_direction = DirectionsEnum.left_bottom
                    break
                pyautogui.moveRel(-step, -step, duration=duration)

            # Влево вниз
            if (current_direction == DirectionsEnum.left_bottom):
                if (pos.x <= border_indent):
                    current_direction = DirectionsEnum.right_bottom
                    break
                if (pos.y >= screen_size.height - border_indent):
                    current_direction = DirectionsEnum.left_top
                    break
                pyautogui.moveRel(-step, step, duration=duration)


if __name__ == "__main__":
    thread = threading.Thread(target=_exit_listener)
    thread.start()
    start_mouse_walk(10)
