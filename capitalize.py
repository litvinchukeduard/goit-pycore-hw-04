"""
Написати функцію, яка буде брати слово та перетворювати першу літеру у верхній регістр
"""

# My comment
# Second comment
sum([1, 2, 3])

def capitalize_word(word: str) -> str:
    """Function that accepts a word and returns it with first symbol capitalized
    
    Args:
        word: Word to be capitalized (str)

    Returns:
        Word with first symbol in upper registry
    """
    return word.capitalize()

print(capitalize_word("hello"))
