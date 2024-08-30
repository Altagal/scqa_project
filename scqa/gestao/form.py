from gestao.models import RegistroEntrada, EntradaAmostra
from home.form import ScqaModelForm, exclude_softdelete_fields


class RegistroEntradaForm(ScqaModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['id_interna'].size = 4
        self.fields['id_interna'].widget.attrs['data-mask'] = "0000/00"
        self.fields['id_interna'].widget.attrs['placeholder'] = '0000/00'

        self.fields['id_externa'].size = 4
        self.fields['data_entrada'].size = 4
        self.fields['ceua'].size = 4

    class Meta:
        model = RegistroEntrada
        exclude = exclude_softdelete_fields


class EntradaAmostraForm(ScqaModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['registro_entrada_pk'].widget.input_type = "hidden"

        self.fields['tipo_amostra'].mini = True
        self.fields['nao_conformidade'].mini = True

    class Meta:
        model = EntradaAmostra
        exclude = exclude_softdelete_fields