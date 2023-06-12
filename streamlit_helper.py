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


def get_english_meaning(verse_text):
    verse_text = str(verse_text).replace("\n", " ")
    verse_text = "{};".format(verse_text)
    extracted_text = "\n".join(re.findall("—(.*?);", verse_text))
    return extracted_text


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