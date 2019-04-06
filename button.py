from tkinter import *
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


root=Tk()
root.geometry('500x500')

l1=Label(root,text='Enter the first paragraph')

l2=Label(root,text='Enter the second paragraph')

labelfont = ('times', 20, 'bold')

content1= StringVar()
content2= StringVar()

ent1= Entry(root,textvariable=content1)
ent2= Entry(root,textvariable=content2)


l1.grid(row=0)
l2.grid(row=1)

ent1.grid(row=0, column=1)
ent2.grid(row=1, column=1)


def similarity():
    txtName1= content1.get(); 
    txtName2= content2.get(); 

    ps = PorterStemmer()
    stop_words = set(stopwords.words("english"))
    words1 = word_tokenize(txtName1); 
    words2 = word_tokenize(txtName2); 
    filtered_sentence1 = []
    filtered_sentence2 = []
    
    for w in words1:
        if w not in stop_words:
            filtered_sentence1.append(w)
    print(filtered_sentence1)
            
    for w in words2:
        if w not in stop_words:
            filtered_sentence2.append(w)
            
    stemmed_words1 = []
    for w in filtered_sentence1:
        stemmed_words1.append(ps.stem(w))
            
    stemmed_words2 = []
    for w in filtered_sentence2:
        stemmed_words2.append(ps.stem(w))

    count = 0

    for w in stemmed_words1:
        if w in stemmed_words2:
            count= count+1

    res = 0
    if count!=0:
        if txtName1 == txtName2 :
            print("100.00")
        else:
            res = 0
            l1 = len(txtName1)
            l2 = len(txtName2)
            res = 100 -(l1+l2)/count
            if res < 0:
                res =  res * -1
                print(res)
            else:
                print(res)
    outputString="Rate is "+str(res)
    l3=Label(root,text= outputString)
    l3.grid(row=5)


button = Button(text="Check Similarity", command=similarity)
button.grid(row=3, columnspan=2)
root.mainloop()
