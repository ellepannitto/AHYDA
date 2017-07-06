
class BaseRun:
	
	def __init__ ( self, output_filename, matrice_filtrata, dataset, dih, measures ):
		'''
		   dataset: [ (target, relatum, relazione), ... ]
			
		
		'''
		self.matrice_filtrata, self.dataset, self.dih = matrice_filtrata, dataset, dih
		self.measures = measures
		self.fout = open ( output_filename, "w" )
		
	def compute_measures (self, ipo, iper):
	
		if not self.dih:
			ipo, iper = iper, ipo
		
		u = self.matrice_filtrata[ipo]
		v = self.matrice_filtrata[iper]
		
		self.measures.reset ()
		ret = { "cos": self.measures.compute ("cos", ipo, iper) }
		for meas in self.measures.selected_measures:
			ret[meas] = self.measures.compute ( meas, u, v )

		return ret
	
	
	def esegui_calcoli ( self ):
		
		sorted_selected_measures = sorted ( list(self.measures.selected_measures) )
		self.fout.write ("target\trelatum\trelazione\t"+"\t".join (sorted_selected_measures)+"\n")
		
		for target, relatum, relazione in self.dataset:
			self.fout.write (target+"\t"+relatum+"\t"+relazione+"\t")
			measdict = self.compute_measures ( target, relatum )
			for meas in sorted_selected_measures :
				self.fout.write (str(measdict[meas])+"\t")
			
			self.fout.write("\n")
			
		self.fout.close()
