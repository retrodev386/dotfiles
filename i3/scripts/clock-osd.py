#!/usr/bin/env python3
"""Cyberpunk-themed floating clock widget — shows time, day, date, and battery."""
import tkinter as tk
from datetime import datetime

# ── Cyberpunk theme palette ──
BG_OUTER      = "#05d9e8"   # cursor_bg — neon cyan glow border
BG_INNER      = "#0d0221"   # background — deep purple-black
TIME_COLOR    = "#ff2a6d"   # foreground — hot pink
DAY_COLOR     = "#05d9e8"   # cursor_bg — neon cyan
DATE_COLOR    = "#d1f7ff"   # brights[7] — pale cyan-white
DIVIDER_1     = "#d300c5"   # tab_inactive_fg — magenta
DIVIDER_2     = "#f9f871"   # selection_fg — neon yellow
BATTERY_COLOR = "#39ff88"   # brights[2] — neon green

def get_battery_info():
    """Read battery percent and charging status from sysfs (no extra deps)."""
    try:
        with open("/sys/class/power_supply/BAT0/capacity") as f:
            percent = f.read().strip()
        with open("/sys/class/power_supply/BAT0/status") as f:
            status = f.read().strip()
        icon = "⚡" if status == "Charging" else "🔋"
        return f"{icon} {percent}%"
    except FileNotFoundError:
        try:
            with open("/sys/class/power_supply/BAT1/capacity") as f:
                percent = f.read().strip()
            return f"🔋 {percent}%"
        except FileNotFoundError:
            return "⚡ AC"

def show_clock():
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.configure(bg=BG_OUTER)

    w, h = 320, 220
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    x = sw - w - 20
    y = 20
    root.geometry(f"{w}x{h}+{x}+{y}")

    inner = tk.Frame(root, bg=BG_INNER)
    inner.place(x=3, y=3, width=w - 6, height=h - 6)

    now = datetime.now()
    time_str = now.strftime("%H:%M:%S")
    date_str = now.strftime("%d %b %Y")
    day_str = now.strftime("%A").upper()
    battery_str = get_battery_info()

    time_label = tk.Label(
        inner, text=time_str, font=("Terminus (TTF)", 36, "bold"),
        fg=TIME_COLOR, bg=BG_INNER
    )
    time_label.place(relx=0.5, rely=0.22, anchor="center")

    def tick():
        time_label.config(text=datetime.now().strftime("%H:%M:%S"))
        time_label.after(1000, tick)

    tick()

    divider = tk.Frame(inner, bg=DIVIDER_1, height=1)
    divider.place(relx=0.5, rely=0.4, anchor="center", relwidth=0.8)

    day_label = tk.Label(
        inner, text=day_str, font=("Terminus (TTF)", 22, "bold"),
        fg=DAY_COLOR, bg=BG_INNER
    )
    day_label.place(relx=0.5, rely=0.55, anchor="center")

    date_label = tk.Label(
        inner, text=date_str, font=("Terminus (TTF)", 13),
        fg=DATE_COLOR, bg=BG_INNER
    )
    date_label.place(relx=0.5, rely=0.68, anchor="center")

    divider2 = tk.Frame(inner, bg=DIVIDER_2, height=1)
    divider2.place(relx=0.5, rely=0.80, anchor="center", relwidth=0.4)

    battery_label = tk.Label(
        inner, text=battery_str, font=("Terminus (TTF)", 20, "bold"),
        fg=BATTERY_COLOR, bg=BG_INNER
    )
    battery_label.place(relx=0.5, rely=0.90, anchor="center")

    root.after(10000, root.destroy)
    root.mainloop()

show_clock()
