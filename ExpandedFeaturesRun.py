
import os

class ExpandedFeaturesRun:
	
	def __init__ ( self, filename, matrice_filtrata, dataset, dih, measures, threshold ):
		'''
		   dataset: [ (target, relatum, relazione), ... ]
		
		
		'''
		self.matrice_filtrata, self.dataset, self.dih = matrice_filtrata, dataset, dih
		self.measures = measures
		self.fout = open ( filename, "w" )
		
		self.threshold = threshold
		
		self.features_expanded = {}
		self.already_processed = {}
		
	def compute_measures (self, ipo, iper):
	
		#considera vicini ipo
		#per ogni feature dell'iponimo, la espande considerando i vicini dell'iponimo
	
		if not self.dih:
			ipo, iper = iper, ipo	
	
		features = self.expand_features(ipo)
		
		u = self.matrice_filtrata[ipo]
		v = self.matrice_filtrata[iper]
		
		self.measures.reset ()
		ret = { "cos": self.measures.compute ("cos", ipo, iper, features) }
		for meas in self.measures.selected_measures:
			ret[meas] = self.measures.compute ( meas, u, v, features )

		return ret
	
	def expand_features (self, t):
		
		path = "/home/ludovica.pannitto/progetto_sns/TypeDM/simpart/"
		fileslist = os.listdir(path)
		
		if not t in self.features_expanded:
			feats = {}
			if t+".sim" in fileslist:	
					f_ipo = open(path+t+".sim")
					
					feats_to_consider = set([el for el in self.matrice_filtrata[t]])
					
					w = 1
					while w > self.threshold:
						line = f_ipo.readline().split()
						corr = line[0].strip()
						w = float(line[1].strip())
						
						if w > self.threshold and not corr == t and corr in self.matrice_filtrata and corr[-1] == t[-1]:
							for el in self.matrice_filtrata[corr]:
								feats_to_consider.add(el)
											
	
					for el in self.matrice_filtrata[t]:
						
						feats[el] = set()
						
						lemma_el = el.split(":")[0]
						
						if lemma_el in self.already_processed:
							
							feats[el] = self.already_processed[lemma_el]

						elif lemma_el+".sim" in fileslist:
							f_feat = open(path+lemma_el+".sim")
							
							w = 1
							while w > self.threshold:
								line = f_feat.readline().split()
								corr = line[0]
								w = float(line[1])
								
								if w > self.threshold and corr[-1] == lemma_el[-1] and corr+":"+el.split(":")[1] in feats_to_consider:
									feats[el].add(corr+":"+el.split(":")[1])
	
							self.already_processed[lemma_el] = feats[el]
		
		
			self.features_expanded[t] = feats
		
		return self.features_expanded[t]
	
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
