// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provides a Cloudflare page rule resource.
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as cloudflare from "@pulumi/cloudflare";
 * 
 * // Add a page rule to the domain
 * const foobar = new cloudflare.PageRule("foobar", {
 *     zoneId: var.cloudflare_zone_id,
 *     target: `sub.${var.cloudflare_zone}/page`,
 *     priority: 1,
 *     actions: {
 *         ssl: "flexible",
 *         emailObfuscation: "on",
 *         minify: [{
 *             html: "off",
 *             css: "on",
 *             js: "on",
 *         }],
 *     },
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/page_rule.html.markdown.
 */
export class PageRule extends pulumi.CustomResource {
    /**
     * Get an existing PageRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PageRuleState, opts?: pulumi.CustomResourceOptions): PageRule {
        return new PageRule(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'cloudflare:index/pageRule:PageRule';

    /**
     * Returns true if the given object is an instance of PageRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PageRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PageRule.__pulumiType;
    }

    /**
     * The actions taken by the page rule, options given below.
     */
    public readonly actions!: pulumi.Output<outputs.PageRuleActions>;
    /**
     * The priority of the page rule among others for this target, the higher the number the higher the priority as per [API documentation](https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule).
     */
    public readonly priority!: pulumi.Output<number | undefined>;
    /**
     * Whether the page rule is active or disabled.
     */
    public readonly status!: pulumi.Output<string | undefined>;
    /**
     * The URL pattern to target with the page rule.
     */
    public readonly target!: pulumi.Output<string>;
    /**
     * The DNS zone ID to which the page rule should be added.
     */
    public readonly zoneId!: pulumi.Output<string>;

    /**
     * Create a PageRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PageRuleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PageRuleArgs | PageRuleState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as PageRuleState | undefined;
            inputs["actions"] = state ? state.actions : undefined;
            inputs["priority"] = state ? state.priority : undefined;
            inputs["status"] = state ? state.status : undefined;
            inputs["target"] = state ? state.target : undefined;
            inputs["zoneId"] = state ? state.zoneId : undefined;
        } else {
            const args = argsOrState as PageRuleArgs | undefined;
            if (!args || args.actions === undefined) {
                throw new Error("Missing required property 'actions'");
            }
            if (!args || args.target === undefined) {
                throw new Error("Missing required property 'target'");
            }
            if (!args || args.zoneId === undefined) {
                throw new Error("Missing required property 'zoneId'");
            }
            inputs["actions"] = args ? args.actions : undefined;
            inputs["priority"] = args ? args.priority : undefined;
            inputs["status"] = args ? args.status : undefined;
            inputs["target"] = args ? args.target : undefined;
            inputs["zoneId"] = args ? args.zoneId : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(PageRule.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PageRule resources.
 */
export interface PageRuleState {
    /**
     * The actions taken by the page rule, options given below.
     */
    readonly actions?: pulumi.Input<inputs.PageRuleActions>;
    /**
     * The priority of the page rule among others for this target, the higher the number the higher the priority as per [API documentation](https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule).
     */
    readonly priority?: pulumi.Input<number>;
    /**
     * Whether the page rule is active or disabled.
     */
    readonly status?: pulumi.Input<string>;
    /**
     * The URL pattern to target with the page rule.
     */
    readonly target?: pulumi.Input<string>;
    /**
     * The DNS zone ID to which the page rule should be added.
     */
    readonly zoneId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a PageRule resource.
 */
export interface PageRuleArgs {
    /**
     * The actions taken by the page rule, options given below.
     */
    readonly actions: pulumi.Input<inputs.PageRuleActions>;
    /**
     * The priority of the page rule among others for this target, the higher the number the higher the priority as per [API documentation](https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule).
     */
    readonly priority?: pulumi.Input<number>;
    /**
     * Whether the page rule is active or disabled.
     */
    readonly status?: pulumi.Input<string>;
    /**
     * The URL pattern to target with the page rule.
     */
    readonly target: pulumi.Input<string>;
    /**
     * The DNS zone ID to which the page rule should be added.
     */
    readonly zoneId: pulumi.Input<string>;
}
