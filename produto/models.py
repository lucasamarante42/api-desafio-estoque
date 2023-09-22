from django.db import models
from estoque_geral.utils import show_message_to_unique_error

class Produto(models.Model):
	id = models.AutoField(db_column='id',
						primary_key=True)

	codigo = models.CharField(db_column='codigo',
								max_length=30,
								unique=True,
								null=False,
								blank=False,
								error_messages=show_message_to_unique_error('codigo'))

	descricao = models.CharField(db_column='descricao',
								max_length=200,
								unique=True,
								null=False,
								blank=False,
								error_messages=show_message_to_unique_error('descricao'))

	ativo = models.BooleanField(db_column='ativo',
								null=False,
								blank=False)

	dt_criacao = models.DateField(db_column='dt_criacao',
								null=True,
								blank=True,
								auto_now=False,
								auto_now_add=True)

	dt_atualizacao = models.DateField(db_column='dt_atualizacao',
								null=True,
								blank=True,
								auto_now=True,
								auto_now_add=False)

	class Meta:
		db_table = 'produto'

		indexes = [
			models.Index(
				name='fields_produto_idx',
				fields=['id', 'codigo']
				)
		]

	def __str__(self):
		return '%s - %s - %s' % (self.id, self.codigo, self.descricao)
