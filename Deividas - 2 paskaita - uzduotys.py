# 1 uzduotis - sukurti .py faila
#
# 2 uzduotis - isivesti teksta kaip var
text = ('        Alberas Kamiu (Albert Camus, 1913–1960) – prancūzų rašytojas, eseistas '
        'ir dramaturgas, Nobelio premijos laureatas. Vienas svarbiausių modernių mąstytojų. '
        'Kamiu siekė sakyti tiesą apie šiuolaikinį žmogų, sklaidyti iliuzijas, bet ir neprarasti '
        'humanistinio tikėjimo. Iki šiol populiarus ir vertinamas visame pasaulyje ne tik dėl      '
        'literatūrinės kūrybos, bet ir dėl autentiško kalbėjimo, dėl to, kad ieškojo vertybių, '
        'kurios kartėlio, netikėjimo ir XX a. žiaurumų iškankintai širdžiai būtų tikros ir savos.'
        '          ')

# 3 uzduotis - susikuriam 2 inputus
word = input("Iveskite... ")  # raktinis zodis kurio ieskosime tekste
length = input("Simboliu ilgis (int tipo): ") # simboliu ilgis

# 4 uzduotis - sutvarkom teksta kad atrodytu graziai (isimt nereikalingus tarpus, etc.)
text1 = text.split()
text1 = " ".join(text1)
print(text1 + "\n") # pasicheckinu ar viskas ok

# 5 uzduotis - keiciam visus "ir" i "bei"
text1 = text1.replace("ir", "bei")
print(text1 + "\n") # pasicheckinu ar viskas ok

# 6 uzduotis - checkinam kiek kartu kartojas zodis "bei"
bei_sk = text1.count("bei")
print(bei_sk) # pasicheckinu rezultata

# 7 uzduotis - randam 6-tos uzduoties rezultato (bei_sk) iki 13-to simbolio
print(text1[bei_sk + 1:13 + 1]) # iki 14 nes pythonas skaiciuoja ne imtinai.

# 8 uzduotis - kuriu var
kas = (text1[bei_sk + 1:13 + 1] + "yra puikus rasytojas") # priskiriu 7-ta uzduoti i var
print(kas) # pasicheckinu ar viskas ok

# 9 uzduotis - indexuoju kur yra skliaustai ir issikeliu teksta tarp skliaustu
print(text1.find("(")) # randu indexa kur yra skliaustu atidarymas
print(text1.find(")")) # randu indexa kur yra skliaustu uzdarymas
text2 = (text1[14:38 + 1]) # 38+1 nes pythonas skaiciuoja ne imtinai
print(text2) # pasicheckinu ar viskas ok

# 10 uzduotis - is 9-tos uzduoties var susirandu kur prasideda datos nuo 1 (1913) iki 0 (1960)
date1 = text2.find("1")
date2 = text2.find("0")
print(date1) # pasitikrinu ju indexus
print(date2) # pasitikrinu ju indexus
dates = (text2[15:23 + 1]) # sukuriu var kad butu tik datos

# 11 uzduotis - isskaidau datas, naudodamas split su minusu kaip skaidytoju
skaidytas = dates.split('–')
print(skaidytas)

# 12 uzduotis - paskaiciuot kiek metu gyveno rasytojas
skaidytas1 = int(skaidytas[0]) # pasiverciu skaidytas datas i int
skaidytas2 = int(skaidytas[1]) # pasiverciu skaidytas datas i int
metai = str(skaidytas2 - skaidytas1) # randu skirtuma, paverciu i str ir isidedu i var
print("Kamiu nugyveno " + metai + " grazius metus")

# 13 uzduotis - naudojant 3-ios uzduoties inputus, atspausdinti visus 2 uzduoties
#               teksto simbolius nuo ivesto zodzio (var word) iki simboliu ilgio (var length)
print("Ivestas zodis: " + word)
print("Simboliu ilgis: " + length)
word_index = int(text.find(word)) # idedu i var zodzio indexa
if word == str and length == int: # jeigu word yra stringas ir length yra skaicius
    print(text[word_index:word_index + length]) # tada spausdinu nuo word_index indexo iki word_index + length indexo
elif word != str or length != int: # arba jeigu word nera stringas ARBA length nera skaicius
    word = str(word) # tada word pasiverciu stringu
    length = int(length) # length pasiverciu skaicium
    print(text[word_index:word_index + length]) # ir spausdinu nuo word_index indexo iki word_index + length indexo
else:
    print("Ivyko 13-tos uzduoties klaida")

# Aciu!