// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudflare
{
    public static class GetZoneDnssec
    {
        /// <summary>
        /// Use this data source to look up [Zone][1] DNSSEC settings.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Cloudflare = Pulumi.Cloudflare;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var example = Output.Create(Cloudflare.GetZoneDnssec.InvokeAsync(new Cloudflare.GetZoneDnssecArgs
        ///         {
        ///             ZoneId = "&lt;zone_id&gt;",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetZoneDnssecResult> InvokeAsync(GetZoneDnssecArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetZoneDnssecResult>("cloudflare:index/getZoneDnssec:getZoneDnssec", args ?? new GetZoneDnssecArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to look up [Zone][1] DNSSEC settings.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Cloudflare = Pulumi.Cloudflare;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var example = Output.Create(Cloudflare.GetZoneDnssec.InvokeAsync(new Cloudflare.GetZoneDnssecArgs
        ///         {
        ///             ZoneId = "&lt;zone_id&gt;",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetZoneDnssecResult> Invoke(GetZoneDnssecInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetZoneDnssecResult>("cloudflare:index/getZoneDnssec:getZoneDnssec", args ?? new GetZoneDnssecInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetZoneDnssecArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The zone id for the zone.
        /// </summary>
        [Input("zoneId", required: true)]
        public string ZoneId { get; set; } = null!;

        public GetZoneDnssecArgs()
        {
        }
    }

    public sealed class GetZoneDnssecInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The zone id for the zone.
        /// </summary>
        [Input("zoneId", required: true)]
        public Input<string> ZoneId { get; set; } = null!;

        public GetZoneDnssecInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetZoneDnssecResult
    {
        /// <summary>
        /// Zone DNSSEC algorithm.
        /// </summary>
        public readonly string Algorithm;
        /// <summary>
        /// Zone DNSSEC digest.
        /// </summary>
        public readonly string Digest;
        /// <summary>
        /// Digest algorithm use for Zone DNSSEC.
        /// </summary>
        public readonly string DigestAlgorithm;
        /// <summary>
        /// Digest Type for Zone DNSSEC.
        /// </summary>
        public readonly string DigestType;
        /// <summary>
        /// DS for the Zone DNSSEC.
        /// </summary>
        public readonly string Ds;
        /// <summary>
        /// Zone DNSSEC flags.
        /// </summary>
        public readonly int Flags;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Key Tag for the Zone DNSSEC.
        /// </summary>
        public readonly int KeyTag;
        /// <summary>
        /// Key type used for Zone DNSSEC.
        /// </summary>
        public readonly string KeyType;
        /// <summary>
        /// Public Key for the Zone DNSSEC.
        /// </summary>
        public readonly string PublicKey;
        /// <summary>
        /// The status of the Zone DNSSEC.
        /// </summary>
        public readonly string Status;
        public readonly string ZoneId;

        [OutputConstructor]
        private GetZoneDnssecResult(
            string algorithm,

            string digest,

            string digestAlgorithm,

            string digestType,

            string ds,

            int flags,

            string id,

            int keyTag,

            string keyType,

            string publicKey,

            string status,

            string zoneId)
        {
            Algorithm = algorithm;
            Digest = digest;
            DigestAlgorithm = digestAlgorithm;
            DigestType = digestType;
            Ds = ds;
            Flags = flags;
            Id = id;
            KeyTag = keyTag;
            KeyType = keyType;
            PublicKey = publicKey;
            Status = status;
            ZoneId = zoneId;
        }
    }
}
