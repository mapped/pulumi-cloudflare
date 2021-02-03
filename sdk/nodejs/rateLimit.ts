// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Provides a Cloudflare rate limit resource for a given zone. This can be used to limit the traffic you receive zone-wide, or matching more specific types of requests/responses.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as cloudflare from "@pulumi/cloudflare";
 *
 * const example = new cloudflare.RateLimit("example", {
 *     zoneId: _var.cloudflare_zone_id,
 *     threshold: 2000,
 *     period: 2,
 *     match: {
 *         request: {
 *             urlPattern: `${_var.cloudflare_zone}/*`,
 *             schemes: [
 *                 "HTTP",
 *                 "HTTPS",
 *             ],
 *             methods: [
 *                 "GET",
 *                 "POST",
 *                 "PUT",
 *                 "DELETE",
 *                 "PATCH",
 *                 "HEAD",
 *             ],
 *         },
 *         response: {
 *             statuses: [
 *                 200,
 *                 201,
 *                 202,
 *                 301,
 *                 429,
 *             ],
 *             originTraffic: false,
 *             headers: [
 *                 {
 *                     name: "Host",
 *                     op: "eq",
 *                     value: "localhost",
 *                 },
 *                 {
 *                     name: "X-Example",
 *                     op: "ne",
 *                     value: "my-example",
 *                 },
 *             ],
 *         },
 *     },
 *     action: {
 *         mode: "simulate",
 *         timeout: 43200,
 *         response: {
 *             contentType: "text/plain",
 *             body: "custom response body",
 *         },
 *     },
 *     correlate: {
 *         by: "nat",
 *     },
 *     disabled: false,
 *     description: "example rate limit for a zone",
 *     bypassUrlPatterns: [
 *         `${_var.cloudflare_zone}/bypass1`,
 *         `${_var.cloudflare_zone}/bypass2`,
 *     ],
 * });
 * ```
 *
 * ## Import
 *
 * Rate limits can be imported using a composite ID formed of zone name and rate limit ID, e.g.
 *
 * ```sh
 *  $ pulumi import cloudflare:index/rateLimit:RateLimit default d41d8cd98f00b204e9800998ecf8427e/ch8374ftwdghsif43
 * ```
 */
export class RateLimit extends pulumi.CustomResource {
    /**
     * Get an existing RateLimit resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RateLimitState, opts?: pulumi.CustomResourceOptions): RateLimit {
        return new RateLimit(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'cloudflare:index/rateLimit:RateLimit';

    /**
     * Returns true if the given object is an instance of RateLimit.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RateLimit {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RateLimit.__pulumiType;
    }

    /**
     * The action to be performed when the threshold of matched traffic within the period defined is exceeded.
     */
    public readonly action!: pulumi.Output<outputs.RateLimitAction>;
    /**
     * URLs matching the patterns specified here will be excluded from rate limiting.
     */
    public readonly bypassUrlPatterns!: pulumi.Output<string[] | undefined>;
    /**
     * Determines how rate limiting is applied. By default if not specified, rate limiting applies to the clients IP address.
     */
    public readonly correlate!: pulumi.Output<outputs.RateLimitCorrelate | undefined>;
    /**
     * A note that you can use to describe the reason for a rate limit. This value is sanitized and all tags are removed.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Whether this ratelimit is currently disabled. Default: `false`.
     */
    public readonly disabled!: pulumi.Output<boolean | undefined>;
    /**
     * Determines which traffic the rate limit counts towards the threshold. By default matches all traffic in the zone. See definition below.
     */
    public readonly match!: pulumi.Output<outputs.RateLimitMatch>;
    /**
     * The time in seconds to count matching traffic. If the count exceeds threshold within this period the action will be performed (min: 1, max: 86,400).
     */
    public readonly period!: pulumi.Output<number>;
    /**
     * The threshold that triggers the rate limit mitigations, combine with period. i.e. threshold per period (min: 2, max: 1,000,000).
     */
    public readonly threshold!: pulumi.Output<number>;
    /**
     * The DNS zone ID to apply rate limiting to.
     */
    public readonly zoneId!: pulumi.Output<string>;

    /**
     * Create a RateLimit resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RateLimitArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RateLimitArgs | RateLimitState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as RateLimitState | undefined;
            inputs["action"] = state ? state.action : undefined;
            inputs["bypassUrlPatterns"] = state ? state.bypassUrlPatterns : undefined;
            inputs["correlate"] = state ? state.correlate : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["disabled"] = state ? state.disabled : undefined;
            inputs["match"] = state ? state.match : undefined;
            inputs["period"] = state ? state.period : undefined;
            inputs["threshold"] = state ? state.threshold : undefined;
            inputs["zoneId"] = state ? state.zoneId : undefined;
        } else {
            const args = argsOrState as RateLimitArgs | undefined;
            if ((!args || args.action === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'action'");
            }
            if ((!args || args.period === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'period'");
            }
            if ((!args || args.threshold === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'threshold'");
            }
            if ((!args || args.zoneId === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'zoneId'");
            }
            inputs["action"] = args ? args.action : undefined;
            inputs["bypassUrlPatterns"] = args ? args.bypassUrlPatterns : undefined;
            inputs["correlate"] = args ? args.correlate : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["disabled"] = args ? args.disabled : undefined;
            inputs["match"] = args ? args.match : undefined;
            inputs["period"] = args ? args.period : undefined;
            inputs["threshold"] = args ? args.threshold : undefined;
            inputs["zoneId"] = args ? args.zoneId : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(RateLimit.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RateLimit resources.
 */
export interface RateLimitState {
    /**
     * The action to be performed when the threshold of matched traffic within the period defined is exceeded.
     */
    readonly action?: pulumi.Input<inputs.RateLimitAction>;
    /**
     * URLs matching the patterns specified here will be excluded from rate limiting.
     */
    readonly bypassUrlPatterns?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Determines how rate limiting is applied. By default if not specified, rate limiting applies to the clients IP address.
     */
    readonly correlate?: pulumi.Input<inputs.RateLimitCorrelate>;
    /**
     * A note that you can use to describe the reason for a rate limit. This value is sanitized and all tags are removed.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Whether this ratelimit is currently disabled. Default: `false`.
     */
    readonly disabled?: pulumi.Input<boolean>;
    /**
     * Determines which traffic the rate limit counts towards the threshold. By default matches all traffic in the zone. See definition below.
     */
    readonly match?: pulumi.Input<inputs.RateLimitMatch>;
    /**
     * The time in seconds to count matching traffic. If the count exceeds threshold within this period the action will be performed (min: 1, max: 86,400).
     */
    readonly period?: pulumi.Input<number>;
    /**
     * The threshold that triggers the rate limit mitigations, combine with period. i.e. threshold per period (min: 2, max: 1,000,000).
     */
    readonly threshold?: pulumi.Input<number>;
    /**
     * The DNS zone ID to apply rate limiting to.
     */
    readonly zoneId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a RateLimit resource.
 */
export interface RateLimitArgs {
    /**
     * The action to be performed when the threshold of matched traffic within the period defined is exceeded.
     */
    readonly action: pulumi.Input<inputs.RateLimitAction>;
    /**
     * URLs matching the patterns specified here will be excluded from rate limiting.
     */
    readonly bypassUrlPatterns?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Determines how rate limiting is applied. By default if not specified, rate limiting applies to the clients IP address.
     */
    readonly correlate?: pulumi.Input<inputs.RateLimitCorrelate>;
    /**
     * A note that you can use to describe the reason for a rate limit. This value is sanitized and all tags are removed.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Whether this ratelimit is currently disabled. Default: `false`.
     */
    readonly disabled?: pulumi.Input<boolean>;
    /**
     * Determines which traffic the rate limit counts towards the threshold. By default matches all traffic in the zone. See definition below.
     */
    readonly match?: pulumi.Input<inputs.RateLimitMatch>;
    /**
     * The time in seconds to count matching traffic. If the count exceeds threshold within this period the action will be performed (min: 1, max: 86,400).
     */
    readonly period: pulumi.Input<number>;
    /**
     * The threshold that triggers the rate limit mitigations, combine with period. i.e. threshold per period (min: 2, max: 1,000,000).
     */
    readonly threshold: pulumi.Input<number>;
    /**
     * The DNS zone ID to apply rate limiting to.
     */
    readonly zoneId: pulumi.Input<string>;
}
