import tkinter as tk
from tkinter import messagebox

class Workout:
    def __init__(self, date, exercise_type, duration, calories_burned):
        self.date = date
        self.exercise_type = exercise_type
        self.duration = duration
        self.calories_burned = calories_burned

    def __str__(self):
        return f"{self.date}: {self.exercise_type} for {self.duration} minutes, {self.calories_burned} calories burned"

class User:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def view_workouts(self):
        return "\n".join(str(workout) for workout in self.workouts)

    def save_data(self, filename):
        with open(filename, 'w') as file:
            for workout in self.workouts:
                file.write(f"{workout.date},{workout.exercise_type},{workout.duration},{workout.calories_burned}\n")

    def load_data(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                date, exercise_type, duration, calories_burned = line.strip().split(',')
                workout = Workout(date, exercise_type, int(duration), int(calories_burned))
                self.workouts.append(workout)

def add_workout(user, entry_date, entry_exercise, entry_duration, entry_calories):
    date = entry_date.get()
    exercise_type = entry_exercise.get()
    try:
        duration = int(entry_duration.get())
        calories_burned = int(entry_calories.get())
        workout = Workout(date, exercise_type, duration, calories_burned)
        user.add_workout(workout)
        messagebox.showinfo("Success", "Workout added successfully!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for duration and calories!")

def view_workouts(user, label_view):
    workouts = user.view_workouts()
    label_view.config(text=f"{user.name}'s Workouts:\n{workouts if workouts else 'No workouts added yet.'}")

def save_data(user, entry_filename):
    filename = entry_filename.get()
    if filename:
        user.save_data(filename)
        messagebox.showinfo("Success", "Data saved successfully!")
    else:
        messagebox.showerror("Error", "Please enter a filename!")

def load_data(user, entry_filename, label_view):
    filename = entry_filename.get()
    try:
        user.load_data(filename)
        messagebox.showinfo("Success", "Data loaded successfully!")
        view_workouts(user, label_view)
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found! Please check the filename and try again.")

def main():
    root = tk.Tk()
    root.title("Workout Tracker")
    root.geometry("500x400")
    root.configure(bg="#f0f8ff")  # Light blue background

    # User Information
    label_name = tk.Label(root, text="Enter your name:", bg="#f0f8ff", font=("Arial", 12))
    label_name.pack(pady=10)
    entry_name = tk.Entry(root, font=("Arial", 12))
    entry_name.pack(pady=5)

    label_age = tk.Label(root, text="Enter your age:", bg="#f0f8ff", font=("Arial", 12))
    label_age.pack(pady=10)
    entry_age = tk.Entry(root, font=("Arial", 12))
    entry_age.pack(pady=5)

    label_weight = tk.Label(root, text="Enter your weight:", bg="#f0f8ff", font=("Arial", 12))
    label_weight.pack(pady=10)
    entry_weight = tk.Entry(root, font=("Arial", 12))
    entry_weight.pack(pady=5)

    user = None

    def create_user():
        nonlocal user
        name = entry_name.get()
        try:
            age = int(entry_age.get())
            weight = float(entry_weight.get())
            user = User(name, age, weight)
            messagebox.showinfo("Success", f"User {user.name} created!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for age and weight!")

    # Workout Information
    label_date = tk.Label(root, text="Enter workout date (YYYY-MM-DD):", bg="#f0f8ff", font=("Arial", 12))
    label_date.pack(pady=10)
    entry_date = tk.Entry(root, font=("Arial", 12))
    entry_date.pack(pady=5)

    label_exercise = tk.Label(root, text="Enter exercise type:", bg="#f0f8ff", font=("Arial", 12))
    label_exercise.pack(pady=10)
    entry_exercise = tk.Entry(root, font=("Arial", 12))
    entry_exercise.pack(pady=5)

    label_duration = tk.Label(root, text="Enter duration (minutes):", bg="#f0f8ff", font=("Arial", 12))
    label_duration.pack(pady=10)
    entry_duration = tk.Entry(root, font=("Arial", 12))
    entry_duration.pack(pady=5)

    label_calories = tk.Label(root, text="Enter calories burned:", bg="#f0f8ff", font=("Arial", 12))
    label_calories.pack(pady=10)
    entry_calories = tk.Entry(root, font=("Arial", 12))
    entry_calories.pack(pady=5)

    label_filename = tk.Label(root, text="Enter filename (for saving/loading data):", bg="#f0f8ff", font=("Arial", 12))
    label_filename.pack(pady=10)
    entry_filename = tk.Entry(root, font=("Arial", 12))
    entry_filename.pack(pady=5)

    label_view = tk.Label(root, text="Workouts will appear here.", bg="#f0f8ff", font=("Arial", 12))
    label_view.pack(pady=20)

    # Buttons
    button_create_user = tk.Button(root, text="Create User", command=create_user, bg="#4CAF50", fg="white", font=("Arial", 12))
    button_create_user.pack(pady=10)

    button_add_workout = tk.Button(root, text="Add Workout", command=lambda: add_workout(user, entry_date, entry_exercise, entry_duration, entry_calories), bg="#4CAF50", fg="white", font=("Arial", 12))
    button_add_workout.pack(pady=10)

    button_view_workouts = tk.Button(root, text="View Workouts", command=lambda: view_workouts(user, label_view), bg="#4CAF50", fg="white", font=("Arial", 12))
    button_view_workouts.pack(pady=10)

    button_save_data = tk.Button(root, text="Save Data", command=lambda: save_data(user, entry_filename), bg="#4CAF50", fg="white", font=("Arial", 12))
    button_save_data.pack(pady=10)

    button_load_data = tk.Button(root, text="Load Data", command=lambda: load_data(user, entry_filename, label_view), bg="#4CAF50", fg="white", font=("Arial", 12))
    button_load_data.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
