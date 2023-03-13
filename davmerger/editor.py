from typing import Iterable
import ffmpeg


class Editor:

    def __init__(self, videos: Iterable[str]) -> None:
        self.video = self._concat(videos)
    

    def _concat(self, videos: Iterable[str]):
        return ffmpeg.concat(*[ffmpeg.input(v) for v in videos])
    

    def save(
        self, 
        output_filename: str, 
        speed_times: float = 1, 
        preset: str = "veryfast",
        width: int = 1280,
        height: int = 720,
        codec: str = "libx264",
        maxrate: str = "3000k"
    ) -> None:
        if type(speed_times) is not float or speed_times <= 0:
            speed_times = 1

        if speed_times != 1:
            self.video = ffmpeg.filter(self.video, 'setpts', f'{1/speed_times}*PTS')
        
        self.video = ffmpeg.output(
            self.video, 
            filename=output_filename,
            vcodec=codec, 
            maxrate=maxrate,
            preset=preset,
            s=f'{width}x{height}'
        )

        print("Comando enviado: ")
        print(
            ffmpeg.compile(
                self.video, 
                cmd='ffmpeg', 
                overwrite_output=False
            )
        )
        print()

        print("Rodando FFMPEG: ")
        ffmpeg.run(self.video, overwrite_output=True)
