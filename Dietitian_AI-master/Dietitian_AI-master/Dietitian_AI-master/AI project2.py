import tkinter as tk
from tkinter import messagebox

class DietitianApp:
    def __init__(self, master):
        self.master = master
        self.master.title("AI Dietitian")
        self.master.geometry("400x300")

        self.label_weight = tk.Label(master, text="Enter your weight (kg):")
        self.label_weight.pack()

        self.entry_weight = tk.Entry(master)
        self.entry_weight.pack()

        self.label_goal_weight = tk.Label(master, text="Enter your goal weight (kg):")
        self.label_goal_weight.pack()

        self.entry_goal_weight = tk.Entry(master)
        self.entry_goal_weight.pack()

        self.button_calculate = tk.Button(master, text="Calculate Diet Plan", command=self.calculate_diet_plan)
        self.button_calculate.pack()

    def calculate_diet_plan(self):
        try:
            current_weight = float(self.entry_weight.get())
            goal_weight = float(self.entry_goal_weight.get())

            if current_weight <= 0 or goal_weight <= 0:
                raise ValueError("Weights must be positive numbers.")

            if goal_weight >= current_weight:
                messagebox.showinfo("Diet Plan", "You are already at or above your goal weight!")
            else:
                # Example diet plan calculation logic
                calorie_intake = 30 * (current_weight - goal_weight) + 1500
                protein_intake = 0.8 * current_weight  # in grams

                messagebox.showinfo("Diet Plan", f"Calorie Intake: {calorie_intake} kcal\nProtein Intake: {protein_intake} grams")
        except ValueError as e:
            messagebox.showerror("Error", str(e))


def main():
    root = tk.Tk()
    app = DietitianApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
