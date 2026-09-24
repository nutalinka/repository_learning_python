vowels = ['а','е','ё','и','о','у','ы','э','ю','я','ь','ъ']
text=input()
text=text.lower()
list_text=list(text)
result=[item for item in list_text if item not in vowels]
#text1=set(text)
result_str=(''.join(result))
#print(result_str)
print(len(result_str))
