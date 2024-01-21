import numpy as np
import sounddevice as sd
import time
from scipy import signal
from tqdm import tqdm  # 進度條


class SquareWaveGenerator:
    def __init__(self, frequency, duration, amplitude, duty_cycle, duty_cycle_phase=None, phase=None, sample_rate=44100):
        """
        :type frequency: int           # 頻率，單位為赫茲
        :type duration: float          # 單次持續時間，單位為秒
        :type amplitude: float         # 振幅，範圍為0到1
        :type duty_cycle: float        # 佔空比1，範圍為0到1 (調整不超過0.5)
        :type duty_cycle_phase: float  # 佔空比2，範圍為0到1 (調整不超過0.5)
        :type phase: float             # 相位差，範圍為0到2π
        :type sample_rate: int         # 採樣率，多為44100
        """
        self.frequency = frequency
        self.duration = duration
        self.amplitude = amplitude
        self.duty_cycle = duty_cycle
        self.duty_cycle_phase = duty_cycle_phase
        self.phase = phase
        self.sample_rate = sample_rate

    def generate_duo_square_wave(self):
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration), False)
        square_wave1 = self.amplitude * signal.square(2 * np.pi * self.frequency * t, duty=self.duty_cycle)
        square_wave2 = self.amplitude * signal.square(2 * np.pi * frequency * t + phase, duty=duty_cycle_phase)
        final_wave = square_wave1 + square_wave2
        return final_wave

    def generate_square_wave(self):
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration), False)
        final_wave = self.amplitude * signal.square(2 * np.pi * self.frequency * t, duty=self.duty_cycle)
        return final_wave

    def play_wave(self, square_wave):
        print("-------- 開始播放 --------")
        print(f"播放時長: {self.duration} s")
        print(f"頻率: {self.frequency} Hz")
        print(f"振幅: {self.amplitude * 100:.2f} %")
        print(f"佔空比1: {self.duty_cycle * 100:.2f} %")
        print(f"佔空比2: {self.duty_cycle_phase * 100:.2f} %")
        print(f"相位差: {self.phase} rad")
        print(f"採樣率: {self.sample_rate} rad")
        print("-------------------------")

        time.sleep(0.1)
        start_time = time.time()
        sd.play(square_wave)

        for i in tqdm(range(0, int(self.duration))):
            current_time = time.time()
            elapsed_time = current_time - start_time
            time.sleep(1)


if __name__ == '__main__':
    # 指定參數
    duration = 10.0         # 單次持續時間，單位為秒
    frequency = 100         # 頻率，單位為赫茲
    amplitude = 1           # 振幅，範圍為0到1
    duty_cycle = 0.8        # 佔空比1，範圍為0到1 (調整不超過0.5)
    duty_cycle_phase = 0.1  # 佔空比2，範圍為0到1 (調整不超過0.5)
    phase = np.pi / 2       # 相位差，範圍為0到2π

    # 建立物件
    generator = SquareWaveGenerator(frequency, duration, amplitude, duty_cycle, duty_cycle_phase, phase)

    # 生成方波
    square_wave = generator.generate_duo_square_wave()

    # 播放方波
    generator.play_wave(square_wave)
