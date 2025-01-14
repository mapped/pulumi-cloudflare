// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudflare

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to lookup a single [Access Identity Provider][accessIdentityProviderGuide] by name.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-cloudflare/sdk/v4/go/cloudflare"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		mainAccessIdentityProvider, err := cloudflare.LookupAccessIdentityProvider(ctx, &GetAccessIdentityProviderArgs{
// 			Name:      "Google SSO",
// 			AccountId: pulumi.StringRef("example-account-id"),
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = cloudflare.NewAccessApplication(ctx, "mainAccessApplication", &cloudflare.AccessApplicationArgs{
// 			ZoneId:          pulumi.String("example.com"),
// 			Name:            pulumi.String("name"),
// 			Domain:          pulumi.String("name.example.com"),
// 			Type:            pulumi.String("self_hosted"),
// 			SessionDuration: pulumi.String("24h"),
// 			AllowedIdps: pulumi.StringArray{
// 				pulumi.String(mainAccessIdentityProvider.Id),
// 			},
// 			AutoRedirectToIdentity: pulumi.Bool(true),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupAccessIdentityProvider(ctx *pulumi.Context, args *LookupAccessIdentityProviderArgs, opts ...pulumi.InvokeOption) (*LookupAccessIdentityProviderResult, error) {
	var rv LookupAccessIdentityProviderResult
	err := ctx.Invoke("cloudflare:index/getAccessIdentityProvider:getAccessIdentityProvider", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getAccessIdentityProvider.
type LookupAccessIdentityProviderArgs struct {
	// The account for which to look for an Access Identity Provider. Conflicts with `zoneId`.
	AccountId *string `pulumi:"accountId"`
	// Access Identity Provider name to search for.
	Name string `pulumi:"name"`
	// The Zone's ID. Conflicts with `accountId`.
	ZoneId *string `pulumi:"zoneId"`
}

// A collection of values returned by getAccessIdentityProvider.
type LookupAccessIdentityProviderResult struct {
	AccountId *string `pulumi:"accountId"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// Access Identity Provider Name
	Name string `pulumi:"name"`
	// Access Identity Provider Type
	Type   string  `pulumi:"type"`
	ZoneId *string `pulumi:"zoneId"`
}

func LookupAccessIdentityProviderOutput(ctx *pulumi.Context, args LookupAccessIdentityProviderOutputArgs, opts ...pulumi.InvokeOption) LookupAccessIdentityProviderResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupAccessIdentityProviderResult, error) {
			args := v.(LookupAccessIdentityProviderArgs)
			r, err := LookupAccessIdentityProvider(ctx, &args, opts...)
			var s LookupAccessIdentityProviderResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupAccessIdentityProviderResultOutput)
}

// A collection of arguments for invoking getAccessIdentityProvider.
type LookupAccessIdentityProviderOutputArgs struct {
	// The account for which to look for an Access Identity Provider. Conflicts with `zoneId`.
	AccountId pulumi.StringPtrInput `pulumi:"accountId"`
	// Access Identity Provider name to search for.
	Name pulumi.StringInput `pulumi:"name"`
	// The Zone's ID. Conflicts with `accountId`.
	ZoneId pulumi.StringPtrInput `pulumi:"zoneId"`
}

func (LookupAccessIdentityProviderOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAccessIdentityProviderArgs)(nil)).Elem()
}

// A collection of values returned by getAccessIdentityProvider.
type LookupAccessIdentityProviderResultOutput struct{ *pulumi.OutputState }

func (LookupAccessIdentityProviderResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAccessIdentityProviderResult)(nil)).Elem()
}

func (o LookupAccessIdentityProviderResultOutput) ToLookupAccessIdentityProviderResultOutput() LookupAccessIdentityProviderResultOutput {
	return o
}

func (o LookupAccessIdentityProviderResultOutput) ToLookupAccessIdentityProviderResultOutputWithContext(ctx context.Context) LookupAccessIdentityProviderResultOutput {
	return o
}

func (o LookupAccessIdentityProviderResultOutput) AccountId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAccessIdentityProviderResult) *string { return v.AccountId }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupAccessIdentityProviderResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAccessIdentityProviderResult) string { return v.Id }).(pulumi.StringOutput)
}

// Access Identity Provider Name
func (o LookupAccessIdentityProviderResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAccessIdentityProviderResult) string { return v.Name }).(pulumi.StringOutput)
}

// Access Identity Provider Type
func (o LookupAccessIdentityProviderResultOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAccessIdentityProviderResult) string { return v.Type }).(pulumi.StringOutput)
}

func (o LookupAccessIdentityProviderResultOutput) ZoneId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAccessIdentityProviderResult) *string { return v.ZoneId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAccessIdentityProviderResultOutput{})
}
