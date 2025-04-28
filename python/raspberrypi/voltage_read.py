from DFRobot_ADS1115 import ADS1115
import tkinter as tk

# Gain settings
ADS1115_REG_CONFIG_PGA_6_144V = 0x00  # ±6.144V range (Gain 2/3)

# Create ADS1115 object
ads1115 = ADS1115()
# Set I2C address and gain once
ads1115.set_addr_ADS1115(0x48)
ads1115.set_gain(ADS1115_REG_CONFIG_PGA_6_144V)

# Function to read the voltage
def read_voltage():
    adc0 = ads1115.read_voltage(0)
    voltage_label.config(text=f"A0: {adc0['r']} mV")
    root.after(500, read_voltage)  # Call this function again after 500ms

# Setup GUI
root = tk.Tk()
root.title("Voltage Reader")

voltage_label = tk.Label(root, text="Reading...", font=("Helvetica", 24))
voltage_label.pack(padx=20, pady=20)

# Start reading voltage
read_voltage()

# Start GUI loop
root.mainloop()
