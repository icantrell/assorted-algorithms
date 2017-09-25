Natural Language Processing(NLP):
These files contain an implementation of the baum welch algorithm. The algorithm is used to recognise patterns in sentences such as
grammar by tagging a sequence of words with a sequence of hidden markov model states. The formal problem is ussually reffered to as parts
of speech tagging. This algorithm also has many other uses in recognising time series such as predicting stock values, speech recognition, 
genetics and even body frame recognition. HOWEVER, THIS ALGORITHM STILL HAS A BUG. 

The algorithm is trained inside nlp_training.py where it is feed a .dat file containing the brown corpus and a training file with any
english text. The algorithm will recognize the patterns in the training file and use these label words with it's states these states can
then be statistically compared angainst words labeled with english grammar symbols. The brown_words.dat file contains a corpus that is 
labeled with correct english grammar symbols. However, in practice one might often see the labels left as raw states.
