// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudflare.Inputs
{

    public sealed class GetWafPackagesFilterArgs : Pulumi.InvokeArgs
    {
        [Input("actionMode")]
        public string? ActionMode { get; set; }

        [Input("detectionMode")]
        public string? DetectionMode { get; set; }

        [Input("name")]
        public string? Name { get; set; }

        [Input("sensitivity")]
        public string? Sensitivity { get; set; }

        public GetWafPackagesFilterArgs()
        {
        }
    }
}