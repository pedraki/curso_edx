fichero_dna="H:\git\curso_edx\edx\DNA\dna.txt"
f_dna=open(fichero_dna,'r')
seq=f_dna.read()
#quita el retorno de carro
# se ve el caracter en el idel sin hacer print
# ya que print formatea
seq_dna=seq.replace('\n','')
print(seq_dna)
for letra in seq_dna.rstrip(' \t\n\r'):

	print(letra)


