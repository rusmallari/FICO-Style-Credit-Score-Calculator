# FICO Credit Score Estimator

An interactive web-based credit score estimator built with vanilla HTML, CSS, and JavaScript. Enter your financial details and get an estimated FICO score with a full breakdown of each contributing factor.

**Live demo:** [rusmallari.github.io/CS-Calculator](https://rusmallari.github.io/CS-Calculator)

---

## Features

- **Dynamic account input** — add multiple credit cards, car loans, student loans, mortgages, and personal loans; only include what applies to you
- **Per-factor score breakdown** — see exactly how payment history, utilization, history length, credit mix, and new inquiries contribute to your score
- **Realistic scoring model** — tiered utilization penalties, logarithmic history curve, late payment recency weighting, derogatory mark caps, and installment loan softening
- **Improvement tips** — personalized advice based on your result
- **How to fill this out guide** — plain-English instructions for every input field
- **FAQ section** — answers to common credit score questions
- **Fully responsive** — works on mobile and desktop

---

## How It Works

The estimator uses FICO's publicly documented weighting model:

| Factor | Weight |
|--------|--------|
| Payment history | 35% |
| Credit utilization | 30% |
| Length of credit history | 15% |
| Credit mix | 10% |
| New inquiries | 10% |

### Scoring details

**Payment history** is calculated from the ratio of on-time payments to total scheduled payments across all accounts, then adjusted based on the recency of any late payments. Recent late payments are penalized more heavily than older ones.

**Credit utilization** uses a tiered curve rather than a linear penalty — utilization under 9% scores perfectly, with progressively steeper penalties above 30% and 50%. Accounts with installment loans receive a softened utilization penalty, reflecting real FICO's more lenient treatment of borrowers with diverse credit types.

**History length** uses a logarithmic curve so early years of credit history are rewarded significantly, with diminishing but continued returns past 20 years. There is no hard cap.

**Credit mix** rewards having both revolving credit (cards) and installment loans (car, student, mortgage) active simultaneously.

**New inquiries** deduct points per hard inquiry in the past 12 months, with a floor of 0.

**Derogatory marks** apply hard score caps — collections cap the score at 720, bankruptcy at 650, regardless of other factors.

The weighted composite is then scaled to the 300–850 FICO range.

---

## Usage

No installation or build step required. Open `index.html` directly in any browser, or visit the live GitHub Pages deployment.

```bash
# Clone the repo
git clone https://github.com/rusmallari/CS-Calculator.git
cd CS-Calculator

# Open in browser
open index.html
```

---

## Disclaimer

This tool is for **educational purposes only**. It is not affiliated with or endorsed by FICO, Equifax, Experian, or TransUnion. Actual credit scores are calculated by credit bureaus using proprietary models with additional data points not captured here. Do not use this as a substitute for your official credit report.

---

## Tech Stack

- HTML5
- CSS3 (custom properties, CSS Grid, animations)
- Vanilla JavaScript (no frameworks or dependencies)

---

## License

This project is open source and available under the MIT License.

