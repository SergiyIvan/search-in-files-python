from pathlib import Path


# Banned words text file has to be in the same directory as this file
# Fill this file with a single word per line:
# word1
# word2
def get_banned_words():
    banned_words_file = open("banned_words.txt", "r")
    return list(set( [x.strip(' ') for x in banned_words_file.read().splitlines()] ))


def execute(filename, result_list, banned_words):
    file_content = open(filename, encoding="utf8").read().lower()
    result = {
        'filename' : str(filename)
    }

    for word in banned_words:
        result[word] = file_content.count(word.lower())
         
    result_list.append(result)



if __name__ == "__main__":
    banned_words = get_banned_words()
    print('Banned words to search in files:\n' + str(banned_words) + '\n')

    # Provide your directory for search here
    directory = 'ENTER YOUR DIRECTORY HERE'
    print('Directory to search in:\n' + directory + '\n')
    # '**/*.html' to perform search in this directory and all subdirectories
    pathlist = Path(directory).glob('**/*.html')
    
    # Result is the list of dictionary-like objects, each contains filename and 
    # count of each banned word in this file. Banned words are keys, counts of 
    # those words are values
    result = []
    for path in pathlist:
        execute(path, result, banned_words)

    format_result = []
    for r in result:
        for word in banned_words:
            if r[word] > 0:
                format_result.append({'word': word, 'count': r[word], 'filename': r['filename']})

    choise = input('Enter "c" if you want to sort output by counts of banned words (ascending),\n'+
                   '"w" if you want to sort output by words (ascending),\n'+
                   '"f" if you want to sort output by filenames (ascending),\n'+
                   'or press any other key not to sort the output: ')

    if choise.lower() == 'c':
        format_result = sorted(format_result, key = lambda i: i['count'])
        print('\nResult sorted by counts of words\n')
    elif choise.lower() == 'w':
        format_result = sorted(format_result, key = lambda i: i['word'])
        print('\nResult sorted by words in alphabetical order\n')
    elif choise.lower() == 'f':
        format_result = sorted(format_result, key = lambda i: i['filename'])
        print('\nResult sorted by filenames in alphabetical order\n')
    else:
        print('\nYou haven\'t applied any sort\n')

    f = open('results.txt', 'w')

    # for r in result:
    #     for word in banned_words:
    #         if r[word] > 0:
    #             f.write('word: ' + word + ', count: ' + str(r[word]) + ', filename: ' + r['filename'] + '\n')

    for fr in format_result:
        f.write('word: ' + fr['word'] + ', count: ' + str(fr['count']) + ', filename: ' + fr['filename'] + '\n')
    f.close()
    print('Results are saved to results.txt file')
