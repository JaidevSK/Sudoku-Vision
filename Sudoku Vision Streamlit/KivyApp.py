from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.graphics.texture import Texture
import numpy as np
import cv2
import SolveSudoku
import Img2Arr
import matplotlib.pyplot as plt

class CameraApp(App):
    def build(self):
        self.camera = Camera(resolution=(640, 480), play=True)
        self.capture_button = Button(text="Capture")
        self.capture_button.bind(on_press=self.capture)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.camera)
        layout.add_widget(self.capture_button)

        return layout

    def capture(self, instance):
        texture = self.camera.texture
        size = texture.size
        pixels = texture.pixels

        # Convert byte array to numpy array
        pixels = np.frombuffer(pixels, dtype=np.uint8)

        # Convert the texture to a NumPy array
        np_image = np.array(pixels, dtype=np.uint8).reshape(size[1], size[0], 4)

        np_image = cv2.cvtColor(np_image, cv2.COLOR_RGBA2RGB)

        
        # Convert the image to Array
        arr = Img2Arr.img2arr(np_image)

        # Solve the Sudoku
        grid = SolveSudoku.solve(arr)

        
        fig, ax = plt.subplots()
        for i in range(10):
            if i % 3 == 0:
                linewidth = 2
            else:
                linewidth = 1

            ax.plot([i, i], [0, 9], color='black', linewidth=linewidth)
            ax.plot([0, 9], [i, i], color='black', linewidth=linewidth)

        for i in range(9):
            for j in range(9):
                if grid[i][j] != 0:
                    ax.text(j + 0.5, 8.5 - i, grid[i][j], ha='center', va='center', fontsize=16)

        plt.axis('off')
        plt.title("Solved Sudoku")
        # Display the solved Sudoku plot
        plt.show()

if __name__ == '__main__':
    CameraApp().run()
