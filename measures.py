
import math
import os

class MeasuresExpandedFeatures:
	
	def __init__ (self, cosines, selected_measures ):
		self.cosines = cosines
		self.selected_measures = selected_measures
		self.current = {}	
	
	def reset ( self ):
		self.current = {}	
		
	def compute ( self, meas_name, u, v, feats ):
		if not meas_name in self.current:
			if meas_name == "cos":
				meas = self.cos ( u, v)
			elif meas_name == "weedsprec":
				meas = self.weedsprec ( u, v, feats)
			elif meas_name == "clarkede":
				meas = self.clarkede ( u, v, feats)
			elif meas_name == "clarkedeinv":
				meas = self.clarkede ( v, u, feats)
			elif meas_name == "cosweeds":
				self.compute ( "weedsprec", u, v, feats )
				meas = self.cosweeds ( u, v, feats )		
			elif meas_name == "invcl":
				self.compute ( "clarkede", u, v, feats )
				self.compute ( "clarkedeinv", u, v, feats )
				meas = self.invcl ( u, v, feats )
			elif meas_name == "media":
				meas = self.num_feats( u, v, feats )
			elif meas_name == "cosmedia":
				self.compute ( "media", u, v, feats )
				meas = self.num_feats_2( u, v, feats )
			elif meas_name == "nmedia":
				meas = self.num_feats_n( u, v, feats )
			elif meas_name == "wmedia":
				meas = self.num_feats_w( u, v, feats )
				
			self.current[meas_name] = meas
		
		return self.current[meas_name]
			
	
	def cos ( self, a, b ):
		return self.cosines[min(a,b)][max(a,b)]
		
	def weedsprec (self, u, v, features):
		
		num = 0.0
		den = 0.0

		for f in features:
			if any ( [ v.get(el, 0.0)>0 for el in features[f] ] ):
				num+=u.get (f, 0.0)
		
		for i in u:
			den+=u[i]
		
		if den > 0:
			ret = num/den
		else:
			ret = 0
		
		return ret
		

	def clarkede (self, u, v, features):
			
		num = 0.0
		den = 0.0

		for f in features:
			num += min ( u.get(f, 0.0), max ([ v.get(el, 0.0) for el in features[f]]) )
		
		for i in u:
			
			den+=u[i]
		
		if den > 0:
			ret = num/den
		else:
			ret = 0
		
		return ret

			
	def cosweeds (self, u, v, features):
		WP = self.current["weedsprec"]
		COS = self.current["cos"]
					
		arg = WP*COS
		
		return math.sqrt(arg)
		
		
	def invcl (self, u, v, feats):
		
		cd1 = self.current["clarkede"]
		cd2 = self.current["clarkedeinv"]
		
		try:
			return math.sqrt(cd1 * (1-cd2))
		except:
			return 0
			
	def num_feats (self, u, v, features):
		
		num = 0.0
		den = len(u)*1.0
		for f in features:
			l = sum([1 if v.get(x, 0.0) > 0 else 0 for x in features[f]])
			#~ num+=l*len(features[f])
			num+=l
			#~ den+=len(features[f])
			
		return num/den

	def num_feats_n (self, u, v, features):
		
		num = 0.0
		
		sorted_f = sorted([(x, u[x]) for x in features], key = lambda x: x[1], reverse = True)
		
		i = 0
		
		for f in features:
			l = sum([1 if v.get(x, 0.0) > 0 else 0 for x in features[f]])

			num+=l*(1-i/len(features))
			i+=1
			
			
		return num

	def num_feats_w (self, u, v, features):
		
		num = 0.0
		den = len(u)*1.0
				
		mod_u = math.sqrt (sum([x**2 for x in u.values()]))
		new_u = {x: u[x]/mod_u for x in features}
		
		i = 0
		for f in features:
			l = sum([1 if v.get(x, 0.0) > 0 else 0 for x in features[f]])
			num+=l*new_u[f]
			
			i+=1
			
		return num

	def num_feats_2 (self, u, v, features):
		
		NF = self.current["media"]
		COS = self.current["cos"]
		
		return NF*COS
		
		
