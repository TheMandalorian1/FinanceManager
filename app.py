import streamlit as st

def calculate_remaining_income(monthly_income, education, food, rent, transport, general_expenses):
    total_expenses = education + food + rent + transport + general_expenses
    remaining_income = monthly_income - total_expenses
    remaining_after_deduction = remaining_income - (0.3 * remaining_income)
    return remaining_after_deduction

def check_income_interval(remaining_amount):
    if remaining_amount < 10000:
        return "Your remaining amount is less than 10000."
    elif remaining_amount < 50000:
        return "Your remaining amount is between 10000 and 50000."
    else:
        return "Your remaining amount is above 100000."

def main():
    st.title("Monthly Income Analysis")
    st.write("Enter your monthly income and expenses:")

    monthly_income = st.number_input("Monthly Income", min_value=0.0, step=1000.0)
    education = st.number_input("Education Expenses", min_value=0.0, step=100.0)
    food = st.number_input("Food Expenses", min_value=0.0, step=100.0)
    rent = st.number_input("Rent Expenses", min_value=0.0, step=100.0)
    transport = st.number_input("Transport Expenses", min_value=0.0, step=100.0)
    general_expenses = st.number_input("General Expenses/Others", min_value=0.0, step=100.0)

    remaining_amount = calculate_remaining_income(monthly_income, education, food, rent, transport, general_expenses)
    interval_result = check_income_interval(remaining_amount)

    st.write("Remaining Amount after Expenses:", remaining_amount)
    st.write(interval_result)

if __name__ == "__main__":
    main()
