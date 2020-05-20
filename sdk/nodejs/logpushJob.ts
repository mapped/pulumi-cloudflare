// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class LogpushJob extends pulumi.CustomResource {
    /**
     * Get an existing LogpushJob resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LogpushJobState, opts?: pulumi.CustomResourceOptions): LogpushJob {
        return new LogpushJob(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'cloudflare:index/logpushJob:LogpushJob';

    /**
     * Returns true if the given object is an instance of LogpushJob.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LogpushJob {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LogpushJob.__pulumiType;
    }

    /**
     * Which type of dataset resource to use. Available values are `"firewallEvents"`, `"httpRequests"`, and `"spectrumEvents"`.
     */
    public readonly dataset!: pulumi.Output<string>;
    /**
     * Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See [Logpush destination documentation](https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination).
     */
    public readonly destinationConf!: pulumi.Output<string>;
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    /**
     * Configuration string for the Logshare API. It specifies things like requested fields and timestamp formats. See [Logpull options documentation](https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#options).
     */
    public readonly logpullOptions!: pulumi.Output<string | undefined>;
    /**
     * The name of the logpush job to create. Must match the regular expression `^[a-zA-Z0-9\-\.]*$`.
     */
    public readonly name!: pulumi.Output<string | undefined>;
    /**
     * Ownership challenge token to prove destination ownership. See [Developer documentation](https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#usage).
     */
    public readonly ownershipChallenge!: pulumi.Output<string>;
    /**
     * The zone ID where the logpush job should be created.
     */
    public readonly zoneId!: pulumi.Output<string>;

    /**
     * Create a LogpushJob resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LogpushJobArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: LogpushJobArgs | LogpushJobState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as LogpushJobState | undefined;
            inputs["dataset"] = state ? state.dataset : undefined;
            inputs["destinationConf"] = state ? state.destinationConf : undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["logpullOptions"] = state ? state.logpullOptions : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["ownershipChallenge"] = state ? state.ownershipChallenge : undefined;
            inputs["zoneId"] = state ? state.zoneId : undefined;
        } else {
            const args = argsOrState as LogpushJobArgs | undefined;
            if (!args || args.dataset === undefined) {
                throw new Error("Missing required property 'dataset'");
            }
            if (!args || args.destinationConf === undefined) {
                throw new Error("Missing required property 'destinationConf'");
            }
            if (!args || args.ownershipChallenge === undefined) {
                throw new Error("Missing required property 'ownershipChallenge'");
            }
            if (!args || args.zoneId === undefined) {
                throw new Error("Missing required property 'zoneId'");
            }
            inputs["dataset"] = args ? args.dataset : undefined;
            inputs["destinationConf"] = args ? args.destinationConf : undefined;
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["logpullOptions"] = args ? args.logpullOptions : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["ownershipChallenge"] = args ? args.ownershipChallenge : undefined;
            inputs["zoneId"] = args ? args.zoneId : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(LogpushJob.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering LogpushJob resources.
 */
export interface LogpushJobState {
    /**
     * Which type of dataset resource to use. Available values are `"firewallEvents"`, `"httpRequests"`, and `"spectrumEvents"`.
     */
    readonly dataset?: pulumi.Input<string>;
    /**
     * Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See [Logpush destination documentation](https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination).
     */
    readonly destinationConf?: pulumi.Input<string>;
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * Configuration string for the Logshare API. It specifies things like requested fields and timestamp formats. See [Logpull options documentation](https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#options).
     */
    readonly logpullOptions?: pulumi.Input<string>;
    /**
     * The name of the logpush job to create. Must match the regular expression `^[a-zA-Z0-9\-\.]*$`.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Ownership challenge token to prove destination ownership. See [Developer documentation](https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#usage).
     */
    readonly ownershipChallenge?: pulumi.Input<string>;
    /**
     * The zone ID where the logpush job should be created.
     */
    readonly zoneId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a LogpushJob resource.
 */
export interface LogpushJobArgs {
    /**
     * Which type of dataset resource to use. Available values are `"firewallEvents"`, `"httpRequests"`, and `"spectrumEvents"`.
     */
    readonly dataset: pulumi.Input<string>;
    /**
     * Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See [Logpush destination documentation](https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination).
     */
    readonly destinationConf: pulumi.Input<string>;
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * Configuration string for the Logshare API. It specifies things like requested fields and timestamp formats. See [Logpull options documentation](https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#options).
     */
    readonly logpullOptions?: pulumi.Input<string>;
    /**
     * The name of the logpush job to create. Must match the regular expression `^[a-zA-Z0-9\-\.]*$`.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Ownership challenge token to prove destination ownership. See [Developer documentation](https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#usage).
     */
    readonly ownershipChallenge: pulumi.Input<string>;
    /**
     * The zone ID where the logpush job should be created.
     */
    readonly zoneId: pulumi.Input<string>;
}
