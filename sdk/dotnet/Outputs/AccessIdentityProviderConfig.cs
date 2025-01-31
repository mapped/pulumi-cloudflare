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
    public sealed class AccessIdentityProviderConfig
    {
        public readonly string? ApiToken;
        public readonly string? AppsDomain;
        public readonly ImmutableArray<string> Attributes;
        public readonly string? AuthUrl;
        public readonly string? CentrifyAccount;
        public readonly string? CentrifyAppId;
        public readonly string? CertsUrl;
        public readonly string? ClientId;
        public readonly string? ClientSecret;
        public readonly string? DirectoryId;
        public readonly string? EmailAttributeName;
        public readonly string? IdpPublicCert;
        public readonly string? IssuerUrl;
        public readonly string? OktaAccount;
        public readonly string? OneloginAccount;
        public readonly string? RedirectUrl;
        public readonly bool? SignRequest;
        public readonly string? SsoTargetUrl;
        public readonly bool? SupportGroups;
        public readonly string? TokenUrl;

        [OutputConstructor]
        private AccessIdentityProviderConfig(
            string? apiToken,

            string? appsDomain,

            ImmutableArray<string> attributes,

            string? authUrl,

            string? centrifyAccount,

            string? centrifyAppId,

            string? certsUrl,

            string? clientId,

            string? clientSecret,

            string? directoryId,

            string? emailAttributeName,

            string? idpPublicCert,

            string? issuerUrl,

            string? oktaAccount,

            string? oneloginAccount,

            string? redirectUrl,

            bool? signRequest,

            string? ssoTargetUrl,

            bool? supportGroups,

            string? tokenUrl)
        {
            ApiToken = apiToken;
            AppsDomain = appsDomain;
            Attributes = attributes;
            AuthUrl = authUrl;
            CentrifyAccount = centrifyAccount;
            CentrifyAppId = centrifyAppId;
            CertsUrl = certsUrl;
            ClientId = clientId;
            ClientSecret = clientSecret;
            DirectoryId = directoryId;
            EmailAttributeName = emailAttributeName;
            IdpPublicCert = idpPublicCert;
            IssuerUrl = issuerUrl;
            OktaAccount = oktaAccount;
            OneloginAccount = oneloginAccount;
            RedirectUrl = redirectUrl;
            SignRequest = signRequest;
            SsoTargetUrl = ssoTargetUrl;
            SupportGroups = supportGroups;
            TokenUrl = tokenUrl;
        }
    }
}
