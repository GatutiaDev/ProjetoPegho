from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .forms import formularioCadastro, formularioContato, formularioExperiencia, formularioFormacao, ExperienciaFormSet, FormacaoFormSet
from .models import Pessoa, Contato, Experiencia, Formacao
from django.contrib.auth.mixins import LoginRequiredMixin


def acesso(request):
        return render(request, 'form/acesso.html')


#chama os formularios
def formulario(request):
        form = formularioCadastro()
        formc = formularioContato()
        forme = ExperienciaFormSet(queryset=Experiencia.objects.none())
        formf = FormacaoFormSet(queryset=Formacao.objects.none())
        return render(request, 'form/formulario.html', {'form': form, 'formc': formc, 'forme':forme, 'formf': formf}, )

#salva as informações
def processa_formulario(request):
    if request.method == 'POST':
        form = formularioCadastro(request.POST)
        formc = formularioContato(request.POST)
        forme = ExperienciaFormSet(request.POST)
        formf = FormacaoFormSet(request.POST)

        if form.is_valid() and formc.is_valid() and forme.is_valid() and formf.is_valid():
            contato = formc.save()
            pessoa = form.save(commit=False)
            pessoa.contato = contato
            pessoa.save()

            experiencias = forme.save(commit=False)
            for experiencia in experiencias:
                experiencia.save()
                pessoa.experiencias.add(experiencia)

            formacoes = formf.save(commit=False)
            for formacao in formacoes:
                formacao.save()
                pessoa.formacoes.add(formacao)


            return redirect('envio_formulario', pessoa_id=pessoa.id)
        else:
            return render(request, 'form/formulario.html', {'form': form, 'formc': formc, 'forme':forme, 'formf': formf}, )

    return HttpResponse('Método de requisição inválido')


#direciona para mostrar os dados salvos
def envio_formulario(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    return render(request, 'form/envio.html', {'pessoa': pessoa})


#uma class based view para a lista
class PessoaList(LoginRequiredMixin, ListView):
    model = Pessoa
    queryset = Pessoa.objects.all()

#class based view para mostrar todas as infos do candidato
class PessoaDetail(LoginRequiredMixin, DetailView):
    model = Pessoa
    queryset = Pessoa.objects.all()

#class based view para atualizar as infos
class PessoaUpdate(LoginRequiredMixin, UpdateView):
    model = Pessoa
    fields = '__all__'
    success_url = reverse_lazy('pessoa-lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['forme'] = formularioExperiencia(self.request.POST, instance=self.object.experiencias.first())
            context['formf'] = formularioFormacao(self.request.POST, instance=self.object.formacoes.first())
            context['formc'] = formularioContato(self.request.POST, instance=self.object.contato)
        else:
            context['forme'] = formularioExperiencia(instance=self.object.experiencias.first())
            context['formf'] = formularioFormacao(instance=self.object.formacoes.first())
            context['formc'] = formularioContato(instance=self.object.contato)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        forme = context['forme']
        formf = context['formf']
        formc = context['formc']

        if forme.is_valid() and formf.is_valid() and formc.is_valid():
            form.save()
            formc.save()
            forme.save()
            formf.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

#function based view para deletar as informações pelo id da pessoa
def delete_pessoa(request, pk):
    try:
        pessoa = get_object_or_404(Pessoa, id=pk)
        print(f"Pessoa: {pessoa}")

        experiencia_ids = pessoa.experiencias.values_list('id', flat=True)
        print(f"Experiencia IDs: {experiencia_ids}")

        formacao_ids = pessoa.formacoes.values_list('id', flat=True)
        print(f"Formacao IDs: {formacao_ids}")

        Experiencia.objects.filter(id__in=experiencia_ids).delete()
        Formacao.objects.filter(id__in=formacao_ids).delete()
        pessoa.contato.delete()
        pessoa.delete()
        print(f"Pessoa {pk} deletada com sucesso!")

        return redirect('pessoa-lista')
    except Exception as e:
        print(f"Erro ao deletar: {e}")
        return redirect('pessoa-lista')

#login para entrar na lista e sua funções
def login(request):
    if request.method == "GET":
        return render(request, 'form/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)

            return render(request, 'form/abrirlista.html')
        else:
            return render(request, 'form/login.html')



