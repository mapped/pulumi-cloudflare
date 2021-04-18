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

__all__ = ['RecordArgs', 'Record']

@pulumi.input_type
class RecordArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 type: pulumi.Input[str],
                 zone_id: pulumi.Input[str],
                 data: Optional[pulumi.Input['RecordDataArgs']] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 proxied: Optional[pulumi.Input[bool]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Record resource.
        :param pulumi.Input[str] name: The name of the record
        :param pulumi.Input[str] type: The type of the record
        :param pulumi.Input[str] zone_id: The DNS zone ID to add the record to
        :param pulumi.Input['RecordDataArgs'] data: Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or `value` must be specified
        :param pulumi.Input[int] priority: The priority of the record
        :param pulumi.Input[bool] proxied: Whether the record gets Cloudflare's origin protection; defaults to `false`.
        :param pulumi.Input[int] ttl: The TTL of the record ([automatic: '1'](https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record))
        :param pulumi.Input[str] value: The (string) value of the record. Either this or `data` must be specified
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "zone_id", zone_id)
        if data is not None:
            pulumi.set(__self__, "data", data)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if proxied is not None:
            pulumi.set(__self__, "proxied", proxied)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the record
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of the record
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[str]:
        """
        The DNS zone ID to add the record to
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone_id", value)

    @property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input['RecordDataArgs']]:
        """
        Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or `value` must be specified
        """
        return pulumi.get(self, "data")

    @data.setter
    def data(self, value: Optional[pulumi.Input['RecordDataArgs']]):
        pulumi.set(self, "data", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        The priority of the record
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def proxied(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the record gets Cloudflare's origin protection; defaults to `false`.
        """
        return pulumi.get(self, "proxied")

    @proxied.setter
    def proxied(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "proxied", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[int]]:
        """
        The TTL of the record ([automatic: '1'](https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record))
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ttl", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The (string) value of the record. Either this or `data` must be specified
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class _RecordState:
    def __init__(__self__, *,
                 created_on: Optional[pulumi.Input[str]] = None,
                 data: Optional[pulumi.Input['RecordDataArgs']] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 modified_on: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 proxiable: Optional[pulumi.Input[bool]] = None,
                 proxied: Optional[pulumi.Input[bool]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Record resources.
        :param pulumi.Input[str] created_on: The RFC3339 timestamp of when the record was created
        :param pulumi.Input['RecordDataArgs'] data: Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or `value` must be specified
        :param pulumi.Input[str] hostname: The FQDN of the record
        :param pulumi.Input[Mapping[str, Any]] metadata: A key-value map of string metadata Cloudflare associates with the record
        :param pulumi.Input[str] modified_on: The RFC3339 timestamp of when the record was last modified
        :param pulumi.Input[str] name: The name of the record
        :param pulumi.Input[int] priority: The priority of the record
        :param pulumi.Input[bool] proxiable: Shows whether this record can be proxied, must be true if setting `proxied=true`
        :param pulumi.Input[bool] proxied: Whether the record gets Cloudflare's origin protection; defaults to `false`.
        :param pulumi.Input[int] ttl: The TTL of the record ([automatic: '1'](https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record))
        :param pulumi.Input[str] type: The type of the record
        :param pulumi.Input[str] value: The (string) value of the record. Either this or `data` must be specified
        :param pulumi.Input[str] zone_id: The DNS zone ID to add the record to
        """
        if created_on is not None:
            pulumi.set(__self__, "created_on", created_on)
        if data is not None:
            pulumi.set(__self__, "data", data)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if modified_on is not None:
            pulumi.set(__self__, "modified_on", modified_on)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if proxiable is not None:
            pulumi.set(__self__, "proxiable", proxiable)
        if proxied is not None:
            pulumi.set(__self__, "proxied", proxied)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> Optional[pulumi.Input[str]]:
        """
        The RFC3339 timestamp of when the record was created
        """
        return pulumi.get(self, "created_on")

    @created_on.setter
    def created_on(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_on", value)

    @property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input['RecordDataArgs']]:
        """
        Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or `value` must be specified
        """
        return pulumi.get(self, "data")

    @data.setter
    def data(self, value: Optional[pulumi.Input['RecordDataArgs']]):
        pulumi.set(self, "data", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        """
        The FQDN of the record
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        A key-value map of string metadata Cloudflare associates with the record
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="modifiedOn")
    def modified_on(self) -> Optional[pulumi.Input[str]]:
        """
        The RFC3339 timestamp of when the record was last modified
        """
        return pulumi.get(self, "modified_on")

    @modified_on.setter
    def modified_on(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "modified_on", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the record
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        The priority of the record
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def proxiable(self) -> Optional[pulumi.Input[bool]]:
        """
        Shows whether this record can be proxied, must be true if setting `proxied=true`
        """
        return pulumi.get(self, "proxiable")

    @proxiable.setter
    def proxiable(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "proxiable", value)

    @property
    @pulumi.getter
    def proxied(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the record gets Cloudflare's origin protection; defaults to `false`.
        """
        return pulumi.get(self, "proxied")

    @proxied.setter
    def proxied(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "proxied", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[int]]:
        """
        The TTL of the record ([automatic: '1'](https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record))
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ttl", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the record
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The (string) value of the record. Either this or `data` must be specified
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The DNS zone ID to add the record to
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class Record(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data: Optional[pulumi.Input[pulumi.InputType['RecordDataArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 proxied: Optional[pulumi.Input[bool]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Cloudflare record resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        # Add a record to the domain
        foobar = cloudflare.Record("foobar",
            zone_id=var["cloudflare_zone_id"],
            name="terraform",
            value="192.168.0.11",
            type="A",
            ttl=3600)
        # Add a record requiring a data map
        _sip_tls = cloudflare.Record("_sipTls",
            zone_id=var["cloudflare_zone_id"],
            name="_sip._tls",
            type="SRV",
            data=cloudflare.RecordDataArgs(
                service="_sip",
                proto="_tls",
                name="terraform-srv",
                priority=0,
                weight=0,
                port=443,
                target="example.com",
            ))
        ```

        ## Import

        Records can be imported using a composite ID formed of zone ID and record ID, e.g.

        ```sh
         $ pulumi import cloudflare:index/record:Record default ae36f999674d196762efcc5abb06b345/d41d8cd98f00b204e9800998ecf8427e
        ```

         where* `ae36f999674d196762efcc5abb06b345` - the zone ID * `d41d8cd98f00b204e9800998ecf8427e` - record ID as returned by [API](https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['RecordDataArgs']] data: Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or `value` must be specified
        :param pulumi.Input[str] name: The name of the record
        :param pulumi.Input[int] priority: The priority of the record
        :param pulumi.Input[bool] proxied: Whether the record gets Cloudflare's origin protection; defaults to `false`.
        :param pulumi.Input[int] ttl: The TTL of the record ([automatic: '1'](https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record))
        :param pulumi.Input[str] type: The type of the record
        :param pulumi.Input[str] value: The (string) value of the record. Either this or `data` must be specified
        :param pulumi.Input[str] zone_id: The DNS zone ID to add the record to
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RecordArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloudflare record resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        # Add a record to the domain
        foobar = cloudflare.Record("foobar",
            zone_id=var["cloudflare_zone_id"],
            name="terraform",
            value="192.168.0.11",
            type="A",
            ttl=3600)
        # Add a record requiring a data map
        _sip_tls = cloudflare.Record("_sipTls",
            zone_id=var["cloudflare_zone_id"],
            name="_sip._tls",
            type="SRV",
            data=cloudflare.RecordDataArgs(
                service="_sip",
                proto="_tls",
                name="terraform-srv",
                priority=0,
                weight=0,
                port=443,
                target="example.com",
            ))
        ```

        ## Import

        Records can be imported using a composite ID formed of zone ID and record ID, e.g.

        ```sh
         $ pulumi import cloudflare:index/record:Record default ae36f999674d196762efcc5abb06b345/d41d8cd98f00b204e9800998ecf8427e
        ```

         where* `ae36f999674d196762efcc5abb06b345` - the zone ID * `d41d8cd98f00b204e9800998ecf8427e` - record ID as returned by [API](https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records)

        :param str resource_name: The name of the resource.
        :param RecordArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RecordArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data: Optional[pulumi.Input[pulumi.InputType['RecordDataArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 proxied: Optional[pulumi.Input[bool]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RecordArgs.__new__(RecordArgs)

            __props__.__dict__["data"] = data
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["priority"] = priority
            __props__.__dict__["proxied"] = proxied
            __props__.__dict__["ttl"] = ttl
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["value"] = value
            if zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'zone_id'")
            __props__.__dict__["zone_id"] = zone_id
            __props__.__dict__["created_on"] = None
            __props__.__dict__["hostname"] = None
            __props__.__dict__["metadata"] = None
            __props__.__dict__["modified_on"] = None
            __props__.__dict__["proxiable"] = None
        super(Record, __self__).__init__(
            'cloudflare:index/record:Record',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_on: Optional[pulumi.Input[str]] = None,
            data: Optional[pulumi.Input[pulumi.InputType['RecordDataArgs']]] = None,
            hostname: Optional[pulumi.Input[str]] = None,
            metadata: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            modified_on: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            proxiable: Optional[pulumi.Input[bool]] = None,
            proxied: Optional[pulumi.Input[bool]] = None,
            ttl: Optional[pulumi.Input[int]] = None,
            type: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'Record':
        """
        Get an existing Record resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_on: The RFC3339 timestamp of when the record was created
        :param pulumi.Input[pulumi.InputType['RecordDataArgs']] data: Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or `value` must be specified
        :param pulumi.Input[str] hostname: The FQDN of the record
        :param pulumi.Input[Mapping[str, Any]] metadata: A key-value map of string metadata Cloudflare associates with the record
        :param pulumi.Input[str] modified_on: The RFC3339 timestamp of when the record was last modified
        :param pulumi.Input[str] name: The name of the record
        :param pulumi.Input[int] priority: The priority of the record
        :param pulumi.Input[bool] proxiable: Shows whether this record can be proxied, must be true if setting `proxied=true`
        :param pulumi.Input[bool] proxied: Whether the record gets Cloudflare's origin protection; defaults to `false`.
        :param pulumi.Input[int] ttl: The TTL of the record ([automatic: '1'](https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record))
        :param pulumi.Input[str] type: The type of the record
        :param pulumi.Input[str] value: The (string) value of the record. Either this or `data` must be specified
        :param pulumi.Input[str] zone_id: The DNS zone ID to add the record to
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RecordState.__new__(_RecordState)

        __props__.__dict__["created_on"] = created_on
        __props__.__dict__["data"] = data
        __props__.__dict__["hostname"] = hostname
        __props__.__dict__["metadata"] = metadata
        __props__.__dict__["modified_on"] = modified_on
        __props__.__dict__["name"] = name
        __props__.__dict__["priority"] = priority
        __props__.__dict__["proxiable"] = proxiable
        __props__.__dict__["proxied"] = proxied
        __props__.__dict__["ttl"] = ttl
        __props__.__dict__["type"] = type
        __props__.__dict__["value"] = value
        __props__.__dict__["zone_id"] = zone_id
        return Record(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[str]:
        """
        The RFC3339 timestamp of when the record was created
        """
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter
    def data(self) -> pulumi.Output[Optional['outputs.RecordData']]:
        """
        Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or `value` must be specified
        """
        return pulumi.get(self, "data")

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[str]:
        """
        The FQDN of the record
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        A key-value map of string metadata Cloudflare associates with the record
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter(name="modifiedOn")
    def modified_on(self) -> pulumi.Output[str]:
        """
        The RFC3339 timestamp of when the record was last modified
        """
        return pulumi.get(self, "modified_on")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the record
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        The priority of the record
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def proxiable(self) -> pulumi.Output[bool]:
        """
        Shows whether this record can be proxied, must be true if setting `proxied=true`
        """
        return pulumi.get(self, "proxiable")

    @property
    @pulumi.getter
    def proxied(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the record gets Cloudflare's origin protection; defaults to `false`.
        """
        return pulumi.get(self, "proxied")

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[int]:
        """
        The TTL of the record ([automatic: '1'](https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record))
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the record
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The (string) value of the record. Either this or `data` must be specified
        """
        return pulumi.get(self, "value")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The DNS zone ID to add the record to
        """
        return pulumi.get(self, "zone_id")

