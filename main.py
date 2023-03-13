from davmerger.interface import Interface

i = Interface()

print("Videos Escolhidos:")
print(i.videos)
print()

print("Vídeo final será salvo em:")
print(i.output_filename)
print()

print("Executando Edição via FFMPEG: ")
i.save_video()
