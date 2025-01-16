import streamlit as st
import requests

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo"

HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# Function to generate a story using Hugging Face
def generate_story_with_huggingface(user_idea):
    try:
        payload = {"inputs": f"Write a creative story based on this idea: {user_idea}"}
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        if response.status_code == 200:
            generated_text = response.json()
            return generated_text[0]["generated_text"]
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Function to rewrite a story
def rewrite_story_with_huggingface(story):
    try:
        payload = {"inputs": f"Rewrite the following story to improve it: {story}"}
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        if response.status_code == 200:
            generated_text = response.json()
            return generated_text[0]["generated_text"]
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# App UI starts here
# Page Config
st.set_page_config(page_title="SCENE - The Writers Room", layout="wide")

# App Title and Styling
st.markdown(
    """
    <style>
        .main-header {
            font-size: 40px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
            margin-bottom: 30px;
        }
        .sidebar .sidebar-content {
            background-color: #F9F9F9;
        }
        .option-buttons {
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
        }
        .tab-header {
            font-size: 24px;
            color: #4CAF50;
            margin-top: 20px;
        }
        .footer {
            margin-top: 50px;
            text-align: center;
            font-size: 14px;
            color: #888888;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-header">SCENE - The Writers Room</div>', unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.header("Menu")
menu_option = st.sidebar.radio("Select an Option", ["New Story", "Rewrite", "Edit", "About"])

# Content Section
if menu_option == "New Story":
    st.markdown('<div class="tab-header">New Story</div>', unsafe_allow_html=True)
    user_idea = st.text_area("Enter a brief idea or theme for the story:")
    if st.button("Generate"):
        if user_idea.strip():
            with st.spinner("Generating your story..."):
                story = generate_story_with_huggingface(user_idea)
                st.success("Here's your story:")
                st.write(story)
        else:
            st.warning("Please enter an idea before generating a story.")

elif menu_option == "Rewrite":
    st.markdown('<div class="tab-header">Rewrite</div>', unsafe_allow_html=True)
    story_to_rewrite = st.text_area("Paste the story you want to rewrite:")
    if st.button("Rewrite"):
        if story_to_rewrite.strip():
            with st.spinner("Rewriting your story..."):
                rewritten_story = rewrite_story_with_huggingface(story_to_rewrite)
                st.success("Here's the rewritten story:")
                st.write(rewritten_story)
        else:
            st.warning("Please enter a story before rewriting.")

elif menu_option == "Edit":
    st.markdown('<div class="tab-header">Edit</div>', unsafe_allow_html=True)
    story_to_edit = st.text_area("Paste the story you want to edit:")
    edit_options = st.selectbox("Choose an edit action", ["Improve Grammar", "Shorten", "Elaborate"])
    if st.button("Edit"):
        if story_to_edit.strip():
            with st.spinner(f"Performing '{edit_options}' on your story..."):
                edited_story = rewrite_story_with_huggingface(story_to_edit)  # Reusing the rewrite function for demo
                st.success("Here's your edited story:")
                st.write(edited_story)
        else:
            st.warning("Please enter a story before editing.")

elif menu_option == "About":
    st.markdown('<div class="tab-header">About</div>', unsafe_allow_html=True)
    st.write("""
        SCENE - The Writers Room is a platform that allows you to generate, rewrite, or edit creative stories with the help of AI.
        Powered by **Hugging Face** and built using **Streamlit**.
    """)

# Footer
st.markdown('<div class="footer">Made with ❤️ by SCENE - The Writers Room Team</div>', unsafe_allow_html=True)
