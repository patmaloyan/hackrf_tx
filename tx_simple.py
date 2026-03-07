import subprocess
import os

# --- User settings ---
dat_path = "waveforms/Hamming_burst_QPSK_msg_5Mhzfs_3sec.dat"
center_freq = 10e6 # Hz
sample_rate = 5_000_000 # Must match waveform created
tx_gain = 40                                # dB
amp_enable = True                       # use RF amplifier
num_samples = sample_rate * 3



# --- Build hackrf_transfer command ---
cmd = [
    "hackrf_transfer",
    "-t", dat_path,                      # transmit file
    "-f", str(center_freq),              # frequency
    "-s", str(sample_rate),              # sample rate
    "-x", str(tx_gain),                  # TX VGA gain
    "-n", str(num_samples)
]



if amp_enable:
    cmd += ["-a", "1"]                   # enable amp

# --- Run command ---
print("Running:", " ".join(cmd))
subprocess.run(cmd, check=True)
print("Transmission complete.")

