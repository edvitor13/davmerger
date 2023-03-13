import tkinter as tk
from tkinter import ttk, messagebox
from typing import Literal

from .editor import Editor


class Interface:

    def __init__(self) -> None:
        self.videos: tuple[str] = self._choice_files()
        self.output_filename: str = self._ask_output_filename()
        self.is_cancel: bool = False
        self.width: int = 1280
        self.height: int = 720
        self.speed: float = 64.0
        self.quality: str = 'veryfast'


    def _choice_files(self) -> tuple[str]:
        from tkinter import Tk, filedialog
        Tk().withdraw()

        videos: tuple[str] | Literal[''] = filedialog.askopenfilenames(
            title="Selecione as gravações", 
            filetypes=(
                ("Arquivos DAV", "*.dav"), 
                ("Todos os arquivos", "*.*")
            )
        )
        
        if not videos:
            return tuple()
        
        return videos


    def _ask_output_filename(self) -> str:
        from tkinter import Tk, filedialog
        Tk().withdraw()

        file_path = filedialog.asksaveasfilename(
            defaultextension=".mp4",
            filetypes=(("Vídeos MP4", "*.mp4"), ("Todos Arquivos", "*.*")),
            title="Salvar arquivo como..."
        )

        return file_path


    def save_video(self) -> bool:
        root = tk.Tk()
        root.withdraw()
        VideoSettingsDialog(root, self)

        if self.is_cancel:
            return False

        try:
            ed = Editor(self.videos)
            ed.save(
                self.output_filename, 
                speed_times=self.speed,
                preset=self.quality,
                width=self.width,
                height=self.height
            )
        except:
            messagebox.showerror(
                "Erro", 
                "Falha ai salvar vídeo"
            )
            return False
        
        return True



class VideoSettingsDialog:

    def __init__(self, parent, interface: Interface) -> None:
        self.parent = parent
        self.interface = interface

        # Crie a janela e configure o título
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Configurações do vídeo")
        self.dialog.protocol("WM_DELETE_WINDOW", self.cancel)

        # Crie a entrada de largura
        # Crie a entrada de largura
        lbl_width = tk.Label(self.dialog, text="Largura:", anchor="e")
        lbl_width.grid(row=0, column=0, padx=5, pady=5, columnspan=1)
        self.ent_width = tk.Entry(self.dialog)
        self.ent_width.grid(row=0, column=1, padx=5, pady=5)
        self.ent_width.insert(0, str(self.interface.width))

        # Crie a entrada de altura
        lbl_height = tk.Label(self.dialog, text="Altura:", anchor="e")
        lbl_height.grid(row=1, column=0, padx=5, pady=5, columnspan=1)
        self.ent_height = tk.Entry(self.dialog)
        self.ent_height.grid(row=1, column=1, padx=5, pady=5)
        self.ent_height.insert(0, str(self.interface.height))

        # Crie a entrada de velocidade
        lbl_speed = tk.Label(self.dialog, text="Aumentar velocidade\nem quantas vezes:")
        lbl_speed.grid(row=2, column=0, padx=5, pady=5)
        self.ent_speed = tk.Entry(self.dialog)
        self.ent_speed.grid(row=2, column=1, padx=5, pady=5)
        self.ent_speed.insert(0, str(self.interface.speed))

        # Crie a caixa de seleção de qualidade
        lbl_quality = tk.Label(self.dialog, text="Tempo de Renderização \n(Interfere na Qualidade):")
        lbl_quality.grid(row=3, column=0, padx=5, pady=5)
        self.quality_var = tk.StringVar(self.dialog)
        self.quality_var.set(self.interface.quality)
        self.cmb_quality = ttk.OptionMenu(self.dialog, self.quality_var, self.interface.quality, *[
            "ultrafast", "superfast", "veryfast", 
            "faster", "medium", "slow", "slower", "veryslow"
        ])
        self.cmb_quality.grid(row=3, column=1, padx=5, pady=5)

        # Crie os botões Cancelar/Salvar
        btn_cancel = tk.Button(self.dialog, text="Cancelar", command=self.cancel)
        btn_cancel.grid(row=4, column=0, padx=5, pady=5)
        btn_save = tk.Button(self.dialog, text="Iniciar", command=self.save_settings)
        btn_save.grid(row=4, column=1, padx=5, pady=5)

        self.quality_var.set(self.interface.quality)
        self.dialog.mainloop()


    def cancel(self):
        self.interface.is_cancel = True
        self.destroy()

    
    def destroy(self):
        self.dialog.destroy()
        self.parent.destroy()
        self.parent.quit()
    

    def save_settings(self):
        # Obtenha os valores de largura, altura, velocidade e qualidade
        width = self.ent_width.get()
        height = self.ent_height.get()
        speed = self.ent_speed.get()
        quality = self.quality_var.get()

        # Valide os valores inseridos pelo usuário
        if not width or not height or not speed:
            messagebox.showerror(
                "Erro", 
                "Por favor, preencha todos os campos."
            )
            return

        try:
            width = int(width)
            height = int(height)
            speed = float(speed)

            if width <= 5 or height <= 5:
                raise ValueError("Invalid resolution")
        except ValueError:
            messagebox.showerror(
                "Erro", 
                "Por favor, insira valores numéricos válidos para largura, altura e velocidade."
            )
            return
        
        self.interface.width = width
        self.interface.height = height
        self.interface.speed = speed
        self.interface.quality = quality
        
        self.destroy()
