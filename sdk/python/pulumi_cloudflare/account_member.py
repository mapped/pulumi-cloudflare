# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AccountMemberArgs', 'AccountMember']

@pulumi.input_type
class AccountMemberArgs:
    def __init__(__self__, *,
                 email_address: pulumi.Input[str],
                 role_ids: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        The set of arguments for constructing a AccountMember resource.
        :param pulumi.Input[str] email_address: The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_ids: Array of account role IDs that you want to assign to a member.
        """
        pulumi.set(__self__, "email_address", email_address)
        pulumi.set(__self__, "role_ids", role_ids)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> pulumi.Input[str]:
        """
        The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.
        """
        return pulumi.get(self, "email_address")

    @email_address.setter
    def email_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "email_address", value)

    @property
    @pulumi.getter(name="roleIds")
    def role_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Array of account role IDs that you want to assign to a member.
        """
        return pulumi.get(self, "role_ids")

    @role_ids.setter
    def role_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "role_ids", value)


@pulumi.input_type
class _AccountMemberState:
    def __init__(__self__, *,
                 email_address: Optional[pulumi.Input[str]] = None,
                 role_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering AccountMember resources.
        :param pulumi.Input[str] email_address: The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_ids: Array of account role IDs that you want to assign to a member.
        """
        if email_address is not None:
            pulumi.set(__self__, "email_address", email_address)
        if role_ids is not None:
            pulumi.set(__self__, "role_ids", role_ids)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[str]]:
        """
        The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.
        """
        return pulumi.get(self, "email_address")

    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email_address", value)

    @property
    @pulumi.getter(name="roleIds")
    def role_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Array of account role IDs that you want to assign to a member.
        """
        return pulumi.get(self, "role_ids")

    @role_ids.setter
    def role_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "role_ids", value)


class AccountMember(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 email_address: Optional[pulumi.Input[str]] = None,
                 role_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a resource which manages Cloudflare account members.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        example_user = cloudflare.AccountMember("exampleUser",
            email_address="user@example.com",
            role_ids=[
                "68b329da9893e34099c7d8ad5cb9c940",
                "d784fa8b6d98d27699781bd9a7cf19f0",
            ])
        ```

        ## Import

        Account members can be imported using a composite ID formed of account ID and account member ID, e.g.

        ```sh
         $ pulumi import cloudflare:index/accountMember:AccountMember example_user d41d8cd98f00b204e9800998ecf8427e/b58c6f14d292556214bd64909bcdb118
        ```

         where* `d41d8cd98f00b204e9800998ecf8427e` - account ID as returned by the [API](https://api.cloudflare.com/#accounts-account-details) * `b58c6f14d292556214bd64909bcdb118` - account member ID as returned by the [API](https://api.cloudflare.com/#account-members-member-details)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] email_address: The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_ids: Array of account role IDs that you want to assign to a member.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccountMemberArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource which manages Cloudflare account members.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        example_user = cloudflare.AccountMember("exampleUser",
            email_address="user@example.com",
            role_ids=[
                "68b329da9893e34099c7d8ad5cb9c940",
                "d784fa8b6d98d27699781bd9a7cf19f0",
            ])
        ```

        ## Import

        Account members can be imported using a composite ID formed of account ID and account member ID, e.g.

        ```sh
         $ pulumi import cloudflare:index/accountMember:AccountMember example_user d41d8cd98f00b204e9800998ecf8427e/b58c6f14d292556214bd64909bcdb118
        ```

         where* `d41d8cd98f00b204e9800998ecf8427e` - account ID as returned by the [API](https://api.cloudflare.com/#accounts-account-details) * `b58c6f14d292556214bd64909bcdb118` - account member ID as returned by the [API](https://api.cloudflare.com/#account-members-member-details)

        :param str resource_name: The name of the resource.
        :param AccountMemberArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountMemberArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 email_address: Optional[pulumi.Input[str]] = None,
                 role_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccountMemberArgs.__new__(AccountMemberArgs)

            if email_address is None and not opts.urn:
                raise TypeError("Missing required property 'email_address'")
            __props__.__dict__["email_address"] = email_address
            if role_ids is None and not opts.urn:
                raise TypeError("Missing required property 'role_ids'")
            __props__.__dict__["role_ids"] = role_ids
        super(AccountMember, __self__).__init__(
            'cloudflare:index/accountMember:AccountMember',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            email_address: Optional[pulumi.Input[str]] = None,
            role_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'AccountMember':
        """
        Get an existing AccountMember resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] email_address: The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_ids: Array of account role IDs that you want to assign to a member.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccountMemberState.__new__(_AccountMemberState)

        __props__.__dict__["email_address"] = email_address
        __props__.__dict__["role_ids"] = role_ids
        return AccountMember(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> pulumi.Output[str]:
        """
        The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.
        """
        return pulumi.get(self, "email_address")

    @property
    @pulumi.getter(name="roleIds")
    def role_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        Array of account role IDs that you want to assign to a member.
        """
        return pulumi.get(self, "role_ids")

