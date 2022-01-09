def read_stopword_file(path):
    stopword_file = open(path, "r", encoding = 'utf-8')
    sw = stopword_file.readlines()
    stopword_file.close()
    sw = [x.replace('\n', '') for x in sw]
    return sw

def remove_single_spec_char(char):
    if char != ' ':
        if char.isalnum() == False:
            char = ' '
    return char

def remove_specChar_link(string):
    result = ''
    string = string.replace('\n', ' ').replace('\t', ' ')
    sub_text = string.split(' ')
    links = [link for link in sub_text if len(link) > 15]
    for link in links:
        string = string.replace(link, ' ')
    for char in string:
        result = result + remove_single_spec_char(char)
    result = ' '.join(result.split())    
    return result

def remove_stopword(string, stop_word):
    for stop_word in stop_word:
        string = string.replace(' ' + stop_word + ' ', ' ')
    return string

def text_preprocessing(text):
    stop_word = read_stopword_file("vietnamese-stopwords.txt")
    new_text = remove_specChar_link(text)
    new_text = new_text.lower()
    new_text = remove_stopword(new_text, stop_word)
    return new_text