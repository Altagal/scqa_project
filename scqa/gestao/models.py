from django.db import models

from home.models import ScqaModel


class RegistroEntrada(ScqaModel):
    id_interna = models.CharField(max_length=7, unique=True, verbose_name="Identificação Interna (IDI)")
    id_externa = models.CharField(max_length=10, blank=True, null=True, verbose_name="Identificação Externa (IDE)")
    data_entrada = models.DateField(verbose_name="Data de Entrada")
    ceua = models.CharField(max_length=10, blank=True, null=True, verbose_name="CEUA")

    # responavel = models.CharField(max_length=10, blank=True, null=True, verbose_name="Identificação Externa (IDE)")
    # requisitante = models.CharField(max_length=10, blank=True, null=True, verbose_name="Identificação Externa (IDE)")

    def __str__(self):
        return self.id_interna


class RegistroEntradaExame(ScqaModel):
    registro_entrada_pk = models.ForeignKey("RegistroEntrada", blank=True, on_delete=models.CASCADE)

    exame_hematologia = models.BooleanField(default=False, verbose_name="Hematologia")
    exame_bioquimica = models.BooleanField(default=False, verbose_name="Bioquímica")
    exame_parasitologia = models.BooleanField(default=False, verbose_name="Parasitologia")
    exame_imunologia = models.BooleanField(default=False, verbose_name="Imunologia")
    exame_bacteriologia = models.BooleanField(default=False, verbose_name="Bacteriologia")
    exame_anatomopatologia = models.BooleanField(default=False, verbose_name="Anatomopatologia")
    exame_monitoramento_sanitario = models.BooleanField(default=False, verbose_name="Monitoramento Sanitário")
    exame_monitoramento_genetico = models.BooleanField(default=False, verbose_name="Monitoramento Genético")
    exame_outro = models.CharField(max_length=200, blank=True, null=True, verbose_name="Outros")
    exame_observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")


class RegistroEntradaAmostra(ScqaModel):
    registro_entrada_pk = models.ForeignKey("RegistroEntrada", blank=True, on_delete=models.CASCADE)

    amostra_status = [
        (1, "Entregue"),
        (2, "Não conforme")
    ]
    amostra_animal = models.IntegerField(blank=True, null=True, choices=amostra_status, verbose_name="Animal")
    amostra_cauda = models.IntegerField(blank=True, null=True, choices=amostra_status, verbose_name="Cauda")
    amostra_sangue = models.IntegerField(blank=True, null=True, choices=amostra_status, verbose_name="Sangue")
    amostra_soro = models.IntegerField(blank=True, null=True, choices=amostra_status, verbose_name="Soro")
    amostra_fezes = models.IntegerField(blank=True, null=True, choices=amostra_status, verbose_name="Fezes")
    amostra_outro = models.CharField(max_length=200, blank=True, null=True, verbose_name="Outros")

    amostra_observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")

# ------------
#         (1, "Animal"),
#         (2, "Cauda"),
#         (3, "Sangue"),
#         (4, "Soro"),
#         (5, "Fezes"),
#
#         # Lista com amostras diversas
#         (6, "Água"),
#         (7, "Amostra Controle"),
#         (8, "DNA Bacteriano"),
#         (9, "DNA para Extração"),
#         (10, "Intestino"),
#         (11, "Lâmina com Fita Gomada"),
#         (12, "Lavado Gástrico"),
#         (13, "Lavado Retal"),
#         (14, "Lavado Subcutâneo"),
#         (15, "Lavado Traqueal"),
#         (16, "Líquido"),
#         (17, "Pelo"),
#         (18, "Placenta"),
#         (19, "Plasma"),
#         (20, "Saneante"),
#         (21, "Secreção"),
#         (22, "Swab Ambiental"),
#         (23, "Swab Cutâneo"),
#         (24, "Swab Nasal"),
#         (25, "Swab Orofaríngeo"),
#         (26, "Swab Retal"),
#         (27, "Swab Traqueal"),
#         (28, "Swab Vaginal"),
#         (29, "Tecido (Cauda)"),
#         (30, "Tecido (Orelha)"),
#         (31, "Tecido (Pele)"),
#         (32, "Tecido (Traqueia)"),
#         (33, "Traqueia"),
#         (34, "Validação Interna"),
#
#         # Outros
#         (0, "Outro"),
#
# ----------------
#         (1, "Hematologia"),
#         (2, "Bioquimica"),
#         (3, "Parasitologia"),
#         (4, "Imunologia"),
#         (5, "Bacteriologia"),
#         (6, "Anatomopatologia"),
#         (7, "Monitoramento Sanitário"),
#         (8, "Monitoramento Genético"),
