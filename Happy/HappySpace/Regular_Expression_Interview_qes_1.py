# Find the number of words in the given paragraph using regular expression
import re

text='''Chloroform, or trichloromethane (often abbreviated as TCM), is an organic compound with the formula 
CHCl3 and a common solvent. It is a very volatile, colorless, strong-smelling, 
dense liquid produced on a large scale as a precursor to PTFE and refrigerants[10] and 
is a trihalomethane that serves as a powerful anesthetic, euphoriant, anxiolytic, and 
sedative when inhaled or ingested. Chloroform was used as an anesthetic between the 19th century 
and the first half of the 20th century  10.123.456'''

# words=re.findall(r'\w+',text)
words=re.findall(r'\b\w+\b',text)
match = re.search(r'\d{2}.\d{3}.\d{3}',text)

print(match)
print(text[494:504])
print(len(words))