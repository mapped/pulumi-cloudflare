// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudflare
{
    public static class GetWafPackages
    {
        /// <summary>
        /// Use this data source to look up [WAF Rule Packages](https://api.cloudflare.com/#waf-rule-packages-properties).
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// The example below matches all `high` sensitivity WAF Rule Packages, with a `challenge` action mode and an `anomaly` detection mode, that contain the word `example`. The matched WAF Rule Packages are then returned as output.
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Cloudflare = Pulumi.Cloudflare;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var test = Output.Create(Cloudflare.GetWafPackages.InvokeAsync(new Cloudflare.GetWafPackagesArgs
        ///         {
        ///             Filter = new Cloudflare.Inputs.GetWafPackagesFilterArgs
        ///             {
        ///                 Name = ".*example.*",
        ///                 DetectionMode = "anomaly",
        ///                 Sensitivity = "high",
        ///                 ActionMode = "challenge",
        ///             },
        ///         }));
        ///         this.WafPackages = test.Apply(test =&gt; test.Packages);
        ///     }
        /// 
        ///     [Output("wafPackages")]
        ///     public Output&lt;string&gt; WafPackages { get; set; }
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetWafPackagesResult> InvokeAsync(GetWafPackagesArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetWafPackagesResult>("cloudflare:index/getWafPackages:getWafPackages", args ?? new GetWafPackagesArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to look up [WAF Rule Packages](https://api.cloudflare.com/#waf-rule-packages-properties).
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// The example below matches all `high` sensitivity WAF Rule Packages, with a `challenge` action mode and an `anomaly` detection mode, that contain the word `example`. The matched WAF Rule Packages are then returned as output.
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Cloudflare = Pulumi.Cloudflare;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var test = Output.Create(Cloudflare.GetWafPackages.InvokeAsync(new Cloudflare.GetWafPackagesArgs
        ///         {
        ///             Filter = new Cloudflare.Inputs.GetWafPackagesFilterArgs
        ///             {
        ///                 Name = ".*example.*",
        ///                 DetectionMode = "anomaly",
        ///                 Sensitivity = "high",
        ///                 ActionMode = "challenge",
        ///             },
        ///         }));
        ///         this.WafPackages = test.Apply(test =&gt; test.Packages);
        ///     }
        /// 
        ///     [Output("wafPackages")]
        ///     public Output&lt;string&gt; WafPackages { get; set; }
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetWafPackagesResult> Invoke(GetWafPackagesInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetWafPackagesResult>("cloudflare:index/getWafPackages:getWafPackages", args ?? new GetWafPackagesInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetWafPackagesArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// One or more values used to look up WAF Rule Packages. If more than one value is given all
        /// values must match in order to be included, see below for full list.
        /// </summary>
        [Input("filter")]
        public Inputs.GetWafPackagesFilterArgs? Filter { get; set; }

        /// <summary>
        /// The ID of the DNS zone in which to search for the WAF Rule Packages.
        /// </summary>
        [Input("zoneId", required: true)]
        public string ZoneId { get; set; } = null!;

        public GetWafPackagesArgs()
        {
        }
    }

    public sealed class GetWafPackagesInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// One or more values used to look up WAF Rule Packages. If more than one value is given all
        /// values must match in order to be included, see below for full list.
        /// </summary>
        [Input("filter")]
        public Input<Inputs.GetWafPackagesFilterInputArgs>? Filter { get; set; }

        /// <summary>
        /// The ID of the DNS zone in which to search for the WAF Rule Packages.
        /// </summary>
        [Input("zoneId", required: true)]
        public Input<string> ZoneId { get; set; } = null!;

        public GetWafPackagesInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetWafPackagesResult
    {
        public readonly Outputs.GetWafPackagesFilterResult? Filter;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// A map of WAF Rule Packages details. Full list below:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetWafPackagesPackageResult> Packages;
        public readonly string ZoneId;

        [OutputConstructor]
        private GetWafPackagesResult(
            Outputs.GetWafPackagesFilterResult? filter,

            string id,

            ImmutableArray<Outputs.GetWafPackagesPackageResult> packages,

            string zoneId)
        {
            Filter = filter;
            Id = id;
            Packages = packages;
            ZoneId = zoneId;
        }
    }
}
