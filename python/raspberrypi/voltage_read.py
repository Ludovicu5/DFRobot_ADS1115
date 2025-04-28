import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import collections
from DFRobot_ADS1115 import ADS1115

# Gain setting
ADS1115_REG_CONFIG_PGA_6_144V = 0x00  # ±6.144V range (Gain 2/3)

# Create ADS1115 object
ads1115 = ADS1115()
ads1115.set_addr_ADS1115(0x48)
ads1115.set_gain(ADS1115_REG_CONFIG_PGA_6_144V)

# Buffer for last N points
MAX_POINTS = 50
voltages = collections.deque(maxlen=MAX_POINTS)

# Function to read and update voltage
def read_voltage():
    adc0 = ads1115.read_voltage(0)
    voltage = adc0['r']
    voltage_label.config(text=f"A0: {voltage} mV")

    # Add new reading to the buffer
    voltages.append(voltage)

    # Update the graph
    line.set_data(range(len(voltages)), list(voltages))
    ax.relim()
    ax.autoscale_view()

    canvas.draw()

    root.after(500, read_voltage)  # Schedule next reading

# Setup GUI
root = tk.Tk()
root.title("Voltage Reader with Live Graph")

# Voltage display label
voltage_label = tk.Label(root, text="Reading...", font=("Helvetica", 24))
voltage_label.pack(padx=20, pady=10)

# Create Matplotlib figure
fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)
ax.set_title("Voltage Over Time")
ax.set_xlabel("Sample")
ax.set_ylabel("Voltage (mV)")

line, = ax.plot([], [], marker='o')  # Empty line, will be filled dynamically

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(padx=20, pady=20)

# Start reading
read_voltage()

# Start GUI loop
root.mainloop()
