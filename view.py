from tkinter import *
from tkinter import ttk

class YouTubeView:
    def __init__(self, root):
        self.root = root
        self.root.geometry('700x450')  # Ajustar tamaño para incluir la salida de consola
        self.root.resizable(0, 0)
        self.root.title("YouTube Downloader & Converter")
        self.root.configure(bg="#F0F0F0")  # Fondo de ventana

        # Título
        title_label = Label(self.root, text='YouTube Video Downloader', font=('Helvetica', 24, 'bold'), bg="#F0F0F0", fg="#333")
        title_label.pack(pady=20)

        # Campo para el link de YouTube
        self.link = StringVar()
        link_label = Label(self.root, text='Pega el link de YouTube aquí:', font=('Helvetica', 16), bg="#F0F0F0")
        link_label.pack(pady=10)
        link_entry = Entry(self.root, width=55, textvariable=self.link, font=('Helvetica', 12), relief=GROOVE, bd=2)
        link_entry.pack(pady=5)

        # Opciones de formato
        self.format_var = StringVar(value="mp3")
        format_label = Label(self.root, text='Formato de salida:', font=('Helvetica', 14), bg="#F0F0F0")
        format_label.pack(pady=15)
        format_combobox = ttk.Combobox(self.root, textvariable=self.format_var, values=["mp3", "flac", "aac"], font=('Helvetica', 12), state="readonly")
        format_combobox.pack()

        # Botón para descargar
        self.download_btn = Button(self.root, text='DESCARGAR', font=('Helvetica', 14, 'bold'), bg='#3498db', fg='white', width=20, relief=FLAT)
        self.download_btn.pack(pady=30)

        # Espacio para mostrar el estado de la operación
        self.status_label = Label(self.root, text='', font=('Helvetica', 12), bg="#F0F0F0", fg="#333")
        self.status_label.pack(pady=10)

        # Barra de progreso (opcional para mostrar progreso de descarga)
        self.progress = ttk.Progressbar(self.root, orient=HORIZONTAL, length=400, mode='determinate')
        self.progress.pack(pady=10)

        # Widget Text para la salida de la consola
        self.console_output = Text(self.root, width=80, height=10, bg="#f2eee3", font=('Helvetica', 10), wrap=WORD, state=DISABLED)
        self.console_output.pack(pady=10)

    def set_status(self, message, color="black"):
        self.status_label.config(text=message, fg=color)

    def update_progress(self, value):
        """Actualiza el valor de la barra de progreso."""
        self.progress['value'] = value

    def append_to_console(self, message):
        """Añade un mensaje al widget de salida de consola."""
        self.console_output.config(state=NORMAL)  # Habilitar el widget para escribir
        self.console_output.insert(END, message + '\n')  # Insertar el mensaje
        self.console_output.see(END)  # Desplazar hacia abajo
        self.console_output.config(state=DISABLED)  # Deshabilitar el widget de nuevo

