import tkinter as tk
import pyjokes as pj


languages_dict = {
    'hu': 'Hungarian',
    'en': 'English',
    'lt': 'Lithuanian',
    'cs': 'Czech',
    'fr': 'French',
    'sv': 'Swedish',
    'gl': 'Galician',
    'ru': 'Russian',
    'pl': 'Polish',
    'eu': 'Basque',
    'de': 'German',
    'it': 'Italian',
    'es': 'Spanish'
}

categories = list(pj.CATEGORY_VALUES)
languages = list(pj.LANGUAGE_VALUES)

categories_index = 1
languages_index = 1

def get_next_category():
    global categories_index
    categories_index = (categories_index + 1) % len(categories)
    category = categories[categories_index]
    select_category_button.config(text=category.capitalize())

def get_next_language():
    global languages_index
    languages_index = (languages_index + 1) % len(languages)
    language = languages[languages_index]
    select_language_button.config(text =f'{languages_dict[language]}, {language}')


def show_joke():
    lang = select_language_button.cget('text').split(",")[-1].strip().lower()
    cat = select_category_button.cget('text').lower().strip()
    try:
        joke = pj.get_joke(lang, cat)
        entry.delete(0, tk.END)
        entry.insert(0, joke)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error fetching joke")
        print(e)


# Main window
root = tk.Tk()
root.title("Joke generator")
# Entry field
entry = tk.Entry(root, width=100, font=('Arial', 10))
entry.grid(row=0, column=0, columnspan=4)

# Buttons
select_category_button = tk.Button(root, text=categories[0].capitalize(), width=20, height=2)
select_category_button.grid(row=2, column=1)

select_language_button = tk.Button(root, text=f'{languages_dict[languages[0]]}, {languages[0]}', width=20, height=2)
select_language_button.grid(row=2, column=3)

change_category_button = tk.Button(root, text='Change Category', width=20, height=2, command=get_next_category)
change_category_button.grid(row=1, column=1)

change_language_button = tk.Button(root, text='Change Language', width=20, height=2, command=get_next_language)
change_language_button.grid(row=1, column=3)

joke_button = tk.Button(root, text='Get Joke', width=20, height=2, command= show_joke)
joke_button.grid(row=3, column=2)

# Run the Tkinter event loop
root.mainloop()
