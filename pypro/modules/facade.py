from typing import List

from pypro.modules.models import Modulo


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados por tiulos
    :return:
    """

    return list(Modulo.objects.order_by('order').all())
