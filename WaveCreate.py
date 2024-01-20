import numpy as np
import sounddevice as sd
from scipy import signal
import threading

# 全局變量
frequency = 100  # 頻率，單位為赫茲
amplitude = 1  # 振幅，範圍為0到1
duty_cycle = 0.1  # duty cycle，範圍為0到1
sample_rate = 44100  # 採樣率，單位為赫茲

# 生成方波的回調函數
def callback(outdata, frames, time, status):
    global frequency, amplitude, duty_cycle, sample_rate

    # 生成時間數組
    t = (time.outputBufferDacTime + np.arange(frames)) / sample_rate

    # 生成方波
    square_wave = amplitude * signal.square(2 * np.pi * frequency * t, duty=duty_cycle)

    # 確保方波與outdata具有相同的形狀
    square_wave = square_wave.reshape(-1, 1)

    outdata[:] = square_wave

# 創建一個新的Stream來播放聲音
stream = sd.OutputStream(callback=callback, channels=1, samplerate=sample_rate)

# 開始播放Stream
stream.start()

# 在主線程中讀取和更新參數
while True:
    frequency = float(input("請輸入新的頻率（赫茲）："))
    amplitude = float(input("請輸入新的振幅（0到1）："))
    duty_cycle = float(input("請輸入新的duty cycle（0到1）："))
