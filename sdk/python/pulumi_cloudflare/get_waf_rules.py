# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetWafRulesResult:
    """
    A collection of values returned by getWafRules.
    """
    def __init__(__self__, filter=None, id=None, package_id=None, rules=None, zone_id=None):
        if filter and not isinstance(filter, dict):
            raise TypeError("Expected argument 'filter' to be a dict")
        __self__.filter = filter
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if package_id and not isinstance(package_id, str):
            raise TypeError("Expected argument 'package_id' to be a str")
        __self__.package_id = package_id
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        __self__.rules = rules
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        __self__.zone_id = zone_id
class AwaitableGetWafRulesResult(GetWafRulesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWafRulesResult(
            filter=self.filter,
            id=self.id,
            package_id=self.package_id,
            rules=self.rules,
            zone_id=self.zone_id)

def get_waf_rules(filter=None,package_id=None,zone_id=None,opts=None):
    """
    Use this data source to look up [WAF Rules](https://api.cloudflare.com/#waf-rule-groups-properties).

    ## Example Usage



    ```python
    import pulumi
    import pulumi_cloudflare as cloudflare

    test = cloudflare.get_waf_rules(zone_id="ae36f999674d196762efcc5abb06b345",
        package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        filter={
            "description": ".*example.*",
            "mode": "on",
            "groupId": "de677e5818985db1285d0e80225f06e5",
        })
    pulumi.export("wafRules", test.rules)
    ```




    The **filter** object supports the following:

      * `description` (`str`)
      * `group_id` (`str`)
      * `mode` (`str`)
    """
    __args__ = dict()


    __args__['filter'] = filter
    __args__['packageId'] = package_id
    __args__['zoneId'] = zone_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getWafRules:getWafRules', __args__, opts=opts).value

    return AwaitableGetWafRulesResult(
        filter=__ret__.get('filter'),
        id=__ret__.get('id'),
        package_id=__ret__.get('packageId'),
        rules=__ret__.get('rules'),
        zone_id=__ret__.get('zoneId'))
