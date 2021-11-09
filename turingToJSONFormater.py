import json

machineDef = {
'Q' : [],           #states
'Sigma' : [],     #alphabet
'Gamma' : [],       #tape
#transition format:
#qn = {'read':{'next':'qm', 'write': ' ', 'move': [-1 or 1]}, 
#       'read':{'next':'qm', 'write': ' ', 'move': [-1 or 1]},  }
'Delta' : {},       #transición
'Q0' : '',          #initial state
'Qaccept' : '',     #acceptation state
'Qreject' : ''      #rejection state
}

#la maquina pedira la cantidad de iteraciones que se quieren imprimir cada vez que imprime
#la cinta será un string y siempre tendrá ' ' al final. Si se intenta accesar a -1 se hará:
#string = ' ' + string y se cambiará el index a 0
#machineDef['Q'] = ['q1', 'q2', 'q3', 'q4', 'q5', 'qaccept', 'qreject']
#machineDef['Sigma'] = ['0']
#machineDef['Gamma'] = ['0', 'x', ' ']
#machineDef['Q0'] = 'q1'
#machineDef['Qaccept'] = 'qaccept'
#machineDef['Qreject'] = 'qreject'
#machineDef['Delta'] = {
#    'q1':{'0':{'next':'q2', 'write': ' ', 'move': 1}, 
#            ' ':{'next':'qreject', 'write': ' ', 'move': 1}, 
#            'x':{'next':'qreject', 'write': 'x', 'move': 1}, },
#    'q2':{'0':{'next':'q3', 'write': 'x', 'move': 1}, 
#            ' ':{'next':'qaccept', 'write': ' ', 'move': 1}, 
#            'x':{'next':'q2', 'write': 'x', 'move': 1}, },
#    'q3':{'0':{'next':'q4', 'write': '0', 'move': 1}, 
#            ' ':{'next':'q5', 'write': ' ', 'move': -1}, 
#            'x':{'next':'q3', 'write': 'x', 'move': 1}, },
#    'q4':{'0':{'next':'q3', 'write': 'x', 'move': 1}, 
#            ' ':{'next':'qreject', 'write': ' ', 'move': 1}, 
#            'x':{'next':'q4', 'write': 'x', 'move': 1}, },
#    'q5':{'0':{'next':'q5', 'write': '0', 'move': -1}, 
#            ' ':{'next':'q2', 'write': ' ', 'move': 1}, 
#            'x':{'next':'q5', 'write': 'x', 'move': -1}, },
#
#}
machineDef['Q'] = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6',]
machineDef['Sigma'] = ['a', 'b', 'c', 'd']
machineDef['Gamma'] = ['a', 'b', 'c', 'd', ' ', 'x']
machineDef['Q0'] = 'q1'
machineDef['Qaccept'] = 'q6'
machineDef['Qreject'] = 'q0'
machineDef['Delta'] = {
    'q1':{'a':{'next':'q2', 'write': ' ', 'move': 1}, 
            'b':{'next':'q0', 'write': 'b', 'move': 1},
            'c':{'next':'q0', 'write': 'c', 'move': 1},
            'd':{'next':'q0', 'write': 'd', 'move': 1}, 
            ' ':{'next':'q0', 'write': ' ', 'move': 1}, 
            'x':{'next':'q0', 'write': 'x', 'move': 1},},
   'q2':{'b':{'next':'q3', 'write': 'x', 'move': 1}, 
            'a':{'next':'q0', 'write': 'a', 'move': 1},
            'c':{'next':'q0', 'write': 'c', 'move': 1},
            'd':{'next':'q0', 'write': 'd', 'move': 1}, 
            ' ':{'next':'q0', 'write': ' ', 'move': 1}, 
            'x':{'next':'q0', 'write': 'x', 'move': 1},},
   'q3':{'c':{'next':'q4', 'write': 'x', 'move': 1}, 
            'a':{'next':'q0', 'write': 'a', 'move': 1},
            'b':{'next':'q0', 'write': 'b', 'move': 1},
            'd':{'next':'q0', 'write': 'd', 'move': 1}, 
            ' ':{'next':'q0', 'write': ' ', 'move': 1}, 
            'x':{'next':'q0', 'write': 'x', 'move': 1},},
   'q4':{'d':{'next':'q6', 'write': 'd', 'move': 1}, 
            'a':{'next':'q0', 'write': 'a', 'move': 1},
            'b':{'next':'q0', 'write': 'b', 'move': 1},
            'c':{'next':'q0', 'write': 'c', 'move': 1}, 
            ' ':{'next':'q5', 'write': ' ', 'move': 1}, 
            'x':{'next':'q4', 'write': 'x', 'move': -1},},
   'q5':{'d':{'next':'q0', 'write': 'd', 'move': 1}, 
            'a':{'next':'q0', 'write': 'a', 'move': 1},
            'b':{'next':'q0', 'write': 'b', 'move': 1},
            'c':{'next':'q0', 'write': 'c', 'move': 1}, 
            ' ':{'next':'q4', 'write': ' ', 'move': -1}, 
            'x':{'next':'q5', 'write': 'x', 'move': 1},},
}


with open('turingMachine.tur', 'w') as dump:
    dump.write(json.dumps(machineDef))

#with open('turingMachine.tur', 'r') as check:
#    x = json.loads(check.read())
#    print(x)