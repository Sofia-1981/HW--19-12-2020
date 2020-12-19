# dictionary_1={'a': 300, 'b': 400}
# dictionary_2={'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)
#
#
# my_dictionary={"data1":375, "data2":567, "data3":-37, 'data4':21 }
# comp=my_dictionary["data1"]*my_dictionary["data2"]*my_dictionary["data3"]*my_dictionary["data4"]
# print(comp)
#
#
# dict1={i:i**3 for i in range(11)}
# print(dict1)
#
#
# school={'1а':30, '1б':27, '2а':36, '2б':31, '3а':45, '3б':30, '4а':28, '4б':38, '5а':36, '5б':34, '5в':29}
# school['1а']=35
# print(school)
# school["5г"]=34
# print(school)
# school.pop("5г")
# print(school)
# s=0
# for i in school:
#     s=s+school[i]
# print(s)
#
#
# shop={"тетрадь":40, "ручка":20, "карандаш":5, "лист бумаги":6, "альбом":50}
# # s=0
# # for i in shop:
# #     s=shop[i]+s
# #     avr=s/len(shop)
# # print(avr)
# print (sum(shop.values())/len(shop))
# print(min(shop.values()))
# print(max(shop.values()))
# print (sum(shop.values())-shop["альбом"])
# print (sum(shop.values())*2)
#
#
# dictAR={"dog": "собака", "cat":"кошка", "mouse":"мышь", "bird": "птица", "elefant": "слон"}
# dictRA={v:k for k,v in dictAR.items()}
# print(dictRA)