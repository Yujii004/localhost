
import tkinter as tk
from tkinter import ttk, messagebox

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор перевода единиц")
        self.root.geometry("350x280")
        self.root.resizable(False, False)

        self.unit_to_meters = {
            'м': 1,
            'км': 1000,
            'см': 0.01,
            'мм': 0.001
        }

        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        title_label = ttk.Label(self.root, text="Калькулятор перевода единиц", font=("Segoe UI", 14, "bold"))
        title_label.pack(pady=10)

        value_frame = ttk.Frame(self.root)
        value_frame.pack(pady=5, fill="x", padx=20)

        ttk.Label(value_frame, text="Введите значение:").pack(anchor="w")
        self.value_var = tk.StringVar()
        self.value_entry = ttk.Entry(value_frame, textvariable=self.value_var)
        self.value_entry.pack(fill="x")

        # Единица "Из"
        from_frame = ttk.Frame(self.root)
        from_frame.pack(pady=5, fill="x", padx=20)
        ttk.Label(from_frame, text="Из единиц:").pack(anchor="w")

        self.from_unit_var = tk.StringVar(value='м')
        self.from_unit_combo = ttk.Combobox(from_frame, textvariable=self.from_unit_var, values=list(self.unit_to_meters.keys()), state="readonly")
        self.from_unit_combo.pack(fill="x")

        # Единица "В"
        to_frame = ttk.Frame(self.root)
        to_frame.pack(pady=5, fill="x", padx=20)
        ttk.Label(to_frame, text="В единицы:").pack(anchor="w")

        self.to_unit_var = tk.StringVar(value='км')
        self.to_unit_combo = ttk.Combobox(to_frame, textvariable=self.to_unit_var, values=list(self.unit_to_meters.keys()), state="readonly")
        self.to_unit_combo.pack(fill="x")

        # Кнопка перевода
        convert_btn = ttk.Button(self.root, text="Перевести", command=self.com)
        convert_btn.pack(pady=15, padx=20, fill="x")

        # Результат
        self.result_label = ttk.Label(self.root, text="", font=("Segoe UI", 12, "bold"), foreground="#007700")
        self.result_label.pack(pady=5)
        
    def com(self):
        value = float(self.value_var.get())
    
        from_unit = self.from_unit_var.get()
        to_unit = self.to_unit_var.get()

        # Перевод в метры
        value_in_meters = value * self.unit_to_meters[from_unit]
        # Перевод в целевые единицы
        converted_value = value_in_meters / self.unit_to_meters[to_unit]

        self.result_label.config(text=f"{value} {from_unit} = {converted_value:.4f} {to_unit}")

def main():
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

