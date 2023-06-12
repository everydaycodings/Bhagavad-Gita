import json
import re

def get_chapter_name(chapter_number):
    with open('data/gita/chapters.json', 'r') as file:
        data = json.load(file)
        for chapter in data:
            if chapter['chapter_number'] == chapter_number:
                return "{} ({})".format(chapter["name"], chapter["name_meaning"])
    return None


def get_chapter_number():

    with open('data/gita/chapters.json', 'r') as file:
        data = json.load(file)
        chapter_number = [chapter['chapter_number'] for chapter in data]
        return chapter_number
    
    return None


def get_verse_numbers(chapter_number):
    with open('data/gita/verse.json', 'r') as file:
        data = json.load(file)

        verse_numbers = [verse['verse_number'] for verse in data if verse['chapter_number'] == chapter_number]

        return verse_numbers


def extract_english_meaning(verse_text):
    verse_text = str(verse_text).replace("\n", " ")
    verse_text = "{};".format(verse_text)
    extracted_text = "\n".join(re.findall("—(.*?);", verse_text))
    return extracted_text


def get_translation(chapter_number, verse_number, lang, author):

    verse_id = 0
    if chapter_number != 1:
        for i in range(1, chapter_number):
            total_number_of_verse = get_verse_numbers(i)
            verse_id += max(total_number_of_verse)

        verse_id += verse_number
    
    else:
        verse_id = verse_number

    with open('data/gita/translation.json', 'r') as file:
        data = json.load(file)

        for verse in data:
            if verse['verseNumber'] == verse_id:
                if verse["lang"] == lang:
                    if verse["authorName"] == author:
                        return verse["description"]



def get_chapter_image(chapter_number):
    with open('data/gita/chapters.json', 'r') as file:
        data = json.load(file)
        for chapter in data:
            if chapter['chapter_number'] == chapter_number:
                return "https://bhagavadgita.io/static/images/{}.jpg".format(chapter["image_name"])
    return None


def get_chapter_summary_data(chapter_number):
    with open('data/gita/chapters.json', 'r') as file:
        data = json.load(file)
        for chapter in data:
            if chapter['chapter_number'] == chapter_number:
                return chapter
    return None



def get_verse_data(chapter_number,verse_number):
    with open('data/gita/verse.json', 'r') as file:
        data = json.load(file)
        filtered_data = [d for d in data if d['chapter_number'] == chapter_number]

        for verse in filtered_data:
            if verse['verse_number'] == verse_number:
                return verse
    return None


def get_verse_commentary_data(chapter_number,verse_number):
    with open('data/gita/commentary.json', 'r') as file:
        data = json.load(file)
        filtered_data = [d for d in data if d['chapter_id'] == chapter_number]

        for verse in filtered_data:
            if verse['verse_id'] == verse_number:
                return verse
    return None