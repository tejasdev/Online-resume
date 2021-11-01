from rdflib import URIRef
resource = URIRef('http://dbpedia.org/resource/Ann_Dunham')
print (resource.split('/')[-1])