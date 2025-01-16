import streamlit as st
import openai


# Set your OpenAI API key here


# Title of the app
st.title("SCENE-The Writers Room")

# Sidebar for user navigation
st.sidebar.header("Menu")
menu_option = st.sidebar.radio("Select Option", ["Enter Idea", "About"])

if menu_option == "Enter Idea":
    st.header("Share Your Idea")
    user_idea = st.text_area("Enter a brief idea or theme for the story:")
    
    if st.button("Generate Story"):
        if user_idea.strip():
            with st.spinner("Generating your story..."):
                try:
                    # Generate story using OpenAI API (updated to use ChatCompletion)
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a creative story writer."},
                            {"role": "user", "content": f"Write a creative story based on this idea: {user_idea}"},
                        ],
                        max_tokens=500,
                        temperature=0.7,
                    )
                    story = response["choices"][0]["message"]["content"].strip()
                    st.success("Here's your story:")
                    st.write(story)
                except Exception as e:
                    st.error(f"Error generating story: {e}")
        else:
            st.warning("Please enter an idea before generating a story.")
elif menu_option == "About":
    st.header("About")
    st.write("""
    This application allows you to enter an idea or theme, and it generates a creative story based on your input.
    Built with **Streamlit** and powered by **OpenAI**.
    """)

# Footer
st.sidebar.info("Made with ❤️ using Streamlit and OpenAI")
