from ..models import Desbravador


def listar_desbravadores():
    desbravadores =Desbravador.objects.all()
    return desbravadores

def listar_desbravador_id (id):
    desbravador = Desbravador.objects.get(id=id)
    return desbravador

def remover_desbravador(desbravador):
    desbravador.delete()

def cadastrar_desbravador(desbravador):
    Desbravador.objects.create(nome=desbravador.nome, sexo = desbravador.sexo, data_nascimento = desbravador.data_nascimento,
                               email= desbravador.email)

def editar_desbravador(desbravador, desbravador_novo):
    desbravador.nome = desbravador_novo.nome
    desbravador.sexo = desbravador_novo.sexo
    desbravador.data_nascimento = desbravador_novo.data_nascimento
    desbravador.email = desbravador_novo.email
    desbravador.save(force_update=True)
