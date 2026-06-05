import math
from tkinter import messagebox

def calculate_fico_score():
    try:
        # USER INPUTS
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

        # 1. PAYMENT HISTORY (40%) FIXED
        payment_ratio = on_time_payments / total_payments
        payment_score = 100 * (payment_ratio ** 3)
        payment_score = max(payment_score - missed_payments * 5, 0)

        # 2. CREDIT UTILIZATION (30%) (good as-is)
        if credit_utilization <= 10:
            util_score = 100
        elif credit_utilization <= 30:
            util_score = 80
        elif credit_utilization <= 50:
            util_score = 50
        elif credit_utilization <= 80:
            util_score = 30
        else:
            util_score = 10

        # 3. LENGTH OF CREDIT (15%) FIXED (saturation curve)
        length_score = 100 * (math.log(length_of_credit + 1) / math.log(12))
        length_score = min(length_score, 100)

        # 4. HARD INQUIRIES (10%) FIXED (reduced impact)
        if inquiries == 0:
            inquiry_score = 100
        elif inquiries == 1:
            inquiry_score = 85
        elif inquiries <= 3:
            inquiry_score = 70
        elif inquiries <= 5:
            inquiry_score = 50
        else:
            inquiry_score = 25

        # WEIGHTED COMBINATION (FIXED WEIGHTS)
        base_score = (
            payment_score * 0.40 +
            util_score * 0.30 +
            length_score * 0.15 +
            inquiry_score * 0.10
        )

        # FINAL SCALING (FIXED — NO DISTORTION)
        score = 300 + base_score * 5.5
        score = max(300, min(int(score), 850))

        # RATING
        if score >= 750:
            rating = "Excellent"
        elif score >= 700:
            rating = "Good"
        elif score >= 650:
            rating = "Fair"
        else:
            rating = "Poor"

        # OUTPUT
        result_label.config(
            text=f"Estimated FICO Score: {score} / 850\n"
                 f"Rating: {rating}\n"
                 f"Utilization: {credit_utilization:.2f}%\n"
                 f"Missed Payments: {missed_payments}\n"
                 f"Inquiries: {inquiries}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")
