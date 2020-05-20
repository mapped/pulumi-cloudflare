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
    public sealed class PageRuleActionsCacheKeyFieldsHeader
    {
        /// <summary>
        /// Check for presence of specified HTTP headers, without including their actual values.
        /// </summary>
        public readonly ImmutableArray<string> CheckPresences;
        /// <summary>
        /// Exclude these query string parameters from Cache Key.
        /// </summary>
        public readonly ImmutableArray<string> Excludes;
        /// <summary>
        /// Only use values of specified query string parameters in Cache Key.
        /// </summary>
        public readonly ImmutableArray<string> Includes;

        [OutputConstructor]
        private PageRuleActionsCacheKeyFieldsHeader(
            ImmutableArray<string> checkPresences,

            ImmutableArray<string> excludes,

            ImmutableArray<string> includes)
        {
            CheckPresences = checkPresences;
            Excludes = excludes;
            Includes = includes;
        }
    }
}
