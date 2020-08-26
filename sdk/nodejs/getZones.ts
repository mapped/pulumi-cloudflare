// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Use this data source to look up [Zone](https://api.cloudflare.com/#zone-properties) records.
 *
 * ## Example Usage
 *
 * Given you have the following zones in Cloudflare.
 *
 * - example.com
 * - example.net
 * - not-example.com
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as cloudflare from "@pulumi/cloudflare";
 *
 * // Look for a single zone that you know exists using an exact match.
 * // API request will be for zones?name=example.com. Will not match not-example.com
 * // or example.net.
 * const example = pulumi.output(cloudflare.getZones({
 *     filter: {
 *         name: "example.com",
 *     },
 * }, { async: true }));
 * ```
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as cloudflare from "@pulumi/cloudflare";
 *
 * // Look for all zones which include "example".
 * // API request will be for zones?name=contains:example. Will return all three
 * // zones.
 * const example = pulumi.output(cloudflare.getZones({
 *     filter: {
 *         lookupType: "contains",
 *         name: "example",
 *     },
 * }, { async: true }));
 * ```
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as cloudflare from "@pulumi/cloudflare";
 *
 * // Look for all zones which include "example" but start with "not-".
 * // API request will be for zones?name=contains:example. Will perform client side
 * // filtering using the provided regex and will only match the single zone,
 * // not-example.com.
 * const example = pulumi.output(cloudflare.getZones({
 *     filter: {
 *         lookupType: "contains",
 *         match: "^not-",
 *         name: "example",
 *     },
 * }, { async: true }));
 * ```
 * ### Example usage with other resources
 *
 * The example below matches all zones which have "example" in their value, end
 * with ".com" and are active. The matched zone is then referenced in the zone
 * lockdown resource.
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as cloudflare from "@pulumi/cloudflare";
 *
 * const test = pulumi.output(cloudflare.getZones({
 *     filter: {
 *         lookupType: "contains",
 *         match: ".com$",
 *         name: "example",
 *         status: "active",
 *     },
 * }, { async: true }));
 * const endpointLockdown = new cloudflare.ZoneLockdown("endpoint_lockdown", {
 *     configurations: [{
 *         target: "ip",
 *         value: "198.51.100.4",
 *     }],
 *     description: "Restrict access to these endpoints to requests from a known IP address",
 *     paused: false,
 *     urls: ["api.mysite.com/some/endpoint*"],
 *     zone: test.apply(test => (<any>test.zones[0])["name"]),
 * });
 * ```
 */
export function getZones(args: GetZonesArgs, opts?: pulumi.InvokeOptions): Promise<GetZonesResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("cloudflare:index/getZones:getZones", {
        "filter": args.filter,
    }, opts);
}

/**
 * A collection of arguments for invoking getZones.
 */
export interface GetZonesArgs {
    /**
     * One or more values used to look up zone records. If more than one value is given all
     * values must match in order to be included, see below for full list.
     */
    readonly filter: inputs.GetZonesFilter;
}

/**
 * A collection of values returned by getZones.
 */
export interface GetZonesResult {
    readonly filter: outputs.GetZonesFilter;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * A map of zone details. Full list below:
     */
    readonly zones: outputs.GetZonesZone[];
}
