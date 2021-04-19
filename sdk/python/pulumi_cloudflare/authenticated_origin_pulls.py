# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AuthenticatedOriginPullsArgs', 'AuthenticatedOriginPulls']

@pulumi.input_type
class AuthenticatedOriginPullsArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 zone_id: pulumi.Input[str],
                 authenticated_origin_pulls_certificate: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AuthenticatedOriginPulls resource.
        :param pulumi.Input[bool] enabled: Whether or not to enable Authenticated Origin Pulls on the given zone or hostname.
        :param pulumi.Input[str] zone_id: The zone ID to upload the certificate to.
        :param pulumi.Input[str] authenticated_origin_pulls_certificate: The id of an uploaded Authenticated Origin Pulls certificate. If no hostname is provided, this certificate will be used zone wide as Per-Zone Authenticated Origin Pulls.
        :param pulumi.Input[str] hostname: Specify a hostname to enable Per-Hostname Authenticated Origin Pulls on, using the provided certificate.
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "zone_id", zone_id)
        if authenticated_origin_pulls_certificate is not None:
            pulumi.set(__self__, "authenticated_origin_pulls_certificate", authenticated_origin_pulls_certificate)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Whether or not to enable Authenticated Origin Pulls on the given zone or hostname.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[str]:
        """
        The zone ID to upload the certificate to.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone_id", value)

    @property
    @pulumi.getter(name="authenticatedOriginPullsCertificate")
    def authenticated_origin_pulls_certificate(self) -> Optional[pulumi.Input[str]]:
        """
        The id of an uploaded Authenticated Origin Pulls certificate. If no hostname is provided, this certificate will be used zone wide as Per-Zone Authenticated Origin Pulls.
        """
        return pulumi.get(self, "authenticated_origin_pulls_certificate")

    @authenticated_origin_pulls_certificate.setter
    def authenticated_origin_pulls_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authenticated_origin_pulls_certificate", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        """
        Specify a hostname to enable Per-Hostname Authenticated Origin Pulls on, using the provided certificate.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)


