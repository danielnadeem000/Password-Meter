import streamlit as st
import random
import string

# List of commonly used weak passwords
COMMON_PASSWORDS = {"password", "123456", "123456789", "qwerty", "abc123", "password1", "123123"}

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Uppercase & lowercase check
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    # Digit check
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include at least one digit (0-9).")
    
    # Special character check
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    # Check against common passwords
    if password in COMMON_PASSWORDS:
        score = 1  # Automatically weak if it's in the blacklist
        feedback.append("This is a commonly used password. Choose a more secure one.")
    
    # Determine password strength level
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    return strength, score, feedback

# Function to generate a strong random password
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("Password Strength Meter")
st.header("Password Strength Meter")
st.subheader("Check the strength of your password or generate a strong one.")

# User password input
password = st.text_input("Enter your password:", type="password")
if st.button("Check Strength"):
    if password:
        strength, score, feedback = check_password_strength(password)
        st.write(f"**Strength:** {strength} ({score}/5)")
        
        if feedback:
            st.warning("\n".join(feedback))
        else:
            st.success("Great! Your password is strong.")
    else:
        st.error("Please enter a password to check.")

# Password Generator Button
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.success(f"Generated Password: `{strong_password}`")
