import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from typing import List, Optional
import numpy as np

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Algorithm Visualizer")
        self.setup_main_window()
        self.create_main_buttons()
        
    def setup_main_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = 400
        height = 300
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2        
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.resizable(True, True)
        self.root.overrideredirect(False)
        self.root.attributes('-toolwindow', True)
        
    def create_main_buttons(self):
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True)        
        ttk.Button(frame, text="Disk Scheduling Algorithm", 
            command=self.open_disk_scheduling).pack(pady=10, padx=20, fill=tk.X)
        ttk.Button(frame, text="Page Replacement Algorithm", 
            command=self.open_page_replacement).pack(pady=10, padx=20, fill=tk.X)
    
    def confirm_exit(self, window):
        if messagebox.askyesno("Confirm", "Are you sure you want to go back?"):
            window.destroy()
            self.root.deiconify()
    
    def open_disk_scheduling(self):
        self.root.withdraw()
        DiskSchedulingWindow(self)
    
    def open_page_replacement(self):
        self.root.withdraw()
        PageReplacementWindow(self)
        
    def run(self):
        self.root.mainloop()

class PageReplacementWindow:
    def __init__(self, main_app):
        self.main_app = main_app
        self.window = tk.Toplevel()
        self.window.title("Page Replacement Algorithm")
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        width = 600
        height = 400
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        self.window.resizable(True, True)
        self.window.attributes('-toolwindow', True)
        
    def create_widgets(self):
        input_frame = ttk.Frame(self.window, padding="10")
        input_frame.pack(fill=tk.X)
        ttk.Label(input_frame, text="Number of Page Frames:").pack()
        self.frames_var = tk.StringVar()
        self.frames_entry = ttk.Entry(input_frame, textvariable=self.frames_var)
        self.frames_entry.pack()
        ttk.Label(input_frame, text="Length of Reference String:").pack()
        self.length_var = tk.StringVar()
        self.length_entry = ttk.Entry(input_frame, textvariable=self.length_var)
        self.length_entry.pack()
        self.confirm_btn = ttk.Button(input_frame, text="Confirm", 
            command=self.on_confirm, state=tk.DISABLED)
        self.confirm_btn.pack(pady=10)
        self.ref_string_frame = ttk.Frame(self.window, padding="10")
        self.ref_string_frame.pack(fill=tk.X)
        algo_frame = ttk.Frame(self.window, padding="10")
        algo_frame.pack(fill=tk.X)
        self.algo_var = tk.StringVar()
        ttk.Radiobutton(algo_frame, text="FIFO", variable=self.algo_var, 
                       value="FIFO").pack()
        ttk.Radiobutton(algo_frame, text="LRU", variable=self.algo_var, 
                       value="LRU").pack()
        ttk.Radiobutton(algo_frame, text="Optimal", variable=self.algo_var, 
                       value="Optimal").pack()
        self.calc_btn = ttk.Button(self.window, text="Calculate", 
                                 command=self.calculate, state=tk.DISABLED)
        self.calc_btn.pack(pady=10)
        nav_frame = ttk.Frame(self.window, padding="10")
        nav_frame.pack(side=tk.BOTTOM, fill=tk.X)
        ttk.Button(nav_frame, text="Back", 
                  command=lambda: self.main_app.confirm_exit(self.window)).pack(side=tk.LEFT)
        ttk.Button(nav_frame, text="Home", 
                  command=lambda: self.main_app.confirm_exit(self.window)).pack(side=tk.LEFT)
        self.frames_var.trace('w', self.validate_inputs)
        self.length_var.trace('w', self.validate_inputs)
        
    def validate_inputs(self, *args):
        try:
            frames = int(self.frames_var.get())
            length = int(self.length_var.get())
            if frames > 0 and length > 0:
                self.confirm_btn.config(state=tk.NORMAL)
            else:
                self.confirm_btn.config(state=tk.DISABLED)
        except ValueError:
            self.confirm_btn.config(state=tk.DISABLED)
            
    def on_confirm(self):
        for widget in self.ref_string_frame.winfo_children():
            widget.destroy()
        self.ref_entries = []
        length = int(self.length_var.get())
        for i in range(length):
            entry = ttk.Entry(self.ref_string_frame, width=5)
            entry.pack(side=tk.LEFT, padx=2)
            entry.bind('<KeyRelease>', self.validate_ref_string)
            self.ref_entries.append(entry)
            
    def validate_ref_string(self, event):
        valid = True
        ref_string = []
        for entry in self.ref_entries:
            value = entry.get().strip()
            if value.isdigit() and 0 <= int(value) <= 9:
                ref_string.append(int(value))
            else:
                valid = False
                break
        if valid and self.algo_var.get():
            self.calc_btn.config(state=tk.NORMAL)
        else:
            self.calc_btn.config(state=tk.DISABLED)
            
    def calculate(self):
        frames = int(self.frames_var.get())
        ref_string = [int(entry.get()) for entry in self.ref_entries]
        algorithm = self.algo_var.get()
        result_window = tk.Toplevel(self.window)
        result_window.title(f"{algorithm} Page Replacement Results")
        tree = ttk.Treeview(result_window, columns=('Step', 'Memory', 'Fault'), 
            show='headings')
        tree.heading('Step', text='Step')
        tree.heading('Memory', text='Memory Frame')
        tree.heading('Fault', text='Page Fault')
        memory = [None] * frames
        faults = 0
        if algorithm == "FIFO":
            frame_ages = [0] * frames 
            current_time = 0
            for i, page in enumerate(ref_string):
                if page not in memory:
                    fault = True
                    if None in memory:
                        frame_index = memory.index(None)
                    else:
                        frame_index = frame_ages.index(min(frame_ages))
                    memory[frame_index] = page
                    frame_ages[frame_index] = current_time
                    faults += 1
                else:
                    fault = False
                current_time += 1
                tree.insert('', 'end', values=(i + 1, str(memory), 'Yes' if fault else 'No'))
        elif algorithm == "LRU":
            last_used = [0] * frames  
            current_time = 0
            for i, page in enumerate(ref_string):
                if page not in memory:
                    fault = True
                    if None in memory:
                        frame_index = memory.index(None)
                    else:
                        frame_index = last_used.index(min(last_used))
                    memory[frame_index] = page
                    faults += 1
                else:
                    fault = False
                    frame_index = memory.index(page)
                
                last_used[frame_index] = current_time
                current_time += 1
                tree.insert('', 'end', values=(i + 1, str(memory), 'Yes' if fault else 'No'))
                
        elif algorithm == "Optimal":
            for i, page in enumerate(ref_string):
                if page not in memory:
                    fault = True
                    if None in memory:
                        frame_index = memory.index(None)
                    else:
                        future_use = []
                        for frame_page in memory:
                            try:
                                next_use = ref_string[i+1:].index(frame_page) + i + 1
                            except ValueError:
                                next_use = float('inf') 
                            future_use.append(next_use)
                        frame_index = future_use.index(max(future_use))
                    memory[frame_index] = page
                    faults += 1
                else:
                    fault = False
                tree.insert('', 'end', values=(i + 1, str(memory), 'Yes' if fault else 'No'))
        tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        ttk.Label(result_window, text=f"Total Page Faults: {faults}").pack(pady=5)

