# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetAccountRolesResult',
    'AwaitableGetAccountRolesResult',
    'get_account_roles',
    'get_account_roles_output',
]

@pulumi.output_type
class GetAccountRolesResult:
    """
    A collection of values returned by getAccountRoles.
    """
    def __init__(__self__, account_id=None, id=None, roles=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if roles and not isinstance(roles, list):
            raise TypeError("Expected argument 'roles' to be a list")
        pulumi.set(__self__, "roles", roles)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def roles(self) -> Sequence['outputs.GetAccountRolesRoleResult']:
        """
        A list of roles object. See below for nested attributes.
        """
        return pulumi.get(self, "roles")


class AwaitableGetAccountRolesResult(GetAccountRolesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountRolesResult(
            account_id=self.account_id,
            id=self.id,
            roles=self.roles)


def get_account_roles(account_id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountRolesResult:
    """
    Use this data source to lookup [Account Roles](https://api.cloudflare.com/#account-roles-properties).


    :param str account_id: The account for which to list the roles.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getAccountRoles:getAccountRoles', __args__, opts=opts, typ=GetAccountRolesResult).value

    return AwaitableGetAccountRolesResult(
        account_id=__ret__.account_id,
        id=__ret__.id,
        roles=__ret__.roles)


@_utilities.lift_output_func(get_account_roles)
def get_account_roles_output(account_id: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccountRolesResult]:
    """
    Use this data source to lookup [Account Roles](https://api.cloudflare.com/#account-roles-properties).


    :param str account_id: The account for which to list the roles.
    """
    ...
