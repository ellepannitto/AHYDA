import ForBoxplotExtractor
import BaseRun
import ExpandedFeaturesRun
import Matrice
from measures import *
import Bless
import TimeCalc

if __name__ == "__main__":
	
	t = TimeCalc.TimeCalc ()
	
	t.print_message ("inizio...")
	
	matrix = Matrice.Matrice ( "/home/ludovica.pannitto/progetto_sns/TypeDM/typedm.filtered.txt" )
	mf = matrix.get_filtered_matrix ( lambda y: True )
	
	t.print_message ( "caricato matrice" )
	
	b = Bless.Bless ( "/home/ludovica.pannitto/progetto_sns/filteredbless", matrix.lemmaset )
	df = b.get_triples_for_a_run ()
	
	t.print_message ( "caricato dataset" )
	
	cm = CosineManager ( "../data/coseni_svd", None, None ) 
	t.print_message ( "caricati coseni" )

	

	meas = MeasuresBase ( cm.cosines, set(["cos", "clarkede", "invcl", "cosweeds", "weedsprec"]) )	

	t.print_message ( "creo Lenci 2012 svd dih ..." )

	br = BaseRun.BaseRun ( "../results/Lenci2012.svd.dih", mf, df, True, meas )
	t.print_message ( "inizio calcoli ..." )
	br.esegui_calcoli ()
	t.print_message ( "fine calcoli Lenci 2012 svd dih" )


	t.print_message ( "inizio estrazione dati per boxplot ..." )

	fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/Lenci2012.svd.dih", "../results", "max" )
	fbe.extract ()

	fbe_new = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/Lenci2012.svd.dih", "../results", "avg" )
	fbe_new.extract ()

	t.print_message ( "fine estrazioni dati per boxplot" )


	t.print_message ( "creo Lenci 2012 svd dih-rev ..." )

	br = BaseRun.BaseRun ( "../results/Lenci2012.svd.dih-rev", mf, df, False, meas )
	t.print_message ( "inizio calcoli ..." )
	br.esegui_calcoli ()
	t.print_message ( "fine calcoli Lenci 2012 svd dih-rev" )


	t.print_message ( "inizio estrazione dati per boxplot ..." )

	fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/Lenci2012.svd.dih-rev", "../results", "max" )
	fbe.extract ()

	fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/Lenci2012.svd.dih-rev", "../results", "avg" )
	fbe.extract ()

	t.print_message ( "fine estrazioni dati per boxplot" )


	meas = MeasuresExpandedFeatures ( cm.cosines, set(["cos", "clarkede", "invcl", "cosweeds", "weedsprec", "media", "cosmedia", "nmedia", "wmedia"]) ) 
	
	t.print_message ( "creo Expanded Features svd dih ..." )

	br = ExpandedFeaturesRun.ExpandedFeaturesRun ( "../results/ExpandedFeatures.svd.dih", mf, df, True, meas, 0.9 )
	t.print_message ( "inizio calcoli ..." )
	br.esegui_calcoli ()
	t.print_message ( "fine calcoli Expanded Features svd dih" )


	t.print_message ( "inizio estrazione dati per boxplot ..." )

	fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/ExpandedFeatures.svd.dih", "../results", "max" )
	fbe.extract ()

	fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/ExpandedFeatures.svd.dih", "../results", "avg" )
	fbe.extract ()

	t.print_message ( "fine estrazioni dati per boxplot" )

	t.print_message ( "creo Expanded Features svd dih-rev ..." )

	br = ExpandedFeaturesRun.ExpandedFeaturesRun ( "../results/ExpandedFeatures.svd.dih-rev", mf, df, False, meas, 0.9 )
	t.print_message ( "inizio calcoli ..." )
	br.esegui_calcoli ()
	t.print_message ( "fine calcoli Expanded Features svd dih-rev" )


	t.print_message ( "inizio estrazione dati per boxplot ..." )

	fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/ExpandedFeatures.svd.dih-rev", "../results", "max" )
	fbe.extract ()

	fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/ExpandedFeatures.svd.dih-rev", "../results", "avg" )
	fbe.extract ()

	t.print_message ( "fine estrazioni dati per boxplot" )

	################## NO SVD #########################

	cm = CosineManager ("../data/coseni_svd", mf, df)	
	
	
	meas = MeasuresBase ( cm.cosines, set(["cos", "clarkede", "invcl", "cosweeds", "weedsprec"]) )	

	t.print_message ( "creo Lenci 2012 nosvd dih ..." )

	br = BaseRun.BaseRun ( "../results/Lenci2012.nosvd.dih", mf, df, True, meas )
	t.print_message ( "inizio calcoli ..." )
	br.esegui_calcoli ()
	t.print_message ( "fine calcoli Lenci 2012 nosvd dih" )


	t.print_message ( "inizio estrazione dati per boxplot ..." )

	fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/Lenci2012.nosvd.dih", "../results", "max" )
	fbe.extract ()

	fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/Lenci2012.nosvd.dih", "../results", "avg" )
	fbe.extract ()

	t.print_message ( "fine estrazioni dati per boxplot" )


	t.print_message ( "creo Lenci 2012 nosvd dih-rev ..." )

	br = BaseRun.BaseRun ( "../results/Lenci2012.nosvd.dih-rev", mf, df, False, meas )
	t.print_message ( "inizio calcoli ..." )
	br.esegui_calcoli ()
	t.print_message ( "fine calcoli Lenci 2012 nosvd dih-rev" )


	t.print_message ( "inizio estrazione dati per boxplot ..." )

	fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/Lenci2012.nosvd.dih-rev", "../results", "max" )
	fbe.extract ()

	fbe = ForBoxplotExtractor.ForBoxplotExtractor ( "../results/Lenci2012.nosvd.dih-rev", "../results", "avg" )
	fbe.extract ()

	t.print_message ( "fine estrazioni dati per boxplot" )	

	
	
	
	
	

