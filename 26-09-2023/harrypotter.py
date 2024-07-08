from logic import *

rain = Symbol("rain") # esta chovendo p
hagrid = Symbol("hagrid") #visitou hagrid q
dumbledoure = Symbol("dumbledoure") #visitou dumbledoure r

#sentence = And(rain,hagrid)
#print(sentence.formula()

# (~p -> q) v (q ^ e)

kb = And(
        Implication(Not(rain), hagrid), # se entao
        Or(hagrid, dumbledoure),
        Not(And(hagrid, dumbledoure)),''
)
print(kb.formula())
kb.add(dumbledoure)
print("Choveu: ", model_check(kb,rain))
print("Visitou Hagrid: ", model_check(kb,hagrid))