# basically this is a function that cleans text from censorship.
# I like this censor personally ( #@_& )

def cleanThis(text, censor_List):
  for word in censor_List:
    if word in censor_List:
      text = text.replace(word, '#@_&')
  return text
  
text_input = input('Enter your text here for cleaning: ')
text = text_input.lower()
censor_list = ['shit', 'ass', 'idiot']

censored_text = cleanThis(text, censor_list)
print(censored_text)



