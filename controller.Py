import sys
import time
from tkinter import END
from model import YouTubeModel
from view import YouTubeView



class YouTubeController:
    def __init__(self, root):
        self.model = YouTubeModel()  # Crear instancia del modelo
        self.view = YouTubeView(root)  # Crear instancia de la vista

        # Conectar la acción del botón a la función correspondiente
        self.view.download_btn.config(command=self.download_video)

    def download_video(self):
        video_url = self.view.link.get()  # Obtener link desde la vista
        select_format = self.view.format_var.get()  # Obtener formato seleccionado
        success, message = self.model.download_video(video_url, select_format)  # Llamar al modelo para descargar el video

        if success:
            self.view.set_status(message, color="green")
        else:
            self.view.set_status("ERROR EN DESCARGA", color="red")
def download_video(self):
    video_url = self.view.link.get()
    select_format = self.view.format_var.get()
    
    # Redirigir salida a Text widget
    sys.stdout = StreamToText(self.view.console_output)
    # Simulación del progreso de descarga (puedes conectarlo con la lógica real)
    for i in range(101):
        self.view.update_progress(i)  # Actualiza la barra de progreso
        self.view.root.update_idletasks()  # Actualiza la interfaz gráfica
        time.sleep(0.05)  # Simulación de retraso

    success, message = self.model.download_video(video_url, select_format)
    
    if success:
        self.view.set_status(message, color="green")
    else:
        self.view.set_status("ERROR EN DESCARGA", color="red")
        
# Redirigir la salida
class StreamToText:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(END, message)
        self.text_widget.see(END)  # Desplazar hacia abajo

    def flush(self):
        pass  # No es necesario para el uso básico
