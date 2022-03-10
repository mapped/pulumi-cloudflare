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

__all__ = ['AccessRuleArgs', 'AccessRule']

@pulumi.input_type
class AccessRuleArgs:
    def __init__(__self__, *,
                 configuration: pulumi.Input['AccessRuleConfigurationArgs'],
                 mode: pulumi.Input[str],
                 notes: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AccessRule resource.
        :param pulumi.Input['AccessRuleConfigurationArgs'] configuration: Rule configuration to apply to a matched request. It's a complex value. See description below.
        :param pulumi.Input[str] mode: The action to apply to a matched request. Allowed values: "block", "challenge", "whitelist", "js_challenge", "managed_challenge"
        :param pulumi.Input[str] notes: A personal note about the rule. Typically used as a reminder or explanation for the rule.
        :param pulumi.Input[str] zone_id: The DNS zone to which the access rule should be added.
        """
        pulumi.set(__self__, "configuration", configuration)
        pulumi.set(__self__, "mode", mode)
        if notes is not None:
            pulumi.set(__self__, "notes", notes)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Input['AccessRuleConfigurationArgs']:
        """
        Rule configuration to apply to a matched request. It's a complex value. See description below.
        """
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: pulumi.Input['AccessRuleConfigurationArgs']):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Input[str]:
        """
        The action to apply to a matched request. Allowed values: "block", "challenge", "whitelist", "js_challenge", "managed_challenge"
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[str]]:
        """
        A personal note about the rule. Typically used as a reminder or explanation for the rule.
        """
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The DNS zone to which the access rule should be added.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


@pulumi.input_type
class _AccessRuleState:
    def __init__(__self__, *,
                 configuration: Optional[pulumi.Input['AccessRuleConfigurationArgs']] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AccessRule resources.
        :param pulumi.Input['AccessRuleConfigurationArgs'] configuration: Rule configuration to apply to a matched request. It's a complex value. See description below.
        :param pulumi.Input[str] mode: The action to apply to a matched request. Allowed values: "block", "challenge", "whitelist", "js_challenge", "managed_challenge"
        :param pulumi.Input[str] notes: A personal note about the rule. Typically used as a reminder or explanation for the rule.
        :param pulumi.Input[str] zone_id: The DNS zone to which the access rule should be added.
        """
        if configuration is not None:
            pulumi.set(__self__, "configuration", configuration)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if notes is not None:
            pulumi.set(__self__, "notes", notes)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input['AccessRuleConfigurationArgs']]:
        """
        Rule configuration to apply to a matched request. It's a complex value. See description below.
        """
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input['AccessRuleConfigurationArgs']]):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[str]]:
        """
        The action to apply to a matched request. Allowed values: "block", "challenge", "whitelist", "js_challenge", "managed_challenge"
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[str]]:
        """
        A personal note about the rule. Typically used as a reminder or explanation for the rule.
        """
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The DNS zone to which the access rule should be added.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class AccessRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['AccessRuleConfigurationArgs']]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Cloudflare IP Firewall Access Rule resource. Access control can be applied on basis of IP addresses, IP ranges, AS numbers or countries.

        ## Import

        Records can be imported using a composite ID formed of access rule type, access rule type identifier and identifer value, e.g.

        ```sh
         $ pulumi import cloudflare:index/accessRule:AccessRule default zone/cb029e245cfdd66dc8d2e570d5dd3322/d41d8cd98f00b204e9800998ecf8427e
        ```

         where* `zone` - access rule type (`account`, `zone` or `user`) * `cb029e245cfdd66dc8d2e570d5dd3322` - access rule type ID (i.e the zone ID

         or account ID you wish to target) * `d41d8cd98f00b204e9800998ecf8427e` - access rule ID as returned by

         respective API endpoint for the type you are attempting to import.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AccessRuleConfigurationArgs']] configuration: Rule configuration to apply to a matched request. It's a complex value. See description below.
        :param pulumi.Input[str] mode: The action to apply to a matched request. Allowed values: "block", "challenge", "whitelist", "js_challenge", "managed_challenge"
        :param pulumi.Input[str] notes: A personal note about the rule. Typically used as a reminder or explanation for the rule.
        :param pulumi.Input[str] zone_id: The DNS zone to which the access rule should be added.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloudflare IP Firewall Access Rule resource. Access control can be applied on basis of IP addresses, IP ranges, AS numbers or countries.

        ## Import

        Records can be imported using a composite ID formed of access rule type, access rule type identifier and identifer value, e.g.

        ```sh
         $ pulumi import cloudflare:index/accessRule:AccessRule default zone/cb029e245cfdd66dc8d2e570d5dd3322/d41d8cd98f00b204e9800998ecf8427e
        ```

         where* `zone` - access rule type (`account`, `zone` or `user`) * `cb029e245cfdd66dc8d2e570d5dd3322` - access rule type ID (i.e the zone ID

         or account ID you wish to target) * `d41d8cd98f00b204e9800998ecf8427e` - access rule ID as returned by

         respective API endpoint for the type you are attempting to import.

        :param str resource_name: The name of the resource.
        :param AccessRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['AccessRuleConfigurationArgs']]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
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
            __props__ = AccessRuleArgs.__new__(AccessRuleArgs)

            if configuration is None and not opts.urn:
                raise TypeError("Missing required property 'configuration'")
            __props__.__dict__["configuration"] = configuration
            if mode is None and not opts.urn:
                raise TypeError("Missing required property 'mode'")
            __props__.__dict__["mode"] = mode
            __props__.__dict__["notes"] = notes
            __props__.__dict__["zone_id"] = zone_id
        super(AccessRule, __self__).__init__(
            'cloudflare:index/accessRule:AccessRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            configuration: Optional[pulumi.Input[pulumi.InputType['AccessRuleConfigurationArgs']]] = None,
            mode: Optional[pulumi.Input[str]] = None,
            notes: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'AccessRule':
        """
        Get an existing AccessRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AccessRuleConfigurationArgs']] configuration: Rule configuration to apply to a matched request. It's a complex value. See description below.
        :param pulumi.Input[str] mode: The action to apply to a matched request. Allowed values: "block", "challenge", "whitelist", "js_challenge", "managed_challenge"
        :param pulumi.Input[str] notes: A personal note about the rule. Typically used as a reminder or explanation for the rule.
        :param pulumi.Input[str] zone_id: The DNS zone to which the access rule should be added.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccessRuleState.__new__(_AccessRuleState)

        __props__.__dict__["configuration"] = configuration
        __props__.__dict__["mode"] = mode
        __props__.__dict__["notes"] = notes
        __props__.__dict__["zone_id"] = zone_id
        return AccessRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Output['outputs.AccessRuleConfiguration']:
        """
        Rule configuration to apply to a matched request. It's a complex value. See description below.
        """
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[str]:
        """
        The action to apply to a matched request. Allowed values: "block", "challenge", "whitelist", "js_challenge", "managed_challenge"
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[str]]:
        """
        A personal note about the rule. Typically used as a reminder or explanation for the rule.
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The DNS zone to which the access rule should be added.
        """
        return pulumi.get(self, "zone_id")

