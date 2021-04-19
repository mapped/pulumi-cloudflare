# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['FirewallRuleArgs', 'FirewallRule']

@pulumi.input_type
class FirewallRuleArgs:
    def __init__(__self__, *,
                 action: pulumi.Input[str],
                 filter_id: pulumi.Input[str],
                 zone_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 paused: Optional[pulumi.Input[bool]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 products: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a FirewallRule resource.
        :param pulumi.Input[str] action: The action to apply to a matched request. Allowed values: "block", "challenge", "allow", "js_challenge", "bypass". Enterprise plan also allows "log".
        :param pulumi.Input[str] zone_id: The DNS zone to which the Filter should be added.
        :param pulumi.Input[str] description: A description of the rule to help identify it.
        :param pulumi.Input[bool] paused: Whether this filter based firewall rule is currently paused. Boolean value.
        :param pulumi.Input[int] priority: The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] products: List of products to bypass for a request when the bypass action is used. Allowed values: "zoneLockdown", "uaBlock", "bic", "hot", "securityLevel", "rateLimit", "waf".
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "filter_id", filter_id)
        pulumi.set(__self__, "zone_id", zone_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if paused is not None:
            pulumi.set(__self__, "paused", paused)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if products is not None:
            pulumi.set(__self__, "products", products)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input[str]:
        """
        The action to apply to a matched request. Allowed values: "block", "challenge", "allow", "js_challenge", "bypass". Enterprise plan also allows "log".
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input[str]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="filterId")
    def filter_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "filter_id")

    @filter_id.setter
    def filter_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "filter_id", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[str]:
        """
        The DNS zone to which the Filter should be added.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the rule to help identify it.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def paused(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this filter based firewall rule is currently paused. Boolean value.
        """
        return pulumi.get(self, "paused")

    @paused.setter
    def paused(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "paused", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def products(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of products to bypass for a request when the bypass action is used. Allowed values: "zoneLockdown", "uaBlock", "bic", "hot", "securityLevel", "rateLimit", "waf".
        """
        return pulumi.get(self, "products")

    @products.setter
    def products(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "products", value)


@pulumi.input_type
class _FirewallRuleState:
    def __init__(__self__, *,
                 action: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 filter_id: Optional[pulumi.Input[str]] = None,
                 paused: Optional[pulumi.Input[bool]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 products: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FirewallRule resources.
        :param pulumi.Input[str] action: The action to apply to a matched request. Allowed values: "block", "challenge", "allow", "js_challenge", "bypass". Enterprise plan also allows "log".
        :param pulumi.Input[str] description: A description of the rule to help identify it.
        :param pulumi.Input[bool] paused: Whether this filter based firewall rule is currently paused. Boolean value.
        :param pulumi.Input[int] priority: The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] products: List of products to bypass for a request when the bypass action is used. Allowed values: "zoneLockdown", "uaBlock", "bic", "hot", "securityLevel", "rateLimit", "waf".
        :param pulumi.Input[str] zone_id: The DNS zone to which the Filter should be added.
        """
        if action is not None:
            pulumi.set(__self__, "action", action)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if filter_id is not None:
            pulumi.set(__self__, "filter_id", filter_id)
        if paused is not None:
            pulumi.set(__self__, "paused", paused)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if products is not None:
            pulumi.set(__self__, "products", products)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[str]]:
        """
        The action to apply to a matched request. Allowed values: "block", "challenge", "allow", "js_challenge", "bypass". Enterprise plan also allows "log".
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the rule to help identify it.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="filterId")
    def filter_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "filter_id")

    @filter_id.setter
    def filter_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter_id", value)

    @property
    @pulumi.getter
    def paused(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this filter based firewall rule is currently paused. Boolean value.
        """
        return pulumi.get(self, "paused")

    @paused.setter
    def paused(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "paused", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def products(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of products to bypass for a request when the bypass action is used. Allowed values: "zoneLockdown", "uaBlock", "bic", "hot", "securityLevel", "rateLimit", "waf".
        """
        return pulumi.get(self, "products")

    @products.setter
    def products(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "products", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The DNS zone to which the Filter should be added.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class FirewallRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 filter_id: Optional[pulumi.Input[str]] = None,
                 paused: Optional[pulumi.Input[bool]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 products: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Define Firewall rules using filter expressions for more control over how traffic is matched to the rule.
        A filter expression permits selecting traffic by multiple criteria allowing greater freedom in rule creation.

        Filter expressions needs to be created first before using Firewall Rule. See Filter.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        wordpress_filter = cloudflare.Filter("wordpressFilter",
            zone_id="d41d8cd98f00b204e9800998ecf8427e",
            description="Wordpress break-in attempts that are outside of the office",
            expression="(http.request.uri.path ~ \".*wp-login.php\" or http.request.uri.path ~ \".*xmlrpc.php\") and ip.src ne 192.0.2.1")
        wordpress_firewall_rule = cloudflare.FirewallRule("wordpressFirewallRule",
            zone_id="d41d8cd98f00b204e9800998ecf8427e",
            description="Block wordpress break-in attempts",
            filter_id=wordpress_filter.id,
            action="block")
        ```

        ## Import

        Firewall Rule can be imported using a composite ID formed of zone ID and rule ID, e.g.

        ```sh
         $ pulumi import cloudflare:index/firewallRule:FirewallRule default d41d8cd98f00b204e9800998ecf8427e/9e107d9d372bb6826bd81d3542a419d6
        ```

         where* `d41d8cd98f00b204e9800998ecf8427e` - zone ID * `9e107d9d372bb6826bd81d3542a419d6` - rule ID as returned by [API](https://api.cloudflare.com/#zone-firewall-filter-rules)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: The action to apply to a matched request. Allowed values: "block", "challenge", "allow", "js_challenge", "bypass". Enterprise plan also allows "log".
        :param pulumi.Input[str] description: A description of the rule to help identify it.
        :param pulumi.Input[bool] paused: Whether this filter based firewall rule is currently paused. Boolean value.
        :param pulumi.Input[int] priority: The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] products: List of products to bypass for a request when the bypass action is used. Allowed values: "zoneLockdown", "uaBlock", "bic", "hot", "securityLevel", "rateLimit", "waf".
        :param pulumi.Input[str] zone_id: The DNS zone to which the Filter should be added.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FirewallRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Define Firewall rules using filter expressions for more control over how traffic is matched to the rule.
        A filter expression permits selecting traffic by multiple criteria allowing greater freedom in rule creation.

        Filter expressions needs to be created first before using Firewall Rule. See Filter.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        wordpress_filter = cloudflare.Filter("wordpressFilter",
            zone_id="d41d8cd98f00b204e9800998ecf8427e",
            description="Wordpress break-in attempts that are outside of the office",
            expression="(http.request.uri.path ~ \".*wp-login.php\" or http.request.uri.path ~ \".*xmlrpc.php\") and ip.src ne 192.0.2.1")
        wordpress_firewall_rule = cloudflare.FirewallRule("wordpressFirewallRule",
            zone_id="d41d8cd98f00b204e9800998ecf8427e",
            description="Block wordpress break-in attempts",
            filter_id=wordpress_filter.id,
            action="block")
        ```

        ## Import

        Firewall Rule can be imported using a composite ID formed of zone ID and rule ID, e.g.

        ```sh
         $ pulumi import cloudflare:index/firewallRule:FirewallRule default d41d8cd98f00b204e9800998ecf8427e/9e107d9d372bb6826bd81d3542a419d6
        ```

         where* `d41d8cd98f00b204e9800998ecf8427e` - zone ID * `9e107d9d372bb6826bd81d3542a419d6` - rule ID as returned by [API](https://api.cloudflare.com/#zone-firewall-filter-rules)

        :param str resource_name: The name of the resource.
        :param FirewallRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 filter_id: Optional[pulumi.Input[str]] = None,
                 paused: Optional[pulumi.Input[bool]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 products: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = FirewallRuleArgs.__new__(FirewallRuleArgs)

            if action is None and not opts.urn:
                raise TypeError("Missing required property 'action'")
            __props__.__dict__["action"] = action
            __props__.__dict__["description"] = description
            if filter_id is None and not opts.urn:
                raise TypeError("Missing required property 'filter_id'")
            __props__.__dict__["filter_id"] = filter_id
            __props__.__dict__["paused"] = paused
            __props__.__dict__["priority"] = priority
            __props__.__dict__["products"] = products
            if zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'zone_id'")
            __props__.__dict__["zone_id"] = zone_id
        super(FirewallRule, __self__).__init__(
            'cloudflare:index/firewallRule:FirewallRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            filter_id: Optional[pulumi.Input[str]] = None,
            paused: Optional[pulumi.Input[bool]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            products: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'FirewallRule':
        """
        Get an existing FirewallRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: The action to apply to a matched request. Allowed values: "block", "challenge", "allow", "js_challenge", "bypass". Enterprise plan also allows "log".
        :param pulumi.Input[str] description: A description of the rule to help identify it.
        :param pulumi.Input[bool] paused: Whether this filter based firewall rule is currently paused. Boolean value.
        :param pulumi.Input[int] priority: The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] products: List of products to bypass for a request when the bypass action is used. Allowed values: "zoneLockdown", "uaBlock", "bic", "hot", "securityLevel", "rateLimit", "waf".
        :param pulumi.Input[str] zone_id: The DNS zone to which the Filter should be added.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FirewallRuleState.__new__(_FirewallRuleState)

        __props__.__dict__["action"] = action
        __props__.__dict__["description"] = description
        __props__.__dict__["filter_id"] = filter_id
        __props__.__dict__["paused"] = paused
        __props__.__dict__["priority"] = priority
        __props__.__dict__["products"] = products
        __props__.__dict__["zone_id"] = zone_id
        return FirewallRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output[str]:
        """
        The action to apply to a matched request. Allowed values: "block", "challenge", "allow", "js_challenge", "bypass". Enterprise plan also allows "log".
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the rule to help identify it.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="filterId")
    def filter_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "filter_id")

    @property
    @pulumi.getter
    def paused(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether this filter based firewall rule is currently paused. Boolean value.
        """
        return pulumi.get(self, "paused")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def products(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of products to bypass for a request when the bypass action is used. Allowed values: "zoneLockdown", "uaBlock", "bic", "hot", "securityLevel", "rateLimit", "waf".
        """
        return pulumi.get(self, "products")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The DNS zone to which the Filter should be added.
        """
        return pulumi.get(self, "zone_id")

