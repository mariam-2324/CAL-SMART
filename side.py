import streamlit as st

def main():
    st.title("Simple Calculator")

    st.write("This is a simple calculator built with Streamlit.")

    # Input fields for numbers
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

    # Dropdown for selecting operation
    operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

    # Perform calculation based on selected operation
    result = None
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero")

# Display result
    if result is not None:
        st.write(f"The result is: {result}")

if __name__ == "__main__":
    main()