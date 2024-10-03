import tkinter as tk
from tkinter import filedialog, messagebox

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Application de Dessin")

        # Barre de menu
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nouveau", command=self.clear_canvas)
        filemenu.add_command(label="Ouvrir", command=self.open_file)
        filemenu.add_command(label="Sauver", command=self.save_file, state=tk.DISABLED)
        filemenu.add_command(label="Quitter", command=self.confirm_quit)
        menubar.add_cascade(label="Fichier", menu=filemenu)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Aide", command=self.show_help)
        menubar.add_cascade(label="Aide", menu=helpmenu)
        root.config(menu=menubar)

        # Canvas
        self.canvas = tk.Canvas(root, bg="white", width=500, height=500)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        # Label (barre d'état)
        self.status_label = tk.Label(root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

        # Variable pour sauvegarder l'état du dessin
        self.drawing = False
        self.current_line = None
        self.selected_line = None

        # Binding des événements de la souris et du clavier
        self.canvas.bind("<B1-Motion>", self.draw_line)
        self.canvas.bind("<Enter>", self.on_canvas_enter)
        self.canvas.bind("<Leave>", self.on_canvas_leave)
        self.canvas.bind("<ButtonPress-1>", self.start_draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)
        self.canvas.bind("<Control-ButtonPress-1>", self.start_move)
        self.canvas.bind("<Control-ButtonRelease-1>", self.end_move)

        # Liste pour stocker les traces (lignes) créées
        self.lines = []

    def clear_canvas(self):
        self.canvas.delete("all")
        self.lines = []
        self.status_label.config(text="")
        self.update_save_menu()

    def open_file(self):
        filename = filedialog.askopenfilename(title="Ouvrir un fichier", filetypes=[("Text files", "*.txt")])
        if filename:
            self.clear_canvas()
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    coords = list(map(int, line.split()))
                    self.lines.append(self.canvas.create_line(coords, fill="black"))
            self.status_label.config(text=f"Fichier ouvert : {filename}")
            self.update_save_menu()

    def save_file(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, 'w') as file:
                for line_id in self.lines:
                    coords = self.canvas.coords(line_id)
                    file.write(" ".join(map(str, coords)) + "\n")
            self.status_label.config(text=f"Fichier sauvegardé : {filename}")

    def confirm_quit(self):
        if self.lines:
            result = messagebox.askyesno("Quitter", "Voulez-vous quitter? Toutes les modifications non sauvegardées seront perdues.")
            if result:
                self.root.destroy()
        else:
            self.root.destroy()

    def draw_line(self, event):
        if self.drawing:
            x, y = event.x, event.y
            self.canvas.coords(self.current_line, *self.flatten(self.canvas.coords(self.current_line)) + [x, y])
            self.update_status_label()

    def start_draw(self, event):
        self.drawing = True
        x, y = event.x, event.y
        self.current_line = self.canvas.create_line(x, y, x, y, fill="black", width=2)
        self.lines.append(self.current_line)
        self.update_save_menu()
        self.update_status_label()

    def end_draw(self, event):
        self.drawing = False

    def start_move(self, event):
        if self.selected_line:
            self.move_start_x = event.x
            self.move_start_y = event.y

    def end_move(self, event):
        self.selected_line = None

    def flatten(self, lst):
        return list(tk._flatten(lst))

    def on_canvas_enter(self, event):
        if self.selected_line:
            self.canvas.itemconfig(self.selected_line, fill="red")

    def on_canvas_leave(self, event):
        if self.selected_line:
            self.canvas.itemconfig(self.selected_line, fill="black")

    def move_selected_line(self, event):
        if self.selected_line:
            delta_x = event.x - self.move_start_x
            delta_y = event.y - self.move_start_y
            self.canvas.move(self.selected_line, delta_x, delta_y)
            self.move_start_x = event.x
            self.move_start_y = event.y
            self.update_status_label()

    def update_status_label(self):
        if self.selected_line:
            coords = self.canvas.coords(self.selected_line)
            self.status_label.config(text=f"ID : {self.selected_line}, Coords : {coords}")
        else:
            self.status_label.config(text="")

    def update_save_menu(self):
        if self.lines:
            self.root.nametowidget("Fichier").entryconfig("Sauver", state=tk.NORMAL)
        else:
            self.root.nametowidget("Fichier").entryconfig("Sauver", state=tk.DISABLED)

    def show_help(self):
        help_text = "Ceci est l'aide en ligne.\n"
        help_text += "L'application vous permet de dessiner des lignes dans le canvas.\n"
        help_text += "Vous pouvez créer une nouvelle trace en maintenant la touche Ctrl et en cliquant avec le bouton gauche de la souris.\n"
        help_text += "Vous pouvez déplacer une trace en cliquant avec le bouton gauche de la souris sur la trace et en la faisant glisser.\n"
        help_text += "L'entrée Sauver dans le menu Fichier sera activée une fois que vous aurez créé au moins une trace.\n"
        help_text += "L'entrée Ouvrir permet de charger un dessin à partir d'un fichier.\n"
        help_text += "L'entrée Quitter demande confirmation si vous avez créé au moins une trace.\n"
        help_text += "L'entrée Aide dans le menu Aide affiche cette fenêtre d'aide.\n"
        messagebox.showinfo("Aide en ligne", help_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()

