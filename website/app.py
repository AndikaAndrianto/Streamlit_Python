from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie



st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#----LOAD ASSETS----
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_bewdaxyv.json")
img_contact_form = Image.open("images/Topology.png")



#----HEADER SECTION----
with st.container():
    st.header("Hi, I'm Andika Andrianto")
    st.title("A Cloud SRE at SoftwareOne")
    st.write("I'm passionate in assisting the world towards a better solution for Infrastrcture.")
    st.write("[Learn more here]>https://www.linkedin.com/in/andika-a-9b773b199/")


#----WHAT I DO----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """Create a News and Media Web App with AWS as Infrastructure:

            Project description
            Working as a team of 10 people, we design a 
            Cloud Infrastructure
            to host the client's Web App.

            Following the clients requirement we had:
                - Build WebApp within budget
                - Testing Security
                - Deploy back-up server that operate alongside the
                 main server.

            Discerning point:
                Purposely let our Cloud Infrastructure
                accessed
                by hacker to be destroyed, 
                we were able to strengthen our Security

            technology used:
                - SQL vs Windows vs AWS

            team size:
                - 10 people

            Team Role:
                Kelsen - Project PIC
                Agus - Main Support
                Rama - Main Support  
                David - Support Cloud Engineer
                Lukas - Support Cloud Engineer
                Andika - IT Security Engineer
                Jacky - IT Security Engineer
                Udin - IT Security Engineer
                Adi - Support DevOps Engineer
                Naufal - Support DevOps Engineer
            """
        )

        st.write("[Learn more here]>https://www.linkedin.com/in/andika-a-9b773b199/")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


#----PROJECT----
with st.container():
    st.write("---")
    st.header("My Project")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        # insert image
        st.image(img_contact_form)

    with text_column:
        st.subheader("Build WebApp Infrastructure")
        st.write(
            """
            Build an AWS Cloud Infrastructure to host a client's WebApp:

            - Satisfy the noted requirements.
            - Built with in budget.
            - Operating Paremeter requirement followed.
            """
        )