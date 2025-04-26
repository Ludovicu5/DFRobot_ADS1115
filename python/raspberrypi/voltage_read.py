import time
from DFRobot_ADS1115 import ADS1115

# Gain settings
ADS1115_REG_CONFIG_PGA_6_144V = 0x00  # ±6.144V range (Gain 2/3)
ADS1115_REG_CONFIG_PGA_4_096V = 0x02  # ±4.096V range (Gain 1)
ADS1115_REG_CONFIG_PGA_2_048V = 0x04  # ±2.048V range (Gain 2, default)
ADS1115_REG_CONFIG_PGA_1_024V = 0x06  # ±1.024V range (Gain 4)
ADS1115_REG_CONFIG_PGA_0_512V = 0x08  # ±0.512V range (Gain 8)
ADS1115_REG_CONFIG_PGA_0_256V = 0x0A  # ±0.256V range (Gain 16)

# Create ADS1115 object
ads1115 = ADS1115()

# Set I2C address and gain once
ads1115.set_addr_ADS1115(0x48)
ads1115.set_gain(ADS1115_REG_CONFIG_PGA_6_144V)

while True:
    # Read all 4 channels
    adc0 = ads1115.read_voltage(0)
    time.sleep(0.2)
    # adc1 = ads1115.read_voltage(1)
    # time.sleep(0.2)
    # adc2 = ads1115.read_voltage(2)
    # time.sleep(0.2)
    # adc3 = ads1115.read_voltage(3)

    # # Print results
    # print("A0: {0} mV  A1: {1} mV  A2: {2} mV  A3: {3} mV".format(
    #     adc0['r'], adc1['r'], adc2['r'], adc3['r']
    # ))

    # Print results
    print("A0: {0} mV".format(
        adc0['r']
    ))
