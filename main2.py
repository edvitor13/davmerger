from typing import Literal

from davmerger.editor import Editor


LAST_CHOICE_FILE = ""
LAST_CHOICE_OUTPUT = ""

def choice_files() -> tuple[str]:
    global LAST_CHOICE_FILE

    from tkinter import Tk, filedialog
    Tk().withdraw()

    videos: tuple[str] | Literal[''] = filedialog.askopenfilenames(
        title="Selecione as gravações", 
        filetypes=(
            ("Arquivos DAV", "*.dav"), 
            ("Todos os arquivos", "*.*")
        ),
        initialdir=LAST_CHOICE_FILE,
        initialfile=LAST_CHOICE_FILE
    )

    if videos:
        LAST_CHOICE_FILE = videos[-1]
    
    if not videos:
        return tuple()
    
    return videos


def ask_output_filename() -> str:
    global LAST_CHOICE_OUTPUT

    from tkinter import Tk, filedialog
    Tk().withdraw()

    file_path = filedialog.asksaveasfilename(
        defaultextension=".mp4",
        filetypes=(("Vídeos MP4", "*.mp4"), ("Todos Arquivos", "*.*")),
        title="Salvar arquivo como...",
        initialdir=LAST_CHOICE_OUTPUT,
        initialfile=LAST_CHOICE_OUTPUT
    )

    LAST_CHOICE_OUTPUT = file_path

    return file_path


def save_video(files: tuple[str], output: str) -> bool:
    try:
        ed = Editor(files)
        ed.save(output, speed_times=64.0)
    except Exception as e:
        print(f"Falha ao salvar vídeo: {e}")
        return False
    
    return True


def main():
    all_files: list[dict] = []
    while True:
        files: tuple[str] = choice_files()
        if not files:
            break
        output_file: str = ask_output_filename()

        if not output_file:
            print("Erro fatal! Escolha um arquivo!!")
            exit(1)
        
        all_files.append({
            "files": files,
            "output": output_file
        })

        print(all_files[-1])

    if not all_files:
        print("Erro faltal! Nenhum vídeo selecionado!!")
        exit(1)
    
    for i, file in enumerate(all_files, start=1):
        print(f"{i}/{len(all_files)} Renderizando Vídeo:")
        save_video(file['files'], file['output'])


if __name__ == "__main__":
    main()
