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
    public sealed class TeamsAccountBlockPage
    {
        /// <summary>
        /// Hex code of block page background color.
        /// </summary>
        public readonly string? BackgroundColor;
        /// <summary>
        /// Indicator of enablement.
        /// </summary>
        public readonly bool? Enabled;
        /// <summary>
        /// Block page header text.
        /// </summary>
        public readonly string? FooterText;
        /// <summary>
        /// Block page footer text.
        /// </summary>
        public readonly string? HeaderText;
        /// <summary>
        /// URL of block page logo.
        /// </summary>
        public readonly string? LogoPath;
        /// <summary>
        /// Name of block page configuration.
        /// </summary>
        public readonly string? Name;

        [OutputConstructor]
        private TeamsAccountBlockPage(
            string? backgroundColor,

            bool? enabled,

            string? footerText,

            string? headerText,

            string? logoPath,

            string? name)
        {
            BackgroundColor = backgroundColor;
            Enabled = enabled;
            FooterText = footerText;
            HeaderText = headerText;
            LogoPath = logoPath;
            Name = name;
        }
    }
}