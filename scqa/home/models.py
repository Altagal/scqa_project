import re

from django.contrib import messages
from django.db import models, IntegrityError
from django.utils import timezone
from django.db.models import ProtectedError
from django_softdelete.models import SoftDeleteModel

from datetime import datetime


class ScqaModel(SoftDeleteModel):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(blank=True, default=timezone.now)
    modified_at = models.DateTimeField(blank=True)

    # modified_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,
    #                                 blank=True)

    def scqa_save_no_message(self, request):
        try:
            self.modified_by = request.user
            self.modified_at = datetime.now()
            obj = super().save()

            # retorna o objeto que foi salvo
            return obj

        except IntegrityError:
            messages.warning(request, "Este registro já existe.")

        except Exception as e:
            print(e)
            messages.warning(request, "Error na criação.")

    def scqa_save(self, request):
        try:
            self.modified_by = request.user
            self.modified_at = datetime.now()
            obj = super().save()
            messages.success(request, "Cadastrado com sucesso.")

            # retorna o objeto que foi salvo
            return obj

        except IntegrityError:
            messages.warning(request, "Este registro já existe.")

        except Exception as e:
            print(e)
            messages.warning(request, "Error na criação.")

    def scqa_update(self, request):
        try:
            self.modified_by = request.user
            self.modified_at = datetime.now()
            super().save()
            messages.success(request, "Alterado com sucesso.")

        except IntegrityError:
            messages.warning(request, "Este registro já existe.")

        except Exception as e:
            print(e)
            messages.warning(request, "Error na alteração.")

    def scqa_delete(self, request):
        try:
            self.modified_by = request.user
            self.modified_at = datetime.now()
            super().save()
            super().delete()
            messages.success(request, "Excluido com sucesso.")
            return True

        except ProtectedError:
            messages.warning(request, "Este registro ainda está sendo usado em outro lugar.")

        except Exception as e:
            messages.warning(request, "Error ao excluir.")
            print(e)

    @property
    def model_name(self):
        name = self.__class__.__name__
        return str(re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower())
