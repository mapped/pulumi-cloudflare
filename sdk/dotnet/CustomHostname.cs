// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudflare
{
    /// <summary>
    /// Provides a Cloudflare custom hostname (also known as SSL for SaaS) resource.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Cloudflare = Pulumi.Cloudflare;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var exampleHostname = new Cloudflare.CustomHostname("exampleHostname", new Cloudflare.CustomHostnameArgs
    ///         {
    ///             Hostname = "hostname.example.com",
    ///             Ssls = 
    ///             {
    ///                 new Cloudflare.Inputs.CustomHostnameSslArgs
    ///                 {
    ///                     Method = "txt",
    ///                 },
    ///             },
    ///             ZoneId = "d41d8cd98f00b204e9800998ecf8427e",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Custom hostname certificates can be imported using a composite ID formed of the zone ID and [hostname ID](https://api.cloudflare.com/#custom-hostname-for-a-zone-properties), separated by a "/" e.g.
    /// 
    /// ```sh
    ///  $ pulumi import cloudflare:index/customHostname:CustomHostname example d41d8cd98f00b204e9800998ecf8427e/0d89c70d-ad9f-4843-b99f-6cc0252067e9
    /// ```
    /// </summary>
    [CloudflareResourceType("cloudflare:index/customHostname:CustomHostname")]
    public partial class CustomHostname : Pulumi.CustomResource
    {
        /// <summary>
        /// The custom origin server used for certificates.
        /// </summary>
        [Output("customOriginServer")]
        public Output<string?> CustomOriginServer { get; private set; } = null!;

        /// <summary>
        /// The [custom origin SNI](https://developers.cloudflare.com/ssl/ssl-for-saas/hostname-specific-behavior/custom-origin) used for certificates.
        /// </summary>
        [Output("customOriginSni")]
        public Output<string?> CustomOriginSni { get; private set; } = null!;

        /// <summary>
        /// Hostname you intend to request a certificate for.
        /// </summary>
        [Output("hostname")]
        public Output<string> Hostname { get; private set; } = null!;

        [Output("ownershipVerification")]
        public Output<ImmutableDictionary<string, string>> OwnershipVerification { get; private set; } = null!;

        [Output("ownershipVerificationHttp")]
        public Output<ImmutableDictionary<string, string>> OwnershipVerificationHttp { get; private set; } = null!;

        /// <summary>
        /// SSL configuration of the certificate. See further notes below.
        /// </summary>
        [Output("ssls")]
        public Output<ImmutableArray<Outputs.CustomHostnameSsl>> Ssls { get; private set; } = null!;

        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        /// <summary>
        /// The DNS zone ID where the custom hostname should be assigned.
        /// </summary>
        [Output("zoneId")]
        public Output<string> ZoneId { get; private set; } = null!;


        /// <summary>
        /// Create a CustomHostname resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CustomHostname(string name, CustomHostnameArgs args, CustomResourceOptions? options = null)
            : base("cloudflare:index/customHostname:CustomHostname", name, args ?? new CustomHostnameArgs(), MakeResourceOptions(options, ""))
        {
        }

        private CustomHostname(string name, Input<string> id, CustomHostnameState? state = null, CustomResourceOptions? options = null)
            : base("cloudflare:index/customHostname:CustomHostname", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing CustomHostname resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CustomHostname Get(string name, Input<string> id, CustomHostnameState? state = null, CustomResourceOptions? options = null)
        {
            return new CustomHostname(name, id, state, options);
        }
    }

    public sealed class CustomHostnameArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The custom origin server used for certificates.
        /// </summary>
        [Input("customOriginServer")]
        public Input<string>? CustomOriginServer { get; set; }

        /// <summary>
        /// The [custom origin SNI](https://developers.cloudflare.com/ssl/ssl-for-saas/hostname-specific-behavior/custom-origin) used for certificates.
        /// </summary>
        [Input("customOriginSni")]
        public Input<string>? CustomOriginSni { get; set; }

        /// <summary>
        /// Hostname you intend to request a certificate for.
        /// </summary>
        [Input("hostname", required: true)]
        public Input<string> Hostname { get; set; } = null!;

        [Input("ssls")]
        private InputList<Inputs.CustomHostnameSslArgs>? _ssls;

        /// <summary>
        /// SSL configuration of the certificate. See further notes below.
        /// </summary>
        public InputList<Inputs.CustomHostnameSslArgs> Ssls
        {
            get => _ssls ?? (_ssls = new InputList<Inputs.CustomHostnameSslArgs>());
            set => _ssls = value;
        }

        /// <summary>
        /// The DNS zone ID where the custom hostname should be assigned.
        /// </summary>
        [Input("zoneId", required: true)]
        public Input<string> ZoneId { get; set; } = null!;

        public CustomHostnameArgs()
        {
        }
    }

    public sealed class CustomHostnameState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The custom origin server used for certificates.
        /// </summary>
        [Input("customOriginServer")]
        public Input<string>? CustomOriginServer { get; set; }

        /// <summary>
        /// The [custom origin SNI](https://developers.cloudflare.com/ssl/ssl-for-saas/hostname-specific-behavior/custom-origin) used for certificates.
        /// </summary>
        [Input("customOriginSni")]
        public Input<string>? CustomOriginSni { get; set; }

        /// <summary>
        /// Hostname you intend to request a certificate for.
        /// </summary>
        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        [Input("ownershipVerification")]
        private InputMap<string>? _ownershipVerification;
        public InputMap<string> OwnershipVerification
        {
            get => _ownershipVerification ?? (_ownershipVerification = new InputMap<string>());
            set => _ownershipVerification = value;
        }

        [Input("ownershipVerificationHttp")]
        private InputMap<string>? _ownershipVerificationHttp;
        public InputMap<string> OwnershipVerificationHttp
        {
            get => _ownershipVerificationHttp ?? (_ownershipVerificationHttp = new InputMap<string>());
            set => _ownershipVerificationHttp = value;
        }

        [Input("ssls")]
        private InputList<Inputs.CustomHostnameSslGetArgs>? _ssls;

        /// <summary>
        /// SSL configuration of the certificate. See further notes below.
        /// </summary>
        public InputList<Inputs.CustomHostnameSslGetArgs> Ssls
        {
            get => _ssls ?? (_ssls = new InputList<Inputs.CustomHostnameSslGetArgs>());
            set => _ssls = value;
        }

        [Input("status")]
        public Input<string>? Status { get; set; }

        /// <summary>
        /// The DNS zone ID where the custom hostname should be assigned.
        /// </summary>
        [Input("zoneId")]
        public Input<string>? ZoneId { get; set; }

        public CustomHostnameState()
        {
        }
    }
}
