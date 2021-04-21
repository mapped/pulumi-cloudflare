// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudflare.Inputs
{

    public sealed class LoadBalancerRuleGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The statement to evaluate to determine if this rules effects should be applied. An empty condition is always true. See [load balancing rules](https://developers.cloudflare.com/load-balancing/understand-basics/load-balancing-rules).
        /// </summary>
        [Input("condition")]
        public Input<string>? Condition { get; set; }

        /// <summary>
        /// A disabled rule will be be executed.
        /// </summary>
        [Input("disabled")]
        public Input<bool>? Disabled { get; set; }

        /// <summary>
        /// Settings for a HTTP response to return directly to the eyeball if the condition is true. Note: overrides or fixed_response must be set. See the field documentation below.
        /// </summary>
        [Input("fixedResponse")]
        public Input<Inputs.LoadBalancerRuleFixedResponseGetArgs>? FixedResponse { get; set; }

        /// <summary>
        /// Human readable name for this rule.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("overrides")]
        private InputList<Inputs.LoadBalancerRuleOverrideGetArgs>? _overrides;

        /// <summary>
        /// The Load Balancer settings to alter if this rules condition is true. Note: overrides or fixed_response must be set. See the field documentation below.
        /// </summary>
        public InputList<Inputs.LoadBalancerRuleOverrideGetArgs> Overrides
        {
            get => _overrides ?? (_overrides = new InputList<Inputs.LoadBalancerRuleOverrideGetArgs>());
            set => _overrides = value;
        }

        /// <summary>
        /// Priority used when determining the order of rule execution. Lower values are executed first. If not provided list order will be used.
        /// </summary>
        [Input("priority")]
        public Input<int>? Priority { get; set; }

        /// <summary>
        /// Terminates indicates that if this rule is true no further rules should be executed. Note: setting a fixed_response forces this field to true.
        /// </summary>
        [Input("terminates")]
        public Input<bool>? Terminates { get; set; }

        public LoadBalancerRuleGetArgs()
        {
        }
    }
}