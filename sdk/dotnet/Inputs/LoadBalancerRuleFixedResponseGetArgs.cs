// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudflare.Inputs
{

    public sealed class LoadBalancerRuleFixedResponseGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The value of the HTTP context-type header for this fixed response.
        /// </summary>
        [Input("contentType")]
        public Input<string>? ContentType { get; set; }

        /// <summary>
        /// The value of the HTTP location header for this fixed response.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The text used as the html body for this fixed response.
        /// </summary>
        [Input("messageBody")]
        public Input<string>? MessageBody { get; set; }

        /// <summary>
        /// The HTTP status code used for this fixed response.
        /// </summary>
        [Input("statusCode")]
        public Input<int>? StatusCode { get; set; }

        public LoadBalancerRuleFixedResponseGetArgs()
        {
        }
    }
}
