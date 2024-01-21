import numpy as np
import sounddevice as sd
import time
from scipy import signal
from tqdm import tqdm  # 進度條


class SquareWaveGenerator:
    def __init__(self, frequency, duration, amplitude, duty_cycle, duty_cycle_phase, phase, sample_rate=44100):
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
        print(f"佔空比: {self.duty_cycle * 100:.2f} %")
        print(f"相位差: {self.phase} rad")
        print("-------------------------")

        time.sleep(0.1)
        start_time = time.time()
        sd.play(square_wave, device=1)

        for i in tqdm(range(0, int(self.duration))):
            current_time = time.time()
            elapsed_time = current_time - start_time
            time.sleep(1)


if __name__ == '__main__':
    # 指定參數
    duration = 500.0
    frequency = 200
    amplitude = 1
    duty_cycle = 0.8
    duty_cycle_phase = 0.1
    phase = np.pi / 2

    # 建立物件
    generator = SquareWaveGenerator(frequency, duration, amplitude, duty_cycle, duty_cycle_phase, phase)

    # 生成方波
    square_wave = generator.generate_duo_square_wave()

    # 播放方波
    generator.play_wave(square_wave)
