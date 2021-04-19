# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['WorkersKvNamespaceArgs', 'WorkersKvNamespace']

@pulumi.input_type
class WorkersKvNamespaceArgs:
    def __init__(__self__, *,
                 title: pulumi.Input[str]):
        """
        The set of arguments for constructing a WorkersKvNamespace resource.
        :param pulumi.Input[str] title: The name of the namespace you wish to create.
        """
        pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        """
        The name of the namespace you wish to create.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)


@pulumi.input_type
class _WorkersKvNamespaceState:
    def __init__(__self__, *,
                 title: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering WorkersKvNamespace resources.
        :param pulumi.Input[str] title: The name of the namespace you wish to create.
        """
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the namespace you wish to create.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)


class WorkersKvNamespace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Workers KV Namespace

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        example = cloudflare.WorkersKvNamespace("example", title="test-namespace")
        ```

        ## Import

        Workers KV Namespace settings can be imported using it's ID

        ```sh
         $ pulumi import cloudflare:index/workersKvNamespace:WorkersKvNamespace example beaeb6716c9443eaa4deef11763ccca6
        ```

         where- `beaeb6716c9443eaa4deef11763ccca6` is the ID of the namespace

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] title: The name of the namespace you wish to create.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkersKvNamespaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Workers KV Namespace

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        example = cloudflare.WorkersKvNamespace("example", title="test-namespace")
        ```

        ## Import

        Workers KV Namespace settings can be imported using it's ID

        ```sh
         $ pulumi import cloudflare:index/workersKvNamespace:WorkersKvNamespace example beaeb6716c9443eaa4deef11763ccca6
        ```

         where- `beaeb6716c9443eaa4deef11763ccca6` is the ID of the namespace

        :param str resource_name: The name of the resource.
        :param WorkersKvNamespaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkersKvNamespaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 title: Optional[pulumi.Input[str]] = None,
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
            __props__ = WorkersKvNamespaceArgs.__new__(WorkersKvNamespaceArgs)

            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__.__dict__["title"] = title
        super(WorkersKvNamespace, __self__).__init__(
            'cloudflare:index/workersKvNamespace:WorkersKvNamespace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            title: Optional[pulumi.Input[str]] = None) -> 'WorkersKvNamespace':
        """
        Get an existing WorkersKvNamespace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] title: The name of the namespace you wish to create.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WorkersKvNamespaceState.__new__(_WorkersKvNamespaceState)

        __props__.__dict__["title"] = title
        return WorkersKvNamespace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        The name of the namespace you wish to create.
        """
        return pulumi.get(self, "title")

