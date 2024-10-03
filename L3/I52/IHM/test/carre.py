import tkinter as tk

class SquareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Square Mover App")

        self.canvas = tk.Canvas(root, bg="white", width=500, height=500)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.square = None
        self.is_button3_pressed = False

        button1 = tk.Button(root, text="Create Square", command=self.create_square)
        button1.pack(side=tk.LEFT)

        button3 = tk.Button(root, text="Move Square", command=self.toggle_move_mode)
        button3.pack(side=tk.LEFT)

        root.bind("<ButtonPress-3>", self.button3_press)
        root.bind("<ButtonRelease-3>", self.button3_release)
        root.bind("<B1-Motion>", self.move_square)

    def create_square(self):
        self.square = self.canvas.create_rectangle(50, 50, 100, 100, fill="blue")

    def toggle_move_mode(self):
        self.is_button3_pressed = not self.is_button3_pressed

    def button3_press(self, event):
        if self.square and self.is_button3_pressed:
            self.start_x = event.x
            self.start_y = event.y

    def button3_release(self, event):
        self.is_button3_pressed = False

    def move_square(self, event):
        if self.square and self.is_button3_pressed:
            delta_x = event.x - self.start_x
            delta_y = event.y - self.start_y
            self.canvas.move(self.square, delta_x, delta_y)
            self.start_x = event.x
            self.start_y = event.y

if __name__ == "__main__":
    root = tk.Tk()
    app = SquareApp(root)
    root.mainloop()

