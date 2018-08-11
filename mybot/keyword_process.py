import jieba
import jieba.analyse
jieba.set_dictionary('jieba/dict.txt')
def jieba_analyse(recevied_message):
    #global recevied_message
    analyse_word = ""
    contend = jieba.analyse.extract_tags(recevied_message, topK=100, withWeight=True)
    print("contend",str(contend))
    #recevied_message = contend[0][0]
    for i,j in contend:
        print("iJ",i,j)
        analyse_word = analyse_word + i +" "
        print("word1", analyse_word)
    recevied_message = analyse_word
    return recevied_message