class MeasuresBase:
	
	def __init__ ( self, cosines, selected_measures ):
		
		self.cosines = cosines
		self.selected_measures = selected_measures
		self.current = {}	

	def reset ( self ):
		self.current = {}	
		
	def compute ( self, meas_name, u, v ):
		if not meas_name in self.current:
			if meas_name == "cos":
				meas = self.cos ( u, v )
			elif meas_name == "weedsprec":
				meas = self.weedsprec ( u, v )
			elif meas_name == "clarkede":
				meas = self.clarkede ( u, v )
			elif meas_name == "clarkedeinv":
				meas = self.clarkede ( v, u )
			elif meas_name == "cosweeds":
				self.compute ( "weedsprec", u, v )
				meas = self.cosweeds ( u, v )		
			elif meas_name == "invcl":
				self.compute ( "clarkede", u, v )
				self.compute ( "clarkedeinv", u, v )
				meas = self.invcl ( u, v )
				
				
			self.current[meas_name] = meas
		
		return self.current[meas_name]
			
	
	def cos ( self, a, b ):
		return self.cosines[min(a,b)][max(a,b)]
	
	
	def weedsprec (self, u, v):
			
		num = 0.0
		den = 0.0

		for i in u:
			if v.get(i, 0.0)>0:
				num+=u[i]
				
			den+=u[i]
		
		if den > 0:
			ret = num/den
		else:
			ret = 0
		
		return ret
		
		
	def clarkede (self, u, v):
			
		num = 0.0
		den = 0.0

		for i in u:
			
			num+=min(u[i], v.get(i, 0.0))
				
			den+=u[i]
		
		if den > 0:
			ret = num/den
		else:
			ret = 0
		
		return ret
			
	def cosweeds (self, u, v):
		
		WP = self.current["weedsprec"]	
		COS = self.current["cos"]
			
		arg = WP*COS
		
		return math.sqrt(arg)	
		
	def invcl (self, u, v):
		cd1 = self.current["clarkede"]
		cd2 = self.current["clarkedeinv"]
		
		return math.sqrt(cd1 * (1-cd2))
		
class CosineManager:
	
	def __init__ ( self, filename, matrix, dataset ):
		
		self.filename = filename
		
		if os.path.exists ( filename ):
			fin = open (filename)
			self.cosines = self.load_cosines ( fin )
			fin.close ()
		else:
			self.cosines = self.compute_cosines ( matrix, dataset )
			self.dump ()
			

	def load_cosines ( self, fin ):
		ret = {}
		for line in fin:
			linesplit = line.strip().split()
			s1 = linesplit[0]
			s2 = linesplit[1]
			cos = float(linesplit[2])
			
			min_s = min (s1,s2)
			max_s = max (s1,s2)
			
			if not min_s in ret:
				ret[min_s] = {}
			
			ret[min_s][max_s] = max(cos, 0)
			
		return ret

		
	def dump ( self ):
		fout = open (self.filename, "w")
		for s1 in self.cosines:
			for s2 in self.cosines[s1]:
				fout.write (s1+"\t"+s2+"\t"+str(self.cosines[s1][s2])+"\n")
		fout.close ()
		
	def compute_cosines ( self, matrix, dataset ):
		ret = {}
		for s1, s2, rel in dataset:
			min_s = min (s1, s2)
			max_s = max (s1, s2)
			
			if not min_s in ret:
				ret[min_s] = {}
			
			u = matrix.dict_matrice [min_s]
			v = matrix.dict_matrice [max_s]
			mod_u = matrix.modules_vect [min_s]
			mod_v = matrix.modules_vect [max_s]
			
			ret[min_s][max_s] = cos ( u, v, mod_u, mod_v )
		
		return ret

def cos (u, v, mod_u, mod_v):

	if mod_u*mod_v == 0:
		ret = 0
	else:
		num = 0.0
		
		for i in u:
			num+=u[i]*v.get(i, 0.0)

		ret = num/(mod_u*mod_v)
	
	return ret
