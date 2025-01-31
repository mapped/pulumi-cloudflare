// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudflare.Inputs
{

    public sealed class RulesetRuleActionParametersArgs : Pulumi.ResourceArgs
    {
        [Input("cookieFields")]
        private InputList<string>? _cookieFields;

        /// <summary>
        /// List of cookie values to include as part of custom fields logging.
        /// </summary>
        public InputList<string> CookieFields
        {
            get => _cookieFields ?? (_cookieFields = new InputList<string>());
            set => _cookieFields = value;
        }

        [Input("headers")]
        private InputList<Inputs.RulesetRuleActionParametersHeaderArgs>? _headers;

        /// <summary>
        /// List of HTTP header modifications to perform in the ruleset rule (refer to the nested schema).
        /// </summary>
        public InputList<Inputs.RulesetRuleActionParametersHeaderArgs> Headers
        {
            get => _headers ?? (_headers = new InputList<Inputs.RulesetRuleActionParametersHeaderArgs>());
            set => _headers = value;
        }

        /// <summary>
        /// Host Header that request origin receives.
        /// </summary>
        [Input("hostHeader")]
        public Input<string>? HostHeader { get; set; }

        /// <summary>
        /// Rule ID to apply the override to.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("increment")]
        public Input<int>? Increment { get; set; }

        /// <summary>
        /// List of properties to configure WAF payload logging (refer to the nested schema).
        /// </summary>
        [Input("matchedData")]
        public Input<Inputs.RulesetRuleActionParametersMatchedDataArgs>? MatchedData { get; set; }

        /// <summary>
        /// List of properties to change request origin (refer to the nested schema).
        /// </summary>
        [Input("origin")]
        public Input<Inputs.RulesetRuleActionParametersOriginArgs>? Origin { get; set; }

        /// <summary>
        /// List of override configurations to apply to the ruleset (refer to the nested schema).
        /// </summary>
        [Input("overrides")]
        public Input<Inputs.RulesetRuleActionParametersOverridesArgs>? Overrides { get; set; }

        [Input("phases")]
        private InputList<string>? _phases;
        public InputList<string> Phases
        {
            get => _phases ?? (_phases = new InputList<string>());
            set => _phases = value;
        }

        [Input("products")]
        private InputList<string>? _products;

        /// <summary>
        /// Products to target with the actions. Valid values are `"bic"`, `"hot"`, `"ratelimit"`, `"securityLevel"`, `"uablock"`, `"waf"` or `"zonelockdown"`.
        /// </summary>
        public InputList<string> Products
        {
            get => _products ?? (_products = new InputList<string>());
            set => _products = value;
        }

        [Input("requestFields")]
        private InputList<string>? _requestFields;

        /// <summary>
        /// List of request headers to include as part of custom fields logging, in lowercase.
        /// </summary>
        public InputList<string> RequestFields
        {
            get => _requestFields ?? (_requestFields = new InputList<string>());
            set => _requestFields = value;
        }

        [Input("responseFields")]
        private InputList<string>? _responseFields;

        /// <summary>
        /// List of response headers to include as part of custom fields logging, in lowercase.
        /// </summary>
        public InputList<string> ResponseFields
        {
            get => _responseFields ?? (_responseFields = new InputList<string>());
            set => _responseFields = value;
        }

        [Input("responses")]
        private InputList<Inputs.RulesetRuleActionParametersResponseArgs>? _responses;

        /// <summary>
        /// List of parameters that configure the response given to end users (refer to the nested schema).
        /// </summary>
        public InputList<Inputs.RulesetRuleActionParametersResponseArgs> Responses
        {
            get => _responses ?? (_responses = new InputList<Inputs.RulesetRuleActionParametersResponseArgs>());
            set => _responses = value;
        }

        [Input("rules")]
        private InputMap<string>? _rules;

        /// <summary>
        /// List of rule-based overrides (refer to the nested schema).
        /// </summary>
        public InputMap<string> Rules
        {
            get => _rules ?? (_rules = new InputMap<string>());
            set => _rules = value;
        }

        /// <summary>
        /// Which ruleset ID to target.
        /// </summary>
        [Input("ruleset")]
        public Input<string>? Ruleset { get; set; }

        [Input("rulesets")]
        private InputList<string>? _rulesets;

        /// <summary>
        /// List of managed WAF rule IDs to target. Only valid when the "action" is set to skip.
        /// </summary>
        public InputList<string> Rulesets
        {
            get => _rulesets ?? (_rulesets = new InputList<string>());
            set => _rulesets = value;
        }

        /// <summary>
        /// List of URI properties to configure for the ruleset rule when performing URL rewrite transformations (refer to the nested schema).
        /// </summary>
        [Input("uri")]
        public Input<Inputs.RulesetRuleActionParametersUriArgs>? Uri { get; set; }

        [Input("version")]
        public Input<string>? Version { get; set; }

        public RulesetRuleActionParametersArgs()
        {
        }
    }
}
