import streamlit as st
from streamlit_helper import get_chapter_summary_data, get_verse_numbers, get_chapter_number, get_verse_data, get_chapter_name, get_translation, get_verse_commentary_data, get_chapter_image


st.sidebar.title("Bhagavad Gita")

gita_type = st.sidebar.selectbox(label="Select the type: ", options=["Chapter Summary", "Verse Explanation"])

if gita_type == "Chapter Summary":

    chapter_number = st.sidebar.selectbox(label="Enter The Chapter Number: ", options=get_chapter_number())
    
    if st.sidebar.button("Get Summary"):

        st.image("https://bhagavadgita.io/static/images/{}.jpg".format(get_chapter_image(chapter_number)), width=600)
        
        chapter_data = get_chapter_summary_data(chapter_number=chapter_number)
        st.markdown("""<h3 style="color: yellow;">Chapter Name: {} ({})</h3>""".format(chapter_data["name"], chapter_data["name_meaning"]), unsafe_allow_html=True)
        st.markdown("""<h3 style="color: yellow;">Verse Number: {}</h3>""".format(chapter_data["verses_count"]), unsafe_allow_html=True)
        st.markdown("""<h3 style="color: brown;">Chapter Summary</h3>""", unsafe_allow_html=True)
        st.markdown(chapter_data["chapter_summary_hindi"])
        st.markdown("""<h6 style="color: brown;">Chapter Summary (English)</h6>""", unsafe_allow_html=True)
        st.markdown(chapter_data["chapter_summary"])


if gita_type == "Verse Explanation":
    chapter_number = st.sidebar.selectbox(label="Enter The Chapter Number: ", options=get_chapter_number())
    verse_number = st.sidebar.selectbox(label="Enter The Verse Number: ", options=get_verse_numbers(chapter_number))
    
    if st.sidebar.button("Get Verse"):

        st.image("https://bhagavadgita.io/static/images/{}.jpg".format(get_chapter_image(chapter_number)), width=600)

        chapter_name = get_chapter_name(chapter_number)
        verse_data = get_verse_data(chapter_number, verse_number)
        verse_commentary_data = get_verse_commentary_data(chapter_number, verse_number)
        audio_file = open('data/gita/verse_recitation/{}/{}.mp3'.format(chapter_number, verse_number), 'rb').read()

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