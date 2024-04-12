from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic2.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | santhosh kumar D"
PAGE_ICON = ":wave:"
NAME = "Santhosh Kumar D"
DESCRIPTION = """
I'm a web developer wielding the Web-develop like a seasoned architect. I enjoy building sites & apps. My focus is React (Node.js).
"""
EMAIL = "santhosh.mce1234@gmail.com"
SOCIAL_MEDIA = {
    "💻 LinkedIn": "https://www.linkedin.com/in/santhosh1507/",
    "🔏 GitHub": "https://github.com/Santhosh1507",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

Portfolio ={
    "🌐 https://santhosh-portfolio-web.netlify.app/": "https://santhosh-portfolio-web.netlify.app/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)



with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

st.subheader("My Profile")
st.write("---")


col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=280)
    st.write('\n')
    st.write("---")
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")
    

with col2:
    st.title("Santhosh Kumar D")
    st.write("---")
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


st.write('\n')
st.subheader("About Me")
st.write("---")
st.write(
    """
- ✔️ I'm Graduated from Meenakshi College with a B.E in Computer
Science and Engineering, achieving a total grade point average of
7.4%. My academic journey has equipped me with a solid
foundation and a drive to harness technology in addressing realworld challenges.
- ✔️ To obtain a challenging career in the IT industry and put all my efforts into the growth of the organization and have a great working environment.
- ✔️ An enthusiastic, punctual & carer minded individual with excellent communication and interpersonal skills.
"""
)

st.write('\n')
st.subheader("Education")
st.write("---")
st.write(
    """
- 🏣 Meenakshi College Of Engineering 2020 - 2024
- 🏣 B.E . in Computer Science and Engineering
"""
)

st.write('\n')
st.subheader("Skills")
st.write("---")
st.write(
    """
- 👩‍💻 HTML, CSS, Javascript
- 👩‍💻 Bootstrap, Git
- 👩‍💻 React js, tailwindcss
- 👩‍💻 SQL, MySql, MongoDB
- 👩‍💻 Python
- 👩‍💻 Java
- 👩‍💻 Node js
"""
)

st.write('\n')
st.subheader("Experience")
st.write("---")
st.write(
    """
- 👨🏻‍🎓 Fresher

"""
)

st.write('\n')
st.subheader("Portfolio (Front-End)")
st.write("---")
for portfolio, link in Portfolio.items():
    st.write(f"[{portfolio}]({link})")
st.write("""
- 🤝 Created a Portfolio website to demonstrate my skills and small Projects.
""")

