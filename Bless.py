class Bless:
	def __init__(self, fin, lemmaset):
		self.lemmaset = lemmaset
		self.items = {}
		self.noitems = 0
		
		self.leggi(open(fin))


	def leggi(self, fin_dataset):
		
		for line_dataset in fin_dataset:

			linesplit = line_dataset.split(";")
			
			target = linesplit[0].strip()
			relatum = linesplit[1].strip()
			rel = linesplit[2].strip()

			if not self.lemmaset or ( target in self.lemmaset and relatum in self.lemmaset ):

				self.noitems += 1

				if not target in self.items:
					self.items[target] = {}
				
				if not rel in self.items[target]:
					self.items[target][rel] = []
					
				self.items[target][rel].append(relatum)
		
	def get_triples ( self ):
		return [ (target, relatum, rel) for target in self.items for rel in self.items[target] for relatum in self.items[target][rel] ]
	
	#TODO: scrivere per bene
	def get_triples_for_a_run ( self ):		
		return self.get_triples ()

if __name__ == "__main__":
	
	BLESS = Bless("/home/ludovica.pannitto/progetto_sns/filteredbless", set(["knife-n", "hotel-n", "alligator-n", "frog-n", "end-n"]))

	for t in BLESS.items:
		print t
		print BLESS.items[t]
		print
