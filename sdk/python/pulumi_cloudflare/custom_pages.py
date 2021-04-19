# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CustomPagesArgs', 'CustomPages']

@pulumi.input_type
class CustomPagesArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 url: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CustomPages resource.
        :param pulumi.Input[str] type: The type of custom page you wish to update. Must
               be one of `basic_challenge`, `waf_challenge`, `waf_block`,
               `ratelimit_block`, `country_challenge`, `ip_block`, `under_attack`,
               `500_errors`, `1000_errors`, `always_online`.
        :param pulumi.Input[str] url: URL of where the custom page source is located.
        :param pulumi.Input[str] account_id: The account ID where the custom pages should be
               updated. Either `account_id` or `zone_id` must be provided. If
               `account_id` is present, it will override the zone setting.
        :param pulumi.Input[str] zone_id: The zone ID where the custom pages should be
               updated. Either `zone_id` or `account_id` must be provided.
        """
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "url", url)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of custom page you wish to update. Must
        be one of `basic_challenge`, `waf_challenge`, `waf_block`,
        `ratelimit_block`, `country_challenge`, `ip_block`, `under_attack`,
        `500_errors`, `1000_errors`, `always_online`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        URL of where the custom page source is located.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account ID where the custom pages should be
        updated. Either `account_id` or `zone_id` must be provided. If
        `account_id` is present, it will override the zone setting.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The zone ID where the custom pages should be
        updated. Either `zone_id` or `account_id` must be provided.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


@pulumi.input_type
class _CustomPagesState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CustomPages resources.
        :param pulumi.Input[str] account_id: The account ID where the custom pages should be
               updated. Either `account_id` or `zone_id` must be provided. If
               `account_id` is present, it will override the zone setting.
        :param pulumi.Input[str] type: The type of custom page you wish to update. Must
               be one of `basic_challenge`, `waf_challenge`, `waf_block`,
               `ratelimit_block`, `country_challenge`, `ip_block`, `under_attack`,
               `500_errors`, `1000_errors`, `always_online`.
        :param pulumi.Input[str] url: URL of where the custom page source is located.
        :param pulumi.Input[str] zone_id: The zone ID where the custom pages should be
               updated. Either `zone_id` or `account_id` must be provided.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if url is not None:
            pulumi.set(__self__, "url", url)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account ID where the custom pages should be
        updated. Either `account_id` or `zone_id` must be provided. If
        `account_id` is present, it will override the zone setting.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of custom page you wish to update. Must
        be one of `basic_challenge`, `waf_challenge`, `waf_block`,
        `ratelimit_block`, `country_challenge`, `ip_block`, `under_attack`,
        `500_errors`, `1000_errors`, `always_online`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        URL of where the custom page source is located.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The zone ID where the custom pages should be
        updated. Either `zone_id` or `account_id` must be provided.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class CustomPages(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a resource which manages Cloudflare custom error pages.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        basic_challenge = cloudflare.CustomPages("basicChallenge",
            state="customized",
            type="basic_challenge",
            url="https://example.com/challenge.html",
            zone_id="d41d8cd98f00b204e9800998ecf8427e")
        ```

        ## Import

        Custom pages can be imported using a composite ID formed of* `customPageLevel` - Either `account` or `zone`. * `identifier` - The ID of the account or zone you intend to manage. * `pageType` - The value from the `type` argument. Example for a zone

        ```sh
         $ pulumi import cloudflare:index/customPages:CustomPages basic_challenge zone/d41d8cd98f00b204e9800998ecf8427e/basic_challenge
        ```

         Example for an account

        ```sh
         $ pulumi import cloudflare:index/customPages:CustomPages basic_challenge account/e268443e43d93dab7ebef303bbe9642f/basic_challenge
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account ID where the custom pages should be
               updated. Either `account_id` or `zone_id` must be provided. If
               `account_id` is present, it will override the zone setting.
        :param pulumi.Input[str] type: The type of custom page you wish to update. Must
               be one of `basic_challenge`, `waf_challenge`, `waf_block`,
               `ratelimit_block`, `country_challenge`, `ip_block`, `under_attack`,
               `500_errors`, `1000_errors`, `always_online`.
        :param pulumi.Input[str] url: URL of where the custom page source is located.
        :param pulumi.Input[str] zone_id: The zone ID where the custom pages should be
               updated. Either `zone_id` or `account_id` must be provided.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomPagesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource which manages Cloudflare custom error pages.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        basic_challenge = cloudflare.CustomPages("basicChallenge",
            state="customized",
            type="basic_challenge",
            url="https://example.com/challenge.html",
            zone_id="d41d8cd98f00b204e9800998ecf8427e")
        ```

        ## Import

        Custom pages can be imported using a composite ID formed of* `customPageLevel` - Either `account` or `zone`. * `identifier` - The ID of the account or zone you intend to manage. * `pageType` - The value from the `type` argument. Example for a zone

        ```sh
         $ pulumi import cloudflare:index/customPages:CustomPages basic_challenge zone/d41d8cd98f00b204e9800998ecf8427e/basic_challenge
        ```

         Example for an account

        ```sh
         $ pulumi import cloudflare:index/customPages:CustomPages basic_challenge account/e268443e43d93dab7ebef303bbe9642f/basic_challenge
        ```

        :param str resource_name: The name of the resource.
        :param CustomPagesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomPagesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
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
            __props__ = CustomPagesArgs.__new__(CustomPagesArgs)

            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["state"] = state
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
            __props__.__dict__["zone_id"] = zone_id
        super(CustomPages, __self__).__init__(
            'cloudflare:index/customPages:CustomPages',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'CustomPages':
        """
        Get an existing CustomPages resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account ID where the custom pages should be
               updated. Either `account_id` or `zone_id` must be provided. If
               `account_id` is present, it will override the zone setting.
        :param pulumi.Input[str] type: The type of custom page you wish to update. Must
               be one of `basic_challenge`, `waf_challenge`, `waf_block`,
               `ratelimit_block`, `country_challenge`, `ip_block`, `under_attack`,
               `500_errors`, `1000_errors`, `always_online`.
        :param pulumi.Input[str] url: URL of where the custom page source is located.
        :param pulumi.Input[str] zone_id: The zone ID where the custom pages should be
               updated. Either `zone_id` or `account_id` must be provided.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CustomPagesState.__new__(_CustomPagesState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["state"] = state
        __props__.__dict__["type"] = type
        __props__.__dict__["url"] = url
        __props__.__dict__["zone_id"] = zone_id
        return CustomPages(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[Optional[str]]:
        """
        The account ID where the custom pages should be
        updated. Either `account_id` or `zone_id` must be provided. If
        `account_id` is present, it will override the zone setting.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of custom page you wish to update. Must
        be one of `basic_challenge`, `waf_challenge`, `waf_block`,
        `ratelimit_block`, `country_challenge`, `ip_block`, `under_attack`,
        `500_errors`, `1000_errors`, `always_online`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        URL of where the custom page source is located.
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[Optional[str]]:
        """
        The zone ID where the custom pages should be
        updated. Either `zone_id` or `account_id` must be provided.
        """
        return pulumi.get(self, "zone_id")

