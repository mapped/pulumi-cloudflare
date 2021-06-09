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
    public sealed class LoadBalancerPoolOrigin
    {
        /// <summary>
        /// The IP address (IPv4 or IPv6) of the origin, or the publicly addressable hostname. Hostnames entered here should resolve directly to the origin, and not be a hostname proxied by Cloudflare.
        /// </summary>
        public readonly string Address;
        /// <summary>
        /// Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.
        /// </summary>
        public readonly bool? Enabled;
        /// <summary>
        /// The header name.
        /// </summary>
        public readonly ImmutableArray<Outputs.LoadBalancerPoolOriginHeader> Headers;
        /// <summary>
        /// A human-identifiable name for the origin.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The weight (0.01 - 1.00) of this origin, relative to other origins in the pool. Equal values mean equal weighting. A weight of 0 means traffic will not be sent to this origin, but health is still checked. Default: 1.
        /// </summary>
        public readonly double? Weight;

        [OutputConstructor]
        private LoadBalancerPoolOrigin(
            string address,

            bool? enabled,

            ImmutableArray<Outputs.LoadBalancerPoolOriginHeader> headers,

            string name,

            double? weight)
        {
            Address = address;
            Enabled = enabled;
            Headers = headers;
            Name = name;
            Weight = weight;
        }
    }
}
