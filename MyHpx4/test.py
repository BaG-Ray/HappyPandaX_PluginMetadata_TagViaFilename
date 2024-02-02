import json


def trans_Chinese(word):
    with open(r'./db.text.json', 'r', encoding='utf-8') as json_File:
        json_Data = json.load(json_File)
        try:
            word_Value_Dic = json_Data["data"]
        except:
            return word

        Dic_Times = len(word_Value_Dic) + 1

        count = 2
        Chinese_Word = ""
        while count < Dic_Times:

            Dic_List = word_Value_Dic[count]
            try:
                Dic = Dic_List['data']
                Word_Dic = Dic[word]
                Chinese_Word = Word_Dic['name']
                if Chinese_Word != "":
                    break
            except:
                count = count + 1

        if count == Dic_Times:
            return word

        else:
            return Chinese_Word


trans_Chinese("no penetration")
