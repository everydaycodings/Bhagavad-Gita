import streamlit as st
from streamlit_helper import get_chapter_summary_data, get_verse_numbers, get_chapter_number, get_verse_data, get_chapter_name, get_english_meaning, get_verse_commentary_data


st.title("Bhagavad Gita")

gita_type = st.selectbox(label="Select the type: ", options=["Chapter Summary", "Verse Explanation"])

if gita_type == "Chapter Summary":

    chapter_number = st.selectbox(label="Enter The Chapter Number: ", options=get_chapter_number())
    
    if st.button("Get Summary"):
        chapter_data = get_chapter_summary_data(chapter_number=chapter_number)
        st.markdown("##### Chapter Name: {} ({})".format(chapter_data["name"], chapter_data["name_meaning"]))
        st.markdown("##### Total Number Of Verses: {}".format(chapter_data["verses_count"]))
        st.markdown("**Chapter Summary**")
        st.markdown(chapter_data["chapter_summary_hindi"])
        st.markdown("**Chapter Summary (English)**")
        st.markdown(chapter_data["chapter_summary"])


if gita_type == "Verse Explanation":
    chapter_number = st.selectbox(label="Enter The Chapter Number: ", options=get_chapter_number())
    verse_number = st.selectbox(label="Enter The Verse Number: ", options=get_verse_numbers(chapter_number))
    
    if st.button("Get Verse"):
        chapter_name = get_chapter_name(chapter_number)
        verse_data = get_verse_data(chapter_number, verse_number)
        verse_commentary_data = get_verse_commentary_data(chapter_number, verse_number)
        audio_file = open('data/gita/verse_recitation/{}/{}.mp3'.format(chapter_number, verse_number), 'rb').read()

        st.markdown("##### Chapter Name: {}".format(chapter_name))
        st.markdown("##### Verse Number: {}".format(verse_data["verse_number"]))
        st.markdown("**Text**")
        st.markdown(verse_data["text"])
        st.markdown("**Transliteration**")
        st.markdown(verse_data["transliteration"])
        st.markdown("**Verse Audio**")
        st.audio(audio_file, format='audio/mp3')
        st.markdown("**Word Meanings**")
        st.markdown(verse_data["word_meanings"])
        st.markdown("**English Translation**")
        st.markdown(get_english_meaning(verse_data["word_meanings"]))
        st.markdown("**Commentary**")
        st.markdown(verse_commentary_data["commentary"])