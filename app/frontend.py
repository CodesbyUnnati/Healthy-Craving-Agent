import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.absppath(__file__))))

import streamlit as st
from app.graph import app as agent_app

st.set_page_config(page_title="Healthy Craving AI", page_icon="🍱")
st.title("🍱 Healthy Craving Agent")

craving=st.text_input("What are your cravings?")

if st.button("Generate Healthy Recipe"):
    if not craving:
        st.warning("Please enter a craving first!")
    else:
        with st.spinner("👩🏻‍🍳 Chef is cooking..."):
            try:
                initial_state= {"user_craving": craving}
                result= agent_app.invoke(initial_state)

                analysis= result.get("analysis", "")
                recipe= result.get("final_recipe", "")

                st.subheader("🕵🏻‍♀️Analysis")
                st.info(analysis)

                if "INVALID" not in analysis:
                    st.subheader("🔖 The Healthy Swap")
                    st.success(recipe)

            except Exception as e:
                st.error(f"Error: {e}")