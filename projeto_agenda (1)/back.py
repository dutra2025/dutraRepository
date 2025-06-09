import json

ARQUIVO = 'contatos.json'

def carregar():
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar(contatos):
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(contatos, f, indent=4, ensure_ascii=False)

def listar():
    return carregar()

def adicionar(nome, telefone):
    contatos = carregar()
    contatos.append({'nome': nome, 'telefone': telefone})
    salvar(contatos)

def buscar(nome):
    contatos = carregar()
    return [c for c in contatos if nome.lower() in c['nome'].lower()]

def editar(index, nome, telefone):
    contatos = carregar()
    if 0 <= index < len(contatos):
        contatos[index] = {'nome': nome, 'telefone': telefone}
        salvar(contatos)
        return True
    return False

def apagar(index):
    contatos = carregar()
    if 0 <= index < len(contatos):
        contatos.pop(index)
        salvar(contatos)
        return True
    return False
