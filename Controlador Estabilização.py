import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

#Variaveis de Entrada do ângulo do pendulo e velocidade angular do pendulo (Antecedent)
ang = ctrl.Antecedent(np.arange(-30, 30, 1), 'angulo')
velang = ctrl.Antecedent(np.arange(-6, 6, 1), 'velocidade angular')

#Variaveis de Entrada da posicao do carrinho e da velocidade do carrinho (Antecedent)
xcar = ctrl.Antecedent(np.arange(-0.4, 0.4, 0.1), 'posicao carrinho')
velcar = ctrl.Antecedent(np.arange(-1, 1, 0.1), 'velocidade carrinho')

#Variaveis de saída (Consequent)
output = ctrl.Consequent(np.arange(-6, 6, 1), 'output')
outputcar = ctrl.Consequent(np.arange(-6, 6, 1), 'outputcar')

#atribuicao manual para o angulo do pendulo
ang['NVB'] = fuzz.trapmf(ang.universe, [-30,-30,-18,-12])
ang['NB'] = fuzz.trimf(ang.universe, [-16.5,-10.5,-4.5])
ang['N'] = fuzz.trimf(ang.universe, [-9,-4.5,0])
ang['ZO'] = fuzz.trimf(ang.universe, [-3,0,3])
ang['P'] = fuzz.trimf(ang.universe, [0,4.5,9])
ang['PB'] = fuzz.trimf(ang.universe, [4,10.5,16.5])
ang['PVB'] = fuzz.trapmf(ang.universe, [12,18,30,30])

# atribuicao manual para o velocidade angular do pendulo
velang['NB'] = fuzz.trapmf(velang.universe, [-6,-6,-4,-2])
velang['N'] = fuzz.trimf(velang.universe, [-4,-2,0])
velang['ZO'] = fuzz.trimf(velang.universe, [-2,0,2])
velang['P'] = fuzz.trimf(velang.universe, [0,2,4])
velang['PB'] = fuzz.trapmf(velang.universe, [2,4,6,6])

#atribuicao manual para a posicao do carrinho
xcar['NBIG'] = fuzz.trapmf(xcar.universe, [-0.4,-0.4,-0.3,-0.15])
xcar['NEG'] = fuzz.trimf(xcar.universe, [-0.3,-0.15,0])
xcar['Z'] = fuzz.trimf(xcar.universe, [-0.15,0,0.15])
xcar['POS'] = fuzz.trimf(xcar.universe, [0,0.15,0.3])
xcar['PBIG'] = fuzz.trapmf(xcar.universe, [0.15,0.3,0.4,0.4])

#atribuicao manual para a velocidade do carrinho
velcar['NEG'] = fuzz.trapmf(velcar.universe, [-1,-1,-0.1,0])
velcar['Z'] = fuzz.trimf(velcar.universe, [-0.1,0,0.1])
velcar['POS'] = fuzz.trapmf(velcar.universe, [0,0.1,1,1])

# atribuição automatica para o output (força aplicada)
output.automf(names=['NVVB','NVB','NB','N','Z','P','PB','PVB','PVVB'],)
outputcar.automf(names=['NVVB','NVB','NB','N','Z','P','PB','PVB','PVVB'],)

#Visualizando as variáveis
ang.view()
velang.view()
output.view()
xcar.view()
velcar.view()
outputcar.view()

#Criando as regras do pendulo
regra_1 = ctrl.Rule(ang['NVB'] & velang['NB'], output['NVVB'])
regra_2 = ctrl.Rule(ang['NVB'] & velang['N'], output['NVVB'])
regra_3 = ctrl.Rule(ang['NVB'] & velang['ZO'], output['NVB'])
regra_4 = ctrl.Rule(ang['NVB'] & velang['P'], output['NB'])
regra_5 = ctrl.Rule(ang['NVB'] & velang['PB'], output['N'])

regra_6 = ctrl.Rule(ang['NB'] & velang['NB'], output['NVVB'])
regra_7 = ctrl.Rule(ang['NB'] & velang['N'], output['NVB'])
regra_8 = ctrl.Rule(ang['NB'] & velang['ZO'], output['NB'])
regra_9 = ctrl.Rule(ang['NB'] & velang['P'], output['N'])
regra_10 = ctrl.Rule(ang['NB'] & velang['PB'], output['Z'])

regra_11 = ctrl.Rule(ang['N'] & velang['NB'], output['NVB'])
regra_12 = ctrl.Rule(ang['N'] & velang['N'], output['NB'])
regra_13 = ctrl.Rule(ang['N'] & velang['ZO'], output['N'])
regra_14 = ctrl.Rule(ang['N'] & velang['P'], output['Z'])
regra_15 = ctrl.Rule(ang['N'] & velang['PB'], output['P'])

