
import os

def read_list(filename):
	
	ret_k = []
	ret_v = []
	
	with open(filename) as f:
		for line in f:
			linesplit = line.split()
			
			ret_k.append(linesplit[0])
			ret_v.append(float(linesplit[1]))
			
	return ret_k, ret_v

def read(filename):
	
	ret = {}
	
	with open(filename) as f:
		for line in f:
			linesplit = line.split()
			
			e = float(linesplit[1])
			
			ret[linesplit[0]] = e if e > 0 else 0.01
			
	return ret


class SLQSFeaturesRun:
	
	def __init__ ( self, filename, matrice_filtrata, dataset, dih, measures, threshold, quartile ):
		'''
		   dataset: [ (target, relatum, relazione), ... ]
		
		
		'''
		
		self.matrice_filtrata, self.dataset, self.dih = matrice_filtrata, dataset, dih
		
		self.measures = measures
		self.fout = open ( filename, "w" )
		
		self.threshold = threshold
		self.k = quartile
		
		self.features_expanded = {}
		self.already_processed = {}
		
		#~ self.entropies_k, self.entropies_v = read("../TypeDM/entropies")
		#~ self.entropies = read("../TypeDM/entropies2")
		self.entropies = read("../TypeDM/sing_entropies2")
		
		
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
			
			feats_to_expand = {x for x in self.matrice_filtrata[t]}
			
			f_ipo = open(path+t+".sim")
			
			neighbours_feats = set([el for el in self.matrice_filtrata[t]])
			w = 1
			while w > self.threshold:
				line = f_ipo.readline().split()
				corr = line[0].strip()
				w = float(line[1].strip())
				
				if w > self.threshold and not corr == t and corr in self.matrice_filtrata and corr[-1] == t[-1]:
						for el in self.matrice_filtrata[corr]:
							neighbours_feats.add(el)
		
			feats = {}	
			for el in feats_to_expand:
				
				if el in self.already_processed:
					feats[el] = self.already_processed[el]
				else:
					lemma_el, synrel = el.split(":")[0], el.split(":")[1]
					
					feats[el] = {}
					
					f_feat = open(path+lemma_el+".sim")
					
					w = 1
					while w > self.threshold:
						line = f_feat.readline().split()
						corr = line[0]
						w = float(line[1])
						
						new_feat = corr+":"+synrel
						
						
						if corr in self.entropies:
							entropy_corr = self.entropies[corr]
							
							if w > self.threshold and corr[-1] == lemma_el[-1]:
									feats[el][new_feat] = entropy_corr
				
				
					topk = int(self.k * len(feats[el]) )
					self.already_processed[el] = sorted(feats[el].items(), key = lambda x: x[1], reverse = True)[:topk]
					
					#~ print t
					#~ print el, feats[el]
					#~ raw_input()
				
				
				feats[el] = set()
				
				
				
				#~ print "JUST A CHECK:", t, el
				#~ print len(self.already_processed[el])
				#~ print "most entropic: ", self.already_processed[el][0]
				#~ print "least entropic: ", self.already_processed[el][topk]
				#~ print "least entropic of list: ", self.already_processed[el][-1]
				
				for x in self.already_processed[el]:
					#~ print x, x[0] in neighbours_feats
					#~ raw_input()
					if x[0] in neighbours_feats:
						feats[el].add(x[0])			
				
				#~ print len(feats[el])
				#~ print
		
		
			self.features_expanded[t] = feats
		
		return self.features_expanded[t]
	
	def esegui_calcoli ( self ):
		
		sorted_selected_measures = sorted ( list(self.measures.selected_measures) )
		self.fout.write ("target\trelatum\trelazione\t"+"\t".join (sorted_selected_measures)+"\n")
		
		print "coppie:", len(self.dataset)
		
		i = 0
		for target, relatum, relazione in self.dataset:
			i+=1
			if not i%1000:
				print "coppia", i, "->", target, relatum
			
			self.fout.write (target+"\t"+relatum+"\t"+relazione+"\t")
			measdict = self.compute_measures ( target, relatum )
			for meas in sorted_selected_measures :
				self.fout.write (str(measdict[meas])+"\t")
			
			self.fout.write("\n")
			
		self.fout.close()
