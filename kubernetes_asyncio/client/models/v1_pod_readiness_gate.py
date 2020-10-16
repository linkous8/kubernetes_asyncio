# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.16.14
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes_asyncio.client.configuration import Configuration


class V1PodReadinessGate(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'condition_type': 'str'
    }

    attribute_map = {
        'condition_type': 'conditionType'
    }

    def __init__(self, condition_type=None, local_vars_configuration=None):  # noqa: E501
        """V1PodReadinessGate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._condition_type = None
        self.discriminator = None

        self.condition_type = condition_type

    @property
    def condition_type(self):
        """Gets the condition_type of this V1PodReadinessGate.  # noqa: E501

        ConditionType refers to a condition in the pod's condition list with matching type.  # noqa: E501

        :return: The condition_type of this V1PodReadinessGate.  # noqa: E501
        :rtype: str
        """
        return self._condition_type

    @condition_type.setter
    def condition_type(self, condition_type):
        """Sets the condition_type of this V1PodReadinessGate.

        ConditionType refers to a condition in the pod's condition list with matching type.  # noqa: E501

        :param condition_type: The condition_type of this V1PodReadinessGate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and condition_type is None:  # noqa: E501
            raise ValueError("Invalid value for `condition_type`, must not be `None`")  # noqa: E501

        self._condition_type = condition_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, V1PodReadinessGate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1PodReadinessGate):
            return True

        return self.to_dict() != other.to_dict()
