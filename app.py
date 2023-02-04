import tkinter as tk


class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Sush Edit 1.0")
        self.root.geometry("800x600")

        self.text = tk.Text(self.root, wrap="word")
        self.text.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    app.run()
