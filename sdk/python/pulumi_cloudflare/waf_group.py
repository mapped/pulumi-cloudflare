# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['WafGroupArgs', 'WafGroup']

@pulumi.input_type
class WafGroupArgs:
    def __init__(__self__, *,
                 group_id: pulumi.Input[str],
                 zone_id: pulumi.Input[str],
                 mode: Optional[pulumi.Input[str]] = None,
                 package_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WafGroup resource.
        :param pulumi.Input[str] group_id: The WAF Rule Group ID.
        :param pulumi.Input[str] zone_id: The DNS zone ID to apply to.
        :param pulumi.Input[str] mode: The mode of the group, can be one of ["on", "off"].
        :param pulumi.Input[str] package_id: The ID of the WAF Rule Package that contains the group.
        """
        pulumi.set(__self__, "group_id", group_id)
        pulumi.set(__self__, "zone_id", zone_id)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if package_id is not None:
            pulumi.set(__self__, "package_id", package_id)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[str]:
        """
        The WAF Rule Group ID.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[str]:
        """
        The DNS zone ID to apply to.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone_id", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[str]]:
        """
        The mode of the group, can be one of ["on", "off"].
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter(name="packageId")
    def package_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the WAF Rule Package that contains the group.
        """
        return pulumi.get(self, "package_id")

    @package_id.setter
    def package_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "package_id", value)


@pulumi.input_type
class _WafGroupState:
    def __init__(__self__, *,
                 group_id: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 package_id: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering WafGroup resources.
        :param pulumi.Input[str] group_id: The WAF Rule Group ID.
        :param pulumi.Input[str] mode: The mode of the group, can be one of ["on", "off"].
        :param pulumi.Input[str] package_id: The ID of the WAF Rule Package that contains the group.
        :param pulumi.Input[str] zone_id: The DNS zone ID to apply to.
        """
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if package_id is not None:
            pulumi.set(__self__, "package_id", package_id)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The WAF Rule Group ID.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[str]]:
        """
        The mode of the group, can be one of ["on", "off"].
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter(name="packageId")
    def package_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the WAF Rule Package that contains the group.
        """
        return pulumi.get(self, "package_id")

    @package_id.setter
    def package_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "package_id", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The DNS zone ID to apply to.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class WafGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 package_id: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Cloudflare WAF rule group resource for a particular zone. This can be used to configure firewall behaviour for pre-defined firewall groups.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        honey_pot = cloudflare.WafGroup("honeyPot",
            group_id="de677e5818985db1285d0e80225f06e5",
            mode="on",
            zone_id="ae36f999674d196762efcc5abb06b345")
        ```

        ## Import

        WAF Rule Groups can be imported using a composite ID formed of zone ID and the WAF Rule Group ID, e.g.

        ```sh
         $ pulumi import cloudflare:index/wafGroup:WafGroup honey_pot ae36f999674d196762efcc5abb06b345/de677e5818985db1285d0e80225f06e5
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_id: The WAF Rule Group ID.
        :param pulumi.Input[str] mode: The mode of the group, can be one of ["on", "off"].
        :param pulumi.Input[str] package_id: The ID of the WAF Rule Package that contains the group.
        :param pulumi.Input[str] zone_id: The DNS zone ID to apply to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WafGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloudflare WAF rule group resource for a particular zone. This can be used to configure firewall behaviour for pre-defined firewall groups.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        honey_pot = cloudflare.WafGroup("honeyPot",
            group_id="de677e5818985db1285d0e80225f06e5",
            mode="on",
            zone_id="ae36f999674d196762efcc5abb06b345")
        ```

        ## Import

        WAF Rule Groups can be imported using a composite ID formed of zone ID and the WAF Rule Group ID, e.g.

        ```sh
         $ pulumi import cloudflare:index/wafGroup:WafGroup honey_pot ae36f999674d196762efcc5abb06b345/de677e5818985db1285d0e80225f06e5
        ```

        :param str resource_name: The name of the resource.
        :param WafGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WafGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 package_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = WafGroupArgs.__new__(WafGroupArgs)

            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__.__dict__["group_id"] = group_id
            __props__.__dict__["mode"] = mode
            __props__.__dict__["package_id"] = package_id
            if zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'zone_id'")
            __props__.__dict__["zone_id"] = zone_id
        super(WafGroup, __self__).__init__(
            'cloudflare:index/wafGroup:WafGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            group_id: Optional[pulumi.Input[str]] = None,
            mode: Optional[pulumi.Input[str]] = None,
            package_id: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'WafGroup':
        """
        Get an existing WafGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_id: The WAF Rule Group ID.
        :param pulumi.Input[str] mode: The mode of the group, can be one of ["on", "off"].
        :param pulumi.Input[str] package_id: The ID of the WAF Rule Package that contains the group.
        :param pulumi.Input[str] zone_id: The DNS zone ID to apply to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WafGroupState.__new__(_WafGroupState)

        __props__.__dict__["group_id"] = group_id
        __props__.__dict__["mode"] = mode
        __props__.__dict__["package_id"] = package_id
        __props__.__dict__["zone_id"] = zone_id
        return WafGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        """
        The WAF Rule Group ID.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[str]]:
        """
        The mode of the group, can be one of ["on", "off"].
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter(name="packageId")
    def package_id(self) -> pulumi.Output[str]:
        """
        The ID of the WAF Rule Package that contains the group.
        """
        return pulumi.get(self, "package_id")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The DNS zone ID to apply to.
        """
        return pulumi.get(self, "zone_id")

