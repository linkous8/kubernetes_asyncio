# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.10.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1Toleration(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'effect': 'str',
        'key': 'str',
        'operator': 'str',
        'toleration_seconds': 'int',
        'value': 'str'
    }

    attribute_map = {
        'effect': 'effect',
        'key': 'key',
        'operator': 'operator',
        'toleration_seconds': 'tolerationSeconds',
        'value': 'value'
    }

    def __init__(self, effect=None, key=None, operator=None, toleration_seconds=None, value=None):  # noqa: E501
        """V1Toleration - a model defined in Swagger"""  # noqa: E501

        self._effect = None
        self._key = None
        self._operator = None
        self._toleration_seconds = None
        self._value = None
        self.discriminator = None

        if effect is not None:
            self.effect = effect
        if key is not None:
            self.key = key
        if operator is not None:
            self.operator = operator
        if toleration_seconds is not None:
            self.toleration_seconds = toleration_seconds
        if value is not None:
            self.value = value

    @property
    def effect(self):
        """Gets the effect of this V1Toleration.  # noqa: E501

        Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.  # noqa: E501

        :return: The effect of this V1Toleration.  # noqa: E501
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this V1Toleration.

        Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.  # noqa: E501

        :param effect: The effect of this V1Toleration.  # noqa: E501
        :type: str
        """

        self._effect = effect

    @property
    def key(self):
        """Gets the key of this V1Toleration.  # noqa: E501

        Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.  # noqa: E501

        :return: The key of this V1Toleration.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this V1Toleration.

        Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.  # noqa: E501

        :param key: The key of this V1Toleration.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def operator(self):
        """Gets the operator of this V1Toleration.  # noqa: E501

        Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.  # noqa: E501

        :return: The operator of this V1Toleration.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this V1Toleration.

        Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.  # noqa: E501

        :param operator: The operator of this V1Toleration.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def toleration_seconds(self):
        """Gets the toleration_seconds of this V1Toleration.  # noqa: E501

        TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.  # noqa: E501

        :return: The toleration_seconds of this V1Toleration.  # noqa: E501
        :rtype: int
        """
        return self._toleration_seconds

    @toleration_seconds.setter
    def toleration_seconds(self, toleration_seconds):
        """Sets the toleration_seconds of this V1Toleration.

        TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.  # noqa: E501

        :param toleration_seconds: The toleration_seconds of this V1Toleration.  # noqa: E501
        :type: int
        """

        self._toleration_seconds = toleration_seconds

    @property
    def value(self):
        """Gets the value of this V1Toleration.  # noqa: E501

        Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.  # noqa: E501

        :return: The value of this V1Toleration.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this V1Toleration.

        Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.  # noqa: E501

        :param value: The value of this V1Toleration.  # noqa: E501
        :type: str
        """

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1Toleration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
