# Credit Score Calculator

A C-based command-line application that estimates a user's credit score based on common credit factors such as payment history, credit utilization, account age, credit mix, and recent credit inquiries.

## Features

* Calculates an estimated credit score
* User-friendly menu interface
* Accepts multiple credit-related inputs
* Provides credit score category feedback
* Fast and lightweight command-line execution

## Credit Factors Considered

* Payment History
* Credit Utilization Ratio
* Length of Credit History
* Credit Mix
* New Credit Inquiries

## Technologies Used

* C Programming Language
* GCC Compiler

## Getting Started

### Prerequisites

* GCC Compiler
* Terminal or Command Prompt

### Installation

1. Clone the repository:

```bash
git clone https://github.com/rusmallari/CS-Calculator.git
```

2. Navigate to the project folder:

```bash
cd CS-Calculator
```

3. Compile the program:

```bash
gcc credit_score_calculator.c -o credit_calculator
```

4. Run the application:

```bash
./credit_calculator
```

For Windows:

```bash
credit_calculator.exe
```

## Example

```text
===== Credit Score Calculator =====

Enter Payment History Score (0-100): 95
Enter Credit Utilization (%): 20
Enter Length of Credit History (Years): 5
Enter Number of Credit Accounts: 4
Enter Recent Credit Inquiries: 1

Estimated Credit Score: 742

Credit Rating: Very Good
```

## Learning Objectives

This project was developed to strengthen knowledge of:

* C Programming
* Functions and Modular Design
* User Input Validation
* Conditional Logic
* Financial Data Processing
* Algorithm Design

## Future Improvements

* More accurate FICO-style calculations
* Graphical User Interface (GUI)
* Credit improvement recommendations
* Score history tracking
* Data export functionality

## Disclaimer

This calculator provides educational estimates only and does not represent an official FICO® or VantageScore® credit score.

## License

This project is open source and available under the MIT License.

