import numpy as np
import sounddevice as sd
import time
from scipy import signal
from tqdm import tqdm  # 進度條


# 單次播放方玻功能

def generate_square_wave(frequency, duration, amplitude, duty_cycle, sample_rate=44100):
    # 生成時間數組
    t = np.linspace(0, duration, int(sample_rate * duration), False)

    # 生成方波
    # square_wave = amplitude * (signal.square(2 * np.pi * frequency * t, duty=duty_cycle)+signal.square(2 * np.pi * (0.5*frequency) * t, duty=duty_cycle)/2)

    square_wave1 = amplitude * signal.square(2 * np.pi * frequency * t, duty=duty_cycle)
    square_wave2 = amplitude * signal.square(2 * np.pi * (2 * frequency) * t, duty=duty_cycle)
    square_wave = square_wave1 + square_wave2
    return square_wave


# 指定參數
duration = 60.0  # 單次持續時間，單位為秒
frequency = 5  # 頻率，單位為赫茲
amplitude = 0.8  # 振幅，範圍為0到1
duty_cycle = 0.1  # duty cycle，範圍為0到1

# 生成方波
square_wave = generate_square_wave(frequency, duration, amplitude, duty_cycle)

# 開始播放時間
start_time = time.time()

# 播放方波
sd.play(square_wave, device=1)


print("-------- 開始播放 --------")
print(f"播放時長: {duration} s")
print(f"頻率: {frequency} Hz")
print(f"振幅: {amplitude * 100:.2f} %")
print(f"Duty Cycle: {duty_cycle * 100:.2f} %")
print("-------------------------")
# 顯示播放進度和其他參數
for i in tqdm(range(0, int(duration))):
    current_time = time.time()
    elapsed_time = current_time - start_time

    time.sleep(1)
