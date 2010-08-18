from trombone.corpus import TromboneCorpus

# create a corpus
corpus = TromboneCorpus()

# retrieve result and print it
print corpus.get(
        {'input': "http://localhost/~sgs/Temp/lear.xml"}, # input query
        'DocumentExporter', # tool
        'xml', # output format
    )
