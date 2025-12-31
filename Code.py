import streamlit as st
import google.generativeai as genai

# Setting up the API key
genai.configure(api_key="Enter Your API-Key Here")

# Setting up the headers
st.title("🤖:blue[AI Code Reviewer for Developers!]")
st.subheader(':orange[***Stuck with your code?***]💡')
st.subheader(':orange[***Let me help you debug and optimize!***]🔍')

# Taking user input
user_prompt = st.text_area(
    "Paste your code snippet below 👇", 
    placeholder="Write or paste your code here...", 
    height=250
)
selected_language = st.selectbox(
    "Select your programming language 🎨", 
    ["Select a language...", "Python", "JavaScript", "C++", "Java", "PHP", "Other"]
)

if selected_language != "Select a language...":
    st.write(f"You selected: {selected_language}")
else:
    st.write("Please select a programming language.")

# Prompt setup
sys_prompt = f"""
You are a helpful AI code assistant.
Analyze the given code snippet in "{selected_language}" or try to detect the language if not specified.
Perform the following tasks:
1. Identify bugs or syntax errors.
2. Suggest improvements and optimizations.
3. Highlight potential security concerns.
4. Provide best practices for the specified language.

Ensure your response includes:
- Detailed explanations of the issues.
- Corrected and improved code snippets.
- A clear summary of changes made.

If the input code is invalid, kindly inform the user.
"""

# Setting up the generative model
model = genai.GenerativeModel(model_name="models/gemini-2.5-flash", system_instruction=sys_prompt)

# Generate response when the button is clicked
button = st.button(":green[Review My Code! 🚀]")
if button:
    try:
        response = model.generate_content([user_prompt, sys_prompt])
        st.title(":blue[Your Code Review Results 🌟]")
        # Displaying the response
        st.markdown("### :green[Feedback and Suggestions]")
        st.write(response.text)
    except Exception as e:
        st.error(f"An error occurred: {e}")

