// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Cloudflare Teams List resource. Teams lists are referenced when creating secure web gateway policies or device posture rules.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as cloudflare from "@pulumi/cloudflare";
 *
 * const corporateDevices = new cloudflare.TeamsList("corporate_devices", {
 *     accountId: "1d5fdc9e88c8a8c4518b068cd94331fe",
 *     description: "Serial numbers for all corporate devices.",
 *     items: [
 *         "8GE8721REF",
 *         "5RE8543EGG",
 *         "1YE2880LNP",
 *     ],
 *     name: "Corporate devices",
 *     type: "SERIAL",
 * });
 * ```
 *
 * ## Import
 *
 * Teams lists can be imported using a composite ID formed of account ID and teams list ID.
 *
 * ```sh
 *  $ pulumi import cloudflare:index/teamsList:TeamsList corporate_devices cb029e245cfdd66dc8d2e570d5dd3322/d41d8cd98f00b204e9800998ecf8427e
 * ```
 */
export class TeamsList extends pulumi.CustomResource {
    /**
     * Get an existing TeamsList resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TeamsListState, opts?: pulumi.CustomResourceOptions): TeamsList {
        return new TeamsList(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'cloudflare:index/teamsList:TeamsList';

    /**
     * Returns true if the given object is an instance of TeamsList.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TeamsList {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TeamsList.__pulumiType;
    }

    /**
     * The account to which the teams list should be added.
     */
    public readonly accountId!: pulumi.Output<string>;
    /**
     * The description of the teams list.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The items of the teams list.
     */
    public readonly items!: pulumi.Output<string[] | undefined>;
    /**
     * Name of the teams list.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The teams list type. Valid values are `SERIAL`, `URL`, `DOMAIN`, and `EMAIL`.
     */
    public readonly type!: pulumi.Output<string>;

    /**
     * Create a TeamsList resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TeamsListArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TeamsListArgs | TeamsListState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as TeamsListState | undefined;
            inputs["accountId"] = state ? state.accountId : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["items"] = state ? state.items : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as TeamsListArgs | undefined;
            if ((!args || args.accountId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'accountId'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            inputs["accountId"] = args ? args.accountId : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["items"] = args ? args.items : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["type"] = args ? args.type : undefined;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(TeamsList.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering TeamsList resources.
 */
export interface TeamsListState {
    /**
     * The account to which the teams list should be added.
     */
    accountId?: pulumi.Input<string>;
    /**
     * The description of the teams list.
     */
    description?: pulumi.Input<string>;
    /**
     * The items of the teams list.
     */
    items?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Name of the teams list.
     */
    name?: pulumi.Input<string>;
    /**
     * The teams list type. Valid values are `SERIAL`, `URL`, `DOMAIN`, and `EMAIL`.
     */
    type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a TeamsList resource.
 */
export interface TeamsListArgs {
    /**
     * The account to which the teams list should be added.
     */
    accountId: pulumi.Input<string>;
    /**
     * The description of the teams list.
     */
    description?: pulumi.Input<string>;
    /**
     * The items of the teams list.
     */
    items?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Name of the teams list.
     */
    name: pulumi.Input<string>;
    /**
     * The teams list type. Valid values are `SERIAL`, `URL`, `DOMAIN`, and `EMAIL`.
     */
    type: pulumi.Input<string>;
}
