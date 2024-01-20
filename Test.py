import numpy as np
import sounddevice as sd
import time
from scipy import signal
from tqdm import tqdm  # 進度條

# 單次播放方玻功能
def generate_square_wave(frequency, duration, amplitude, duty_cycle, duty_cycle_phase, phase, sample_rate=44100):
    # 生成時間數組
    t = np.linspace(0, duration, int(sample_rate * duration), False)

    # 生成方波
    square_wave1 = amplitude * signal.square(2 * np.pi * frequency * t, duty=duty_cycle)
    # square_wave2 = amplitude * signal.square(2 * np.pi * frequency * t + phase, duty=duty_cycle_phase)
    square_wave2 = 0
    square_wave = square_wave1 + square_wave2
    return square_wave

# 指定參數
duration = 500.0  # 單次持續時間，單位為秒
frequency = 200  # 頻率，單位為赫茲 1 20 100 200 1000 (200)
amplitude = 1  # 振幅，範圍為0到1 0.2 0.4 0.5 0.6 0.8 1.0 (0.5)

duty_cycle = 0.8 # dutycycle，範圍為0到1 (調整不超過0.5) 0.8 0.6 0.4 0.2 0.1 0.01 (0.5)

duty_cycle_phase = 0.1  # duty cycle，範圍為0到1 (滯後的那個波)
phase = np.pi / 2  # 相位差，範圍為0到2π

# 生成方波
square_wave = generate_square_wave(frequency, duration, amplitude, duty_cycle , duty_cycle_phase, phase)

print("-------- 開始播放 --------")
print(f"播放時長: {duration} s")
print(f"頻率: {frequency} Hz")
print(f"振幅: {amplitude * 100:.2f} %")
print(f"佔空比: {duty_cycle * 100:.2f} %")
print(f"相位差: {phase} rad")
print("-------------------------")

time.sleep(0.1)
# 開始播放時間
start_time = time.time()

# 播放方波
sd.play(square_wave, device=1)


# 顯示播放進度和其他參數
for i in tqdm(range(0, int(duration))):
    current_time = time.time()
    elapsed_time = current_time - start_time

    time.sleep(1)
