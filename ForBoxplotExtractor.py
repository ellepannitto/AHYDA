import random
import math
import os

import numpy as np
from sklearn.metrics import average_precision_score


INFINITE = float('inf')

def randomselect (lista, n):
	
	return random.sample(lista, n)

class ForBoxplotExtractor:
	
	def __init__ ( self, input_filename, output_directory, fun_str ):
		'''
			input_filename: file contenente la matrice
			self.output_directory: directory in cui salvare i risultati	
		'''	
		self.input_filename = input_filename
		self.output_directory = output_directory
		
		self.function = fun_str
		
							
	
	def extract ( self ):
			
		targets_measures = {}
		
		with open(self.input_filename) as fin:
			
			#first line contains the header
			first_line = fin.readline ()
			self.measures_to_consider = first_line.split ()[3:]
			self.rels_to_consider = set()
			line_no = 0
			
			for line in fin:
				line_no += 1
				linesplit = line.split()
				#~ print line_no, len(linesplit)
				
				target = linesplit[0]
				relatum = linesplit[1]
				rel = linesplit[2]
				
				m = { self.measures_to_consider[i] : float (linesplit[i+3]) for i in xrange (len(self.measures_to_consider)) }
				
				if not rel == '?':
				
					if not target in targets_measures:
						targets_measures[target] = {}
					
					if not rel in targets_measures[target]:
						targets_measures[target][rel] = { m_name: [] for m_name in self.measures_to_consider }
						
					for k, v in m.items():
						targets_measures[target][rel][k].append((v, relatum))

		
		selected_target_measures = {}
		for target in targets_measures:
			minimo = INFINITE
			massimo = 0
			
			
			for rel in targets_measures[target]:
				
				self.rels_to_consider.add (rel)
				
				m = targets_measures[target][rel].keys()[0]
				l = targets_measures[target][rel][m]
				
				if len(l) < minimo:
					minimo = len(l)
				
				if len(l)>massimo:
					massimo = len(l)

			if not target in selected_target_measures:
				selected_target_measures[target] = []
			
			for i in range ( massimo/minimo ):
				
				selected_target_measures[target].append ({})
				for rel in targets_measures[target]:
					if not rel in selected_target_measures[target][i]:
						selected_target_measures[target][i][rel] = { m_name: [] for m_name in self.measures_to_consider }
				
					for m, l in targets_measures[target][rel].items():					
						selected_target_measures[target][i][rel][m] = randomselect(l, minimo)
		
		
		self.compute_and_write_data_for_boxplot ( selected_target_measures )
		self.compute_and_write_average_precision ( selected_target_measures )

	def compute_and_write_average_precision ( self, selected_targets_measures ):
		
		fout = open(self.output_directory+"/apcounts/"+os.path.basename(self.input_filename)+".ap", "w")		
		fout.write("\t\t"+"\t".join([x for x in self.rels_to_consider])+"\n")

		for m in self.measures_to_consider:
			
			ap = {x:0.0 for x in self.rels_to_consider}
			n = 0
			
			for t in selected_targets_measures:
				
				n+=1
				runs_number = len ( selected_targets_measures[t] )
				for j in range ( runs_number ):
					
					run = selected_targets_measures[t][j]
					
					
					rel = []
					values = []
					
					for r in run:
						for i in range(len(run[r][m])):
							rel.append(r)
							values.append(selected_targets_measures[t][j][r][m][i][0])
					
					#~ print rel
					#~ print values
					#~ raw_input()

					for r in ap:
						rel2 = [ 1 if x == r else 0 for x in rel ]
						
						#~ print r
						#~ print rel
						#~ print rel2
						#~ raw_input()
						
						y_true = np.array(rel2)
						y_scores = np.array(values)
						
						ap[r]+=average_precision_score(y_true, y_scores)/runs_number  
			
			#~ print n
			ap = {k:v/n for k,v in ap.items()}
			fout.write(m+"\t"+"\t".join(["{0:.2f}".format(y) for x, y in ap.items()])+"\n")		
			#~ print m
			#~ print ap
		
	def compute_and_write_data_for_boxplot ( self, selected_target_measures ):
		
		maxima = { m: { t: { r:0  for r in self.rels_to_consider } for t in selected_target_measures } for m in self.measures_to_consider }
		
		for target in selected_target_measures:
			
			number_of_runs = len ( selected_target_measures[target] )
			for i in range (number_of_runs):
				
				run = selected_target_measures[target][i]
				
				for rel in run:
					for meas in run[rel]:
						
						if self.function == "max":						
							max_m = max ( run[rel][meas], key=lambda x: x[0] )
						elif self.function == "avg":
							max_m = (sum([el[0] for el in run[rel][meas]])/len(run[rel][meas]), "x")

						maxima[meas][target][rel] += max_m[0]/number_of_runs
					
		
		#~ max_targets_measures = { m_name: {} for m_name in self.measures_to_consider }

		#~ for x in targets_measures:
			
			#~ for rel in targets_measures[x]:
				
				#~ for m in max_targets_measures:
					
					#~ if not x in max_targets_measures[m]:
						#~ max_targets_measures[m][x] = {}
					
					
					#~ if self.function == "max":
						#~ max_targets_measures[m][x][rel] = max(targets_measures[x][rel][m], key = lambda x: x[0])
					#~ elif self.function == "average":
						#~ max_targets_measures[m][x][rel] = (sum([el[0] for el in targets_measures[x][rel][m]])/len(targets_measures[x][rel][m]), "x")
		
		max_targets_measures = maxima
		
		for m in max_targets_measures:
			
			for x in max_targets_measures[m]:
				
				#~ data = [v[0] for rel, v in max_targets_measures[m][x].items()]
				data = [v for rel, v in max_targets_measures[m][x].items()]
				
				mean = sum(data)/len(data)
				
				diff = [d-mean for d in data]
				
				sqdiff = [d**2 for d in diff]

				ssd = sum(sqdiff)
				
				var = ssd / (len(data)-1)
				
				stdev = math.sqrt(var)

				
				for rel in max_targets_measures[m][x]:
					
					old_tuple = max_targets_measures[m][x][rel]
					
					if stdev > 0:
						#~ new_tuple = ((old_tuple-mean)/stdev, old_tuple[1])
						new_tuple = (old_tuple-mean)/stdev
					else:
						#~ new_tuple = (old_tuple[0]-mean, old_tuple[1])
						new_tuple = old_tuple-mean
					
					max_targets_measures[m][x][rel] = new_tuple
					
					
					
		for m in max_targets_measures:
			fout = open(self.output_directory+"/data_boxplots/"+self.function+"."+os.path.basename(self.input_filename)+"."+m, "w")
			
			relists = {}
			for x in max_targets_measures[m]:
				
				for rel in max_targets_measures[m][x]:
					
					if not rel in relists:
						relists[rel]= []
					
					#~ relists[rel].append(str(max_targets_measures[m][x][rel][0]))
					relists[rel].append(str(max_targets_measures[m][x][rel]))
					
			l = []
			
			for rel in relists:
				for el in relists[rel]:
					l.append([rel,el])
			
			fout.write("RELATION\tVALUES\n")
			for x in l:
				fout.write("\t".join(x)+"\n")
				

