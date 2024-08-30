from django.db import models

from home.models import ScqaModel


class RegistroEntrada(ScqaModel):
    id_interna = models.CharField(max_length=7, unique=True, verbose_name="Identificação Interna (IDI)")
    id_externa = models.CharField(max_length=10, blank=True, null=True, verbose_name="Identificação Externa (IDE)")
    data_entrada = models.DateField(verbose_name="Data de Entrada")
    ceua = models.CharField(max_length=10, blank=True, null=True, verbose_name="CEUA")

    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")

    def __str__(self):
        return self.id_interna


class EntradaAmostra(ScqaModel):
    registro_entrada_pk = models.ForeignKey("RegistroEntrada", on_delete=models.PROTECT)
    tipo_amostra_choices = [

        (1, "Animal"),
        (2, "Cauda"),
        (3, "Sangue"),
        (4, "Soro"),
        (5, "Fezes"),

        (6, "Água"),
        (7, "Amostra Controle"),
        (8, "DNA Bacteriano"),
        (9, "DNA para Extração"),
        (10, "Intestino"),
        (11, "Lâmina com Fita Gomada"),
        (12, "Lavado Gástrico"),
        (13, "Lavado Retal"),
        (14, "Lavado Subcutâneo"),
        (15, "Lavado Traqueal"),
        (16, "Líquido"),
        (17, "Pelo"),
        (18, "Placenta"),
        (19, "Plasma"),
        (20, "Saneante"),
        (21, "Secreção"),
        (22, "Swab Ambiental"),
        (23, "Swab Cutâneo"),
        (24, "Swab Nasal"),
        (25, "Swab Orofaríngeo"),
        (26, "Swab Retal"),
        (27, "Swab Traqueal"),
        (28, "Swab Vaginal"),
        (29, "Tecido (Cauda)"),
        (30, "Tecido (Orelha)"),
        (31, "Tecido (Pele)"),
        (32, "Tecido (Traqueia)"),
        (33, "Traqueia"),
        (34, "Validação Interna"),
        (0, "Outro"),

    ]
    tipo_amostra = models.IntegerField(choices=tipo_amostra_choices, verbose_name="Tipo de Amostra")
    nao_conformidade = models.BooleanField(default=False, verbose_name="Não conforme")
