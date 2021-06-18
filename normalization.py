# Customized text normalization function
def normalize(string):
    string = string.replace('\n\n', ' <br> ')
    string = string.replace('\n', ' <br> ')
    string = re.sub('BULLET::::', '', string)
    #string = re.sub('BULLET::::-', '', string)
    string = re.sub('Section::::', '', string)
    #pattern = '(' + '|'.join(puctuation) + ')'
    string = re.sub(r'("|\')', '', string)
    string = re.sub(r'(\,|\.|;|\?|!|:) ', r' \1 ', string)
    string = re.sub(r'(\S)(|\)|\}|\])', r'\1 \2', string)
    string = re.sub(r'(\(|\{|\[)(\S)', r'\1 \2', string)
    string = re.sub(r'\s+', ' ', string)
    return string
