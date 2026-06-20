def normalize_text(text):           #разбиение исходного текста на список слов
    normalized_text = ''
    for letter in text:
        if letter.isalpha() or letter.isdigit():    #если символ является буквой или цифрой
            normalized_text += letter.lower()       #приведение к нижнему регистру
        else:
            normalized_text += ' '
    normalized_text = normalized_text.split()       #разбиение на слова, удаление пробелов
    return normalized_text

def average_word_len(normalized_text):              #средняя длина слов в нормализованном тексте
    all_len = 0
    for word in normalized_text:
        all_len += len(word)
    return all_len / len(normalized_text)

def longest_words(normalized_text):                 #топ 3 самых длинных слов
    top_3_words = []
    for word in normalized_text:
        if word not in top_3_words:
            top_3_words.append(word)        #добавляем новое слово в топ
            if len(top_3_words) > 3:        #если новое слово стало четвёртым
                top_3_words = sorted(top_3_words, key=len,reverse=True)     #сортируем от большего к меньшему
                top_3_words = top_3_words[:3]           #берём срез первых трёх элементов
    return sorted(top_3_words, key=len,reverse=True)    #возвращаем повторно сортированный список, если слов в тексте 3 и менее

def count_target(normalized_text,target):   #количество вхождений ключевого слова в текст
    return normalized_text.count(target)

def get_words_above_limit(normalized_text,n):   #слова длиннее заданного числа
    words = []
    for word in normalized_text:
        if len(word) > n:
            words.append(word)
    return words

def all_words_stat(normalized_text):        #все слова и их количество (полная статистика по всем словам)
    all_words_dict = {}
    for word in normalized_text:
        if word not in all_words_dict:
            all_words_dict[word] = 1
        else:
            all_words_dict[word] += 1
    return all_words_dict

def show_report(text, target, n):           #отобразить результаты
    normalized_text = normalize_text(text)
    if not normalized_text:
        print("Nothing to be done!")    #дополнительная проверка, если нормализованный текст не содержал букв/цифр, но каким-то образом прошёл проверку get_text_input()
    else:
        top3_words = longest_words(normalized_text)
        words_above_limit = get_words_above_limit(normalized_text,n)
        full_stat = all_words_stat(normalized_text)
        print(f"Number of words in the text: {len(normalized_text)}")
        print(f"Top 3 longest words: {', '.join(map(str,top3_words))}")
        print(f"The number of words is greater than {n} symbols: {len(words_above_limit)}")
        print(f"Words longer then {n} symbols: {', '.join(map(str,words_above_limit))}")
        print(f"Search word: {target} found {count_target(normalized_text,target)} times")
        print(f"Average word length: {average_word_len(normalized_text)}")
        print()
        print(f"Full statistics of all words: \n ")
        for key,value in full_stat.items():
            print(f"Word {key} found {value} times")

def get_text_input():               #проверка на ввод нормального текста
    while True:
        text = input("Enter text to analyze:\n")
        if text and text.strip():  #проверка на пустоту текста и содержание символов отличных от пробела
            if any(letter.isalnum() for letter in text):    #проверка на наличие букв/цифр помимо спец символов
                return text
        print("Bad text! Try again!")

def get_target_input():               #проверка на ввод нормального текста
    while True:
        target = input("Enter word for search:\n")
        if target and target.isalnum():  #проверка на пустоту, и наличие только букв/цифр
            return target.lower()       #возврат ключевого слова без регистра
        print("Bad word! Try again!")

def get_len_limit_input():          #проверка на ввод адекватного числа
    while True:
        print("Enter number:")
        try:
            n = int(input())
            if n > 0:           #проверка на ввод отрицательного
                return n
            else:
                print("Enter positive integer!")
        except ValueError:      #если введено не число
            print("Enter valid integer instead of this.")

if __name__ == "__main__":
    print("=================Text analyzer!=================")
    text = get_text_input()
    target = get_target_input()
    n = get_len_limit_input()
    show_report(text,target,n)
