import os

with open("mydata.txt", mode='w', encoding='utf-8') as my_file :
    my_file.write("Some text for me.\nSome More text for me.\nSome easier text for me.\nNow thank you?..")
    

with open('mydata.txt', encoding='utf-8') as my_file:
    c = 0
    for i in my_file.readlines():
        line_word_len = 0
        line_word = i.split()
        c += 1
        for j in line_word:
            for k in j:
                line_word_len += 1
        print("Line #{}".format(c))
        print("Total word number = {}".format(len(line_word)))
        print("Avg. word length = {:0.2f}".format(line_word_len/len(line_word)))
