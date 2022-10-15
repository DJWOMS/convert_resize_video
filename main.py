import os
import typer
import ffmpeg


def create_structure(path: str, folders: list):
    for i in folders:
        if not os.path.exists(f'{path}\\{i}'):
            os.mkdir(f'{path}\\{i}')


def search_files(path: str):
    folders = []
    files = []
    tree = os.walk(path)
    for i in tree:
        files = i[2].copy()

    for file in files:
        part = f'part_{file.split("_")[0][1]}'
        if part not in folders:
            folders.append(part)
    return files, folders


def resize_video(path_file: str, out_put_file: str, w: int, h: int):
    input_file = ffmpeg.input(path_file)
    audio = input_file.audio
    video = input_file.video.filter('scale', w, h)
    out = ffmpeg.output(audio, video, out_put_file, format='mp4', vcodec='h264')
    ffmpeg.run(out, overwrite_output=True, cmd=r'ffmpeg.exe')


def main():
    typer.echo("New resize")
    path = typer.prompt("Path")
    SIZE = (
        (640, 360),
        (960, 540),
        (1280, 720),
        (1920, 1080),
    )

    files, folders = search_files(path)
    create_structure(path, folders)

    for file in files:
        f = f'part_{file.split("_")[0][1]}'
        for w, h in SIZE:
            name = file.split('.')
            resize_video(f"{path}\\{file}", f"{path}\\{f}\\{name[0]}_{h}.{name[1]}", w, h)

    mess = typer.style("Resize done", fg=typer.colors.GREEN)
    typer.echo(mess)


if __name__ == '__main__':
    main()
