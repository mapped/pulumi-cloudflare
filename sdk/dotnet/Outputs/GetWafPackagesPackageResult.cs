// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudflare.Outputs
{

    [OutputType]
    public sealed class GetWafPackagesPackageResult
    {
        public readonly string? ActionMode;
        public readonly string? Description;
        public readonly string? DetectionMode;
        public readonly string? Id;
        public readonly string? Name;
        public readonly string? Sensitivity;

        [OutputConstructor]
        private GetWafPackagesPackageResult(
            string? actionMode,

            string? description,

            string? detectionMode,

            string? id,

            string? name,

            string? sensitivity)
        {
            ActionMode = actionMode;
            Description = description;
            DetectionMode = detectionMode;
            Id = id;
            Name = name;
            Sensitivity = sensitivity;
        }
    }
}