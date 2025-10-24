#################################################################################################
# TASK 1: Wind Speeds at Hub Heights #
#################################################################################################

## Part 1 - Vizualize the Data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Loading the data into python
data_exc1 = pd.read_excel("Module 7 - Exercises data.xlsx", sheet_name='Exercise 1')

#Defining time and wind speed variables
Time = data_exc1["Time (s)"]
V = data_exc1["Wind speed (m/s)"]

#Plotting the time series wind data
fig, ax = plt.subplots()
ax.plot(Time, V)
ax.set_xlabel('Time (s)', fontsize=10)
ax.set_ylabel('Wind speed (m/s)', fontsize=10)
plt.show()

## Part 2 - Remove Noise
from scipy.fft import fft, fftfreq, rfft, rfftfreq
from scipy.signal import welch

# Fast Fouriers Tranform
signal = np.asarray(V) # our signal is the wind speed
t = np.asarray(Time)

spectrum = np.abs(rfft(signal))
freqs = rfftfreq(len(signal), d=t[1]-t[0])


fig, ax2 = plt.subplots()
ax2.plot(freqs, spectrum)
ax2.set_xscale('log')
ax2.set_xlabel('Frequency [Hz]', fontsize=10)
ax2.set_ylabel('Magnitude', fontsize=10)
ax2.set_ylim(0,20000)
plt.show()

# The PSD
fs = 1/(t[1]-t[0])
print(fs)
f, Sx = welch(signal, fs=fs, nperseg=fs)

fig, ax3 = plt.subplots()
ax3.plot(f, Sx)
ax3.loglog(f,Sx)
ax3.set_xlabel('Frequency [Hz]', fontsize=10)
ax3.set_ylabel('PSD [m^2/Hz]', fontsize=10)
plt.show()

#Part 3 - Filtering Data
from scipy.signal import butter, filtfilt, iirnotch

def butter_filter(data, cutoff, fs, order=4, btype='low'):
    nyq = 0.5 * fs  # Nyquist frequency
    normal_cutoff = np.array(cutoff) / nyq
    b, a = butter(order, normal_cutoff, btype=btype, analog=False)
    return filtfilt(b, a, data)

low_pass = butter_filter(signal, cutoff=0.2, fs=40, btype='low')

#Saving the low_pass data to be used in task 2
import json

filtered_data = low_pass.tolist()
time = t.tolist()

data_to_save = {
    "time": time,
    "wind": filtered_data
}

with open("filtered_v_output.json","w") as f:
    json.dump(data_to_save, f)

# Plotting the results
fig, ax4 = plt.subplots()

ax4.plot(t, signal, label='Original signal' )
ax4.plot(t, low_pass, color='r', label='Low-pass filtered (Keep <0.2 Hz)')
ax4.grid(True, linestyle='--', alpha=0.5)
ax4.set_ylabel('Wind speed (m/s)')
ax4.set_xlabel('Time (s)')
ax4.set_title('Low-pass filter')
ax4.legend(fontsize=6,loc='upper left')

plt.show()

"""Cutoff = 0.2 smooths out the signal while keeping the most important trends in the data"""