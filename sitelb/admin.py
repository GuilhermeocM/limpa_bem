from django.contrib import admin
from atendimento.models import Atendimento
from cliente.models import Cliente
from funcionario.models import Funcionario
from servico.models import Servico


class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'atendente', 'cliente', 'data_hora_agendamento', 'situacao')
    list_editable= ('situacao',)



admin.site.register(Atendimento, AtendimentoAdmin)
admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Servico)
