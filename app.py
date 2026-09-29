import streamlit as st
import openai

# 1. App Configuration and Design
st.set_page_config(page_title="Zlender.ai", page_icon="🧊", layout="centered")

st.title("🧊 Zlender.ai - Blender Python Code Generator")
st.write("Welcome to your 3D course web app! Create Blender scripts instantly using AI.")
st.markdown("---")

# 2. Sidebar for API Key
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("OpenAI API Key:", type="password", placeholder="sk-...")
    st.markdown("---")
    st.info("Please enter your OpenAI API Key in the sidebar to use this app.")

# 3. Main Screen - User Input
user_prompt = st.text_area(
    "What would you like to create in Blender?",
    placeholder="e.g., Create a low-poly tree or coffee mug..."
)

if st.button("🚀 Generate Blender Script", type="primary"):
    if not api_key:
        st.error("⚠️ Please enter your OpenAI API Key in the sidebar first!")
    elif not user_prompt:
        st.warning("⚠️ Please write a prompt to describe your 3D model.")
    else:
        with st.spinner("✨ AI is generating your code... Please wait."):
            try:
                # Connecting to OpenAI API
                client = openai.OpenAI(api_key=api_key)
                
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are an expert Blender Python (bpy) developer. Write only clean, executable Blender Python code based on the user's request."},
                        {"role": "user", "content": user_prompt}
                    ]
                )
                
                code_result = response.choices[0].message.content
                
                st.success("🎉 Code generated successfully!")
                
                # Displaying Code and Download Button
                st.subheader("📜 Generated Blender Python Code:")
                st.code(code_result, language="python")
                
                st.download_button(
                    label="📥 Download Script (.py)",
                    data=code_result,
                    file_name="blender_script.py",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"❌ An error occurred (Check your API Key): {e}")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Zlender.ai - Built with Streamlit</p>", unsafe_allow_html=True)
