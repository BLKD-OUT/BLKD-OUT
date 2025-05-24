import os
import shutil
import json
import tkinter as tk
from tkinter import messagebox

def apply_settings():
    local = os.getenv("LOCALAPPDATA")
    rbx_path = os.path.join(local, "Roblox", "ClientSettings")
    os.makedirs(rbx_path, exist_ok=True)

    with open("settings/ClientAppSettings.json", "r") as src:
        data = json.load(src)

    with open(os.path.join(rbx_path, "ClientAppSettings.json"), "w") as dst:
        json.dump(data, dst, indent=4)

    messagebox.showinfo("BLKD OUT", "Optimized settings applied ✅")

def launch_roblox():
    os.system("start roblox-player:")  # Roblox protocol
    messagebox.showinfo("BLKD OUT", "Launching Roblox 💨")

root = tk.Tk()
root.title("BLKD OUT")
root.geometry("300x200")

tk.Label(root, text="BLKD OUT - FPS Optimizer", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="Apply Optimizations", command=apply_settings).pack(pady=10)
tk.Button(root, text="Launch Roblox", command=launch_roblox).pack(pady=10)

root.mainloop()

