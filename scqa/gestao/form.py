from gestao.models import RegistroEntrada, RegistroEntradaExame, RegistroEntradaAmostra
from home.form import ScqaModelForm, exclude_softdelete_fields


class RegistroEntradaForm(ScqaModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['id_interna'].size = 4
        # self.fields['id_interna'].widget.attrs['data-mask'] = "0000/00"
        self.fields['id_interna'].widget.attrs['placeholder'] = '0000/00'

        self.fields['id_externa'].size = 4
        self.fields['data_entrada'].size = 4
        self.fields['ceua'].size = 4

    class Meta:
        model = RegistroEntrada
        exclude = exclude_softdelete_fields


class RegistroEntradaExameForm(ScqaModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['registro_entrada_pk'].widget.input_type = "hidden"

        self.fields['exame_hematologia'].size = 3
        self.fields['exame_bioquimica'].size = 3
        self.fields['exame_parasitologia'].size = 3
        self.fields['exame_imunologia'].size = 3
        self.fields['exame_bacteriologia'].size = 3
        self.fields['exame_anatomopatologia'].size = 3
        self.fields['exame_monitoramento_sanitario'].size = 3
        self.fields['exame_monitoramento_sanitario'].size = 3
        self.fields['exame_monitoramento_genetico'].size = 3
        self.fields['exame_outro'].size = 6

    class Meta:
        model = RegistroEntradaExame
        exclude = exclude_softdelete_fields


class RegistroEntradaAmostraForm(ScqaModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['registro_entrada_pk'].widget.input_type = "hidden"

        self.fields['amostra_animal'].size = 3
        self.fields['amostra_cauda'].size = 3
        self.fields['amostra_sangue'].size = 3
        self.fields['amostra_soro'].size = 3
        self.fields['amostra_fezes'].size = 3
        self.fields['amostra_outro'].size = 6

    class Meta:
        model = RegistroEntradaAmostra
        exclude = exclude_softdelete_fields
