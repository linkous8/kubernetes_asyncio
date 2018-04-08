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



class V1SubjectRulesReviewStatus(object):
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
        'evaluation_error': 'str',
        'incomplete': 'bool',
        'non_resource_rules': 'list[V1NonResourceRule]',
        'resource_rules': 'list[V1ResourceRule]'
    }

    attribute_map = {
        'evaluation_error': 'evaluationError',
        'incomplete': 'incomplete',
        'non_resource_rules': 'nonResourceRules',
        'resource_rules': 'resourceRules'
    }

    def __init__(self, evaluation_error=None, incomplete=None, non_resource_rules=None, resource_rules=None):  # noqa: E501
        """V1SubjectRulesReviewStatus - a model defined in Swagger"""  # noqa: E501

        self._evaluation_error = None
        self._incomplete = None
        self._non_resource_rules = None
        self._resource_rules = None
        self.discriminator = None

        if evaluation_error is not None:
            self.evaluation_error = evaluation_error
        self.incomplete = incomplete
        self.non_resource_rules = non_resource_rules
        self.resource_rules = resource_rules

    @property
    def evaluation_error(self):
        """Gets the evaluation_error of this V1SubjectRulesReviewStatus.  # noqa: E501

        EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn't support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete.  # noqa: E501

        :return: The evaluation_error of this V1SubjectRulesReviewStatus.  # noqa: E501
        :rtype: str
        """
        return self._evaluation_error

    @evaluation_error.setter
    def evaluation_error(self, evaluation_error):
        """Sets the evaluation_error of this V1SubjectRulesReviewStatus.

        EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn't support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete.  # noqa: E501

        :param evaluation_error: The evaluation_error of this V1SubjectRulesReviewStatus.  # noqa: E501
        :type: str
        """

        self._evaluation_error = evaluation_error

    @property
    def incomplete(self):
        """Gets the incomplete of this V1SubjectRulesReviewStatus.  # noqa: E501

        Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn't support rules evaluation.  # noqa: E501

        :return: The incomplete of this V1SubjectRulesReviewStatus.  # noqa: E501
        :rtype: bool
        """
        return self._incomplete

    @incomplete.setter
    def incomplete(self, incomplete):
        """Sets the incomplete of this V1SubjectRulesReviewStatus.

        Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn't support rules evaluation.  # noqa: E501

        :param incomplete: The incomplete of this V1SubjectRulesReviewStatus.  # noqa: E501
        :type: bool
        """
        if incomplete is None:
            raise ValueError("Invalid value for `incomplete`, must not be `None`")  # noqa: E501

        self._incomplete = incomplete

    @property
    def non_resource_rules(self):
        """Gets the non_resource_rules of this V1SubjectRulesReviewStatus.  # noqa: E501

        NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.  # noqa: E501

        :return: The non_resource_rules of this V1SubjectRulesReviewStatus.  # noqa: E501
        :rtype: list[V1NonResourceRule]
        """
        return self._non_resource_rules

    @non_resource_rules.setter
    def non_resource_rules(self, non_resource_rules):
        """Sets the non_resource_rules of this V1SubjectRulesReviewStatus.

        NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.  # noqa: E501

        :param non_resource_rules: The non_resource_rules of this V1SubjectRulesReviewStatus.  # noqa: E501
        :type: list[V1NonResourceRule]
        """
        if non_resource_rules is None:
            raise ValueError("Invalid value for `non_resource_rules`, must not be `None`")  # noqa: E501

        self._non_resource_rules = non_resource_rules

    @property
    def resource_rules(self):
        """Gets the resource_rules of this V1SubjectRulesReviewStatus.  # noqa: E501

        ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.  # noqa: E501

        :return: The resource_rules of this V1SubjectRulesReviewStatus.  # noqa: E501
        :rtype: list[V1ResourceRule]
        """
        return self._resource_rules

    @resource_rules.setter
    def resource_rules(self, resource_rules):
        """Sets the resource_rules of this V1SubjectRulesReviewStatus.

        ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.  # noqa: E501

        :param resource_rules: The resource_rules of this V1SubjectRulesReviewStatus.  # noqa: E501
        :type: list[V1ResourceRule]
        """
        if resource_rules is None:
            raise ValueError("Invalid value for `resource_rules`, must not be `None`")  # noqa: E501

        self._resource_rules = resource_rules

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
        if not isinstance(other, V1SubjectRulesReviewStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
