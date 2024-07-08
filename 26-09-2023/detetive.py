import termcolor
from logic import *

mustard = Symbol("Celmustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard,plum,scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom,kitchen,library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife,revolver,wrench]

symbols = characters + rooms + weapons


def check_kb(kb):
    for s in symbols:
        if (model_check(kb,s)):
            termcolor.cprint(f"{s}: Sim", "green")
        elif (not model_check(kb,Not(s))): # se não tem certeza que nao foi ele
            termcolor.cprint(f"{s}: Talvez", "yellow")
#regras
kb = And(
    Or(mustard, plum, scarlet),
    Or(ballroom,kitchen,library),
    Or(knife,revolver, wrench),

)

#tirando cartas
kb.add(Not(mustard))
kb.add(Not(kitchen))
kb.add(Not(revolver))
#palpite errado
kb.add(Not(And(scarlet,library,wrench)))
#tirou cartas
kb.add(Not(plum))
#kb.add(Not(ballroom))
kb.add(Not(And(scarlet,ballroom, wrench)))
kb.add(Not(And(plum,ballroom, knife)))
kb.add(Not(And(scarlet,ballroom, knife)))
print(kb.formula())
check_kb(kb)