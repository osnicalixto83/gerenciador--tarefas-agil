from src.tarefas import criar_tarefa, listar_tarefas

def test_criar_tarefa():
    tarefa = criar_tarefa("Teste", "Alta")
    assert tarefa["titulo"] == "Teste"
    assert tarefa["prioridade"] == "Alta"

def test_listar_tarefas():
    tarefas = listar_tarefas()
    assert len(tarefas) > 0
