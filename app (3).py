import streamlit as st

st.set_page_config(page_title="Temperature Converter", page_icon="🌡️")

# App title
st.title("🌡️ Simple Temperature Converter")

# Input
temp = st.number_input("Enter temperature value:", value=0.0)

# Conversion choice
conversion = st.radio(
    "Choose conversion type:",
    ["Celsius → Fahrenheit", "Fahrenheit → Celsius", "Celsius → Kelvin", "Kelvin → Celsius"]
)

# Conversion logic
if conversion == "Celsius → Fahrenheit":
    result = (temp * 9/5) + 32
    st.success(f"{temp} °C = {result:.2f} °F")

elif conversion == "Fahrenheit → Celsius":
    result = (temp - 32) * 5/9
    st.success(f"{temp} °F = {result:.2f} °C")

elif conversion == "Celsius → Kelvin":
    result = temp + 273.15
    st.success(f"{temp} °C = {result:.2f} K")

elif conversion == "Kelvin → Celsius":
    result = temp - 273.15
    st.success(f"{temp} K = {result:.2f} °C")

# Footer
st.caption("Made with ❤️ using Streamlit on Hugging Face")
