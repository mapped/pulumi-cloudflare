// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provides a Cloudflare Access Group resource. Access Groups are used
 * in conjunction with Access Policies to restrict access to a
 * particular resource based on group membership.
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as cloudflare from "@pulumi/cloudflare";
 * 
 * // Allowing access to `test@example.com` email address only
 * const testGroupAccessGroup = new cloudflare.AccessGroup("testGroupAccessGroup", {
 *     accountId: "975ecf5a45e3bcb680dba0722a420ad9",
 *     name: "staging group",
 *     include: [{
 *         emails: ["test@example.com"],
 *     }],
 * });
 * // Allowing `test@example.com` to access but only when coming from a
 * // specific IP.
 * const testGroupIndex/accessGroupAccessGroup = new cloudflare.AccessGroup("testGroupIndex/accessGroupAccessGroup", {
 *     accountId: "975ecf5a45e3bcb680dba0722a420ad9",
 *     name: "staging group",
 *     include: [{
 *         emails: ["test@example.com"],
 *     }],
 *     requires: {
 *         ips: [var.office_ip],
 *     },
 * });
 * ```
 * 
 * ## Conditions
 * 
 * `require`, `exclude` and `include` arguments share the available
 * conditions which can be applied. The conditions are:
 * 
 * * `ip` - (Optional) A list of IP addresses or ranges. Example:
 *   `ip = ["1.2.3.4", "10.0.0.0/2"]`
 * * `email` - (Optional) A list of email addresses. Example:
 *   `email = ["test@example.com"]`
 * * `emailDomain` - (Optional) A list of email domains. Example:
 *   `emailDomain = ["example.com"]`
 * * `serviceToken` - (Optional) A list of service token ids. Example:
 *   `serviceToken = [cloudflare_access_service_token.demo.id]`
 * * `anyValidServiceToken` - (Optional) Boolean indicating if allow
 *   all tokens to be granted. Example: `anyValidServiceToken = true`
 * * `group` - (Optional) A list of access group ids. Example:
 *   `group = [cloudflare_access_group.demo.id]`
 * * `everyone` - (Optional) Boolean indicating permitting access for all
 *   requests. Example: `everyone = true`
 * * `certificate` - (Optional) Whether to use mTLS certificate authentication.
 * * `commonName` - (Optional) Use a certificate common name to authenticate with.
 * * `gsuite` - (Optional) Use GSuite as the authentication mechanism. Example:
 * 
 *   ```hcl
 *   # ... other configuration
 *   include {
 *     gsuite {
 *       email = "admins@example.com"
 *       identityProviderId = "ca298b82-93b5-41bf-bc2d-10493f09b761"
 *     }
 *   }
 *   ```
 * * `github` - (Optional) Use a GitHub team as the `include` condition. Example:
 * 
 *   ```hcl
 *   # ... other configuration
 *   include {
 *     github {
 *       name = "my-github-team-name"
 *       identityProviderId = "ca298b82-93b5-41bf-bc2d-10493f09b761"
 *     }
 *   }
 *   ```
 * * `azure` - (Optional) Use Azure AD as the `include` condition. Example:
 * 
 *   ```hcl
 *   # ... other configuration
 *   include {
 *     azure {
 *       id = "86773093-5feb-48dd-814b-7ccd3676ff50e"
 *       identityProviderId = "ca298b82-93b5-41bf-bc2d-10493f09b761"
 *     }
 *   }
 *   ```
 * * `okta` - (Optional) Use Okta as the `include` condition. Example:
 * 
 *   ```hcl
 *   # ... other configuration
 *   include {
 *     okta {
 *       name = "admins"
 *       identityProviderId = "ca298b82-93b5-41bf-bc2d-10493f09b761"
 *     }
 *   }
 *   ```
 * * `saml` - (Optional) Use an external SAML setup as the `include` condition.
 *   Example:
 * 
 *   ```hcl
 *   # ... other configuration
 *   include {
 *     saml {
 *       attributeName = "group"
 *       attributeValue = "admins"
 *       identityProviderId = "ca298b82-93b5-41bf-bc2d-10493f09b761"
 *     }
 *   }
 *   ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_group.html.markdown.
 */
