// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudflare.Inputs
{

    public sealed class PageRuleActionsMinifyGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether CSS should be minified. Valid values are `"on"` or `"off"`.
        /// </summary>
        [Input("css", required: true)]
        public Input<string> Css { get; set; } = null!;

        /// <summary>
        /// Whether HTML should be minified. Valid values are `"on"` or `"off"`.
        /// </summary>
        [Input("html", required: true)]
        public Input<string> Html { get; set; } = null!;

        /// <summary>
        /// Whether Javascript should be minified. Valid values are `"on"` or `"off"`.
        /// </summary>
        [Input("js", required: true)]
        public Input<string> Js { get; set; } = null!;

        public PageRuleActionsMinifyGetArgs()
        {
        }
    }
}