class DiskSchedulingWindow:
    def __init__(self, main_app):
        self.main_app = main_app
        self.window = tk.Toplevel()
        self.window.title("Disk Scheduling Algorithm")
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        width = 600
        height = 400
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        self.window.resizable(True, True)
        self.window.attributes('-toolwindow', True)
        
    def create_widgets(self):
        input_frame = ttk.Frame(self.window, padding="10")
        input_frame.pack(fill=tk.X)
        ttk.Label(input_frame, text="Number of Cylinders:").pack()
        self.cylinders_var = tk.StringVar()
        self.cylinders_entry = ttk.Entry(input_frame, textvariable=self.cylinders_var)
        self.cylinders_entry.pack()
        ttk.Label(input_frame, text="Initial Head Position:").pack()
        self.head_var = tk.StringVar()
        self.head_entry = ttk.Entry(input_frame, textvariable=self.head_var)
        self.head_entry.pack()
        ttk.Label(input_frame, text="Number of Disk Requests:").pack()
        self.requests_var = tk.StringVar()
        self.requests_entry = ttk.Entry(input_frame, textvariable=self.requests_var)
        self.requests_entry.pack()
        self.confirm_btn = ttk.Button(input_frame, text="Confirm", 
            command=self.on_confirm, state=tk.DISABLED)
        self.confirm_btn.pack(pady=10)
        self.request_frame = ttk.Frame(self.window, padding="10")
        self.request_frame.pack(fill=tk.X)
        algo_frame = ttk.Frame(self.window, padding="10")
        algo_frame.pack(fill=tk.X)
        self.algo_var = tk.StringVar()
        ttk.Radiobutton(algo_frame, text="FCFS", variable=self.algo_var, 
            value="FCFS", command=self.update_direction_state).pack()
        ttk.Radiobutton(algo_frame, text="SSTF", variable=self.algo_var, 
            value="SSTF", command=self.update_direction_state).pack()
        ttk.Radiobutton(algo_frame, text="SCAN", variable=self.algo_var, 
            value="SCAN", command=self.update_direction_state).pack()
        ttk.Radiobutton(algo_frame, text="C-SCAN", variable=self.algo_var, 
            value="C-SCAN", command=self.update_direction_state).pack()
        ttk.Radiobutton(algo_frame, text="LOOK", variable=self.algo_var, 
            value="LOOK", command=self.update_direction_state).pack()
        ttk.Radiobutton(algo_frame, text="C-LOOK", variable=self.algo_var, 
            value="C-LOOK", command=self.update_direction_state).pack()
        direction_frame = ttk.Frame(self.window, padding="10")
        direction_frame.pack(fill=tk.X)
        self.direction_var = tk.StringVar()
        self.left_radio = ttk.Radiobutton(direction_frame, text="Left", 
                                         variable=self.direction_var, value="left", 
                                         state=tk.DISABLED)
        self.right_radio = ttk.Radiobutton(direction_frame, text="Right", 
                                          variable=self.direction_var, value="right", 
                                          state=tk.DISABLED)
        self.left_radio.pack(side=tk.LEFT)
        self.right_radio.pack(side=tk.LEFT)
        self.calc_btn = ttk.Button(self.window, text="Calculate", 
                                 command=self.calculate, state=tk.DISABLED)
        self.calc_btn.pack(pady=10)
        nav_frame = ttk.Frame(self.window, padding="10")
        nav_frame.pack(side=tk.BOTTOM, fill=tk.X)
        ttk.Button(nav_frame, text="Back", 
                  command=lambda: self.main_app.confirm_exit(self.window)).pack(side=tk.LEFT)
        ttk.Button(nav_frame, text="Home", 
                  command=lambda: self.main_app.confirm_exit(self.window)).pack(side=tk.LEFT)
        self.cylinders_var.trace('w', self.validate_inputs)
        self.head_var.trace('w', self.validate_inputs)
        self.requests_var.trace('w', self.validate_inputs)
        
    def validate_inputs(self, *args):
        try:
            cylinders = int(self.cylinders_var.get())
            head = int(self.head_var.get())
            requests = int(self.requests_var.get())
            if cylinders > 0 and 0 <= head < cylinders and requests > 0:
                self.confirm_btn.config(state=tk.NORMAL)
            else:
                self.confirm_btn.config(state=tk.DISABLED)
        except ValueError:
            self.confirm_btn.config(state=tk.DISABLED)
            
    def update_direction_state(self):
        if self.algo_var.get() in ["SCAN", "C-SCAN", "LOOK", "C-LOOK"]:
            self.left_radio.config(state=tk.NORMAL)
            self.right_radio.config(state=tk.NORMAL)
        else:
            self.left_radio.config(state=tk.DISABLED)
            self.right_radio.config(state=tk.DISABLED)
        self.validate_all()
            
    def on_confirm(self):
        for widget in self.request_frame.winfo_children():
            widget.destroy()
        self.request_entries = []
        requests = int(self.requests_var.get())
        for i in range(requests):
            entry = ttk.Entry(self.request_frame, width=5)
            entry.pack(side=tk.LEFT, padx=2)
            entry.bind('<KeyRelease>', self.validate_requests)
            self.request_entries.append(entry)
            
    def validate_requests(self, event):
        valid = True
        requests = []
        max_cylinder = int(self.cylinders_var.get()) - 1
        for entry in self.request_entries:
            try:
                value = int(entry.get())
                if 0 <= value <= max_cylinder:
                    requests.append(value)
                else:
                    valid = False
                    break
            except ValueError:
                valid = False
                break
        self.validate_all()
    
    def validate_all(self):
        valid_requests = all(entry.get().isdigit() for entry in getattr(self, 'request_entries', []))
        valid_algo = bool(self.algo_var.get())
        valid_direction = True
        if self.algo_var.get() in ["SCAN", "C-SCAN", "LOOK", "C-LOOK"]:
            valid_direction = bool(self.direction_var.get())
        if valid_requests and valid_algo and valid_direction:
            self.calc_btn.config(state=tk.NORMAL)
        else:
            self.calc_btn.config(state=tk.DISABLED)

    def calculate(self):
        cylinders = int(self.cylinders_var.get())
        initial_head = int(self.head_var.get())
        requests = [int(entry.get()) for entry in self.request_entries]
        algorithm = self.algo_var.get()
        direction = self.direction_var.get() if algorithm in ["SCAN", "C-SCAN", "LOOK", "C-LOOK"] else None
        result_window = tk.Toplevel(self.window)
        result_window.title(f"{algorithm} Disk Scheduling Results")
        result_window.geometry("800x600")
        fig, ax = plt.subplots(figsize=(10, 6))
        sequence = [initial_head]
        total_seek_time = 0
        if algorithm == "FCFS":
            sequence.extend(requests)
        elif algorithm == "SSTF":
            remaining = requests.copy()
            current = initial_head
            while remaining:
                next_request = min(remaining, key=lambda x: abs(x - current))
                sequence.append(next_request)
                current = next_request
                remaining.remove(next_request)
        elif algorithm == "SCAN":
            remaining = sorted(requests)
            if direction == "right":
                for req in remaining:
                    if req >= initial_head:
                        sequence.append(req)
                sequence.append(cylinders - 1)
                for req in reversed(remaining):
                    if req < initial_head:
                        sequence.append(req)
            else:
                for req in reversed(remaining):
                    if req <= initial_head:
                        sequence.append(req)
                sequence.append(0)
                for req in remaining:
                    if req > initial_head:
                        sequence.append(req)
        elif algorithm == "C-SCAN":
            remaining = sorted(requests)
            if direction == "right":
                for req in remaining:
                    if req >= initial_head:
                        sequence.append(req)
                sequence.append(cylinders - 1)
                sequence.append(0)
                for req in remaining:
                    if req < initial_head:
                        sequence.append(req)
            else:
                for req in reversed(remaining):
                    if req <= initial_head:
                        sequence.append(req)
                sequence.append(0)
                sequence.append(cylinders - 1)
                for req in reversed(remaining):
                    if req > initial_head:
                        sequence.append(req)
        elif algorithm == "LOOK":
            remaining = sorted(requests)
            if direction == "right":
                for req in remaining:
                    if req >= initial_head:
                        sequence.append(req)
                for req in reversed(remaining):
                    if req < initial_head:
                        sequence.append(req)
            else:
                for req in reversed(remaining):
                    if req <= initial_head:
                        sequence.append(req)
                for req in remaining:
                    if req > initial_head:
                        sequence.append(req)
        elif algorithm == "C-LOOK":
            remaining = sorted(requests)
            if direction == "right":
                for req in remaining:
                    if req >= initial_head:
                        sequence.append(req)
                for req in remaining:
                    if req < initial_head:
                        sequence.append(req)
            else:
                for req in reversed(remaining):
                    if req <= initial_head:
                        sequence.append(req)
                for req in reversed(remaining):
                    if req > initial_head:
                        sequence.append(req)
        for i in range(len(sequence)-1):
            total_seek_time += abs(sequence[i+1] - sequence[i])
        points_y = range(len(sequence))
        ax.plot(sequence, points_y, 'b-o')
        ax.set_xlabel('Cylinder Number')
        ax.set_ylabel('Request Sequence')
        ax.set_title(f'{algorithm} Disk Scheduling\nTotal Seek Time: {total_seek_time} cylinders')
        ax.grid(True)
        ax.set_xlim(-1, cylinders)
        for i, (x, y) in enumerate(zip(sequence, points_y)):
            ax.annotate(f'({x})', (x, y), textcoords="offset points", xytext=(0,10), ha='center')
        canvas = FigureCanvasTkAgg(fig, master=result_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        ttk.Label(result_window, text=f"Total Seek Time: {total_seek_time} cylinders").pack(pady=5)

def main():
    app = MainApp()
    app.run()

if __name__ == "__main__":
    main()
