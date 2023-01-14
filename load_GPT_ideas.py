lines = []  
                             
with open('GPTideas.txt',encoding='utf-8') as file:
    for line in file:
        lines.append(line.split("."))

for line in lines:
    for num,idea in enumerate(line):
        line[num] = line[num].translate({ord(ch): None for ch in '0123456789'})
        line[num] = line[num][1:-1]

with open('formattedGPTideas.txt', 'w') as f:
    for line in lines:
        for idea in line:
            if idea.startswith('enerate') == False and idea != '':
                f.write(f"{idea}\n")