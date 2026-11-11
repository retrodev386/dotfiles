#!/usr/bin/env python3
import i3ipc
import tkinter as tk
import threading

def show_osd(label):
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.attributes("-alpha", 0.85)  # 0.0 = fully invisible, 1.0 = fully opaque
    root.configure(bg="#4DE8E8")  # cyan shows as the border

    w, h = 220, 220
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    #x, y = (sw - w) // 2, (sh - h) // 2
    x = (sw - w) // 2   
    y = 20
    root.geometry(f"{w}x{h}+{x}+{y}")

    inner = tk.Frame(root, bg="#0D0716")
    inner.place(x=3, y=3, width=w - 6, height=h - 6)  # 3px cyan border on all sides

    label = tk.Label(
        inner, text=str(label), font=("Terminus (TTF)", 80, "bold"),
        fg="#FF2D6C", bg="#0D0716"
    )
    label.place(relx=0.5, rely=0.5, anchor="center")  # true dead-center

    root.after(800, root.destroy)
    root.mainloop()

i3 = i3ipc.Connection()

def on_workspace(i3, e):
    if e.change == "focus":
        ws = i3.get_tree().find_focused().workspace()
        label = ws.num if ws.num != -1 else ws.name.split(";")[0]
        threading.Thread(target=show_osd, args=(label,), daemon=True).start()

i3.on("workspace::focus", on_workspace)
i3.main()