export class AccessGroup extends pulumi.CustomResource {
    /**
     * Get an existing AccessGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccessGroupState, opts?: pulumi.CustomResourceOptions): AccessGroup {
        return new AccessGroup(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'cloudflare:index/accessGroup:AccessGroup';

    /**
     * Returns true if the given object is an instance of AccessGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AccessGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AccessGroup.__pulumiType;
    }

    /**
     * The ID of the account the group is
     * associated with.
     */
    public readonly accountId!: pulumi.Output<string>;
    /**
     * A series of access conditions, see below for
     * full list.
     */
    public readonly excludes!: pulumi.Output<outputs.AccessGroupExclude[] | undefined>;
    /**
     * A series of access conditions, see below for
     * full list.
     */
    public readonly includes!: pulumi.Output<outputs.AccessGroupInclude[]>;
    /**
     * Friendly name of the Access Group.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * A series of access conditions, see below for
     * full list.
     */
    public readonly requires!: pulumi.Output<outputs.AccessGroupRequire[] | undefined>;

    /**
     * Create a AccessGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AccessGroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AccessGroupArgs | AccessGroupState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as AccessGroupState | undefined;
            inputs["accountId"] = state ? state.accountId : undefined;
            inputs["excludes"] = state ? state.excludes : undefined;
            inputs["includes"] = state ? state.includes : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["requires"] = state ? state.requires : undefined;
        } else {
            const args = argsOrState as AccessGroupArgs | undefined;
            if (!args || args.accountId === undefined) {
                throw new Error("Missing required property 'accountId'");
            }
            if (!args || args.includes === undefined) {
                throw new Error("Missing required property 'includes'");
            }
            if (!args || args.name === undefined) {
                throw new Error("Missing required property 'name'");
            }
            inputs["accountId"] = args ? args.accountId : undefined;
            inputs["excludes"] = args ? args.excludes : undefined;
            inputs["includes"] = args ? args.includes : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["requires"] = args ? args.requires : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(AccessGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AccessGroup resources.
 */
export interface AccessGroupState {
    /**
     * The ID of the account the group is
     * associated with.
     */
    readonly accountId?: pulumi.Input<string>;
    /**
     * A series of access conditions, see below for
     * full list.
     */
    readonly excludes?: pulumi.Input<pulumi.Input<inputs.AccessGroupExclude>[]>;
    /**
     * A series of access conditions, see below for
     * full list.
     */
    readonly includes?: pulumi.Input<pulumi.Input<inputs.AccessGroupInclude>[]>;
    /**
     * Friendly name of the Access Group.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A series of access conditions, see below for
     * full list.
     */
    readonly requires?: pulumi.Input<pulumi.Input<inputs.AccessGroupRequire>[]>;
}

/**
 * The set of arguments for constructing a AccessGroup resource.
 */
export interface AccessGroupArgs {
    /**
     * The ID of the account the group is
     * associated with.
     */
    readonly accountId: pulumi.Input<string>;
    /**
     * A series of access conditions, see below for
     * full list.
     */
    readonly excludes?: pulumi.Input<pulumi.Input<inputs.AccessGroupExclude>[]>;
    /**
     * A series of access conditions, see below for
     * full list.
     */
    readonly includes: pulumi.Input<pulumi.Input<inputs.AccessGroupInclude>[]>;
    /**
     * Friendly name of the Access Group.
     */
    readonly name: pulumi.Input<string>;
    /**
     * A series of access conditions, see below for
     * full list.
     */
    readonly requires?: pulumi.Input<pulumi.Input<inputs.AccessGroupRequire>[]>;
}
