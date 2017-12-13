# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.pago import Pago
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class ResumenPagos(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, importe_total_matricula: int=None, array_pagos: List[Pago]=None):
        """
        ResumenPagos - a model defined in Swagger

        :param importe_total_matricula: The importe_total_matricula of this ResumenPagos.
        :type importe_total_matricula: int
        :param array_pagos: The array_pagos of this ResumenPagos.
        :type array_pagos: List[Pago]
        """
        self.swagger_types = {
            'importe_total_matricula': int,
            'array_pagos': List[Pago]
        }

        self.attribute_map = {
            'importe_total_matricula': 'importe_total_matricula',
            'array_pagos': 'array_pagos'
        }

        self._importe_total_matricula = importe_total_matricula
        self._array_pagos = array_pagos

    @classmethod
    def from_dict(cls, dikt) -> 'ResumenPagos':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Resumen_Pagos of this ResumenPagos.
        :rtype: ResumenPagos
        """
        return deserialize_model(dikt, cls)

    @property
    def importe_total_matricula(self) -> int:
        """
        Gets the importe_total_matricula of this ResumenPagos.

        :return: The importe_total_matricula of this ResumenPagos.
        :rtype: int
        """
        return self._importe_total_matricula

    @importe_total_matricula.setter
    def importe_total_matricula(self, importe_total_matricula: int):
        """
        Sets the importe_total_matricula of this ResumenPagos.

        :param importe_total_matricula: The importe_total_matricula of this ResumenPagos.
        :type importe_total_matricula: int
        """

        self._importe_total_matricula = importe_total_matricula

    @property
    def array_pagos(self) -> List[Pago]:
        """
        Gets the array_pagos of this ResumenPagos.

        :return: The array_pagos of this ResumenPagos.
        :rtype: List[Pago]
        """
        return self._array_pagos

    @array_pagos.setter
    def array_pagos(self, array_pagos: List[Pago]):
        """
        Sets the array_pagos of this ResumenPagos.

        :param array_pagos: The array_pagos of this ResumenPagos.
        :type array_pagos: List[Pago]
        """

        self._array_pagos = array_pagos

