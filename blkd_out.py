import os
import json
import tkinter as tk
from tkinter import messagebox

def apply_settings():
    local = os.getenv("LOCALAPPDATA")
    rbx_path = os.path.join(local, "Roblox", "ClientSettings")
    os.makedirs(rbx_path, exist_ok=True)

    try:
        with open("settings/ClientAppSettings.json", "r") as src:
            data = json.load(src)

        with open(os.path.join(rbx_path, "ClientAppSettings.json"), "w") as dst:
            json.dump(data, dst, indent=4)

        messagebox.showinfo("BLKD OUT", "✅ Optimization applied successfully")
    except Exception as e:
        messagebox.showerror("BLKD OUT", f"❌ Error: {e}")

def launch_roblox():
    os.system("start roblox-player:")
    messagebox.showinfo("BLKD OUT", "🚀 Roblox is launching...")

root = tk.Tk()
root.title("BLKD OUT")
root.geometry("320x220")
root.resizable(False, False)

tk.Label(root, text="🕶️ BLKD OUT", font=("Arial", 18)).pack(pady=10)
tk.Label(root, text="FPS & Graphics Optimizer for Roblox").pack()

tk.Button(root, text="🧼 Apply Optimizations", command=apply_settings, width=25).pack(pady=12)
tk.Button(root, text="🚀 Launch Roblox", command=launch_roblox, width=25).pack(pady=6)

tk.Label(root, text="Made by BLK").pack(side="bottom", pady=8)
root.mainloop()