regra_16 = ctrl.Rule(ang['ZO'] & velang['NB'], output['NB'])
regra_17 = ctrl.Rule(ang['ZO'] & velang['N'], output['N'])
regra_18 = ctrl.Rule(ang['ZO'] & velang['ZO'], output['Z'])
regra_19 = ctrl.Rule(ang['ZO'] & velang['P'], output['P'])
regra_20 = ctrl.Rule(ang['ZO'] & velang['PB'], output['PB'])

regra_21 = ctrl.Rule(ang['P'] & velang['NB'], output['N'])
regra_22 = ctrl.Rule(ang['P'] & velang['N'], output['Z'])
regra_23 = ctrl.Rule(ang['P'] & velang['ZO'], output['P'])
regra_24 = ctrl.Rule(ang['P'] & velang['P'], output['PB'])
regra_25 = ctrl.Rule(ang['P'] & velang['PB'], output['PVB'])

regra_26 = ctrl.Rule(ang['PB'] & velang['NB'], output['Z'])
regra_27 = ctrl.Rule(ang['PB'] & velang['N'], output['P'])
regra_28 = ctrl.Rule(ang['PB'] & velang['ZO'], output['PB'])
regra_29 = ctrl.Rule(ang['PB'] & velang['P'], output['PVB'])
regra_30 = ctrl.Rule(ang['PB'] & velang['PB'], output['PVVB'])

regra_31 = ctrl.Rule(ang['PVB'] & velang['NB'], output['P'])
regra_32 = ctrl.Rule(ang['PVB'] & velang['N'], output['PB'])
regra_33 = ctrl.Rule(ang['PVB'] & velang['ZO'], output['PVB'])
regra_34 = ctrl.Rule(ang['PVB'] & velang['P'], output['PVVB'])
regra_35 = ctrl.Rule(ang['PVB'] & velang['PB'], output['PVVB'])

controlador = ctrl.ControlSystem([regra_1,regra_2,regra_3,regra_4,regra_5,regra_6,regra_7,regra_8,regra_9,regra_10,
                                 regra_11,regra_12,regra_13,regra_14,regra_15,regra_16,regra_17,regra_18,regra_19,
                                 regra_20,regra_21,regra_22,regra_23,regra_24,regra_25,regra_26,regra_27,regra_28,
                                 regra_29,regra_30,regra_31,regra_32,regra_33,regra_34,regra_35])

#Criando as regras do carrinho
regracar_1 = ctrl.Rule(xcar['NBIG'] & velcar['NEG'], outputcar['PVVB'])
regracar_2 = ctrl.Rule(xcar['NEG'] & velcar['NEG'], outputcar['PVB'])
regracar_3 = ctrl.Rule(xcar['Z'] & velcar['NEG'], outputcar['PB'])
regracar_4 = ctrl.Rule(xcar['Z'] & velcar['Z'], outputcar['Z'])
regracar_5 = ctrl.Rule(xcar['Z'] & velcar['POS'], outputcar['NB'])
regracar_6 = ctrl.Rule(xcar['POS'] & velcar['POS'], outputcar['NVB'])
regracar_7 = ctrl.Rule(xcar['PBIG'] & velcar['POS'], outputcar['NVVB'])

controladorcar = ctrl.ControlSystem([regracar_1,regracar_2,regracar_3,regracar_4,regracar_5,regracar_6,regracar_7])

#Simulando
CalculoOutput = ctrl.ControlSystemSimulation(controlador)
CalculoOutputcar = ctrl.ControlSystemSimulation(controladorcar)

valorAng = float(input('Ângulo (θ): '))
valorVelAng = float(input('Velocidade angular (θ*): '))
CalculoOutput.input['angulo'] = valorAng
CalculoOutput.input['velocidade angular'] = valorVelAng
CalculoOutput.compute()

valorOutput = CalculoOutput.output['output']

valorXcar = float(input('Posicao carrinho (ex): '))
valorVelCar = float(input('Velocidade do carrinho (ex*): '))
CalculoOutputcar.input['posicao carrinho'] = valorXcar
CalculoOutputcar.input['velocidade carrinho'] = valorVelCar
CalculoOutputcar.compute()

valorOutputcar = CalculoOutputcar.output['outputcar']

print("\nÂngulo %f \nVelocidade angular %f \nOutput (força aplicada) de %5.2f" %(
        valorAng,
        valorVelAng,
        valorOutput))


ang.view(sim=CalculoOutput)
velang.view(sim=CalculoOutput)
output.view(sim=CalculoOutput)

plt.show()


print("\nPosição do carrinho %f \nVelocidade do carrinho %f \nOutput (força aplicada) de %5.2f" %(
        valorXcar,
        valorVelCar,
        valorOutputcar))


xcar.view(sim=CalculoOutputcar)
velcar.view(sim=CalculoOutputcar)
outputcar.view(sim=CalculoOutputcar)

plt.show()
