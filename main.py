import tkinter as tk

class whiteboard(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Writing Pad")
        self.previous_x = self.previous_y = 0
        self.x = self.y = 0
        self.points_recorded = []
        self.canvas = tk.Canvas(self, width=600, height=500, bg = "white", cursor="hand2")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.button_print = tk.Button(self, text = "Connect Lines", command = self.connect_points)
        self.button_print.pack(side="left", fill="both", expand=True)
        self.button_clear = tk.Button(self, text = "New Sheet", command = self.erase_all)
        self.button_clear.pack(side="right", fill="both", expand=True)
        self.canvas.bind("<Motion>", self.display_loc)
        self.canvas.bind("<B1-Motion>", self.write_start)

    def erase_all(self):

        self.canvas.delete("all")

    def connect_points(self):
        if self.points_recorded:
            self.points_recorded.pop()
            self.points_recorded.pop()
        self.canvas.create_line(self.points_recorded, fill = "black")
        self.points_recorded[:] = []

    def display_loc(self, event):
        self.previous_x = event.x
        self.previous_y = event.y

    def write_start(self, event):
        if self.points_recorded:
            self.points_recorded.pop()
            self.points_recorded.pop()

        self.x = event.x
        self.y = event.y
        self.canvas.create_line(self.previous_x, self.previous_y, self.x, self.y,fill="black")
        self.points_recorded.append(self.previous_x)
        self.points_recorded.append(self.previous_y)
        self.points_recorded.append(self.x)     
        self.points_recorded.append(self.x)        
        self.previous_x = self.x
        self.previous_y = self.y

     

if __name__ == "__main__":
    app = whiteboard()
    app.mainloop()
