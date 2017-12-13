# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class DepartamentoContable(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_departamento_contable: int=None, nombre_departamento_contable: str=None, descripcion_departamento_contable: str=None, id_facultad: int=None):
        """
        DepartamentoContable - a model defined in Swagger

        :param id_departamento_contable: The id_departamento_contable of this DepartamentoContable.
        :type id_departamento_contable: int
        :param nombre_departamento_contable: The nombre_departamento_contable of this DepartamentoContable.
        :type nombre_departamento_contable: str
        :param descripcion_departamento_contable: The descripcion_departamento_contable of this DepartamentoContable.
        :type descripcion_departamento_contable: str
        :param id_facultad: The id_facultad of this DepartamentoContable.
        :type id_facultad: int
        """
        self.swagger_types = {
            'id_departamento_contable': int,
            'nombre_departamento_contable': str,
            'descripcion_departamento_contable': str,
            'id_facultad': int
        }

        self.attribute_map = {
            'id_departamento_contable': 'id_departamentoContable',
            'nombre_departamento_contable': 'nombreDepartamentoContable',
            'descripcion_departamento_contable': 'descripcionDepartamentoContable',
            'id_facultad': 'id_facultad'
        }

        self._id_departamento_contable = id_departamento_contable
        self._nombre_departamento_contable = nombre_departamento_contable
        self._descripcion_departamento_contable = descripcion_departamento_contable
        self._id_facultad = id_facultad

    @classmethod
    def from_dict(cls, dikt) -> 'DepartamentoContable':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DepartamentoContable of this DepartamentoContable.
        :rtype: DepartamentoContable
        """
        return deserialize_model(dikt, cls)

    @property
    def id_departamento_contable(self) -> int:
        """
        Gets the id_departamento_contable of this DepartamentoContable.

        :return: The id_departamento_contable of this DepartamentoContable.
        :rtype: int
        """
        return self._id_departamento_contable

    @id_departamento_contable.setter
    def id_departamento_contable(self, id_departamento_contable: int):
        """
        Sets the id_departamento_contable of this DepartamentoContable.

        :param id_departamento_contable: The id_departamento_contable of this DepartamentoContable.
        :type id_departamento_contable: int
        """

        self._id_departamento_contable = id_departamento_contable

    @property
    def nombre_departamento_contable(self) -> str:
        """
        Gets the nombre_departamento_contable of this DepartamentoContable.

        :return: The nombre_departamento_contable of this DepartamentoContable.
        :rtype: str
        """
        return self._nombre_departamento_contable

    @nombre_departamento_contable.setter
    def nombre_departamento_contable(self, nombre_departamento_contable: str):
        """
        Sets the nombre_departamento_contable of this DepartamentoContable.

        :param nombre_departamento_contable: The nombre_departamento_contable of this DepartamentoContable.
        :type nombre_departamento_contable: str
        """

        self._nombre_departamento_contable = nombre_departamento_contable

    @property
    def descripcion_departamento_contable(self) -> str:
        """
        Gets the descripcion_departamento_contable of this DepartamentoContable.

        :return: The descripcion_departamento_contable of this DepartamentoContable.
        :rtype: str
        """
        return self._descripcion_departamento_contable

    @descripcion_departamento_contable.setter
    def descripcion_departamento_contable(self, descripcion_departamento_contable: str):
        """
        Sets the descripcion_departamento_contable of this DepartamentoContable.

        :param descripcion_departamento_contable: The descripcion_departamento_contable of this DepartamentoContable.
        :type descripcion_departamento_contable: str
        """

        self._descripcion_departamento_contable = descripcion_departamento_contable

    @property
    def id_facultad(self) -> int:
        """
        Gets the id_facultad of this DepartamentoContable.

        :return: The id_facultad of this DepartamentoContable.
        :rtype: int
        """
        return self._id_facultad

    @id_facultad.setter
    def id_facultad(self, id_facultad: int):
        """
        Sets the id_facultad of this DepartamentoContable.

        :param id_facultad: The id_facultad of this DepartamentoContable.
        :type id_facultad: int
        """

        self._id_facultad = id_facultad

