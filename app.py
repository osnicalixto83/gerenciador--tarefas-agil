from tarefas import criar_tarefa, listar_tarefas

criar_tarefa("Analisar requisitos", "Alta")
criar_tarefa("Criar Kanban", "Média")

for tarefa in listar_tarefas():
    print(tarefa)
