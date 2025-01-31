// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudflare
{
    public static class GetWafGroups
    {
        /// <summary>
        /// Use this data source to look up [WAF Rule Groups](https://api.cloudflare.com/#waf-rule-groups-properties).
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// The example below matches all WAF Rule Groups that contain the word `example` and are currently `on`. The matched WAF Rule Groups are then returned as output.
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Cloudflare = Pulumi.Cloudflare;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var test = Output.Create(Cloudflare.GetWafGroups.InvokeAsync(new Cloudflare.GetWafGroupsArgs
        ///         {
        ///             Filter = new Cloudflare.Inputs.GetWafGroupsFilterArgs
        ///             {
        ///                 Name = ".*example.*",
        ///                 Mode = "on",
        ///             },
        ///         }));
        ///         this.WafGroups = test.Apply(test =&gt; test.Groups);
        ///     }
        /// 
        ///     [Output("wafGroups")]
        ///     public Output&lt;string&gt; WafGroups { get; set; }
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetWafGroupsResult> InvokeAsync(GetWafGroupsArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetWafGroupsResult>("cloudflare:index/getWafGroups:getWafGroups", args ?? new GetWafGroupsArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to look up [WAF Rule Groups](https://api.cloudflare.com/#waf-rule-groups-properties).
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// The example below matches all WAF Rule Groups that contain the word `example` and are currently `on`. The matched WAF Rule Groups are then returned as output.
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Cloudflare = Pulumi.Cloudflare;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var test = Output.Create(Cloudflare.GetWafGroups.InvokeAsync(new Cloudflare.GetWafGroupsArgs
        ///         {
        ///             Filter = new Cloudflare.Inputs.GetWafGroupsFilterArgs
        ///             {
        ///                 Name = ".*example.*",
        ///                 Mode = "on",
        ///             },
        ///         }));
        ///         this.WafGroups = test.Apply(test =&gt; test.Groups);
        ///     }
        /// 
        ///     [Output("wafGroups")]
        ///     public Output&lt;string&gt; WafGroups { get; set; }
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetWafGroupsResult> Invoke(GetWafGroupsInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetWafGroupsResult>("cloudflare:index/getWafGroups:getWafGroups", args ?? new GetWafGroupsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetWafGroupsArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// One or more values used to look up WAF Rule Groups. If more than one value is given all
        /// values must match in order to be included, see below for full list.
        /// </summary>
        [Input("filter")]
        public Inputs.GetWafGroupsFilterArgs? Filter { get; set; }

        /// <summary>
        /// The ID of the WAF Rule Package in which to search for the WAF Rule Groups.
        /// </summary>
        [Input("packageId")]
        public string? PackageId { get; set; }

        /// <summary>
        /// The ID of the DNS zone in which to search for the WAF Rule Groups.
        /// </summary>
        [Input("zoneId", required: true)]
        public string ZoneId { get; set; } = null!;

        public GetWafGroupsArgs()
        {
        }
    }

    public sealed class GetWafGroupsInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// One or more values used to look up WAF Rule Groups. If more than one value is given all
        /// values must match in order to be included, see below for full list.
        /// </summary>
        [Input("filter")]
        public Input<Inputs.GetWafGroupsFilterInputArgs>? Filter { get; set; }

        /// <summary>
        /// The ID of the WAF Rule Package in which to search for the WAF Rule Groups.
        /// </summary>
        [Input("packageId")]
        public Input<string>? PackageId { get; set; }

        /// <summary>
        /// The ID of the DNS zone in which to search for the WAF Rule Groups.
        /// </summary>
        [Input("zoneId", required: true)]
        public Input<string> ZoneId { get; set; } = null!;

        public GetWafGroupsInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetWafGroupsResult
    {
        public readonly Outputs.GetWafGroupsFilterResult? Filter;
        /// <summary>
        /// A map of WAF Rule Groups details. Full list below:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetWafGroupsGroupResult> Groups;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The ID of the WAF Rule Package that contains the WAF Rule Group
        /// </summary>
        public readonly string? PackageId;
        public readonly string ZoneId;

        [OutputConstructor]
        private GetWafGroupsResult(
            Outputs.GetWafGroupsFilterResult? filter,

            ImmutableArray<Outputs.GetWafGroupsGroupResult> groups,

            string id,

            string? packageId,

            string zoneId)
        {
            Filter = filter;
            Groups = groups;
            Id = id;
            PackageId = packageId;
            ZoneId = zoneId;
        }
    }
}
