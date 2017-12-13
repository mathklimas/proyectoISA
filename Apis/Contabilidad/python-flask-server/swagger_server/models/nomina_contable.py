# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class NominaContable(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_nominda_contable: int=None, importe_nomina_contable: int=None, pago_nomina_contable_realizado: bool=None, id_departamento_contable: int=None, id_contable: int=None):
        """
        NominaContable - a model defined in Swagger

        :param id_nominda_contable: The id_nominda_contable of this NominaContable.
        :type id_nominda_contable: int
        :param importe_nomina_contable: The importe_nomina_contable of this NominaContable.
        :type importe_nomina_contable: int
        :param pago_nomina_contable_realizado: The pago_nomina_contable_realizado of this NominaContable.
        :type pago_nomina_contable_realizado: bool
        :param id_departamento_contable: The id_departamento_contable of this NominaContable.
        :type id_departamento_contable: int
        :param id_contable: The id_contable of this NominaContable.
        :type id_contable: int
        """
        self.swagger_types = {
            'id_nominda_contable': int,
            'importe_nomina_contable': int,
            'pago_nomina_contable_realizado': bool,
            'id_departamento_contable': int,
            'id_contable': int
        }

        self.attribute_map = {
            'id_nominda_contable': 'id_nomindaContable',
            'importe_nomina_contable': 'importeNominaContable',
            'pago_nomina_contable_realizado': 'pagoNominaContableRealizado',
            'id_departamento_contable': 'id_departamentoContable',
            'id_contable': 'id_contable'
        }

        self._id_nominda_contable = id_nominda_contable
        self._importe_nomina_contable = importe_nomina_contable
        self._pago_nomina_contable_realizado = pago_nomina_contable_realizado
        self._id_departamento_contable = id_departamento_contable
        self._id_contable = id_contable

    @classmethod
    def from_dict(cls, dikt) -> 'NominaContable':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NominaContable of this NominaContable.
        :rtype: NominaContable
        """
        return deserialize_model(dikt, cls)

    @property
    def id_nominda_contable(self) -> int:
        """
        Gets the id_nominda_contable of this NominaContable.

        :return: The id_nominda_contable of this NominaContable.
        :rtype: int
        """
        return self._id_nominda_contable

    @id_nominda_contable.setter
    def id_nominda_contable(self, id_nominda_contable: int):
        """
        Sets the id_nominda_contable of this NominaContable.

        :param id_nominda_contable: The id_nominda_contable of this NominaContable.
        :type id_nominda_contable: int
        """

        self._id_nominda_contable = id_nominda_contable

    @property
    def importe_nomina_contable(self) -> int:
        """
        Gets the importe_nomina_contable of this NominaContable.

        :return: The importe_nomina_contable of this NominaContable.
        :rtype: int
        """
        return self._importe_nomina_contable

    @importe_nomina_contable.setter
    def importe_nomina_contable(self, importe_nomina_contable: int):
        """
        Sets the importe_nomina_contable of this NominaContable.

        :param importe_nomina_contable: The importe_nomina_contable of this NominaContable.
        :type importe_nomina_contable: int
        """

        self._importe_nomina_contable = importe_nomina_contable

    @property
    def pago_nomina_contable_realizado(self) -> bool:
        """
        Gets the pago_nomina_contable_realizado of this NominaContable.

        :return: The pago_nomina_contable_realizado of this NominaContable.
        :rtype: bool
        """
        return self._pago_nomina_contable_realizado

    @pago_nomina_contable_realizado.setter
    def pago_nomina_contable_realizado(self, pago_nomina_contable_realizado: bool):
        """
        Sets the pago_nomina_contable_realizado of this NominaContable.

        :param pago_nomina_contable_realizado: The pago_nomina_contable_realizado of this NominaContable.
        :type pago_nomina_contable_realizado: bool
        """

        self._pago_nomina_contable_realizado = pago_nomina_contable_realizado

    @property
    def id_departamento_contable(self) -> int:
        """
        Gets the id_departamento_contable of this NominaContable.

        :return: The id_departamento_contable of this NominaContable.
        :rtype: int
        """
        return self._id_departamento_contable

    @id_departamento_contable.setter
    def id_departamento_contable(self, id_departamento_contable: int):
        """
        Sets the id_departamento_contable of this NominaContable.

        :param id_departamento_contable: The id_departamento_contable of this NominaContable.
        :type id_departamento_contable: int
        """

        self._id_departamento_contable = id_departamento_contable

    @property
    def id_contable(self) -> int:
        """
        Gets the id_contable of this NominaContable.

        :return: The id_contable of this NominaContable.
        :rtype: int
        """
        return self._id_contable

    @id_contable.setter
    def id_contable(self, id_contable: int):
        """
        Sets the id_contable of this NominaContable.

        :param id_contable: The id_contable of this NominaContable.
        :type id_contable: int
        """

        self._id_contable = id_contable

