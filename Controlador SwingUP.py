import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

#Variaveis de Entrada (Antecedent)
ang = ctrl.Antecedent(np.arange(30, 330, 1), 'angulo')
velang = ctrl.Antecedent(np.arange(-10, 10, 1), 'velocidade angular')

#Variaveis de saída (Consequent)
output = ctrl.Consequent(np.arange(-6, 6, 1.), 'força aplicada (output)')

# atribuicao manual para o angulo
ang['NLS'] = fuzz.trimf(ang.universe, [90,130,170])
ang['NBS'] = fuzz.trimf(ang.universe, [30,150,170])
ang['SALN'] = fuzz.trimf(ang.universe, [170,175,180])
ang['Z'] = fuzz.trimf(ang.universe, [180,180,180])
ang['SALP'] = fuzz.trimf(ang.universe, [180,185,190])
ang['PBS'] = fuzz.trimf(ang.universe, [190,210,330])
ang['PLS'] = fuzz.trimf(ang.universe, [190,230,270])

# atribuicao manual para o velocidade angular
velang['NEG'] = fuzz.trapmf(velang.universe, [-10,-10,-1,0])
velang['ZS'] = fuzz.trapmf(velang.universe, [-0.1,-0.01,0.01,0.1])
velang['POS'] = fuzz.trapmf(velang.universe, [0,1,10,10])

# atribuição automatica para o output (força aplicada)
output.automf(names=['NVVB','NVB','NB','N','Z','P','PB','PVB','PVVB'],)

#Visualizando as variáveis
ang.view()
velang.view()
output.view()

#Criando as regras
regra_1 = ctrl.Rule(ang['NLS'] & velang['POS'], output['NB'])
regra_2 = ctrl.Rule(ang['NBS'] & velang['POS'], output['Z'])
regra_3 = ctrl.Rule(ang['SALN'] & velang['POS'], output['N'])
regra_4 = ctrl.Rule(ang['Z'] & velang['ZS'], output['P'])
regra_5 = ctrl.Rule(ang['SALP'] & velang['NEG'], output['P'])
regra_6 = ctrl.Rule(ang['PBS'] & velang['NEG'], output['Z'])
regra_7 = ctrl.Rule(ang['PLS'] & velang['NEG'], output['PB'])

controlador = ctrl.ControlSystem([regra_1,regra_2,regra_3,regra_4,regra_5,regra_6,regra_7])

#Simulando
CalculoOutput = ctrl.ControlSystemSimulation(controlador)

valorAng = float(input('Ângulo: '))
valorVelAng = float(input('Velocidade angular: '))
CalculoOutput.input['angulo'] = valorAng
CalculoOutput.input['velocidade angular'] = valorVelAng
CalculoOutput.compute()

valorOutput = CalculoOutput.output['força aplicada (output)']

print("\nÂngulo %d \nVelocidade angular %d \nOutput (força aplicada) de %5.2f" %(
        valorAng,
        valorVelAng,
        valorOutput))


ang.view(sim=CalculoOutput)
velang.view(sim=CalculoOutput)
output.view(sim=CalculoOutput)

plt.show()