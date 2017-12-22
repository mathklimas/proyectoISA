# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Alumno(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, nombre: str=None, apellido: str=None, dni: str=None, direccion: str=None, correo: str=None, telefono: str=None, id_grado: int=None):
        """
        Alumno - a model defined in Swagger

        :param nombre: The nombre of this Alumno.
        :type nombre: str
        :param apellido: The apellido of this Alumno.
        :type apellido: str
        :param dni: The dni of this Alumno.
        :type dni: str
        :param direccion: The direccion of this Alumno.
        :type direccion: str
        :param correo: The correo of this Alumno.
        :type correo: str
        :param telefono: The telefono of this Alumno.
        :type telefono: str
        :param id_grado: The id_grado of this Alumno.
        :type id_grado: int
        """
        self.swagger_types = {
            'nombre': str,
            'apellido': str,
            'dni': str,
            'direccion': str,
            'correo': str,
            'telefono': str,
            'id_grado': int
        }

        self.attribute_map = {
            'nombre': 'nombre',
            'apellido': 'apellido',
            'dni': 'dni',
            'direccion': 'direccion',
            'correo': 'correo',
            'telefono': 'telefono',
            'id_grado': 'id_grado'
        }

        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._direccion = direccion
        self._correo = correo
        self._telefono = telefono
        self._id_grado = id_grado

    @classmethod
    def from_dict(cls, dikt) -> 'Alumno':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Alumno of this Alumno.
        :rtype: Alumno
        """
        return deserialize_model(dikt, cls)

    @property
    def nombre(self) -> str:
        """
        Gets the nombre of this Alumno.

        :return: The nombre of this Alumno.
        :rtype: str
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """
        Sets the nombre of this Alumno.

        :param nombre: The nombre of this Alumno.
        :type nombre: str
        """

        self._nombre = nombre

    @property
    def apellido(self) -> str:
        """
        Gets the apellido of this Alumno.

        :return: The apellido of this Alumno.
        :rtype: str
        """
        return self._apellido

    @apellido.setter
    def apellido(self, apellido: str):
        """
        Sets the apellido of this Alumno.

        :param apellido: The apellido of this Alumno.
        :type apellido: str
        """

        self._apellido = apellido

    @property
    def dni(self) -> str:
        """
        Gets the dni of this Alumno.

        :return: The dni of this Alumno.
        :rtype: str
        """
        return self._dni

    @dni.setter
    def dni(self, dni: str):
        """
        Sets the dni of this Alumno.

        :param dni: The dni of this Alumno.
        :type dni: str
        """

        self._dni = dni

    @property
    def direccion(self) -> str:
        """
        Gets the direccion of this Alumno.

        :return: The direccion of this Alumno.
        :rtype: str
        """
        return self._direccion

    @direccion.setter
    def direccion(self, direccion: str):
        """
        Sets the direccion of this Alumno.

        :param direccion: The direccion of this Alumno.
        :type direccion: str
        """

        self._direccion = direccion

    @property
    def correo(self) -> str:
        """
        Gets the correo of this Alumno.

        :return: The correo of this Alumno.
        :rtype: str
        """
        return self._correo

    @correo.setter
    def correo(self, correo: str):
        """
        Sets the correo of this Alumno.

        :param correo: The correo of this Alumno.
        :type correo: str
        """

        self._correo = correo

    @property
    def telefono(self) -> str:
        """
        Gets the telefono of this Alumno.

        :return: The telefono of this Alumno.
        :rtype: str
        """
        return self._telefono

    @telefono.setter
    def telefono(self, telefono: str):
        """
        Sets the telefono of this Alumno.

        :param telefono: The telefono of this Alumno.
        :type telefono: str
        """

        self._telefono = telefono

    @property
    def id_grado(self) -> int:
        """
        Gets the id_grado of this Alumno.

        :return: The id_grado of this Alumno.
        :rtype: int
        """
        return self._id_grado

    @id_grado.setter
    def id_grado(self, id_grado: int):
        """
        Sets the id_grado of this Alumno.

        :param id_grado: The id_grado of this Alumno.
        :type id_grado: int
        """

        self._id_grado = id_grado

