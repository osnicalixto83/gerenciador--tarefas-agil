tarefas = []

def criar_tarefa(titulo, prioridade):
    tarefa = {
        "titulo": titulo,
        "prioridade": prioridade,
        "status": "A Fazer"
    }
    tarefas.append(tarefa)
    return tarefa

def listar_tarefas():
    return tarefas

def atualizar_status(titulo, novo_status):
    for tarefa in tarefas:
        if tarefa["titulo"] == titulo:
            tarefa["status"] = novo_status
            return True
    return False

def remover_tarefa(titulo):
    global tarefas
    tarefas = [t for t in tarefas if t["titulo"] != titulo]
