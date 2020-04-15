def translate (seq_dna):
#diccionario de correspondencias DNA-> PROTEINAS
# lo que esta entre comilla sale al ejecutra HELP translate

	""" Recibe una sequencia de DNA y devuelve las proteinas """
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

	
	proteina=str()
	for i in range(0,len(seq_dna),3):
		
		if seq_dna[i:i+3] in table.keys():
			proteina+=table[seq_dna[i:i+3]]

	return proteina


def read_file (fichero_dna):
	with open(fichero_dna,'r') as f_dna:
		seq_dna=f_dna.read()
	#equivalente a lo de arriba  pero evita errores
	#f_dna=open(fichero_dna,'r')
	#seq_dna=f_dna.read()
	#quita el retorno de carro
	# se ve el caracter en el idel sin hacer print
	# ya que print formatea
	seq_dna=seq_dna.replace('\n','')
	#en principio esta no hace falta
	seq_dna=seq_dna.replace('\r','')

	return seq_dna

 
fichero_dna="H:\git\curso_edx\edx\DNA\dna.txt"
#seq_dna=read_file(fichero_dna)
#proteina=translate(seq_dna)

## o en una
#proteina=translate(read_file(fichero_dna))
#la movida 20:935 es pq lo dice el doc del dna 
proteina=translate(read_file(fichero_dna)[20:935])
print(proteina)








