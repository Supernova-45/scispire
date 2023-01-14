import numpy as np

lines = []
             
with open('formattedGPTideas.txt',encoding='utf-8') as file:
    for line in file:
        lines.append(line.rstrip())
        
print(lines)
ideas = np.asarray(lines)

generated_ideas = np.random.choice(ideas, 3)
print(generated_ideas)