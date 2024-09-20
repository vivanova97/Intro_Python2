"""
Напишите модуль с функцией, которая принимает строку и возвращает строку с удаленными дублирующимися подряд
идущими символами. Например, строка "aabbccaa" должна быть преобразована в "abca".
"""

__all__ = ['remove_consecutive_duplicates']


def remove_consecutive_duplicates(text: str) -> str:
    if text:
        text = text.lower()
        letter_list = [text[0]]
        letter_list.extend(text[i] for i in range(1,len(text)) if text[i] != text[i-1])
        return ''.join(letter_list)
    return ''


if __name__ == '__main__':
    text_sample = 'Ghhostts'
    print(remove_consecutive_duplicates(text_sample))


