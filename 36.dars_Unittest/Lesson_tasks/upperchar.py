def Upperchar(list):
    for i in range(len(list)):
        list[i] = list[i].capitalize()
    return list


list = ["olma", "anor", "uzum", "nok"]
print(Upperchar(list))
print(Upperchar(["easy", "diffucult", "normal", "wrap", "column", "table"]))
