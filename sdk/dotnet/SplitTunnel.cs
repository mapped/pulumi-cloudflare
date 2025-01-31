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
    /// Provides a Cloudflare Split Tunnel resource. Split tunnels are used to either
    /// include or exclude lists of routes from the WARP client's tunnel.
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
    ///         // Excluding *.example.com from WARP routes
    ///         var exampleSplitTunnelExclude = new Cloudflare.SplitTunnel("exampleSplitTunnelExclude", new Cloudflare.SplitTunnelArgs
    ///         {
    ///             AccountId = "1d5fdc9e88c8a8c4518b068cd94331fe",
    ///             Mode = "exclude",
    ///             Tunnels = 
    ///             {
    ///                 new Cloudflare.Inputs.SplitTunnelTunnelArgs
    ///                 {
    ///                     Description = "example domain",
    ///                     Host = "*.example.com",
    ///                 },
    ///             },
    ///         });
    ///         // Including *.example.com in WARP routes
    ///         var exampleSplitTunnelInclude = new Cloudflare.SplitTunnel("exampleSplitTunnelInclude", new Cloudflare.SplitTunnelArgs
    ///         {
    ///             AccountId = "1d5fdc9e88c8a8c4518b068cd94331fe",
    ///             Mode = "include",
    ///             Tunnels = 
    ///             {
    ///                 new Cloudflare.Inputs.SplitTunnelTunnelArgs
    ///                 {
    ///                     Description = "example domain",
    ///                     Host = "*.example.com",
    ///                 },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Split Tunnels can be imported using the account identifer and mode.
    /// 
    /// ```sh
    ///  $ pulumi import cloudflare:index/splitTunnel:SplitTunnel example 1d5fdc9e88c8a8c4518b068cd94331fe/exclude
    /// ```
    /// </summary>
    [CloudflareResourceType("cloudflare:index/splitTunnel:SplitTunnel")]
    public partial class SplitTunnel : Pulumi.CustomResource
    {
        /// <summary>
        /// The account to which the device posture rule should be added.
        /// </summary>
        [Output("accountId")]
        public Output<string> AccountId { get; private set; } = null!;

        /// <summary>
        /// The split tunnel mode. Valid values are `include` or `exclude`.
        /// </summary>
        [Output("mode")]
        public Output<string> Mode { get; private set; } = null!;

        /// <summary>
        /// The value of the tunnel attributes (refer to the nested schema).
        /// </summary>
        [Output("tunnels")]
        public Output<ImmutableArray<Outputs.SplitTunnelTunnel>> Tunnels { get; private set; } = null!;


        /// <summary>
        /// Create a SplitTunnel resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SplitTunnel(string name, SplitTunnelArgs args, CustomResourceOptions? options = null)
            : base("cloudflare:index/splitTunnel:SplitTunnel", name, args ?? new SplitTunnelArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SplitTunnel(string name, Input<string> id, SplitTunnelState? state = null, CustomResourceOptions? options = null)
            : base("cloudflare:index/splitTunnel:SplitTunnel", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SplitTunnel resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SplitTunnel Get(string name, Input<string> id, SplitTunnelState? state = null, CustomResourceOptions? options = null)
        {
            return new SplitTunnel(name, id, state, options);
        }
    }

    public sealed class SplitTunnelArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The account to which the device posture rule should be added.
        /// </summary>
        [Input("accountId", required: true)]
        public Input<string> AccountId { get; set; } = null!;

        /// <summary>
        /// The split tunnel mode. Valid values are `include` or `exclude`.
        /// </summary>
        [Input("mode", required: true)]
        public Input<string> Mode { get; set; } = null!;

        [Input("tunnels", required: true)]
        private InputList<Inputs.SplitTunnelTunnelArgs>? _tunnels;

        /// <summary>
        /// The value of the tunnel attributes (refer to the nested schema).
        /// </summary>
        public InputList<Inputs.SplitTunnelTunnelArgs> Tunnels
        {
            get => _tunnels ?? (_tunnels = new InputList<Inputs.SplitTunnelTunnelArgs>());
            set => _tunnels = value;
        }

        public SplitTunnelArgs()
        {
        }
    }

    public sealed class SplitTunnelState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The account to which the device posture rule should be added.
        /// </summary>
        [Input("accountId")]
        public Input<string>? AccountId { get; set; }

        /// <summary>
        /// The split tunnel mode. Valid values are `include` or `exclude`.
        /// </summary>
        [Input("mode")]
        public Input<string>? Mode { get; set; }

        [Input("tunnels")]
        private InputList<Inputs.SplitTunnelTunnelGetArgs>? _tunnels;

        /// <summary>
        /// The value of the tunnel attributes (refer to the nested schema).
        /// </summary>
        public InputList<Inputs.SplitTunnelTunnelGetArgs> Tunnels
        {
            get => _tunnels ?? (_tunnels = new InputList<Inputs.SplitTunnelTunnelGetArgs>());
            set => _tunnels = value;
        }

        public SplitTunnelState()
        {
        }
    }
}
