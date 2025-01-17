import streamlit as st
from openai import OpenAI

    # Set up OpenAI API key
honey = OpenAI(api_key=st.secrets["OPENAI"]["OPENAI_API_KEY"])

def generate_story():
        prompt = "Generate a unique and interesting movie storyline with a title."
        response = honey.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="gpt-3.5-turbo",
            max_tokens=4096,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()

def suggest_director(storyline):
        prompt = f"Based on the following movie storyline, suggest the best director and explain why:\n\n{storyline}"
        response = honey.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="gpt-3.5-turbo",
            max_tokens=4096,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()

def suggest_cast(storyline):
        prompt = f"Based on the following movie storyline, suggest the best cast for each character and explain why:\n\n{storyline}"
        response = honey.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="gpt-3.5-turbo",
            max_tokens=4096,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()

st.title("PLoT-AI: The Movie Storyline Generator")

if st.button("Create New Story"):
        storyline = generate_story()
        st.subheader("Storyline")
        st.write(storyline)

        director_suggestion = suggest_director(storyline)
        st.subheader("Director Suggestion")
        st.write(director_suggestion)

        cast_suggestion = suggest_cast(storyline)
        st.subheader("Cast Suggestion")
        st.write(cast_suggestion)