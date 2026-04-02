import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Proposal", page_icon="💍")

# صورة القطة
img = Image.open("cat.jpg")
st.image(img, width=400)

# العنوان
st.title("💍Do you marry me💍?")

# حالة الزرار NO
if 'no_x' not in st.session_state:
    st.session_state['no_x'] = 0
    st.session_state['no_y'] = 0
if 'color' not in st.session_state:
    st.session_state['color'] = "#ff6666"

# زرار YES
YES = st.button("هوافق و امري لله", key="yes")

# CSS لتحريك زرار NO + تغيير لونه
no_style = f"""
    <style>
    div[data-testid="stButton"][aria-label="😓لا مش فاضية😓"] > button {{
        position: relative;
        left: {st.session_state['no_x']}px;
        top: {st.session_state['no_y']}px;
        background-color: {st.session_state['color']};
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }}
    </style>
"""
st.markdown(no_style, unsafe_allow_html=True)

# زرار NO
NO = st.button("😓لا مش فاضية😓", key="no")

# لو ضغطت YES
if YES:
    st.balloons()
    st.success("مبروك ياباشا")
    with open(r"C:\Users\Kariim\OneDrive\Desktop\COURSES\AI\PROPOSAL\proposal.pptx", "rb") as file:
        st.download_button("Download Proposal", file.read(), "proposal.pptx")

# لو ضغطت NO
if NO:
    # يغير مكان الزرار عشوائي
    st.session_state['no_x'] = random.randint(-100, 200)
    st.session_state['no_y'] = random.randint(-50, 200)
    # يغير اللون عشوائي
    colors = ["#ff6666", "#66b3ff", "#99ff99", "#ffcc99", "#ff99c8"]
    st.session_state['color'] = random.choice(colors)
    msgs = [
        "ليه مش فاضية🤨؟",
        "طب خدي فكرة🥲",
        "اديني فرصة🥺",
        "وبعدين في العناد ده😒",
        "انا يقالي ساعتين بعمل الكود ده😭",
        "جربي تدوسي على الزرار التاني🥸"
    ]
    st.warning(random.choice(msgs))

