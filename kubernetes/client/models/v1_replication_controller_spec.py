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



class V1ReplicationControllerSpec(object):
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
        'min_ready_seconds': 'int',
        'replicas': 'int',
        'selector': 'dict(str, str)',
        'template': 'V1PodTemplateSpec'
    }

    attribute_map = {
        'min_ready_seconds': 'minReadySeconds',
        'replicas': 'replicas',
        'selector': 'selector',
        'template': 'template'
    }

    def __init__(self, min_ready_seconds=None, replicas=None, selector=None, template=None):  # noqa: E501
        """V1ReplicationControllerSpec - a model defined in Swagger"""  # noqa: E501

        self._min_ready_seconds = None
        self._replicas = None
        self._selector = None
        self._template = None
        self.discriminator = None

        if min_ready_seconds is not None:
            self.min_ready_seconds = min_ready_seconds
        if replicas is not None:
            self.replicas = replicas
        if selector is not None:
            self.selector = selector
        if template is not None:
            self.template = template

    @property
    def min_ready_seconds(self):
        """Gets the min_ready_seconds of this V1ReplicationControllerSpec.  # noqa: E501

        Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)  # noqa: E501

        :return: The min_ready_seconds of this V1ReplicationControllerSpec.  # noqa: E501
        :rtype: int
        """
        return self._min_ready_seconds

    @min_ready_seconds.setter
    def min_ready_seconds(self, min_ready_seconds):
        """Sets the min_ready_seconds of this V1ReplicationControllerSpec.

        Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)  # noqa: E501

        :param min_ready_seconds: The min_ready_seconds of this V1ReplicationControllerSpec.  # noqa: E501
        :type: int
        """

        self._min_ready_seconds = min_ready_seconds

    @property
    def replicas(self):
        """Gets the replicas of this V1ReplicationControllerSpec.  # noqa: E501

        Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller  # noqa: E501

        :return: The replicas of this V1ReplicationControllerSpec.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this V1ReplicationControllerSpec.

        Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller  # noqa: E501

        :param replicas: The replicas of this V1ReplicationControllerSpec.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def selector(self):
        """Gets the selector of this V1ReplicationControllerSpec.  # noqa: E501

        Selector is a label query over pods that should match the Replicas count. If Selector is empty, it is defaulted to the labels present on the Pod template. Label keys and values that must match in order to be controlled by this replication controller, if empty defaulted to labels on Pod template. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors  # noqa: E501

        :return: The selector of this V1ReplicationControllerSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this V1ReplicationControllerSpec.

        Selector is a label query over pods that should match the Replicas count. If Selector is empty, it is defaulted to the labels present on the Pod template. Label keys and values that must match in order to be controlled by this replication controller, if empty defaulted to labels on Pod template. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors  # noqa: E501

        :param selector: The selector of this V1ReplicationControllerSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._selector = selector

    @property
    def template(self):
        """Gets the template of this V1ReplicationControllerSpec.  # noqa: E501

        Template is the object that describes the pod that will be created if insufficient replicas are detected. This takes precedence over a TemplateRef. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template  # noqa: E501

        :return: The template of this V1ReplicationControllerSpec.  # noqa: E501
        :rtype: V1PodTemplateSpec
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this V1ReplicationControllerSpec.

        Template is the object that describes the pod that will be created if insufficient replicas are detected. This takes precedence over a TemplateRef. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template  # noqa: E501

        :param template: The template of this V1ReplicationControllerSpec.  # noqa: E501
        :type: V1PodTemplateSpec
        """

        self._template = template

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
        if not isinstance(other, V1ReplicationControllerSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
