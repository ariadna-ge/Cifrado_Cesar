import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
from tkinter import PhotoImage
from conexion import insertar_mensaje
from cifrado import cifra_cesar

class CifradorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cifrador César")
        self.root.geometry("700x600")
        self.root.configure(background="#5F99AE")

        self.style = ttk.Style()
        self.style.configure("TFrame", background="#E4EFE7")
        self.style.configure("TButton", background="#27548A", font=("Century Gothic", 12, "bold"),  foreground="#27548A")
        self.style.configure("TLabel", background="#E4EFE7", font=("Century Gothic", 14, "bold"), foreground="#48A6A7")

        self.animacion_activa = False
        self.llave_var = tk.IntVar(value=3)

        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        try:
            self.icono_img = PhotoImage(file="logo.png")
            icono_label = tk.Label(main_frame, image=self.icono_img, background="#E4EFE7")
            icono_label.pack(pady=(0, 5)) 
        except tk.TclError as e:
            print(f"Error al cargar la imagen del icono: {e}")
        
        titulo = tk.Label(main_frame, text="CIFRADOR CÉSAR", fg="#006A71", font=("Century Gothic", 21, "bold"), background="#E4EFE7")
        titulo.pack(pady=10)

        frame_entrada = ttk.Frame(main_frame)
        frame_entrada.pack(fill=tk.X, pady=10)

        lbl_entrada = ttk.Label(frame_entrada, text="Texto a cifrar:")
        lbl_entrada.pack(anchor=tk.W)

        self.entrada_texto = tk.Text(frame_entrada, height=3, width=50, font=("Century Gothic", 11))
        self.entrada_texto.pack(fill=tk.X, pady=5)

        frame_opciones = ttk.Frame(main_frame)
        frame_opciones.pack(fill=tk.X, pady=5)

        lbl_llave = ttk.Label(frame_opciones, text="Llave César:")
        lbl_llave.pack(side=tk.LEFT, padx=(5, 5))

        llave_spin = ttk.Spinbox(frame_opciones, from_=1, to=25, textvariable=self.llave_var, width=5)
        llave_spin.pack(side=tk.LEFT, padx=5)

        frame_botones = ttk.Frame(main_frame)
        frame_botones.pack(fill=tk.X, pady=10)

        self.btn_cifrar = ttk.Button(frame_botones, text="CIFRAR", command=self.iniciar_cifrado)
        self.btn_cifrar.pack(side=tk.LEFT, padx=5)

        self.btn_limpiar = ttk.Button(frame_botones, text="LIMPIAR", command=self.limpiar)
        self.btn_limpiar.pack(side=tk.LEFT, padx=5)

        frame_resultado = ttk.Frame(main_frame)
        frame_resultado.pack(fill=tk.BOTH, expand=True, pady=10)

        lbl_resultado = ttk.Label(frame_resultado, text="Resultado:")
        lbl_resultado.pack(anchor=tk.W)

        self.frame_animacion = tk.Frame(frame_resultado, bg="#ffffff", bd=1, relief=tk.SUNKEN)
        self.frame_animacion.pack(fill=tk.BOTH, expand=True, pady=5)

        self.lbl_animacion = tk.Label(self.frame_animacion, bg="#ffffff", fg="#000000", 
                                      font=("Courier", 14), anchor=tk.W, justify=tk.LEFT)
        self.lbl_animacion.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.barra_estado = ttk.Label(root, text="Listo", relief=tk.SUNKEN, anchor=tk.W, background="#5F99AE", foreground="white", font=("Century Gothic", 10))
        self.barra_estado.pack(fill=tk.X, side=tk.BOTTOM, pady=2)

    def iniciar_cifrado(self):
        if self.animacion_activa:
            return

        self.animacion_activa = True
        self.btn_cifrar.config(state=tk.DISABLED)
        self.barra_estado.config(text="Cifrando...")

        texto_original = self.entrada_texto.get("1.0", "end-1c")
        if not texto_original:
            self.barra_estado.config(text="No hay texto para cifrar")
            self.btn_cifrar.config(state=tk.NORMAL)
            self.animacion_activa = False
            return

        texto_cifrado = cifra_cesar(texto_original, self.llave_var.get())

        insertar_mensaje(texto_original, texto_cifrado)

        self.root.after(100, lambda: self.animar_cifrado(texto_original, texto_cifrado, 0))

    def animar_cifrado(self, texto_original, texto_cifrado, indice):
        if indice <= len(texto_original):
            texto_mostrado = texto_cifrado[:indice]
            if indice < len(texto_original):
                caracteres_aleatorios = ''.join(random.choice(string.ascii_letters + string.digits) 
                                                for _ in range(len(texto_original) - indice))
                texto_mostrado += caracteres_aleatorios

            self.lbl_animacion.config(text=texto_mostrado)
            tiempo_espera = 50 if indice < len(texto_original) else 500
            self.root.after(tiempo_espera, lambda: self.animar_cifrado(texto_original, texto_cifrado, indice + 1))
        else:
            self.barra_estado.config(text="Cifrado completado")
            self.btn_cifrar.config(state=tk.NORMAL)
            self.animacion_activa = False

    def limpiar(self):
        self.entrada_texto.delete("1.0", tk.END)
        self.lbl_animacion.config(text="")
        self.barra_estado.config(text="Listo")

if __name__ == "__main__":
    root = tk.Tk()
    app = CifradorApp(root)
    root.mainloop()