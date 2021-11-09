import json


machineDef = {}
with open('turingMachine.tur', 'r') as machine:
    machineDef = json.loads(machine.read())

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

print('Input chain: ')
chain = input()
currState = machineDef['Q0']
head = 0

while True:
    if currState == machineDef['Qaccept']:
        print('Input chain accepted')
        break
    if currState == machineDef['Qreject']:
        print('Input chain rejected')
        break
    if head == len(chain):
        chain+=' '
    if head >= 0:
        rule = machineDef['Delta'][currState][chain[head]]
        print('current chain: ' + chain + ' state: ' + currState + ' read: ' + chain[head] + ' rule: ' + str(rule))
        chain = chain[:head] + rule['write'] + chain[head+1:]
    else:
        rule = machineDef['Delta'][currState][' ']
        print('current chain: ' + chain + ' state: ' + currState + ' read: ' + ' ' + ' rule: ' + str(rule))
        head = -1
    currState = rule['next']
    head += rule['move']
    
    

