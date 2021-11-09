import json


machineDef = {}
file = input('Input file for machine definition: ')
with open(file, 'r') as machine:
    machineDef = json.loads(machine.read())

print('Input chain: ')
chain = input()

def verification(chain):
    if len(machineDef['Q']) < 1:
        print('No states were specified')
        return False
    if len(machineDef['Delta']) < 1:
        print('No transitions were specified')
        return False
    if len(machineDef['Gamma']) < 1:
        print('No tape alphabet was specified')
        return False
    if not(machineDef['Qaccept'] in machineDef['Q']):
        print('Acceptation state is not specified in the state list')
        return False
    if not(machineDef['Qreject'] in machineDef['Q']):
        print('Rejection state is not specified in the state list')
        return False
    if not(machineDef['Q0'] in machineDef['Q']):
        print('Starting state is not specified in the state list')
        return False
    
    for i in machineDef['Delta'].values():
        for j in i.values():
            if not(j['write'] in machineDef['Gamma']):
                print('State machine can write characters that are not specified in the tape character list')
                return False
    
    for i in chain:
        if not(i in machineDef['Sigma']):
            print('Input chain contains characters that are not specified in the valid character list')
            return False


    print('Loaded machine: ')
    print('M = {')
    print(machineDef['Q'])
    print(machineDef['Sigma'])
    print(machineDef['Gamma'])
    print(machineDef['Delta'])
    print(machineDef['Q0'])
    print(machineDef['Qaccept'])
    print(machineDef['Qreject'])
    print('}')
    return True

output = ''
if verification(chain):

    currState = machineDef['Q0']
    head = 0
    running = True
    iterations = 100
    while running:
        for i in range(iterations):
            if currState == machineDef['Qaccept']:
                output += 'Input chain accepted'
                print('Input chain accepted')
                running = False
                break
            if currState == machineDef['Qreject']:
                output += 'Input chain rejected'
                print('Input chain rejected')
                running = False
                break

            if head == len(chain):
                chain+=' '

            if head < 0:
                head = 0

            rule = machineDef['Delta'][currState][chain[head]]
            line = 'tape state: ' + chain + ' state: ' + currState 
            line += ' read: ' + (chain[head] if chain[head] != ' ' else '_') + ' rule: ' 
            line += ' next state: ' + rule['next']
            line += ' write: ' + (rule['write'] if rule['write'] != ' ' else '_')
            line += ' move: ' + ('Right' if rule['move'] == 1 else 'Left')
            print(line)
            line += '\n'
            output += line
            chain = chain[:head] + rule['write'] + chain[head+1:]
            currState = rule['next']
            head += rule['move']
        if (running):
            print('The cap of execution has been reached.')
            iterations = int(input('If you wish to continue processing, input the amount of iterations to execute (or -1 to stop execution): \n'))
            if iterations < 0:
                output+= 'Execution stoped by user'
                print('Execution stoped by user')
                break

with open('InterpreterLog.log', 'w') as log:
    log.write(output)