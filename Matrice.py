import math

class Matrice:
	'''
		dict_matrice[x] contiene il vettore sparso di x 
		modules_vect[x] contiene il modulo del vettore di x 
		lemmaset contiene tutti i lemmi presenti nella matrice 
	
	'''
	def __init__ (self, filename):
		
		self.dict_matrice = {}
		self.modules_vect = {}
		self.sum_vect = {}
		
		self.lemmaset = set()
		
		self.leggi(open(filename))
		
	def leggi (self, fin_matrice):

		for line in fin_matrice:

			linesplit = line.split()
			
			w1 = linesplit[0].strip()
			link = linesplit[1].strip()
			w2 = linesplit[2].strip()
			weight = float(linesplit[3].strip())
			
			#~ print linesplit
			#~ raw_input()
			
			w2_entry = w2+":"+link
			
			if weight>0:
		
				self.lemmaset.add(w1)				
				#~ self.lemmaset.add(w2)				
				
				if not w1 in self.dict_matrice:
					self.dict_matrice[w1] = {}
					self.modules_vect[w1] = 0
					self.sum_vect[w1] = 0
				
				self.dict_matrice[w1][w2_entry] = weight
				
				self.modules_vect[w1]+=weight**2
				self.sum_vect[w1]+=weight
		
		for x in self.modules_vect:
			self.modules_vect[x] = math.sqrt(self.modules_vect[x])
			
	
	def get_filtered_matrix ( self, filter_condition ):
		ret = {}
		for x in self.dict_matrice:
			dict_row = { y:self.dict_matrice[x][y] for y in self.dict_matrice[x] if filter_condition(y) }
			ret[x] = dict_row
		
		return ret
	
			
if __name__ == "__main__":
	
	Mat = Matrice("/home/ludovica.pannitto/progetto_sns/TypeDM/typedm.head.txt")
	
	#~ for x in Mat.dict_matrice:
		#~ for y in Mat.dict_matrice[x]:
			#~ print x, y, Mat.dict_matrice[x][y]
			
	#~ raw_input()		
			
	print Mat.lemmaset
