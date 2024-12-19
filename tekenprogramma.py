import tkinter as tk
from tkinter import colorchooser, filedialog
import turtle

class TurtleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tekenprogramma met Turtle")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.screen = turtle.TurtleScreen(self.canvas)
        self.t = turtle.RawTurtle(self.screen)
        self.t.speed(5)

        self.pen_color = "black"
        self.fill_color = "white"

        self.create_controls()

        self.commands = []

    def create_controls(self):
        control_frame = tk.Frame(self.root)
        control_frame.pack(side=tk.BOTTOM, fill=tk.X)

        tk.Label(control_frame, text="Afstand:").grid(row=0, column=0)
        self.distance_entry = tk.Entry(control_frame, width=5)
        self.distance_entry.grid(row=0, column=1)
        tk.Button(control_frame, text="Vooruit", command=self.forward).grid(row=0, column=2)
        tk.Button(control_frame, text="Achteruit", command=self.backward).grid(row=0, column=3)

        tk.Label(control_frame, text="Hoek:").grid(row=1, column=0)
        self.angle_entry = tk.Entry(control_frame, width=5)
        self.angle_entry.grid(row=1, column=1)
        tk.Button(control_frame, text="Links", command=self.left).grid(row=1, column=2)
        tk.Button(control_frame, text="Rechts", command=self.right).grid(row=1, column=3)

        tk.Button(control_frame, text="Pen omhoog", command=self.pen_up).grid(row=2, column=0)
        tk.Button(control_frame, text="Pen omlaag", command=self.pen_down).grid(row=2, column=1)

        tk.Button(control_frame, text="Pen kleur", command=self.choose_pen_color).grid(row=2, column=2)
        tk.Button(control_frame, text="Vul kleur", command=self.choose_fill_color).grid(row=2, column=3)

        tk.Label(control_frame, text="X:").grid(row=3, column=0)
        self.x_entry = tk.Entry(control_frame, width=5)
        self.x_entry.grid(row=3, column=1)
        tk.Label(control_frame, text="Y:").grid(row=3, column=2)
        self.y_entry = tk.Entry(control_frame, width=5)
        self.y_entry.grid(row=3, column=3)
        tk.Button(control_frame, text="Ga naar", command=self.go_to).grid(row=3, column=4)

        tk.Button(control_frame, text="Reset", command=self.reset).grid(row=4, column=0)

        tk.Button(control_frame, text="Cirkel", command=self.circle).grid(row=4, column=1)
        tk.Button(control_frame, text="Driehoek", command=self.triangle).grid(row=4, column=2)
        tk.Button(control_frame, text="Vierkant", command=self.square).grid(row=4, column=3)
        tk.Button(control_frame, text="Zeshoek", command=self.hexagon).grid(row=4, column=4)

        tk.Button(control_frame, text="Opslaan", command=self.save).grid(row=5, column=0)
        tk.Button(control_frame, text="Laden", command=self.load).grid(row=5, column=1)

    def forward(self):
        distance = int(self.distance_entry.get() or 0)
        self.t.forward(distance)
        self.log_command(f"t.forward({distance})")

    def backward(self):
        distance = int(self.distance_entry.get() or 0)
        self.t.backward(distance)
        self.log_command(f"t.backward({distance})")

    def left(self):
        angle = int(self.angle_entry.get() or 0)
        self.t.left(angle)
        self.log_command(f"t.left({angle})")

    def right(self):
        angle = int(self.angle_entry.get() or 0)
        self.t.right(angle)
        self.log_command(f"t.right({angle})")

    def pen_up(self):
        self.t.penup()
        self.log_command("t.penup()")

    def pen_down(self):
        self.t.pendown()
        self.log_command("t.pendown()")

    def choose_pen_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.pen_color = color
            self.t.pencolor(color)
            self.log_command(f"t.pencolor('{color}')")

    def choose_fill_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.fill_color = color
            self.log_command(f"t.fillcolor('{color}')")

    def go_to(self):
        x = int(self.x_entry.get() or 0)
        y = int(self.y_entry.get() or 0)
        self.t.goto(x, y)
        self.log_command(f"t.goto({x}, {y})")

    def circle(self):
        self.t.circle(50)
        self.log_command("t.circle(50)")

    def triangle(self):
        for _ in range(3):
            self.t.forward(100)
            self.t.left(120)
        self.log_command("# Draw triangle")

    def square(self):
        for _ in range(4):
            self.t.forward(100)
            self.t.left(90)
        self.log_command("# Draw square")

    def hexagon(self):
        for _ in range(6):
            self.t.forward(100)
            self.t.left(60)
        self.log_command("# Draw hexagon")

    def reset(self):
        self.t.reset()
        self.commands = []

    def save(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write("\n".join(self.commands))

    def load(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                for line in file:
                    exec(line.strip())

    def log_command(self, command):
        self.commands.append(command)

if __name__ == "__main__":
    root = tk.Tk()
    app = TurtleApp(root)
    root.mainloop()
