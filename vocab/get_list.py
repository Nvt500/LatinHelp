file = open("Latin_Words.txt")
file = (file.read()).split("\n")

keywords = ["Nominative", "Genitive", "Gender", "Definition", "1st Principal Part", "2nd Principal Part", "3rd Principal Part", "4th Principal Part", "Masculine", "Feminine", "Neuter", "Latin Word", "Dative", "Accusative", "Ablative"]


for i in range(len(file)):
    file[i] = file[i].strip()

old_file = []
for word in file:
    if len(word) > 0:
        old_file.append(word)
file = old_file

indexes = []
for i, word in enumerate(file):
    if word != word.lower() and not(word in keywords):
        indexes.append(i)


lengths = [0for i in range(len(indexes))]
for i in range(len(indexes)):
    num = 0
    if i == len(indexes)-1:
        for word in file[indexes[i]:]:
            if word in keywords:
                file.remove(word)
                num += 1
        lengths[i] = num
    else:
        for word in file[indexes[i]:indexes[i+1]]:
            if word in keywords:
                file.remove(word)
                for e in range(i+1,len(indexes)):
                    indexes[e] -= 1
                num += 1
        lengths[i] = num

full_length = [0for i in range(len(indexes))]
for i in range(len(indexes)):
    num = 0
    if i == len(indexes)-1:
        for word in file[indexes[i]:]:
            num += 1
        full_length[i] = num
    else:
        for word in file[indexes[i]:indexes[i+1]]:
            num += 1
        full_length[i] = num

try:
    new_file = [
        [
            []for e in range(int((full_length[i]-1)/lengths[i])+1)
        ]for i in range(len(indexes))
    ]
except Exception:
    raise Exception(str(lengths))

for i in range(len(indexes)):
    new_file[i][0] = [file[indexes[i]]]
    ind = indexes[i]+1
    for e in range(len(new_file[i])-1):
        place_holder = []
        for f in range(lengths[i]):
            place_holder.append(file[ind])
            ind += 1
        new_file[i][e+1] = place_holder

place_holder = []
for list_ in new_file:
    if len(list_) != 1:
        place_holder.extend([[]])
        place_holder[place_holder.index([])] = list_
new_file = place_holder