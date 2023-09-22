from django.db import models
from produto.models import Produto

class MovimentoProduto(models.Model):
	id = models.AutoField(db_column='id',
						primary_key=True)

	id_produto = models.ForeignKey(Produto,
								db_column='id_produto',
								related_name='movimento_produto',
								null=False,
								blank=False,
								on_delete=models.PROTECT)

	quantidade_entrada = models.IntegerField(db_column='quantidade_entrada',
								null=True,
								blank=True)

	quantidade_saida = models.IntegerField(db_column='quantidade_saida',
								null=True,
								blank=True)

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
		db_table = 'movimento_produto'

		indexes = [
			models.Index(
				name='fields_movimento_produto_idx',
				fields=['id', 'id_produto']
				)
		]

	def __str__(self):
		return '%s - %s - %s' % (self.id_produto, self.quantidade_entrada, self.quantidade_saida)
