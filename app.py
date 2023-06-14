import streamlit as st
from streamlit_helper import get_chapter_summary_data, get_verse_numbers, get_chapter_number, get_verse_data, get_chapter_name, get_translation, get_verse_commentary_data, get_gita_dhyanam, read_gita_dhyanam, get_chapter_summary_commentry


st.sidebar.title("Bhagavad Gita")

gita_type = st.sidebar.selectbox(label="Select the type: ", options=["Gita Dhyanam", "Verse Explanation", "Chapter Summary"])

if gita_type == "Chapter Summary":

    chapter_number = st.sidebar.selectbox(label="Enter The Chapter Number: ", options=get_chapter_number())
    
    if st.sidebar.button("Get Summary"):

        st.image("data/gita/chapters_img/{}.jpg".format(chapter_number), width=600)
        
        chapter_data = get_chapter_summary_data(chapter_number=chapter_number)
        audio_file = open('data/gita/audio/chapters_summary/{}.mpga'.format(chapter_number), 'rb').read()

        st.markdown("""<h3 style="color: yellow;">Chapter Name: {} ({})</h3>""".format(chapter_data["name"], chapter_data["name_meaning"]), unsafe_allow_html=True)
        st.markdown("""<h3 style="color: yellow;">Chapter Number: {}</h3>""".format(chapter_number), unsafe_allow_html=True)
        st.markdown("""<h6 style="color: brown;">Audible Verses of chapter {}</h6>""".format(chapter_number), unsafe_allow_html=True)
        st.audio(audio_file, format="audio/mpga")
        st.markdown("""<h3 style="color: brown;">Chapter Summary</h3>""", unsafe_allow_html=True)
        st.markdown(chapter_data["chapter_summary_hindi"])
        st.markdown("""<h6 style="color: brown;">Chapter Summary (English)</h6>""", unsafe_allow_html=True)
        st.markdown(chapter_data["chapter_summary"])
        st.markdown("""<h3 style="color: brown;">Bhagavad Gita Chapter {} Summary and Commentary by Swami Paramarthananda</h3>""".format(chapter_number), unsafe_allow_html=True)
        st.markdown(get_chapter_summary_commentry(chapter_number), unsafe_allow_html=True)

if gita_type == "Verse Explanation":
    chapter_number = st.sidebar.selectbox(label="Enter The Chapter Number: ", options=get_chapter_number())
    verse_number = st.sidebar.selectbox(label="Enter The Verse Number: ", options=get_verse_numbers(chapter_number))
    
    if st.sidebar.button("Get Verse"):

        st.image("data/gita/chapters_img/{}.jpg".format(chapter_number), width=600)

        chapter_name = get_chapter_name(chapter_number)
        verse_data = get_verse_data(chapter_number, verse_number)
        verse_commentary_data = get_verse_commentary_data(chapter_number, verse_number)
        audio_file = open('data/gita/audio/verse_recitation/{}/{}.mp3'.format(chapter_number, verse_number), 'rb').read()

        st.markdown("""<h3 style="color: yellow;">Chapter Name: {}</h3>""".format(chapter_name), unsafe_allow_html=True)
        st.markdown("""<h3 style="color: yellow;">Verse Number: {}</h3>""".format(verse_data["verse_number"]), unsafe_allow_html=True)
        st.markdown("""<h3 style="color: brown;">Verse Text</h3>""", unsafe_allow_html=True)
        st.markdown(verse_data["text"])
        st.markdown("""<h6 style="color: brown;">Transliteration</h6>""", unsafe_allow_html=True)
        st.markdown(verse_data["transliteration"])
        st.markdown("""<h6 style="color: brown;">Verse Audio</h6>""", unsafe_allow_html=True)
        st.audio(audio_file, format='audio/mp3')
        st.markdown("""<h3 style="color: brown;">Translation</h3>""", unsafe_allow_html=True)
        st.markdown("""<h6 style="color: brown;">Word Meanings</h6>""", unsafe_allow_html=True)
        st.markdown(verse_data["word_meanings"])
        st.markdown("""<h6 style="color: brown;">Hindi Translation</h6>""", unsafe_allow_html=True)
        st.markdown(get_translation(chapter_number, verse_number, "hindi", "Swami Ramsukhdas"))
        st.markdown("""<h6 style="color: brown;">English Translation</h6>""", unsafe_allow_html=True)
        st.markdown(get_translation(chapter_number, verse_number, "english", "Swami Gambirananda"))
        st.markdown("""<h3 style="color: brown;">Commentary</h3>""", unsafe_allow_html=True)
        st.markdown(verse_commentary_data["commentary"])



if gita_type == "Gita Dhyanam":
    
    gita_dhyanam = get_gita_dhyanam()
    audio_file = open('data/gita/audio/Geeta-Dhyanam.m4a', 'rb').read()
    
    st.title("Gita Dhyanam")
    st.image("data/gita/gita_dhyanam_img.jpeg", width=700)

    st.markdown("""<h5 style="color: brown;">Gita Dhyanam Audio</h5>""", unsafe_allow_html=True)
    st.audio(audio_file, format='audio/m4a' )
    
    st.divider()
    for dhyanam in gita_dhyanam:
        st.markdown("""<h3 style="color: brown;">{}</h3>""".format(dhyanam["verse_sanskrit"]), unsafe_allow_html=True)
        st.markdown("""<h5 style="color: white;">{}</h5>""".format(dhyanam["verse_trans"]), unsafe_allow_html=True)
        st.markdown("**{}**".format(dhyanam["verse_meaning"]))
        st.divider()
    

    st.subheader("Description")
    st.markdown("{}".format(read_gita_dhyanam()))


st.sidebar.markdown("""Source Code:  [Github LInk](https://github.com/everydaycodings/Bhagavad-Gita)""")