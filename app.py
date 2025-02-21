import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", project_icon= "⭐")
st.title("Growth Mindset AI Project!")
st.header("Welcome to my New Project")
st.write("This is a simple test app.")

#quote section

st.header("Quotes of the Day")

quotes = [
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "If you're going through hell, keep going.",
    "Don't let fear hold you back. Fear is a powerful emotion. It's what makes us human.",
    "Believe you can and you're halfway there."
]
st.header("Whats your Challenge Today")
user_input = st.text_input("Describe a chaalenge you are facing..")

#Condition

if user_input:
    st.success(f"You are facing:{user_input}.keep pushing forward towards your goal")
else:
    st.warning("Tell us about your challenge to get started.")

    #Reflexing
    st.header("Reflect on your Learning")
    reflection = st.text_area("Write your reflection here")
    if reflection: 
        st.success(f"Great! Insight your Reflection:{reflection}")
    else:
        st.info("Reflecting on Past Experience Help You Grow! Share Your Difficulties..")

        #Achievements
        st.header("Celebrate Your Win")
        achievement = st.text_input("Share something You have recently accomplished")
        if achievement:
            st.success(f"Congratulations! Your achievement:{achievement}")
        else:
            st.info("Achievements are the catalysts to unlock new growth opportunities!")

            #Footer
            st.write("- - -")
            st.write("Keep believing in Yourself")
            st.write("💖Powered by Annu")