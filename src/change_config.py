import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
import configparser

CONFIG_FILE = 'config/config.ini'


class ConfigChanger:
    def __init__(self, master):
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_FILE)

        self.root = Toplevel(master)
        self.root.title("Einstellungen")
        self.root.geometry("550x350")
        self.root.resizable(None, None)

        self.api_key_var = tk.StringVar()
        self.api_key_var.set(self.config['OPENAI-API']['apikey'])
        self.api_key_label = ttk.Label(self.root, text="API Key:")
        self.api_key_entry = ttk.Entry(self.root, textvariable=self.api_key_var, width=60)

        self.max_tokens_var = tk.StringVar()
        self.max_tokens_var.set(self.config['OPENAI-API']['MaxTokens'])
        self.max_tokens_label = ttk.Label(self.root, text="Max Tokens:")
        self.max_tokens_entry = ttk.Entry(self.root, textvariable=self.max_tokens_var)

        self.engine_var = tk.StringVar()
        self.engine_var.set(self.config['OPENAI-API']['Engine'])
        self.engine_label = ttk.Label(self.root, text="Engine:")
        self.engine_entry = ttk.Entry(self.root, textvariable=self.engine_var)

        self.temperature_var = tk.StringVar()
        self.temperature_var.set(self.config['OPENAI-API']['Temperature'])
        self.temperature_label = ttk.Label(self.root, text="Temperature:")
        self.temperature_entry = ttk.Entry(self.root, textvariable=self.temperature_var)

        self.save_button = ttk.Button(self.root, text="Save", command=self.save_config)

        self.helper_text = "API-Key: Persönlicher API-Key von Openai. \n\n" \
                           "Max Tokens: Maximale Anzahl von Tokens die für die Anfrage ausgegeben werden soll. \n" \
                           "Derzeit maximum 4096. Request UND Response verbrauchen Tokens. Niemals volle 4000 angeben \n\n" \
                           "Engine: text-davinci-003, text-curie-001, text-babbage-001, text-ada-001\n\n" \
                           "Temperature: Die temperature in der chat gpt API bestimmt den Grad der Kreativität und Abweichung \nder generierten Antworten von der vorherigen Trainingsdaten.\nWerte zwischen 0 - 0.9"
        self.helper_label = ttk.Label(self.root, text=self.helper_text)

        self.api_key_label.grid(row=0, column=0, padx=5, pady=5)
        self.api_key_entry.grid(row=0, column=1, padx=5, pady=5)

        self.max_tokens_label.grid(row=1, column=0, padx=5, pady=5)
        self.max_tokens_entry.grid(row=1, column=1, padx=5, pady=5)

        self.engine_label.grid(row=2, column=0, padx=5, pady=5)
        self.engine_entry.grid(row=2, column=1, padx=5, pady=5)

        self.temperature_label.grid(row=3, column=0, padx=5, pady=5)
        self.temperature_entry.grid(row=3, column=1, padx=5, pady=5)

        self.save_button.grid(row=4, column=1, padx=5, pady=5)

        self.helper_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def save_config(self):
        self.config.set('OPENAI-API', 'apikey', self.api_key_var.get())
        self.config.set('OPENAI-API', 'maxtokens', self.max_tokens_var.get())
        self.config.set('OPENAI-API', 'engine', self.engine_var.get())
        self.config.set('OPENAI-API', 'temperature', self.temperature_var.get())

        with open(CONFIG_FILE, 'w') as configfile:
            self.config.write(configfile)

        self.root.destroy()

