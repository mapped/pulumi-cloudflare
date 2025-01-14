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

__all__ = ['PageRuleArgs', 'PageRule']

@pulumi.input_type
class PageRuleArgs:
    def __init__(__self__, *,
                 actions: pulumi.Input['PageRuleActionsArgs'],
                 target: pulumi.Input[str],
                 zone_id: pulumi.Input[str],
                 priority: Optional[pulumi.Input[int]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PageRule resource.
        :param pulumi.Input['PageRuleActionsArgs'] actions: The actions taken by the page rule, options given below.
        :param pulumi.Input[str] target: The URL pattern to target with the page rule.
        :param pulumi.Input[str] zone_id: The DNS zone ID to which the page rule should be added.
        :param pulumi.Input[int] priority: The priority of the page rule among others for this target, the higher the number the higher the priority as per [API documentation](https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule).
        :param pulumi.Input[str] status: Whether the page rule is active or disabled.
        """
        pulumi.set(__self__, "actions", actions)
        pulumi.set(__self__, "target", target)
        pulumi.set(__self__, "zone_id", zone_id)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Input['PageRuleActionsArgs']:
        """
        The actions taken by the page rule, options given below.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: pulumi.Input['PageRuleActionsArgs']):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def target(self) -> pulumi.Input[str]:
        """
        The URL pattern to target with the page rule.
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: pulumi.Input[str]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[str]:
        """
        The DNS zone ID to which the page rule should be added.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone_id", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        The priority of the page rule among others for this target, the higher the number the higher the priority as per [API documentation](https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule).
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Whether the page rule is active or disabled.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class _PageRuleState:
    def __init__(__self__, *,
                 actions: Optional[pulumi.Input['PageRuleActionsArgs']] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PageRule resources.
        :param pulumi.Input['PageRuleActionsArgs'] actions: The actions taken by the page rule, options given below.
        :param pulumi.Input[int] priority: The priority of the page rule among others for this target, the higher the number the higher the priority as per [API documentation](https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule).
        :param pulumi.Input[str] status: Whether the page rule is active or disabled.
        :param pulumi.Input[str] target: The URL pattern to target with the page rule.
        :param pulumi.Input[str] zone_id: The DNS zone ID to which the page rule should be added.
        """
        if actions is not None:
            pulumi.set(__self__, "actions", actions)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if target is not None:
            pulumi.set(__self__, "target", target)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input['PageRuleActionsArgs']]:
        """
        The actions taken by the page rule, options given below.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: Optional[pulumi.Input['PageRuleActionsArgs']]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        The priority of the page rule among others for this target, the higher the number the higher the priority as per [API documentation](https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule).
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Whether the page rule is active or disabled.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[str]]:
        """
        The URL pattern to target with the page rule.
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The DNS zone ID to which the page rule should be added.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class PageRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[pulumi.InputType['PageRuleActionsArgs']]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Cloudflare page rule resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        # Add a page rule to the domain
        foobar = cloudflare.PageRule("foobar",
            zone_id=var["cloudflare_zone_id"],
            target=f"sub.{var['cloudflare_zone']}/page",
            priority=1,
            actions=cloudflare.PageRuleActionsArgs(
                ssl="flexible",
                email_obfuscation="on",
                minifies=[cloudflare.PageRuleActionsMinifyArgs(
                    html="off",
                    css="on",
                    js="on",
                )],
            ))
        ```

        ## Import

        Page rules can be imported using a composite ID formed of zone ID and page rule ID, e.g.

        ```sh
         $ pulumi import cloudflare:index/pageRule:PageRule default d41d8cd98f00b204e9800998ecf8427e/ch8374ftwdghsif43
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['PageRuleActionsArgs']] actions: The actions taken by the page rule, options given below.
        :param pulumi.Input[int] priority: The priority of the page rule among others for this target, the higher the number the higher the priority as per [API documentation](https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule).
        :param pulumi.Input[str] status: Whether the page rule is active or disabled.
        :param pulumi.Input[str] target: The URL pattern to target with the page rule.
        :param pulumi.Input[str] zone_id: The DNS zone ID to which the page rule should be added.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PageRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloudflare page rule resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        # Add a page rule to the domain
        foobar = cloudflare.PageRule("foobar",
            zone_id=var["cloudflare_zone_id"],
            target=f"sub.{var['cloudflare_zone']}/page",
            priority=1,
            actions=cloudflare.PageRuleActionsArgs(
                ssl="flexible",
                email_obfuscation="on",
                minifies=[cloudflare.PageRuleActionsMinifyArgs(
                    html="off",
                    css="on",
                    js="on",
                )],
            ))
        ```

        ## Import

        Page rules can be imported using a composite ID formed of zone ID and page rule ID, e.g.

        ```sh
         $ pulumi import cloudflare:index/pageRule:PageRule default d41d8cd98f00b204e9800998ecf8427e/ch8374ftwdghsif43
        ```

        :param str resource_name: The name of the resource.
        :param PageRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PageRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[pulumi.InputType['PageRuleActionsArgs']]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
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
            __props__ = PageRuleArgs.__new__(PageRuleArgs)

            if actions is None and not opts.urn:
                raise TypeError("Missing required property 'actions'")
            __props__.__dict__["actions"] = actions
            __props__.__dict__["priority"] = priority
            __props__.__dict__["status"] = status
            if target is None and not opts.urn:
                raise TypeError("Missing required property 'target'")
            __props__.__dict__["target"] = target
            if zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'zone_id'")
            __props__.__dict__["zone_id"] = zone_id
        super(PageRule, __self__).__init__(
            'cloudflare:index/pageRule:PageRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            actions: Optional[pulumi.Input[pulumi.InputType['PageRuleActionsArgs']]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            status: Optional[pulumi.Input[str]] = None,
            target: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'PageRule':
        """
        Get an existing PageRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['PageRuleActionsArgs']] actions: The actions taken by the page rule, options given below.
        :param pulumi.Input[int] priority: The priority of the page rule among others for this target, the higher the number the higher the priority as per [API documentation](https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule).
        :param pulumi.Input[str] status: Whether the page rule is active or disabled.
        :param pulumi.Input[str] target: The URL pattern to target with the page rule.
        :param pulumi.Input[str] zone_id: The DNS zone ID to which the page rule should be added.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PageRuleState.__new__(_PageRuleState)

        __props__.__dict__["actions"] = actions
        __props__.__dict__["priority"] = priority
        __props__.__dict__["status"] = status
        __props__.__dict__["target"] = target
        __props__.__dict__["zone_id"] = zone_id
        return PageRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output['outputs.PageRuleActions']:
        """
        The actions taken by the page rule, options given below.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        The priority of the page rule among others for this target, the higher the number the higher the priority as per [API documentation](https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule).
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Whether the page rule is active or disabled.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def target(self) -> pulumi.Output[str]:
        """
        The URL pattern to target with the page rule.
        """
        return pulumi.get(self, "target")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The DNS zone ID to which the page rule should be added.
        """
        return pulumi.get(self, "zone_id")

