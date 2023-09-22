from django.db import models
from produto.models import Produto

class Estoque(models.Model):
	id = models.AutoField(db_column='id',
						primary_key=True)

	id_produto = models.ForeignKey(Produto,
								db_column='id_produto',
								related_name='estoque',
								null=False,
								blank=False,
								on_delete=models.PROTECT)

	quantidade = models.IntegerField(db_column='quantidade',
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
		db_table = 'estoque'

		indexes = [
			models.Index(
				name='fields_estoque_idx',
				fields=['id', 'id_produto']
				)
		]

	def __str__(self):
		return '%s - %s - %s' % (self.id, self.id_produto, self.quantidade)
