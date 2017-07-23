import ForBoxplotExtractor
import BaseRun
import EntropyFeaturesRun
#~ import ExpandedFeaturesRun
import NewExpandedFeaturesRun as ExpandedFeaturesRun
import SLQSFeaturesRun
import Matrice
from measures import *
import Bless
import TimeCalc

if __name__ == "__main__":
	
	t = TimeCalc.TimeCalc ()
	
	t.print_message ("inizio...")
	
	matrix = Matrice.Matrice ( "/home/ludovica.pannitto/progetto_sns/TypeDM/typedm.filtered.txt" )
	#~ matrix = Matrice.Matrice ( "/home/ludovica.pannitto/progetto_sns/TypeDM/typedm.head.txt" )
	mf = matrix.get_filtered_matrix ( lambda y: True )	
	
	t.print_message ( "caricato matrice" )
	
	b = Bless.Bless ( "/home/ludovica.pannitto/progetto_sns/filteredbless", matrix.lemmaset )
	df = b.get_triples_for_a_run ()
	
	t.print_message ( "caricato dataset" )
	
	cm = CosineManager ( "../data/coseni_svd", None, None ) 
	t.print_message ( "caricati coseni" )

	#~ meas = MeasuresBase ( cm.cosines, set(["cos", "clarkede", "invcl", "cosweeds", "weedsprec"]) )	

	#~ t.print_message ( "creo Lenci 2012 svd dih ..." )

	#~ br = BaseRun.BaseRun ( "../results/Lenci2012.svd.dih", mf, df, True, meas )
	#~ t.print_message ( "inizio calcoli ..." )
	#~ br.esegui_calcoli ()
	#~ t.print_message ( "fine calcoli Lenci 2012 svd dih" )


	#~ t.print_message ( "inizio estrazione dati per boxplot ..." )

	#~ fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/Lenci2012.svd.dih", "../results", "max" )
	#~ fbe.extract ()

	#~ fbe_new = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/Lenci2012.svd.dih", "../results", "avg" )
	#~ fbe_new.extract ()

	#~ t.print_message ( "fine estrazioni dati per boxplot" )


	#~ t.print_message ( "creo Lenci 2012 svd dih-rev ..." )

	#~ br = BaseRun.BaseRun ( "../results/Lenci2012.svd.dih-rev", mf, df, False, meas )
	#~ t.print_message ( "inizio calcoli ..." )
	#~ br.esegui_calcoli ()
	#~ t.print_message ( "fine calcoli Lenci 2012 svd dih-rev" )


	#~ t.print_message ( "inizio estrazione dati per boxplot ..." )

	#~ fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/Lenci2012.svd.dih-rev", "../results", "max" )
	#~ fbe.extract ()

	#~ fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/Lenci2012.svd.dih-rev", "../results", "avg" )
	#~ fbe.extract ()

	#~ t.print_message ( "fine estrazioni dati per boxplot" )


	#~ meas = MeasuresExpandedFeatures ( cm.cosines, set(["cos", "clarkede", "invcl", "cosweeds", "weedsprec", "media", "cosmedia", "nmedia", "wmedia"]) ) 
	
	#~ t.print_message ( "creo Expanded Features svd dih ..." )

	#~ br = ExpandedFeaturesRun.ExpandedFeaturesRun ( "../results/ExpandedFeatures.svd.dih", mf, df, True, meas, 0.9 )
	#~ t.print_message ( "inizio calcoli ..." )
	#~ br.esegui_calcoli ()
	#~ t.print_message ( "fine calcoli Expanded Features svd dih" )


	#~ t.print_message ( "inizio estrazione dati per boxplot ..." )

	#~ fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/ExpandedFeatures.svd.dih", "../results", "max" )
	#~ fbe.extract ()

	#~ fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/ExpandedFeatures.svd.dih", "../results", "avg" )
	#~ fbe.extract ()

	#~ t.print_message ( "fine estrazioni dati per boxplot" )

	#~ t.print_message ( "creo Expanded Features svd dih-rev ..." )

	#~ br = ExpandedFeaturesRun.ExpandedFeaturesRun ( "../results/ExpandedFeatures.svd.dih-rev", mf, df, False, meas, 0.9 )
	#~ t.print_message ( "inizio calcoli ..." )
	#~ br.esegui_calcoli ()
	#~ t.print_message ( "fine calcoli Expanded Features svd dih-rev" )


	#~ t.print_message ( "inizio estrazione dati per boxplot ..." )

	#~ fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/ExpandedFeatures.svd.dih-rev", "../results", "max" )
	#~ fbe.extract ()

	#~ fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/ExpandedFeatures.svd.dih-rev", "../results", "avg" )
	#~ fbe.extract ()

	#~ t.print_message ( "fine estrazioni dati per boxplot" )

	#~ ################## NO SVD #########################

	#~ cm = CosineManager ("../data/coseni_svd", mf, df)	
	
	
	#~ meas = MeasuresBase ( cm.cosines, set(["cos", "clarkede", "invcl", "cosweeds", "weedsprec"]) )	

	#~ t.print_message ( "creo Lenci 2012 nosvd dih ..." )

	#~ br = BaseRun.BaseRun ( "../results/Lenci2012.nosvd.dih", mf, df, True, meas )
	#~ t.print_message ( "inizio calcoli ..." )
	#~ br.esegui_calcoli ()
	#~ t.print_message ( "fine calcoli Lenci 2012 nosvd dih" )


	#~ t.print_message ( "inizio estrazione dati per boxplot ..." )

	#~ fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/Lenci2012.nosvd.dih", "../results", "max" )
	#~ fbe.extract ()

	#~ fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/Lenci2012.nosvd.dih", "../results", "avg" )
	#~ fbe.extract ()

	#~ t.print_message ( "fine estrazioni dati per boxplot" )


	#~ t.print_message ( "creo Lenci 2012 nosvd dih-rev ..." )

	#~ br = BaseRun.BaseRun ( "../results/Lenci2012.nosvd.dih-rev", mf, df, False, meas )
	#~ t.print_message ( "inizio calcoli ..." )
	#~ br.esegui_calcoli ()
	#~ t.print_message ( "fine calcoli Lenci 2012 nosvd dih-rev" )


	#~ t.print_message ( "inizio estrazione dati per boxplot ..." )

	#~ fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/Lenci2012.nosvd.dih-rev", "../results", "max" )
	#~ fbe.extract ()

	#~ fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/Lenci2012.nosvd.dih-rev", "../results", "avg" )
	#~ fbe.extract ()

	#~ t.print_message ( "fine estrazioni dati per boxplot" )	
	
	#~ meas = MeasuresExpandedFeatures ( cm.cosines, set(["cos", "clarkede", "invcl", "cosweeds", "weedsprec", "media"]) ) 
	
	#~ t.print_message ( "creo Expanded Features svd dih ..." )

	#~ br = ExpandedFeaturesRun.ExpandedFeaturesRun ( "../results/NewExpandedFeatures.svd.dih", mf, df, True, meas, 0.9 )
	#~ t.print_message ( "inizio calcoli ..." )
	#~ br.esegui_calcoli ()
	#~ t.print_message ( "fine calcoli Expanded Features svd dih" )
	
	#~ fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/NewExpandedFeatures.svd.dih", "../results", "max" )
	#~ fbe.extract ()

	#~ t.print_message ( "creo ENTROPY threshold = 0.5 ..." )

	#~ sr = EntropyFeaturesRun.EntropyFeaturesRun ( "../results/EntropyFeaturesRun05.dih", mf, df, True, meas, 0.5 )
	#~ t.print_message ( "inizio calcoli ..." )
	#~ sr.esegui_calcoli ()
	#~ t.print_message ( "fine calcoli ENTROPY threshold = 0.5 dih" )

	#~ fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/EntropyFeaturesRun05.dih", "../results", "max" )
	#~ fbe.extract ()
	
	
	meas = MeasuresExpandedFeatures ( cm.cosines, set(["hmedia", "havgmedia"]) )	
	t.print_message ( "creo ENTROPY threshold = 0.9 ..." )

	sr = EntropyFeaturesRun.EntropyFeaturesRun ( "../results/EntropyFeaturesRun03.dih", mf, df, True, meas, 0.9 )
	t.print_message ( "inizio calcoli ..." )
	sr.esegui_calcoli ()
	t.print_message ( "fine calcoli ENTROPY threshold = 0.9 dih" )

	fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/EntropyFeaturesRun03.dih", "../results", "max" )
	fbe.extract ()


	#~ t.print_message ( "creo SLQS threshold = 0.5, quartile = 1 ..." )

	#~ sr = SLQSFeaturesRun.SLQSFeaturesRun ( "../results/SLQSFeaturesRun051quart.dih", mf, df, True, meas, 0.5, 0.25 )
	#~ t.print_message ( "inizio calcoli ..." )
	#~ sr.esegui_calcoli ()
	#~ t.print_message ( "fine calcoli SLQS threshold = 0.5, quartile = 1 dih" )

	#~ fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/SLQSFeaturesRun051quart.dih", "../results", "max" )
	#~ fbe.extract ()

	#~ t.print_message ( "creo SLQS threshold = 0.7, quartile = 1 ..." )

	#~ sr = SLQSFeaturesRun.SLQSFeaturesRun ( "../results/SLQSFeaturesRun071quart.dih", mf, df, True, meas, 0.7, 0.25 )
	#~ t.print_message ( "inizio calcoli ..." )
	#~ sr.esegui_calcoli ()
	#~ t.print_message ( "fine calcoli SLQS threshold = 0.7, quartile = 1 ... dih" )

	#~ fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/SLQSFeaturesRun071quart.dih", "../results", "max" )
	#~ fbe.extract ()

	#~ t.print_message ( "creo SLQS threshold = 0.5, quartile = 2  ..." )

	#~ sr = SLQSFeaturesRun.SLQSFeaturesRun ( "../results/SLQSFeaturesRun052quart.dih", mf, df, True, meas, 0.5, 0.5 )
	#~ t.print_message ( "inizio calcoli ..." )
	#~ sr.esegui_calcoli ()
	#~ t.print_message ( "fine calcoli SLQS threshold = 0.5, quartile = 2  ... dih" )

	#~ fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/SLQSFeaturesRun052quart.dih", "../results", "max" )
	#~ fbe.extract ()
	
	
	
	

