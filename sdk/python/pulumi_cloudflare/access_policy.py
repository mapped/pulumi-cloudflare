# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['AccessPolicyArgs', 'AccessPolicy']

@pulumi.input_type
class AccessPolicyArgs:
    def __init__(__self__, *,
                 application_id: pulumi.Input[str],
                 decision: pulumi.Input[str],
                 includes: pulumi.Input[Sequence[pulumi.Input['AccessPolicyIncludeArgs']]],
                 name: pulumi.Input[str],
                 precedence: pulumi.Input[int],
                 account_id: Optional[pulumi.Input[str]] = None,
                 excludes: Optional[pulumi.Input[Sequence[pulumi.Input['AccessPolicyExcludeArgs']]]] = None,
                 requires: Optional[pulumi.Input[Sequence[pulumi.Input['AccessPolicyRequireArgs']]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AccessPolicy resource.
        :param pulumi.Input[str] application_id: The ID of the application the policy is associated with.
        :param pulumi.Input[str] decision: Defines the action Access will take if the policy matches the user.
               Allowed values: `allow`, `deny`, `non_identity`, `bypass`
        :param pulumi.Input[Sequence[pulumi.Input['AccessPolicyIncludeArgs']]] includes: A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        :param pulumi.Input[str] name: Friendly name of the Access Application.
        :param pulumi.Input[int] precedence: The unique precedence for policies on a single application. Integer.
        :param pulumi.Input[str] account_id: The account to which the access rule should be added. Conflicts with `zone_id`.
        :param pulumi.Input[Sequence[pulumi.Input['AccessPolicyExcludeArgs']]] excludes: A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        :param pulumi.Input[Sequence[pulumi.Input['AccessPolicyRequireArgs']]] requires: A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        :param pulumi.Input[str] zone_id: The DNS zone to which the access rule should be added. Conflicts with `account_id`.
        """
        pulumi.set(__self__, "application_id", application_id)
        pulumi.set(__self__, "decision", decision)
        pulumi.set(__self__, "includes", includes)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "precedence", precedence)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if excludes is not None:
            pulumi.set(__self__, "excludes", excludes)
        if requires is not None:
            pulumi.set(__self__, "requires", requires)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[str]:
        """
        The ID of the application the policy is associated with.
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter
    def decision(self) -> pulumi.Input[str]:
        """
        Defines the action Access will take if the policy matches the user.
        Allowed values: `allow`, `deny`, `non_identity`, `bypass`
        """
        return pulumi.get(self, "decision")

    @decision.setter
    def decision(self, value: pulumi.Input[str]):
        pulumi.set(self, "decision", value)

    @property
    @pulumi.getter
    def includes(self) -> pulumi.Input[Sequence[pulumi.Input['AccessPolicyIncludeArgs']]]:
        """
        A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        """
        return pulumi.get(self, "includes")

    @includes.setter
    def includes(self, value: pulumi.Input[Sequence[pulumi.Input['AccessPolicyIncludeArgs']]]):
        pulumi.set(self, "includes", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Friendly name of the Access Application.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def precedence(self) -> pulumi.Input[int]:
        """
        The unique precedence for policies on a single application. Integer.
        """
        return pulumi.get(self, "precedence")

    @precedence.setter
    def precedence(self, value: pulumi.Input[int]):
        pulumi.set(self, "precedence", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account to which the access rule should be added. Conflicts with `zone_id`.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def excludes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccessPolicyExcludeArgs']]]]:
        """
        A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        """
        return pulumi.get(self, "excludes")

    @excludes.setter
    def excludes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccessPolicyExcludeArgs']]]]):
        pulumi.set(self, "excludes", value)

    @property
    @pulumi.getter
    def requires(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccessPolicyRequireArgs']]]]:
        """
        A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        """
        return pulumi.get(self, "requires")

    @requires.setter
    def requires(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccessPolicyRequireArgs']]]]):
        pulumi.set(self, "requires", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The DNS zone to which the access rule should be added. Conflicts with `account_id`.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


@pulumi.input_type
class _AccessPolicyState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 decision: Optional[pulumi.Input[str]] = None,
                 excludes: Optional[pulumi.Input[Sequence[pulumi.Input['AccessPolicyExcludeArgs']]]] = None,
                 includes: Optional[pulumi.Input[Sequence[pulumi.Input['AccessPolicyIncludeArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 precedence: Optional[pulumi.Input[int]] = None,
                 requires: Optional[pulumi.Input[Sequence[pulumi.Input['AccessPolicyRequireArgs']]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AccessPolicy resources.
        :param pulumi.Input[str] account_id: The account to which the access rule should be added. Conflicts with `zone_id`.
        :param pulumi.Input[str] application_id: The ID of the application the policy is associated with.
        :param pulumi.Input[str] decision: Defines the action Access will take if the policy matches the user.
               Allowed values: `allow`, `deny`, `non_identity`, `bypass`
        :param pulumi.Input[Sequence[pulumi.Input['AccessPolicyExcludeArgs']]] excludes: A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        :param pulumi.Input[Sequence[pulumi.Input['AccessPolicyIncludeArgs']]] includes: A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        :param pulumi.Input[str] name: Friendly name of the Access Application.
        :param pulumi.Input[int] precedence: The unique precedence for policies on a single application. Integer.
        :param pulumi.Input[Sequence[pulumi.Input['AccessPolicyRequireArgs']]] requires: A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        :param pulumi.Input[str] zone_id: The DNS zone to which the access rule should be added. Conflicts with `account_id`.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if application_id is not None:
            pulumi.set(__self__, "application_id", application_id)
        if decision is not None:
            pulumi.set(__self__, "decision", decision)
        if excludes is not None:
            pulumi.set(__self__, "excludes", excludes)
        if includes is not None:
            pulumi.set(__self__, "includes", includes)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if precedence is not None:
            pulumi.set(__self__, "precedence", precedence)
        if requires is not None:
            pulumi.set(__self__, "requires", requires)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account to which the access rule should be added. Conflicts with `zone_id`.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the application the policy is associated with.
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter
    def decision(self) -> Optional[pulumi.Input[str]]:
        """
        Defines the action Access will take if the policy matches the user.
        Allowed values: `allow`, `deny`, `non_identity`, `bypass`
        """
        return pulumi.get(self, "decision")

    @decision.setter
    def decision(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "decision", value)

    @property
    @pulumi.getter
    def excludes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccessPolicyExcludeArgs']]]]:
        """
        A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        """
        return pulumi.get(self, "excludes")

    @excludes.setter
    def excludes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccessPolicyExcludeArgs']]]]):
        pulumi.set(self, "excludes", value)

    @property
    @pulumi.getter
    def includes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccessPolicyIncludeArgs']]]]:
        """
        A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        """
        return pulumi.get(self, "includes")

    @includes.setter
    def includes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccessPolicyIncludeArgs']]]]):
        pulumi.set(self, "includes", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Friendly name of the Access Application.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def precedence(self) -> Optional[pulumi.Input[int]]:
        """
        The unique precedence for policies on a single application. Integer.
        """
        return pulumi.get(self, "precedence")

    @precedence.setter
    def precedence(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "precedence", value)

    @property
    @pulumi.getter
    def requires(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccessPolicyRequireArgs']]]]:
        """
        A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        """
        return pulumi.get(self, "requires")

    @requires.setter
    def requires(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccessPolicyRequireArgs']]]]):
        pulumi.set(self, "requires", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The DNS zone to which the access rule should be added. Conflicts with `account_id`.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class AccessPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 decision: Optional[pulumi.Input[str]] = None,
                 excludes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessPolicyExcludeArgs']]]]] = None,
                 includes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessPolicyIncludeArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 precedence: Optional[pulumi.Input[int]] = None,
                 requires: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessPolicyRequireArgs']]]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Cloudflare Access Policy resource. Access Policies are used
        in conjunction with Access Applications to restrict access to a
        particular resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        # Allowing access to `test@example.com` email address only
        test_policy_access_policy = cloudflare.AccessPolicy("testPolicyAccessPolicy",
            application_id="cb029e245cfdd66dc8d2e570d5dd3322",
            zone_id="d41d8cd98f00b204e9800998ecf8427e",
            name="staging policy",
            precedence=1,
            decision="allow",
            includes=[cloudflare.AccessPolicyIncludeArgs(
                emails=["test@example.com"],
            )])
        # Allowing `test@example.com` to access but only when coming from a
        # specific IP.
        test_policy_index_access_policy_access_policy = cloudflare.AccessPolicy("testPolicyIndex/accessPolicyAccessPolicy",
            application_id="cb029e245cfdd66dc8d2e570d5dd3322",
            zone_id="d41d8cd98f00b204e9800998ecf8427e",
            name="staging policy",
            precedence=1,
            decision="allow",
            includes=[cloudflare.AccessPolicyIncludeArgs(
                emails=["test@example.com"],
            )],
            requires={
                "ips": [var["office_ip"]],
            })
        ```

        ## Import

        Access Policies can be imported using a composite ID formed of identifier type (`zone` or `account`), identifier ID (`zone_id` or `account_id`), application ID and policy ID. # import a zone level Access policy

        ```sh
         $ pulumi import cloudflare:index/accessPolicy:AccessPolicy staging zone/cb029e245cfdd66dc8d2e570d5dd3322/d41d8cd98f00b204e9800998ecf8427e/67ea780ce4982c1cfbe6b7293afc765d
        ```

        # import an account level Access policy

        ```sh
         $ pulumi import cloudflare:index/accessPolicy:AccessPolicy production account/0d599f0ec05c3bda8c3b8a68c32a1b47/d41d8cd98f00b204e9800998ecf8427e/67ea780ce4982c1cfbe6b7293afc765d
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account to which the access rule should be added. Conflicts with `zone_id`.
        :param pulumi.Input[str] application_id: The ID of the application the policy is associated with.
        :param pulumi.Input[str] decision: Defines the action Access will take if the policy matches the user.
               Allowed values: `allow`, `deny`, `non_identity`, `bypass`
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessPolicyExcludeArgs']]]] excludes: A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessPolicyIncludeArgs']]]] includes: A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        :param pulumi.Input[str] name: Friendly name of the Access Application.
        :param pulumi.Input[int] precedence: The unique precedence for policies on a single application. Integer.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessPolicyRequireArgs']]]] requires: A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        :param pulumi.Input[str] zone_id: The DNS zone to which the access rule should be added. Conflicts with `account_id`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloudflare Access Policy resource. Access Policies are used
        in conjunction with Access Applications to restrict access to a
        particular resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        # Allowing access to `test@example.com` email address only
        test_policy_access_policy = cloudflare.AccessPolicy("testPolicyAccessPolicy",
            application_id="cb029e245cfdd66dc8d2e570d5dd3322",
            zone_id="d41d8cd98f00b204e9800998ecf8427e",
            name="staging policy",
            precedence=1,
            decision="allow",
            includes=[cloudflare.AccessPolicyIncludeArgs(
                emails=["test@example.com"],
            )])
        # Allowing `test@example.com` to access but only when coming from a
        # specific IP.
        test_policy_index_access_policy_access_policy = cloudflare.AccessPolicy("testPolicyIndex/accessPolicyAccessPolicy",
            application_id="cb029e245cfdd66dc8d2e570d5dd3322",
            zone_id="d41d8cd98f00b204e9800998ecf8427e",
            name="staging policy",
            precedence=1,
            decision="allow",
            includes=[cloudflare.AccessPolicyIncludeArgs(
                emails=["test@example.com"],
            )],
            requires={
                "ips": [var["office_ip"]],
            })
        ```

        ## Import

        Access Policies can be imported using a composite ID formed of identifier type (`zone` or `account`), identifier ID (`zone_id` or `account_id`), application ID and policy ID. # import a zone level Access policy

        ```sh
         $ pulumi import cloudflare:index/accessPolicy:AccessPolicy staging zone/cb029e245cfdd66dc8d2e570d5dd3322/d41d8cd98f00b204e9800998ecf8427e/67ea780ce4982c1cfbe6b7293afc765d
        ```

        # import an account level Access policy

        ```sh
         $ pulumi import cloudflare:index/accessPolicy:AccessPolicy production account/0d599f0ec05c3bda8c3b8a68c32a1b47/d41d8cd98f00b204e9800998ecf8427e/67ea780ce4982c1cfbe6b7293afc765d
        ```

        :param str resource_name: The name of the resource.
        :param AccessPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 decision: Optional[pulumi.Input[str]] = None,
                 excludes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessPolicyExcludeArgs']]]]] = None,
                 includes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessPolicyIncludeArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 precedence: Optional[pulumi.Input[int]] = None,
                 requires: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessPolicyRequireArgs']]]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = AccessPolicyArgs.__new__(AccessPolicyArgs)

            __props__.__dict__["account_id"] = account_id
            if application_id is None and not opts.urn:
                raise TypeError("Missing required property 'application_id'")
            __props__.__dict__["application_id"] = application_id
            if decision is None and not opts.urn:
                raise TypeError("Missing required property 'decision'")
            __props__.__dict__["decision"] = decision
            __props__.__dict__["excludes"] = excludes
            if includes is None and not opts.urn:
                raise TypeError("Missing required property 'includes'")
            __props__.__dict__["includes"] = includes
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if precedence is None and not opts.urn:
                raise TypeError("Missing required property 'precedence'")
            __props__.__dict__["precedence"] = precedence
            __props__.__dict__["requires"] = requires
            __props__.__dict__["zone_id"] = zone_id
        super(AccessPolicy, __self__).__init__(
            'cloudflare:index/accessPolicy:AccessPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            application_id: Optional[pulumi.Input[str]] = None,
            decision: Optional[pulumi.Input[str]] = None,
            excludes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessPolicyExcludeArgs']]]]] = None,
            includes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessPolicyIncludeArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            precedence: Optional[pulumi.Input[int]] = None,
            requires: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessPolicyRequireArgs']]]]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'AccessPolicy':
        """
        Get an existing AccessPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account to which the access rule should be added. Conflicts with `zone_id`.
        :param pulumi.Input[str] application_id: The ID of the application the policy is associated with.
        :param pulumi.Input[str] decision: Defines the action Access will take if the policy matches the user.
               Allowed values: `allow`, `deny`, `non_identity`, `bypass`
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessPolicyExcludeArgs']]]] excludes: A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessPolicyIncludeArgs']]]] includes: A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        :param pulumi.Input[str] name: Friendly name of the Access Application.
        :param pulumi.Input[int] precedence: The unique precedence for policies on a single application. Integer.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessPolicyRequireArgs']]]] requires: A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        :param pulumi.Input[str] zone_id: The DNS zone to which the access rule should be added. Conflicts with `account_id`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccessPolicyState.__new__(_AccessPolicyState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["application_id"] = application_id
        __props__.__dict__["decision"] = decision
        __props__.__dict__["excludes"] = excludes
        __props__.__dict__["includes"] = includes
        __props__.__dict__["name"] = name
        __props__.__dict__["precedence"] = precedence
        __props__.__dict__["requires"] = requires
        __props__.__dict__["zone_id"] = zone_id
        return AccessPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The account to which the access rule should be added. Conflicts with `zone_id`.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        """
        The ID of the application the policy is associated with.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter
    def decision(self) -> pulumi.Output[str]:
        """
        Defines the action Access will take if the policy matches the user.
        Allowed values: `allow`, `deny`, `non_identity`, `bypass`
        """
        return pulumi.get(self, "decision")

    @property
    @pulumi.getter
    def excludes(self) -> pulumi.Output[Optional[Sequence['outputs.AccessPolicyExclude']]]:
        """
        A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        """
        return pulumi.get(self, "excludes")

    @property
    @pulumi.getter
    def includes(self) -> pulumi.Output[Sequence['outputs.AccessPolicyInclude']]:
        """
        A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        """
        return pulumi.get(self, "includes")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Friendly name of the Access Application.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def precedence(self) -> pulumi.Output[int]:
        """
        The unique precedence for policies on a single application. Integer.
        """
        return pulumi.get(self, "precedence")

    @property
    @pulumi.getter
    def requires(self) -> pulumi.Output[Optional[Sequence['outputs.AccessPolicyRequire']]]:
        """
        A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
        """
        return pulumi.get(self, "requires")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The DNS zone to which the access rule should be added. Conflicts with `account_id`.
        """
        return pulumi.get(self, "zone_id")

