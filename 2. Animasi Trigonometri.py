import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from tkinter import messagebox

# Munculkan pop-up window dengan pesan
messagebox.showinfo("MGS Beyond", "Aplikasi ini dibuat untuk contoh bagi MGS Divisi Business Transformation. Happy learning and surfing. (Ek4 B3b3n)")

# Inisialisasi plot
fig, (ax_sinus, ax_cosinus, ax_tangen) = plt.subplots(3, 1, figsize=(8, 10))
fig.canvas.manager.set_window_title("Aplikasi Animasi Trigonometri by Ek4 B3b3n")

# Rentang sumbu x
x = np.linspace(0, 2 * np.pi, 100)
frames = 200

# Data awal sinus
y_sinus = np.sin(x)

# Data awal cosinus
y_cosinus = np.cos(x)

# Data awal tangen
y_tangen = np.tan(x)

# Plot sinus
line_sinus, = ax_sinus.plot(x, y_sinus, color='r', label='Sinus')
ax_sinus.legend()

# Plot cosinus
line_cosinus, = ax_cosinus.plot(x, y_cosinus, color='g', label='Cosinus')
ax_cosinus.legend()

# Plot tangen
line_tangen, = ax_tangen.plot(x, y_tangen, color='b', label='Tangen')
ax_tangen.legend()

# Tombol pause
pause_sinus = False
pause_cosinus = False
pause_tangen = False

def onPress(event):
    global pause_sinus, pause_cosinus, pause_tangen

    if event.key == 'p':
        if event.inaxes == ax_sinus:
            pause_sinus = not pause_sinus
            line_sinus.set_label(f'Sinus (Paused: {pause_sinus})')
            ax_sinus.legend()
        elif event.inaxes == ax_cosinus:
            pause_cosinus = not pause_cosinus
            line_cosinus.set_label(f'Cosinus (Paused: {pause_cosinus})')
            ax_cosinus.legend()
        elif event.inaxes == ax_tangen:
            pause_tangen = not pause_tangen
            line_tangen.set_label(f'Tangen (Paused: {pause_tangen})')
            ax_tangen.legend()

    plt.draw()

# Menambahkan event handler pada figure
fig.canvas.mpl_connect('key_press_event', onPress)

# Fungsi update sinus
def update_sinus(frame):
    if not pause_sinus:
        line_sinus.set_ydata(np.sin(x + frame / 7.0))
    return line_sinus,

# Fungsi update cosinus
def update_cosinus(frame):
    if not pause_cosinus:
        line_cosinus.set_ydata(np.cos(x + frame / 8.0))
    return line_cosinus,

# Fungsi update tangen
def update_tangen(frame):
    if not pause_tangen:
        line_tangen.set_ydata(np.tan(x + frame / 10.0))
    return line_tangen,

# Membuat animasi sinus
ani_sinus = animation.FuncAnimation(fig, update_sinus, frames=frames, interval=30, blit=True)

# Membuat animasi cosinus
ani_cosinus = animation.FuncAnimation(fig, update_cosinus, frames=frames, interval=20, blit=True)

# Membuat animasi tangen
ani_tangen = animation.FuncAnimation(fig, update_tangen, frames=frames, interval=20, blit=True)

# Menampilkan plot
plt.tight_layout()
plt.show()
