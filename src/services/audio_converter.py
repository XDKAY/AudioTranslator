import subprocess


class AudioConverter:
    def __init__(self, path_file_mp3: str):
        self._path_file_mp3 = path_file_mp3

    def convert(self) -> str:
        output_path_file_wav = self._path_file_mp3.replace('mp3', 'wav')
        subprocess.call(['ffmpeg', '-i', self._path_file_mp3, output_path_file_wav])
        return output_path_file_wav