@pulumi.input_type
class _AuthenticatedOriginPullsState:
    def __init__(__self__, *,
                 authenticated_origin_pulls_certificate: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AuthenticatedOriginPulls resources.
        :param pulumi.Input[str] authenticated_origin_pulls_certificate: The id of an uploaded Authenticated Origin Pulls certificate. If no hostname is provided, this certificate will be used zone wide as Per-Zone Authenticated Origin Pulls.
        :param pulumi.Input[bool] enabled: Whether or not to enable Authenticated Origin Pulls on the given zone or hostname.
        :param pulumi.Input[str] hostname: Specify a hostname to enable Per-Hostname Authenticated Origin Pulls on, using the provided certificate.
        :param pulumi.Input[str] zone_id: The zone ID to upload the certificate to.
        """
        if authenticated_origin_pulls_certificate is not None:
            pulumi.set(__self__, "authenticated_origin_pulls_certificate", authenticated_origin_pulls_certificate)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="authenticatedOriginPullsCertificate")
    def authenticated_origin_pulls_certificate(self) -> Optional[pulumi.Input[str]]:
        """
        The id of an uploaded Authenticated Origin Pulls certificate. If no hostname is provided, this certificate will be used zone wide as Per-Zone Authenticated Origin Pulls.
        """
        return pulumi.get(self, "authenticated_origin_pulls_certificate")

    @authenticated_origin_pulls_certificate.setter
    def authenticated_origin_pulls_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authenticated_origin_pulls_certificate", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not to enable Authenticated Origin Pulls on the given zone or hostname.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        """
        Specify a hostname to enable Per-Hostname Authenticated Origin Pulls on, using the provided certificate.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The zone ID to upload the certificate to.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class AuthenticatedOriginPulls(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authenticated_origin_pulls_certificate: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Cloudflare Authenticated Origin Pulls resource. An `AuthenticatedOriginPulls` resource is required to use Per-Zone or Per-Hostname Authenticated Origin Pulls.

        ## Example Usage

        The arguments that you provide determine which form of Authenticated Origin Pulls to use:

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        # Authenticated Origin Pulls
        my_aop = cloudflare.AuthenticatedOriginPulls("myAop",
            zone_id=var["cloudflare_zone_id"],
            enabled=True)
        # Per-Zone Authenticated Origin Pulls
        my_per_zone_aop_cert = cloudflare.AuthenticatedOriginPullsCertificate("myPerZoneAopCert",
            zone_id=var["cloudflare_zone_id"],
            certificate="-----INSERT CERTIFICATE-----",
            private_key="-----INSERT PRIVATE KEY-----",
            type="per-zone")
        my_per_zone_aop = cloudflare.AuthenticatedOriginPulls("myPerZoneAop",
            zone_id=var["cloudflare_zone_id"],
            authenticated_origin_pulls_certificate=my_per_zone_aop_cert.id,
            enabled=True)
        # Per-Hostname Authenticated Origin Pulls
        my_per_hostname_aop_cert = cloudflare.AuthenticatedOriginPullsCertificate("myPerHostnameAopCert",
            zone_id=var["cloudflare_zone_id"],
            certificate="-----INSERT CERTIFICATE-----",
            private_key="-----INSERT PRIVATE KEY-----",
            type="per-hostname")
        my_per_hostname_aop = cloudflare.AuthenticatedOriginPulls("myPerHostnameAop",
            zone_id=var["cloudflare_zone_id"],
            authenticated_origin_pulls_certificate=my_per_hostname_aop_cert.id,
            hostname="aop.example.com",
            enabled=True)
        ```

        ## Import

        Authenticated Origin Pull configuration can be imported using a composite ID formed of the zone ID, the form of Authenticated Origin Pulls, and the certificate ID, with each section filled or left blank e.g. # Import Authenticated Origin Pull configuration

        ```sh
         $ pulumi import cloudflare:index/authenticatedOriginPulls:AuthenticatedOriginPulls my_aop 023e105f4ecef8ad9ca31a8372d0c353//
        ```

        # Import Per-Zone Authenticated Origin Pull configuration

        ```sh
         $ pulumi import cloudflare:index/authenticatedOriginPulls:AuthenticatedOriginPulls my_per_zone_aop 023e105f4ecef8ad9ca31a8372d0c353/2458ce5a-0c35-4c7f-82c7-8e9487d3ff60/
        ```

        # Import Per-Hostname Authenticated Origin Pull configuration

        ```sh
         $ pulumi import cloudflare:index/authenticatedOriginPulls:AuthenticatedOriginPulls my_per_hostname_aop 023e105f4ecef8ad9ca31a8372d0c353/2458ce5a-0c35-4c7f-82c7-8e9487d3ff60/aop.example.com
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authenticated_origin_pulls_certificate: The id of an uploaded Authenticated Origin Pulls certificate. If no hostname is provided, this certificate will be used zone wide as Per-Zone Authenticated Origin Pulls.
        :param pulumi.Input[bool] enabled: Whether or not to enable Authenticated Origin Pulls on the given zone or hostname.
        :param pulumi.Input[str] hostname: Specify a hostname to enable Per-Hostname Authenticated Origin Pulls on, using the provided certificate.
        :param pulumi.Input[str] zone_id: The zone ID to upload the certificate to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AuthenticatedOriginPullsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloudflare Authenticated Origin Pulls resource. An `AuthenticatedOriginPulls` resource is required to use Per-Zone or Per-Hostname Authenticated Origin Pulls.

        ## Example Usage

        The arguments that you provide determine which form of Authenticated Origin Pulls to use:

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        # Authenticated Origin Pulls
        my_aop = cloudflare.AuthenticatedOriginPulls("myAop",
            zone_id=var["cloudflare_zone_id"],
            enabled=True)
        # Per-Zone Authenticated Origin Pulls
        my_per_zone_aop_cert = cloudflare.AuthenticatedOriginPullsCertificate("myPerZoneAopCert",
            zone_id=var["cloudflare_zone_id"],
            certificate="-----INSERT CERTIFICATE-----",
            private_key="-----INSERT PRIVATE KEY-----",
            type="per-zone")
        my_per_zone_aop = cloudflare.AuthenticatedOriginPulls("myPerZoneAop",
            zone_id=var["cloudflare_zone_id"],
            authenticated_origin_pulls_certificate=my_per_zone_aop_cert.id,
            enabled=True)
        # Per-Hostname Authenticated Origin Pulls
        my_per_hostname_aop_cert = cloudflare.AuthenticatedOriginPullsCertificate("myPerHostnameAopCert",
            zone_id=var["cloudflare_zone_id"],
            certificate="-----INSERT CERTIFICATE-----",
            private_key="-----INSERT PRIVATE KEY-----",
            type="per-hostname")
        my_per_hostname_aop = cloudflare.AuthenticatedOriginPulls("myPerHostnameAop",
            zone_id=var["cloudflare_zone_id"],
            authenticated_origin_pulls_certificate=my_per_hostname_aop_cert.id,
            hostname="aop.example.com",
            enabled=True)
        ```

        ## Import

        Authenticated Origin Pull configuration can be imported using a composite ID formed of the zone ID, the form of Authenticated Origin Pulls, and the certificate ID, with each section filled or left blank e.g. # Import Authenticated Origin Pull configuration

        ```sh
         $ pulumi import cloudflare:index/authenticatedOriginPulls:AuthenticatedOriginPulls my_aop 023e105f4ecef8ad9ca31a8372d0c353//
        ```

        # Import Per-Zone Authenticated Origin Pull configuration

        ```sh
         $ pulumi import cloudflare:index/authenticatedOriginPulls:AuthenticatedOriginPulls my_per_zone_aop 023e105f4ecef8ad9ca31a8372d0c353/2458ce5a-0c35-4c7f-82c7-8e9487d3ff60/
        ```

        # Import Per-Hostname Authenticated Origin Pull configuration

        ```sh
         $ pulumi import cloudflare:index/authenticatedOriginPulls:AuthenticatedOriginPulls my_per_hostname_aop 023e105f4ecef8ad9ca31a8372d0c353/2458ce5a-0c35-4c7f-82c7-8e9487d3ff60/aop.example.com
        ```

        :param str resource_name: The name of the resource.
        :param AuthenticatedOriginPullsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AuthenticatedOriginPullsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authenticated_origin_pulls_certificate: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
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
            __props__ = AuthenticatedOriginPullsArgs.__new__(AuthenticatedOriginPullsArgs)

            __props__.__dict__["authenticated_origin_pulls_certificate"] = authenticated_origin_pulls_certificate
            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["hostname"] = hostname
            if zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'zone_id'")
            __props__.__dict__["zone_id"] = zone_id
        super(AuthenticatedOriginPulls, __self__).__init__(
            'cloudflare:index/authenticatedOriginPulls:AuthenticatedOriginPulls',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authenticated_origin_pulls_certificate: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            hostname: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'AuthenticatedOriginPulls':
        """
        Get an existing AuthenticatedOriginPulls resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authenticated_origin_pulls_certificate: The id of an uploaded Authenticated Origin Pulls certificate. If no hostname is provided, this certificate will be used zone wide as Per-Zone Authenticated Origin Pulls.
        :param pulumi.Input[bool] enabled: Whether or not to enable Authenticated Origin Pulls on the given zone or hostname.
        :param pulumi.Input[str] hostname: Specify a hostname to enable Per-Hostname Authenticated Origin Pulls on, using the provided certificate.
        :param pulumi.Input[str] zone_id: The zone ID to upload the certificate to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AuthenticatedOriginPullsState.__new__(_AuthenticatedOriginPullsState)

        __props__.__dict__["authenticated_origin_pulls_certificate"] = authenticated_origin_pulls_certificate
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["hostname"] = hostname
        __props__.__dict__["zone_id"] = zone_id
        return AuthenticatedOriginPulls(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authenticatedOriginPullsCertificate")
    def authenticated_origin_pulls_certificate(self) -> pulumi.Output[Optional[str]]:
        """
        The id of an uploaded Authenticated Origin Pulls certificate. If no hostname is provided, this certificate will be used zone wide as Per-Zone Authenticated Origin Pulls.
        """
        return pulumi.get(self, "authenticated_origin_pulls_certificate")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        Whether or not to enable Authenticated Origin Pulls on the given zone or hostname.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[Optional[str]]:
        """
        Specify a hostname to enable Per-Hostname Authenticated Origin Pulls on, using the provided certificate.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The zone ID to upload the certificate to.
        """
        return pulumi.get(self, "zone_id")

