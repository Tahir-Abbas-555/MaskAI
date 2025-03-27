import streamlit as st
from transformers import pipeline
import random

# Set page config at the very beginning
st.set_page_config(page_title="The Great Text Alchemist", page_icon="🧙‍♂️", layout="centered", initial_sidebar_state="collapsed")

@st.cache_resource
def load_unmasker():
    return pipeline('fill-mask', model='distilbert-base-uncased')

unmasker = load_unmasker()

app_title = "The Great Text Alchemist"
app_subtitle = "Unveil the Hidden Words with AI Magic ✨"
thinking_emojis = ["🤔", "🧐", "💡"]
result_emojis = ["🎉", "🔮", "✨"]
# Sample result emojis


inspiration_texts = [
    "The quick brown [MASK] jumps over the lazy dog.",
    "To be or not to [MASK], that is the question.",
    "May the [MASK] be with you.",
    "All that glitters is not [MASK].",
    "A [MASK] in time saves nine.",
    "Where there's a [MASK], there's a way.",
]

# Ensure session state tracks user input
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

def main():
    st.title(f"{app_title} 🪄")
    st.subheader(app_subtitle)
    st.markdown("---")

    # --- User Input Area ---
    st.subheader("Enter a sentence with a masked word:")
    st.info('Replace the word you want the AI to guess with `[MASK]` (case-insensitive).')

    # Display input box
    user_input = st.text_area("Your masked sentence:", value=st.session_state.user_input, height=100)

    # Update session state when user types
    if user_input:
        st.session_state.user_input = user_input

    # Button to get a random sample sentence
    if st.button("Use a Sample Sentence 🎲"):
        st.session_state.user_input = random.choice(inspiration_texts)
        st.rerun()  # Rerun app to update text area

    # Process user input when button is clicked
    if st.button(f"Reveal the Magic! {thinking_emojis[-1]}"):
        if "[MASK]" not in st.session_state.user_input.upper():  # Case insensitive check
            st.warning("Please include `[MASK]` in your sentence for me to work my magic!")
        else:
            with st.spinner(f"The AI is pondering... {random.choice(thinking_emojis)}"):
                try:
                    predictions = unmasker(st.session_state.get("user_input", ""))
                    st.markdown("---")

                    # Stylish Header with Gradient
                    st.markdown(f"""
                        <h2 style="color: #ff7b00; text-align: center; font-size: 28px;">
                            {random.choice(result_emojis)} AI's Best Predictions
                        </h2>
                        <p style="text-align: center; font-size: 16px; color: #666;">
                            Based on your input, here are the AI's top guesses:
                        </p>
                    """, unsafe_allow_html=True)

                    # Beautiful Result Cards
                    for i, prediction in enumerate(predictions):
                        st.markdown(f"""
                            <div style="
                                background: linear-gradient(135deg, #1e293b, #334155); 
                                padding: 15px; 
                                margin: 10px 0; 
                                border-radius: 12px; 
                                box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
                                color: white;
                            ">
                                <h4 style="margin: 0; font-size: 20px;">🚀 Rank {i+1}: {prediction['token_str']}</h4>
                                <p style="margin: 5px 0 0; font-size: 16px;">
                                    Confidence Score: <b>{prediction['score']:.4f}</b>
                                </p>
                            </div>
                        """, unsafe_allow_html=True)

                except Exception as e:
                    st.markdown("<hr>", unsafe_allow_html=True)
                    st.markdown(f"""
                        <div style="background: #ffdddd; padding: 15px; border-radius: 8px; color: #900;">
                            <b>⚠️ Error:</b> {e}
                        </div>
                    """, unsafe_allow_html=True)
                    st.markdown("<p style='color: #666; text-align: center;'>Please check your input and try again.</p>", unsafe_allow_html=True)

                    st.markdown("---")
                    st.info(
                        "This app uses the `distilbert-base-uncased` model from the `transformers` library to predict the masked word in your sentence. "
                        "It's a demonstration of masked language modeling."
                    )
    st.markdown("---")
    st.markdown("""
        <div style="display: flex; align-items: center;">
            <div style="flex: 0 0 auto; margin-right: 20px;">
                <img src="https://media.licdn.com/dms/image/v2/D4E35AQGaNpMhYXgzJg/profile-framedphoto-shrink_200_200/B4EZUhqRjOH0AY-/0/1740026485311?e=1743714000&v=beta&t=6M5gUJ9LzEzC4_sDlzDA7G55BbzkeCFJXo5-f7BZXls" 
                    alt="Profile Image" width="200" style="border-radius: 10px;">
            </div>
            <div>
                <h3>👨‍💻 <b>Developed by:</b> Tahir Abbas Shaikh</h3>
                <p>📧 <b>Email:</b> <a href="mailto:tahirabbasshaikh555@gmail.com">tahirabbasshaikh555@gmail.com</a></p>
                <p>📍 <b>Location:</b> Sukkur, Sindh, Pakistan</p>
                <p>💼 <b>LinkedIn/GitHub:</b> <a href="https://github.com/Tahir-Abbas-555" target="_blank">Tahir-Abbas-555</a></p>
                <p>📁 <b>LinkedIn/HuggingFace:</b> <a href="https://huggingface.co/Tahir5" target="_blank">Tahir5</a></p>
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
