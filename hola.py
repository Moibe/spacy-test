import spacy 

nlp = spacy.load('es_core_news_sm') #spacy download es_core_news_sm   

print("Tipo nlp: ", type(nlp))

texto = "En términos macroeconómicos, por producto interno bruto (PIB) es la duodécima economía mundial y la decimotercera por paridad del poder adquisitivo (PPA) en 2023; en escala regional, es la segunda economía de América Latina y la cuarta del continente.25​26​ Según el informe de 2023 de desarrollo humano de la ONU, tiene un índice de desarrollo humano alto de 0.781, y ocupa el 77.º lugar en el mundo.27​" 

documento = nlp(texto)

print("Tipo documento: ", type(documento))

for elemento in documento: 
    print(elemento)

for elemento in documento: 
    print(elemento, elemento.pos_)

print(spacy.explain('PROPN'))
print(spacy.explain('NOUN'))
print(spacy.explain('PUNCT'))
print(spacy.explain('ADJ'))
print(spacy.explain('NUM'))
print(spacy.explain('VERB'))

for oracion in documento.sents: #sentences
    print(oracion)
    print('-')