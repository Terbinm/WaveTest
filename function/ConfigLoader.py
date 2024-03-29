import configparser
import os


class ConfigLoader:
    def __init__(self, config_dir):
        self.config_dir = config_dir
        self.config_dict = self.load_all_configs()

    @staticmethod
    def convert_value(value):
        try:
            return int(value)
        except ValueError:
            pass

        try:
            return float(value)
        except ValueError:
            pass

        if value.lower() in ('true', 'false'):
            return value.lower() == 'true'

        return value

    def load_config(self, file_path):
        config = configparser.ConfigParser()
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        cleaned_lines = [line.split('#')[0] + '\n' for line in lines]
        config.read_string(''.join(cleaned_lines))
        config_dict = {s: {k: self.convert_value(v) for k, v in config.items(s)} for s in config.sections()}
        return config_dict

    def load_all_configs(self):
        ini_files = [os.path.join(self.config_dir, f) for f in os.listdir(self.config_dir) if f.endswith('.ini')]
        all_configs = {}

        for file in ini_files:
            try:
                data = self.load_config(file)
            except Exception as exc:
                print(f'Generated an exception: {exc}')
            else:
                all_configs.update(data)

        return all_configs
