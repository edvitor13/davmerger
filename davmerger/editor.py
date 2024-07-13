from typing import Iterable
import ffmpeg


class Editor:

    def __init__(self, videos: Iterable[str]) -> None:
        self.video = None
        self.audio = None
        self._load_and_concat_video_audio(videos)
    

    def _load_and_concat_video_audio(self, videos: Iterable[str]):
        self.video = ffmpeg.concat(*[ffmpeg.input(v) for v in videos], v=1, a=0)
        self.audio = ffmpeg.concat(*[ffmpeg.input(v).audio for v in videos], v=0, a=1)

    
    def save(
        self, 
        output_filename: str, 
        speed_times: float = 1, 
        preset: str = "veryfast",
        width: int = 1920,
        height: int = 1080,
        codec: str = "libx264",
        maxrate: str = "3000k",
        frame_rate: int = 24,
        use_audio: bool = True
    ) -> None:
        if type(speed_times) is not float or speed_times <= 0:
            speed_times = 1
        
        if speed_times != 1:
            self.video = ffmpeg.filter(self.video, 'setpts', f'{1/speed_times}*PTS')
            self.audio = ffmpeg.filter(self.audio, 'atempo', speed_times)
        else:
            self.video = self.video
            self.audio = self.audio

        streams = [self.video]
        if use_audio:
            streams = [
                self.video, 
                self.audio
            ]

        self.output = ffmpeg.output(
            *streams,
            filename=output_filename,
            vcodec=codec, 
            acodec='aac',  # Codec de áudio
            maxrate=maxrate,
            preset=preset,
            r=frame_rate,
            s=f'{width}x{height}'
        )

        print("Comando enviado: ")
        print(
            ffmpeg.compile(
                self.output, 
                cmd='ffmpeg', 
                overwrite_output=False
            )
        )
        print()

        print("Rodando FFMPEG: ")
        ffmpeg.run(self.output, overwrite_output=True)
