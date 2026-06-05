
import math
from tkinter import messagebox

def calculate_fico_score():
    try:
        # USER INPUTS (assumes Tkinter Entry widgets exist globally)
        on_time_payments = int(on_time_payments_entry.get())
        total_payments = int(total_payments_entry.get())

        total_credit_limit = float(total_credit_limit_entry.get())
        total_credit_used = float(total_credit_used_entry.get())

        length_of_credit = float(length_of_credit_entry.get())
        inquiries = int(new_credit_entry.get())

        # VALIDATION
        if total_payments <= 0 or total_credit_limit <= 0:
            messagebox.showerror("Error", "Invalid inputs.")
            return

        missed_payments = max(total_payments - on_time_payments, 0)
        credit_utilization = (total_credit_used / total_credit_limit) * 100

        # PAYMENT HISTORY (35%)
        payment_ratio = on_time_payments / total_payments
        payment_score = 100 * (payment_ratio ** 2.5)
        payment_score = max(payment_score - missed_payments * 6, 0)

        # UTILIZATION (30%)
        if credit_utilization <= 10:
            util_score = 100
        elif credit_utilization <= 30:
            util_score = 90 - (credit_utilization - 10) * 1.0
        elif credit_utilization <= 50:
            util_score = 70 - (credit_utilization - 30) * 1.5
        elif credit_utilization <= 80:
            util_score = 40 - (credit_utilization - 50) * 1.2
        else:
            util_score = max(20 - (credit_utilization - 80) * 0.5, 0)

        # CREDIT AGE (15%)
        length_score = 100 * (math.log(length_of_credit + 1) / math.log(10))
        length_score = min(length_score, 100)

        # INQUIRIES (10%)
        inquiry_score = max(100 - inquiries * 10, 0)

        # MIX (10%)
        mix_score = 70  # simplified placeholder (you can improve later)

        # WEIGHTED SCORE
        raw = (
            payment_score * 0.35 +
            util_score * 0.30 +
            length_score * 0.15 +
            mix_score * 0.10 +
            inquiry_score * 0.10
        )

        # FINAL SCORE (STABLE)
        score = 300 + raw * 5.5
        score = max(300, min(int(score), 850))

        if score >= 750:
            rating = "Excellent"
        elif score >= 700:
            rating = "Good"
        elif score >= 650:
            rating = "Fair"
        else:
            rating = "Poor"

        result_label.config(
            text=f"Estimated FICO Score: {score}/850\\nRating: {rating}\\nUtilization: {credit_utilization:.2f}%"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")
