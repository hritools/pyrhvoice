import os
import subprocess
from tempfile import TemporaryDirectory
from uuid import uuid4


__all__ = ['RHVoice']


class RHVoice:
    def __init__(self, workdir :str =None, default_voice=None):
        if workdir:
            self.workdir = workdir
        else:
            self._tempdir = TemporaryDirectory()
            self.workdir = self._tempdir.name
        self._voice = default_voice or 'aleksandr'


    def get_audio_path(self, text :str, voice :str =None) -> str:
        voice = voice or self._voice
        name = uuid4().hex
        path = os.path.join(self.workdir, name)
        self._gen(text, path, voice)
        return path

    def get_audio(self, text :str, voice :str =None) -> bytes:
        path = self.get_audio_path(text, voice)
        with open(path, 'rb') as f:
            data = f.read()
        return data

    def play(self, text :str, voice :str =None) -> None:
        subprocess.run(['RHVoice-test', '-p', voice or self._voice], input=text.encode())

    def _gen(self, text :str, path :str, voice :str) -> None:
        txt_path = path + '.txt'
        params = ['RHVoice-test', '-i', txt_path, '-o', path, '-p', voice]
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text)
        proc = subprocess.Popen(params, stdin=subprocess.PIPE)
        proc.wait()
