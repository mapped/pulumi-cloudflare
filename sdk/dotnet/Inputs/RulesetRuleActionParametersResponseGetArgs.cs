// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudflare.Inputs
{

    public sealed class RulesetRuleActionParametersResponseGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Body content to include in the response.
        /// </summary>
        [Input("content")]
        public Input<string>? Content { get; set; }

        /// <summary>
        /// HTTP content type to send in the response.
        /// </summary>
        [Input("contentType")]
        public Input<string>? ContentType { get; set; }

        /// <summary>
        /// HTTP status code to send in the response.
        /// </summary>
        [Input("statusCode")]
        public Input<int>? StatusCode { get; set; }

        public RulesetRuleActionParametersResponseGetArgs()
        {
        }
    }
}
