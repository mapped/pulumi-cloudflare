// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudflare.Inputs
{

    public sealed class AccessGroupExcludeExternalEvaluationGetArgs : Pulumi.ResourceArgs
    {
        [Input("evaluateUrl")]
        public Input<string>? EvaluateUrl { get; set; }

        [Input("keysUrl")]
        public Input<string>? KeysUrl { get; set; }

        public AccessGroupExcludeExternalEvaluationGetArgs()
        {
        }
    }
}