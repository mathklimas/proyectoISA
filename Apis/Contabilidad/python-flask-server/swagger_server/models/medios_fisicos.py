# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class MediosFisicos(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_medio: str=None, disponibilidad: bool=None, tipo: str=None, precio_hora: float=None, capacidad: int=None, id_facultad: str=None):
        """
        MediosFisicos - a model defined in Swagger

        :param id_medio: The id_medio of this MediosFisicos.
        :type id_medio: str
        :param disponibilidad: The disponibilidad of this MediosFisicos.
        :type disponibilidad: bool
        :param tipo: The tipo of this MediosFisicos.
        :type tipo: str
        :param precio_hora: The precio_hora of this MediosFisicos.
        :type precio_hora: float
        :param capacidad: The capacidad of this MediosFisicos.
        :type capacidad: int
        :param id_facultad: The id_facultad of this MediosFisicos.
        :type id_facultad: str
        """
        self.swagger_types = {
            'id_medio': str,
            'disponibilidad': bool,
            'tipo': str,
            'precio_hora': float,
            'capacidad': int,
            'id_facultad': str
        }

        self.attribute_map = {
            'id_medio': 'id_medio',
            'disponibilidad': 'disponibilidad',
            'tipo': 'tipo',
            'precio_hora': 'precio_hora',
            'capacidad': 'capacidad',
            'id_facultad': 'id_facultad'
        }

        self._id_medio = id_medio
        self._disponibilidad = disponibilidad
        self._tipo = tipo
        self._precio_hora = precio_hora
        self._capacidad = capacidad
        self._id_facultad = id_facultad

    @classmethod
    def from_dict(cls, dikt) -> 'MediosFisicos':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MediosFisicos of this MediosFisicos.
        :rtype: MediosFisicos
        """
        return deserialize_model(dikt, cls)

    @property
    def id_medio(self) -> str:
        """
        Gets the id_medio of this MediosFisicos.

        :return: The id_medio of this MediosFisicos.
        :rtype: str
        """
        return self._id_medio

    @id_medio.setter
    def id_medio(self, id_medio: str):
        """
        Sets the id_medio of this MediosFisicos.

        :param id_medio: The id_medio of this MediosFisicos.
        :type id_medio: str
        """

        self._id_medio = id_medio

    @property
    def disponibilidad(self) -> bool:
        """
        Gets the disponibilidad of this MediosFisicos.

        :return: The disponibilidad of this MediosFisicos.
        :rtype: bool
        """
        return self._disponibilidad

    @disponibilidad.setter
    def disponibilidad(self, disponibilidad: bool):
        """
        Sets the disponibilidad of this MediosFisicos.

        :param disponibilidad: The disponibilidad of this MediosFisicos.
        :type disponibilidad: bool
        """

        self._disponibilidad = disponibilidad

    @property
    def tipo(self) -> str:
        """
        Gets the tipo of this MediosFisicos.

        :return: The tipo of this MediosFisicos.
        :rtype: str
        """
        return self._tipo

    @tipo.setter
    def tipo(self, tipo: str):
        """
        Sets the tipo of this MediosFisicos.

        :param tipo: The tipo of this MediosFisicos.
        :type tipo: str
        """

        self._tipo = tipo

    @property
    def precio_hora(self) -> float:
        """
        Gets the precio_hora of this MediosFisicos.

        :return: The precio_hora of this MediosFisicos.
        :rtype: float
        """
        return self._precio_hora

    @precio_hora.setter
    def precio_hora(self, precio_hora: float):
        """
        Sets the precio_hora of this MediosFisicos.

        :param precio_hora: The precio_hora of this MediosFisicos.
        :type precio_hora: float
        """

        self._precio_hora = precio_hora

    @property
    def capacidad(self) -> int:
        """
        Gets the capacidad of this MediosFisicos.

        :return: The capacidad of this MediosFisicos.
        :rtype: int
        """
        return self._capacidad

    @capacidad.setter
    def capacidad(self, capacidad: int):
        """
        Sets the capacidad of this MediosFisicos.

        :param capacidad: The capacidad of this MediosFisicos.
        :type capacidad: int
        """

        self._capacidad = capacidad

    @property
    def id_facultad(self) -> str:
        """
        Gets the id_facultad of this MediosFisicos.

        :return: The id_facultad of this MediosFisicos.
        :rtype: str
        """
        return self._id_facultad

    @id_facultad.setter
    def id_facultad(self, id_facultad: str):
        """
        Sets the id_facultad of this MediosFisicos.

        :param id_facultad: The id_facultad of this MediosFisicos.
        :type id_facultad: str
        """

        self._id_facultad = id_facultad

