import streamlit as st
import openai

import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Streamlit app
st.title("Joke Decipher")

# Text box for user to input a joke
joke_input = st.text_area("Enter your joke here:")

# Submit button
if st.button("Submit"):
    if joke_input:
        # Call OpenAI API to get the explanation
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "developer", "content": "Talk like a pirate."},
                    {
                        "role": "user",
                        "content": f"Explain this joke: {joke_input}",
                    },
                        ],
                )


            explanation = response.choices[0].message.content
            #Display the explanation
            st.subheader("Explanation")
            st.write(explanation)

            # Display a related GIF (you can replace the URL with a relevant GIF)
            #gif_url = "https://media.giphy.com/media/3o7aD2sa3g1Y2z5Y4I/giphy.gif"  # Example GIF URL
            #st.image(gif_url, caption="Here's a funny GIF related to your joke!", use_container_width=True)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a joke before submitting.")