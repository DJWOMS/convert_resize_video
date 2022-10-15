import os
import typer
import ffmpeg


class Convert:

    SIZE = (
        (640, 360),
        (960, 540),
        (1280, 720),
        (1920, 1080),
    )

    def __init__(self, path, size=None):
        self.path = path
        if size is not None:
            self.SIZE = size

    def create_structure(self, folders: list):
        for i in folders:
            if not os.path.exists(f'{self.path}\\{i}'):
                os.mkdir(f'{self.path}\\{i}')

    def search_files(self):
        folders = []
        files = []
        tree = os.walk(self.path)
        for i in tree:
            files = i[2].copy()

        for file in files:
            part = f'part_{file.split("_")[0][1]}'
            if part not in folders:
                folders.append(part)
        return files, folders

    def resize_video(self, path_file: str, out_put_file: str, w: int, h: int):
        input_file = ffmpeg.input(path_file)
        audio = input_file.audio
        video = input_file.video.filter('scale', w, h)
        out = ffmpeg.output(audio, video, out_put_file, format='mp4', vcodec='h264')
        ffmpeg.run(out, overwrite_output=True, cmd=r'ffmpeg.exe')

    def _run(self, files: list):
        for file in files:
            f = f'part_{file.split("_")[0][1]}'
            for w, h in self.SIZE:
                name = file.split('.')
                self.resize_video(
                    f"{self.path}\\{file}", f"{self.path}\\{f}\\{name[0]}_{h}.{name[1]}", w, h
                )

    def run(self):
        files, folders = self.search_files()
        self.create_structure(folders)
        self._run(files)

        mess = typer.style("Resize done", fg=typer.colors.GREEN)
        typer.echo(mess)

