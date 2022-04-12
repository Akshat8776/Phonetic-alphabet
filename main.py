import pandas
dict={}
data=pandas.read_csv("nato_phonetic_alphabet.csv")
for i in range(0,len(data["letter"])):
    dict[data["letter"][i]]=data["code"][i]
# way2:To convert into dict
# dict={r.letter:r.code for (i,r) in data.iterrows()}
word=input("Please enter the word ").upper()
st=""
for i in word:
    st=st+dict[i]+" "
print(st)