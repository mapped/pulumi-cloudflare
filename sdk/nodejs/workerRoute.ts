// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Cloudflare worker route resource. A route will also require a `cloudflare.WorkerScript`. *NOTE:*  This resource uses the Cloudflare account APIs. This requires setting the `CLOUDFLARE_ACCOUNT_ID` environment variable or `accountId` provider argument.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as pulumi_cloudflare from "@mapped/pulumi-cloudflare";
 *
 * const myScript = new cloudflare.WorkerScript("myScript", {});
 * // see "cloudflare_worker_script" documentation ...
 * // Runs the specified worker script for all URLs that match `example.com/*`
 * const myRoute = new cloudflare.WorkerRoute("myRoute", {
 *     zoneId: "d41d8cd98f00b204e9800998ecf8427e",
 *     pattern: "example.com/*",
 *     scriptName: myScript.name,
 * });
 * ```
 *
 * ## Import
 *
 * Records can be imported using a composite ID formed of zone ID and route ID, e.g.
 *
 * ```sh
 *  $ pulumi import cloudflare:index/workerRoute:WorkerRoute default d41d8cd98f00b204e9800998ecf8427e/9a7806061c88ada191ed06f989cc3dac
 * ```
 *
 *  where* `d41d8cd98f00b204e9800998ecf8427e` - zone ID * `9a7806061c88ada191ed06f989cc3dac` - route ID as returned by [API](https://api.cloudflare.com/#worker-filters-list-filters)
 */
export class WorkerRoute extends pulumi.CustomResource {
    /**
     * Get an existing WorkerRoute resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WorkerRouteState, opts?: pulumi.CustomResourceOptions): WorkerRoute {
        return new WorkerRoute(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'cloudflare:index/workerRoute:WorkerRoute';

    /**
     * Returns true if the given object is an instance of WorkerRoute.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is WorkerRoute {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === WorkerRoute.__pulumiType;
    }

    /**
     * The [route pattern](https://developers.cloudflare.com/workers/about/routes/)
     */
    public readonly pattern!: pulumi.Output<string>;
    /**
     * Which worker script to run for requests that match the route pattern. If `scriptName` is empty, workers will be skipped for matching requests.
     */
    public readonly scriptName!: pulumi.Output<string | undefined>;
    /**
     * The zone ID to add the route to.
     */
    public readonly zoneId!: pulumi.Output<string>;

    /**
     * Create a WorkerRoute resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: WorkerRouteArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: WorkerRouteArgs | WorkerRouteState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as WorkerRouteState | undefined;
            resourceInputs["pattern"] = state ? state.pattern : undefined;
            resourceInputs["scriptName"] = state ? state.scriptName : undefined;
            resourceInputs["zoneId"] = state ? state.zoneId : undefined;
        } else {
            const args = argsOrState as WorkerRouteArgs | undefined;
            if ((!args || args.pattern === undefined) && !opts.urn) {
                throw new Error("Missing required property 'pattern'");
            }
            if ((!args || args.zoneId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'zoneId'");
            }
            resourceInputs["pattern"] = args ? args.pattern : undefined;
            resourceInputs["scriptName"] = args ? args.scriptName : undefined;
            resourceInputs["zoneId"] = args ? args.zoneId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(WorkerRoute.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering WorkerRoute resources.
 */
export interface WorkerRouteState {
    /**
     * The [route pattern](https://developers.cloudflare.com/workers/about/routes/)
     */
    pattern?: pulumi.Input<string>;
    /**
     * Which worker script to run for requests that match the route pattern. If `scriptName` is empty, workers will be skipped for matching requests.
     */
    scriptName?: pulumi.Input<string>;
    /**
     * The zone ID to add the route to.
     */
    zoneId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a WorkerRoute resource.
 */
export interface WorkerRouteArgs {
    /**
     * The [route pattern](https://developers.cloudflare.com/workers/about/routes/)
     */
    pattern: pulumi.Input<string>;
    /**
     * Which worker script to run for requests that match the route pattern. If `scriptName` is empty, workers will be skipped for matching requests.
     */
    scriptName?: pulumi.Input<string>;
    /**
     * The zone ID to add the route to.
     */
    zoneId: pulumi.Input<string>;
}
