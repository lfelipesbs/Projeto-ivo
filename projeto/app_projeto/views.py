from django.shortcuts import render, redirect
from .models import feedback, atividade
from django.conf import settings

def enviar_feedback(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        turma = request.POST.get('turma')
        feedback1 = request.POST.get('feedback') 

        novo_feedback = feedback(nome=nome, turma=turma, feedbacks=feedback1)
        novo_feedback.save()
        return redirect("obrigado")

    return render(request, '1.html')

def obrigado(request):
    return render(request, '2.html')

def pagina_atividades(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        turma = request.POST.get('turma')
        descricao = request.POST.get('descricao')

        nova_descricao = atividade(nome=nome, turma=turma, descricao=descricao)
        nova_descricao.save()
        return render(request, '4.html')  # Alteração aqui

    return render(request, '3.html')

def envio(request):
    return render(request, '4.html')

def home(request):
    return render(request, 'home.html')
