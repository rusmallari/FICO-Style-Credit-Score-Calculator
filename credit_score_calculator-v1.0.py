# realistic_fico_calculator_12months.py
import tkinter as tk
from tkinter import messagebox

def calculate_fico_score():
    try:
        # Payment History (past 12 months)
        on_time_payments = int(on_time_payments_entry.get())
        total_payments = int(total_payments_entry.get())
        if total_payments <= 0:
            messagebox.showerror("Error", "Total payments must be greater than 0.")
            return
        if on_time_payments > total_payments:
            messagebox.showerror("Error", "On-time payments cannot exceed total payments.")
            return
        payment_history_percent = (on_time_payments / total_payments) * 100

        # Credit Utilization (past 12 months)
        total_credit_limit = float(total_credit_limit_entry.get())
        total_credit_used = float(total_credit_used_entry.get())
        if total_credit_limit <= 0:
            messagebox.showerror("Error", "Total credit limit must be greater than 0.")
            return
        credit_utilization_percent = (total_credit_used / total_credit_limit) * 100
        credit_util_score = max(100 - credit_utilization_percent, 0)

        # Length of Credit History (in years)
        length_of_credit = float(length_of_credit_entry.get())
        length_score = min(length_of_credit * 5, 100)  # scaled to 100

        # Recent Credit Inquiries (past 12 months)
        new_credit_inquiries = int(new_credit_entry.get())
        new_credit_score = max(100 - new_credit_inquiries * 10, 0)

        # Weighted FICO calculation
        score = (
            payment_history_percent * 0.35 +
            credit_util_score * 0.30 +
            length_score * 0.15 +
            new_credit_score * 0.20
        )

        # Scale to 300-850
        score = 300 + (score / 100) * 550
        score = int(score)

        # Rating
        if score >= 750:
            rating = "Excellent"
        elif score >= 700:
            rating = "Good"
        elif score >= 650:
            rating = "Fair"
        else:
            rating = "Poor"

        result_label.config(
            text=f"Estimated FICO Score: {score} / 850\n"
                 f"Rating: {rating}\n"
                 f"Credit Utilization: {credit_utilization_percent:.2f}%\n"
                 f"Payment History (past 12 months): {payment_history_percent:.2f}% on-time"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("FICO Credit Score Calculator (12-Month View)")
root.geometry("550x500")

# Payment History
tk.Label(root, text="Payment History (past 12 months):").pack()
tk.Label(root, text="Enter the number of payments you made ON TIME across all accounts in the past 12 months.").pack()
on_time_payments_entry = tk.Entry(root)
on_time_payments_entry.pack(pady=2)

tk.Label(root, text="Total Payments Scheduled (past 12 months):").pack()
tk.Label(root, text="Enter the total number of scheduled payments across all accounts in the past 12 months.").pack()
total_payments_entry = tk.Entry(root)
total_payments_entry.pack(pady=2)

# Credit Utilization
tk.Label(root, text="Total Credit Limit ($):").pack()
tk.Label(root, text="Sum of all available credit limits across credit cards and revolving accounts.").pack()
total_credit_limit_entry = tk.Entry(root)
total_credit_limit_entry.pack(pady=2)

tk.Label(root, text="Total Credit Used ($):").pack()
tk.Label(root, text="Total outstanding balances you are using currently.").pack()
total_credit_used_entry = tk.Entry(root)
total_credit_used_entry.pack(pady=2)

# Length of Credit History
tk.Label(root, text="Length of Credit History (years):").pack()
tk.Label(root, text="Average or approximate age of your credit accounts.").pack()
length_of_credit_entry = tk.Entry(root)
length_of_credit_entry.pack(pady=2)

# Recent Credit Inquiries
tk.Label(root, text="Recent Credit Inquiries (past 12 months):").pack()
tk.Label(root, text="Number of times lenders have checked your credit in the past 12 months.").pack()
new_credit_entry = tk.Entry(root)
new_credit_entry.pack(pady=2)

tk.Button(root, text="Calculate FICO Score", command=calculate_fico_score).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()
