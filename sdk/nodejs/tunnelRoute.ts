// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a resource, that manages Cloudflare tunnel routes for Zero Trust. Tunnel
 * routes are used to direct IP traffic through Cloudflare Tunnels.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as cloudflare from "@pulumi/cloudflare";
 *
 * const example = new cloudflare.TunnelRoute("example", {
 *     accountId: "c4a7362d577a6c3019a474fd6f485821",
 *     comment: "New tunnel route for documentation",
 *     network: "192.0.2.24/32",
 *     tunnelId: "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
 *     virtualNetworkId: "bdc39a3c-3104-4c23-8ac0-9f455dda691a",
 * });
 * ```
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as pulumi_cloudflare from "@mapped/pulumi-cloudflare";
 *
 * const tunnel = new cloudflare.ArgoTunnel("tunnel", {
 *     accountId: "c4a7362d577a6c3019a474fd6f485821",
 *     name: "my_tunnel",
 *     secret: "AQIDBAUGBwgBAgMEBQYHCAECAwQFBgcIAQIDBAUGBwg=",
 * });
 * const example = new cloudflare.TunnelRoute("example", {
 *     accountId: "c4a7362d577a6c3019a474fd6f485821",
 *     tunnelId: tunnel.id,
 *     network: "192.0.2.24/32",
 *     comment: "New tunnel route for documentation",
 *     virtualNetworkId: "bdc39a3c-3104-4c23-8ac0-9f455dda691a",
 * });
 * ```
 *
 * ## Import
 *
 * An existing tunnel route can be imported using the account ID and network CIDR
 *
 * ```sh
 *  $ pulumi import cloudflare:index/tunnelRoute:TunnelRoute cloudflare_tunnel_route c4a7362d577a6c3019a474fd6f485821/192.0.2.24/32
 * ```
 *
 *  or using account ID, network CIDR and virtual network ID.
 *
 * ```sh
 *  $ pulumi import cloudflare:index/tunnelRoute:TunnelRoute cloudflare_tunnel_route c4a7362d577a6c3019a474fd6f485821/192.0.2.24/32/bdc39a3c-3104-4c23-8ac0-9f455dda691a
 * ```
 */
export class TunnelRoute extends pulumi.CustomResource {
    /**
     * Get an existing TunnelRoute resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TunnelRouteState, opts?: pulumi.CustomResourceOptions): TunnelRoute {
        return new TunnelRoute(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'cloudflare:index/tunnelRoute:TunnelRoute';

    /**
     * Returns true if the given object is an instance of TunnelRoute.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TunnelRoute {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TunnelRoute.__pulumiType;
    }

    /**
     * The ID of the account where the tunnel route is being created.
     */
    public readonly accountId!: pulumi.Output<string>;
    /**
     * Description of the tunnel route.
     */
    public readonly comment!: pulumi.Output<string | undefined>;
    /**
     * The IPv4 or IPv6 network that should use this tunnel route, in CIDR notation.
     */
    public readonly network!: pulumi.Output<string>;
    /**
     * The ID of the tunnel that will service the tunnel route.
     */
    public readonly tunnelId!: pulumi.Output<string>;
    /**
     * The ID of the virtual network for which this route is being added; uses the default virtual network of the account if none is provided.
     */
    public readonly virtualNetworkId!: pulumi.Output<string | undefined>;

    /**
     * Create a TunnelRoute resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TunnelRouteArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TunnelRouteArgs | TunnelRouteState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as TunnelRouteState | undefined;
            resourceInputs["accountId"] = state ? state.accountId : undefined;
            resourceInputs["comment"] = state ? state.comment : undefined;
            resourceInputs["network"] = state ? state.network : undefined;
            resourceInputs["tunnelId"] = state ? state.tunnelId : undefined;
            resourceInputs["virtualNetworkId"] = state ? state.virtualNetworkId : undefined;
        } else {
            const args = argsOrState as TunnelRouteArgs | undefined;
            if ((!args || args.accountId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'accountId'");
            }
            if ((!args || args.network === undefined) && !opts.urn) {
                throw new Error("Missing required property 'network'");
            }
            if ((!args || args.tunnelId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'tunnelId'");
            }
            resourceInputs["accountId"] = args ? args.accountId : undefined;
            resourceInputs["comment"] = args ? args.comment : undefined;
            resourceInputs["network"] = args ? args.network : undefined;
            resourceInputs["tunnelId"] = args ? args.tunnelId : undefined;
            resourceInputs["virtualNetworkId"] = args ? args.virtualNetworkId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(TunnelRoute.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering TunnelRoute resources.
 */
export interface TunnelRouteState {
    /**
     * The ID of the account where the tunnel route is being created.
     */
    accountId?: pulumi.Input<string>;
    /**
     * Description of the tunnel route.
     */
    comment?: pulumi.Input<string>;
    /**
     * The IPv4 or IPv6 network that should use this tunnel route, in CIDR notation.
     */
    network?: pulumi.Input<string>;
    /**
     * The ID of the tunnel that will service the tunnel route.
     */
    tunnelId?: pulumi.Input<string>;
    /**
     * The ID of the virtual network for which this route is being added; uses the default virtual network of the account if none is provided.
     */
    virtualNetworkId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a TunnelRoute resource.
 */
export interface TunnelRouteArgs {
    /**
     * The ID of the account where the tunnel route is being created.
     */
    accountId: pulumi.Input<string>;
    /**
     * Description of the tunnel route.
     */
    comment?: pulumi.Input<string>;
    /**
     * The IPv4 or IPv6 network that should use this tunnel route, in CIDR notation.
     */
    network: pulumi.Input<string>;
    /**
     * The ID of the tunnel that will service the tunnel route.
     */
    tunnelId: pulumi.Input<string>;
    /**
     * The ID of the virtual network for which this route is being added; uses the default virtual network of the account if none is provided.
     */
    virtualNetworkId?: pulumi.Input<string>;
}
