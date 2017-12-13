# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Profesores(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_nominda_profesor: int=None, importe_nomina_profesor: int=None, pago_nomina_profesor_realizado: bool=None, id_departamento_contable: int=None, id_profesor: int=None):
        """
        Profesores - a model defined in Swagger

        :param id_nominda_profesor: The id_nominda_profesor of this Profesores.
        :type id_nominda_profesor: int
        :param importe_nomina_profesor: The importe_nomina_profesor of this Profesores.
        :type importe_nomina_profesor: int
        :param pago_nomina_profesor_realizado: The pago_nomina_profesor_realizado of this Profesores.
        :type pago_nomina_profesor_realizado: bool
        :param id_departamento_contable: The id_departamento_contable of this Profesores.
        :type id_departamento_contable: int
        :param id_profesor: The id_profesor of this Profesores.
        :type id_profesor: int
        """
        self.swagger_types = {
            'id_nominda_profesor': int,
            'importe_nomina_profesor': int,
            'pago_nomina_profesor_realizado': bool,
            'id_departamento_contable': int,
            'id_profesor': int
        }

        self.attribute_map = {
            'id_nominda_profesor': 'id_nomindaProfesor',
            'importe_nomina_profesor': 'importeNominaProfesor',
            'pago_nomina_profesor_realizado': 'pagoNominaProfesorRealizado',
            'id_departamento_contable': 'id_departamentoContable',
            'id_profesor': 'id_profesor'
        }

        self._id_nominda_profesor = id_nominda_profesor
        self._importe_nomina_profesor = importe_nomina_profesor
        self._pago_nomina_profesor_realizado = pago_nomina_profesor_realizado
        self._id_departamento_contable = id_departamento_contable
        self._id_profesor = id_profesor

    @classmethod
    def from_dict(cls, dikt) -> 'Profesores':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Profesores of this Profesores.
        :rtype: Profesores
        """
        return deserialize_model(dikt, cls)

    @property
    def id_nominda_profesor(self) -> int:
        """
        Gets the id_nominda_profesor of this Profesores.

        :return: The id_nominda_profesor of this Profesores.
        :rtype: int
        """
        return self._id_nominda_profesor

    @id_nominda_profesor.setter
    def id_nominda_profesor(self, id_nominda_profesor: int):
        """
        Sets the id_nominda_profesor of this Profesores.

        :param id_nominda_profesor: The id_nominda_profesor of this Profesores.
        :type id_nominda_profesor: int
        """

        self._id_nominda_profesor = id_nominda_profesor

    @property
    def importe_nomina_profesor(self) -> int:
        """
        Gets the importe_nomina_profesor of this Profesores.

        :return: The importe_nomina_profesor of this Profesores.
        :rtype: int
        """
        return self._importe_nomina_profesor

    @importe_nomina_profesor.setter
    def importe_nomina_profesor(self, importe_nomina_profesor: int):
        """
        Sets the importe_nomina_profesor of this Profesores.

        :param importe_nomina_profesor: The importe_nomina_profesor of this Profesores.
        :type importe_nomina_profesor: int
        """

        self._importe_nomina_profesor = importe_nomina_profesor

    @property
    def pago_nomina_profesor_realizado(self) -> bool:
        """
        Gets the pago_nomina_profesor_realizado of this Profesores.

        :return: The pago_nomina_profesor_realizado of this Profesores.
        :rtype: bool
        """
        return self._pago_nomina_profesor_realizado

    @pago_nomina_profesor_realizado.setter
    def pago_nomina_profesor_realizado(self, pago_nomina_profesor_realizado: bool):
        """
        Sets the pago_nomina_profesor_realizado of this Profesores.

        :param pago_nomina_profesor_realizado: The pago_nomina_profesor_realizado of this Profesores.
        :type pago_nomina_profesor_realizado: bool
        """

        self._pago_nomina_profesor_realizado = pago_nomina_profesor_realizado

    @property
    def id_departamento_contable(self) -> int:
        """
        Gets the id_departamento_contable of this Profesores.

        :return: The id_departamento_contable of this Profesores.
        :rtype: int
        """
        return self._id_departamento_contable

    @id_departamento_contable.setter
    def id_departamento_contable(self, id_departamento_contable: int):
        """
        Sets the id_departamento_contable of this Profesores.

        :param id_departamento_contable: The id_departamento_contable of this Profesores.
        :type id_departamento_contable: int
        """

        self._id_departamento_contable = id_departamento_contable

    @property
    def id_profesor(self) -> int:
        """
        Gets the id_profesor of this Profesores.

        :return: The id_profesor of this Profesores.
        :rtype: int
        """
        return self._id_profesor

    @id_profesor.setter
    def id_profesor(self, id_profesor: int):
        """
        Sets the id_profesor of this Profesores.

        :param id_profesor: The id_profesor of this Profesores.
        :type id_profesor: int
        """

        self._id_profesor = id_profesor

