#diccionario de correspondencias DNA-> PROTEINAS
table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

fichero_dna="H:\git\curso_edx\edx\DNA\dna.txt"
f_dna=open(fichero_dna,'r')
seq_dna=f_dna.read()
#quita el retorno de carro
# se ve el caracter en el idel sin hacer print
# ya que print formatea
seq_dna=seq_dna.replace('\n','')
#en principio esta no hace falta
seq_dna=seq_dna.replace('\r','')
lista_dna=list()
#metemos el DNA en una lista de 3 en 3 
#no haria falta pero bueno
#las proteinas van al reves por lo que en vez de en una lista
#se meten en un string o una lista reverse
lista_protein=list()
proteina=str()
for i in range(0,len(seq_dna),3):
	lista_dna.append(seq_dna[i:i+3])

for i in lista_dna:
	if i in table.keys():
		proteina+=table[i]
print (proteina)




