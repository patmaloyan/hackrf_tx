import subprocess
import os

# --- User settings ---
dat_path = "waveforms/Hamming_burst_QPSK_msg_5Mhzfs_3sec.dat"
center_freq = 10e6  # Hz
sample_rate = 5_000_000
tx_gain = 40
amp_enable = True
num_samples = sample_rate * 3

# Serial number of triggering (TX) HackRF
serial_tx = "0000000000000000c66c63dc32999683"

# --- Build hackrf_transfer command ---
cmd = [
    "hackrf_transfer",
    "-d", serial_tx,                 # specify TX HackRF (trigger source)
    "-t", dat_path,                  # transmit file
    "-f", str(center_freq),          # center frequency
    "-s", str(sample_rate),          # sample rate
    "-x", str(tx_gain),              # TX gain
    "-n", str(num_samples)
]

if amp_enable:
    cmd += ["-a", "1"]

# --- Run command ---
print("Running:", " ".join(cmd))
subprocess.run(cmd, check=True)

print("Transmission complete.")