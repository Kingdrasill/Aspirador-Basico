# Método para o agente reagir a situação da localização
def REFLEX_VACCUM_AGENT(location,status):
    if status == 'Dirty': return 'Suck'
    elif location == 'A': return 'Right'
    elif location == 'B': return 'Left'

# Método para fazer a ação do agente
def ACTION_VACCUM_AGENT(action, agent, environment):
    # Se ação for 'Suck' limpa a localização e recebe 10
    if action == 'Suck': 
        environment.update({agent['Location']: 'Clean'})
        return 10
    # Se ação for 'Right' se move para B e recebe -1
    elif action == 'Right': 
        agent.update({'Location': 'B'})
        return -1
    # Se ação for 'Left' se move para A e recebe -1
    elif action == 'Left': 
        agent.update({'Location': 'A'})
        return -1

# Valores para guardar a média e a quantidade de situações
average = 0
count = 0

# Loop para passar por todo as situações possíveis
for A in ['Dirty', 'Clean']:
    for B in ['Dirty', 'Clean']:
        for Start in ['A', 'B']:
            # Pontuação da situação atual
            score = 0
            # Ambiente inicial
            environment = {'A': A, 'B': B}
            # Agente
            agent = {'Location': Start}

            # Período de tempo de 10 períodos de tempo
            for i in range(1,11):
                # Percebe o status da localização atual do agente
                action = REFLEX_VACCUM_AGENT(agent['Location'], environment[agent['Location']])
                # Faz a ação que o agente deve fazer
                score += ACTION_VACCUM_AGENT(action, agent, environment)

            # Printa a pontuação da situação
            average += score
            count += 1
            print(f'Pontuacao Situacao {count}: {score}')

# Printa a média das pontuações das situações
average /= count
print(f'Pontuacao Media: {average}')