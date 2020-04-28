punctuation=['.',',','…','!','»','«','*','(',')','/','—',':','?',';','!']
words=[]
for line in open('tadzik.txt',encoding='utf-8').readlines():
    clear=line.strip()
    for word in clear.split():
        for sign in punctuation:
            word=word.strip(sign)
        if (len(word) > 0):
            words.append(word.lower())


words.sort()

dictionary={}

for word in words:
   if word in dictionary:
       dictionary[word]+=1
       
   else: dictionary.update({word: 1})   
    
print(dictionary)

with open('counter.txt', 'w') as file:
   for key, value in dictionary.items():
      file.write(str(key)+' | '+ str(value)+ '\n')