import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

class LanguageTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")

        self.source_label = ttk.Label(root, text="Source Language:")
        self.source_label.pack(pady=10)
        
        self.source_var = tk.StringVar()
        self.source_combo = ttk.Combobox(root, textvariable=self.source_var, values=list(LANGUAGES.values()))
        self.source_combo.pack(pady=5)

        self.target_label = ttk.Label(root, text="Target Language:")
        self.target_label.pack()

        self.target_var = tk.StringVar()
        self.target_combo = ttk.Combobox(root, textvariable=self.target_var, values=list(LANGUAGES.values()))
        self.target_combo.pack(pady=5)

        self.source_text = tk.Text(root, height=5, width=40)
        self.source_text.pack(pady=10)

        self.translate_button = ttk.Button(root, text="Translate", command=self.translate)
        self.translate_button.pack()

        self.result_label = ttk.Label(root, text="Translation:")
        self.result_label.pack(pady=5)

        self.result_text = tk.Text(root, height=5, width=40, state="disabled")
        self.result_text.pack(pady=10)

    def translate(self):
        source_lang = self.get_language_code(self.source_var.get())
        target_lang = self.get_language_code(self.target_var.get())
        text = self.source_text.get("1.0", "end-1c")
        
        if not source_lang or not target_lang or not text:
            return
        
        translator = Translator()
        translation = translator.translate(text, src=source_lang, dest=target_lang)
        
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", translation.text)
        self.result_text.config(state="disabled")

    def get_language_code(self, language_name):
        for code, name in LANGUAGES.items():
            if name == language_name:
                return code
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslator(root)
    root.mainloop()
