
import Bless
import os

if __name__ == "__main__":
	b = Bless.Bless ( "/home/ludovica.pannitto/progetto_sns/filteredbless", None )
	target_dict = b.items
	
	lista_file = os.listdir ( "../TypeDM/simpart/" )
	
	coseni = []
	
	for target in target_dict:
		if target+".sim" in lista_file:
			
			relatum_set = set ( [ relatum for rel in target_dict[target] for relatum in target_dict[target][rel] ] )
			
			fin = open ( "../TypeDM/simpart/"+target+".sim" )
			
			for line in fin:
				linesplit = line.split ()
				candidate_relatum = linesplit[0]
				cos = linesplit[1]
				
				if candidate_relatum in relatum_set:
					coseni.append ( ( target, candidate_relatum, cos ) )
			fin.close ()
	
	fout = open ("../data/coseni_svd", "w")
	for target, relatum, cos in coseni:
		 fout.write (target+"\t"+relatum+"\t"+cos+"\n")
