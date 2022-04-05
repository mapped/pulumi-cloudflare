// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudflare

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a Cloudflare Teams Proxy Endpoint resource. Teams Proxy Endpoints are used for pointing proxy clients at
// Cloudflare Secure Gateway.
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
// 		_, err := cloudflare.NewTeamsProxyEndpoint(ctx, "corporateOffice", &cloudflare.TeamsProxyEndpointArgs{
// 			AccountId: pulumi.String("1d5fdc9e88c8a8c4518b068cd94331fe"),
// 			Ips: pulumi.StringArray{
// 				pulumi.String("192.0.2.0/24"),
// 			},
// 			Name: pulumi.String("office"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// Teams Proxy Endpoints can be imported using a composite ID formed of account ID and teams proxy_endpoint ID.
//
// ```sh
//  $ pulumi import cloudflare:index/teamsProxyEndpoint:TeamsProxyEndpoint corporate_office cb029e245cfdd66dc8d2e570d5dd3322/d41d8cd98f00b204e9800998ecf8427e
// ```
type TeamsProxyEndpoint struct {
	pulumi.CustomResourceState

	// The account to which the teams proxy endpoint should be added.
	AccountId pulumi.StringOutput `pulumi:"accountId"`
	// The networks CIDRs that will be allowed to initiate proxy connections.
	Ips pulumi.StringArrayOutput `pulumi:"ips"`
	// Name of the teams proxy endpoint.
	Name pulumi.StringOutput `pulumi:"name"`
	// The FQDN that proxy clients should be pointed at.
	Subdomain pulumi.StringOutput `pulumi:"subdomain"`
}

// NewTeamsProxyEndpoint registers a new resource with the given unique name, arguments, and options.
func NewTeamsProxyEndpoint(ctx *pulumi.Context,
	name string, args *TeamsProxyEndpointArgs, opts ...pulumi.ResourceOption) (*TeamsProxyEndpoint, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AccountId == nil {
		return nil, errors.New("invalid value for required argument 'AccountId'")
	}
	if args.Ips == nil {
		return nil, errors.New("invalid value for required argument 'Ips'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	var resource TeamsProxyEndpoint
	err := ctx.RegisterResource("cloudflare:index/teamsProxyEndpoint:TeamsProxyEndpoint", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTeamsProxyEndpoint gets an existing TeamsProxyEndpoint resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTeamsProxyEndpoint(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TeamsProxyEndpointState, opts ...pulumi.ResourceOption) (*TeamsProxyEndpoint, error) {
	var resource TeamsProxyEndpoint
	err := ctx.ReadResource("cloudflare:index/teamsProxyEndpoint:TeamsProxyEndpoint", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TeamsProxyEndpoint resources.
type teamsProxyEndpointState struct {
	// The account to which the teams proxy endpoint should be added.
	AccountId *string `pulumi:"accountId"`
	// The networks CIDRs that will be allowed to initiate proxy connections.
	Ips []string `pulumi:"ips"`
	// Name of the teams proxy endpoint.
	Name *string `pulumi:"name"`
	// The FQDN that proxy clients should be pointed at.
	Subdomain *string `pulumi:"subdomain"`
}

type TeamsProxyEndpointState struct {
	// The account to which the teams proxy endpoint should be added.
	AccountId pulumi.StringPtrInput
	// The networks CIDRs that will be allowed to initiate proxy connections.
	Ips pulumi.StringArrayInput
	// Name of the teams proxy endpoint.
	Name pulumi.StringPtrInput
	// The FQDN that proxy clients should be pointed at.
	Subdomain pulumi.StringPtrInput
}

func (TeamsProxyEndpointState) ElementType() reflect.Type {
	return reflect.TypeOf((*teamsProxyEndpointState)(nil)).Elem()
}

type teamsProxyEndpointArgs struct {
	// The account to which the teams proxy endpoint should be added.
	AccountId string `pulumi:"accountId"`
	// The networks CIDRs that will be allowed to initiate proxy connections.
	Ips []string `pulumi:"ips"`
	// Name of the teams proxy endpoint.
	Name string `pulumi:"name"`
}

// The set of arguments for constructing a TeamsProxyEndpoint resource.
type TeamsProxyEndpointArgs struct {
	// The account to which the teams proxy endpoint should be added.
	AccountId pulumi.StringInput
	// The networks CIDRs that will be allowed to initiate proxy connections.
	Ips pulumi.StringArrayInput
	// Name of the teams proxy endpoint.
	Name pulumi.StringInput
}

func (TeamsProxyEndpointArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*teamsProxyEndpointArgs)(nil)).Elem()
}

type TeamsProxyEndpointInput interface {
	pulumi.Input

	ToTeamsProxyEndpointOutput() TeamsProxyEndpointOutput
	ToTeamsProxyEndpointOutputWithContext(ctx context.Context) TeamsProxyEndpointOutput
}

func (*TeamsProxyEndpoint) ElementType() reflect.Type {
	return reflect.TypeOf((**TeamsProxyEndpoint)(nil)).Elem()
}

func (i *TeamsProxyEndpoint) ToTeamsProxyEndpointOutput() TeamsProxyEndpointOutput {
	return i.ToTeamsProxyEndpointOutputWithContext(context.Background())
}

func (i *TeamsProxyEndpoint) ToTeamsProxyEndpointOutputWithContext(ctx context.Context) TeamsProxyEndpointOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TeamsProxyEndpointOutput)
}

// TeamsProxyEndpointArrayInput is an input type that accepts TeamsProxyEndpointArray and TeamsProxyEndpointArrayOutput values.
// You can construct a concrete instance of `TeamsProxyEndpointArrayInput` via:
//
//          TeamsProxyEndpointArray{ TeamsProxyEndpointArgs{...} }
type TeamsProxyEndpointArrayInput interface {
	pulumi.Input

	ToTeamsProxyEndpointArrayOutput() TeamsProxyEndpointArrayOutput
	ToTeamsProxyEndpointArrayOutputWithContext(context.Context) TeamsProxyEndpointArrayOutput
}

type TeamsProxyEndpointArray []TeamsProxyEndpointInput

func (TeamsProxyEndpointArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*TeamsProxyEndpoint)(nil)).Elem()
}

func (i TeamsProxyEndpointArray) ToTeamsProxyEndpointArrayOutput() TeamsProxyEndpointArrayOutput {
	return i.ToTeamsProxyEndpointArrayOutputWithContext(context.Background())
}

func (i TeamsProxyEndpointArray) ToTeamsProxyEndpointArrayOutputWithContext(ctx context.Context) TeamsProxyEndpointArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TeamsProxyEndpointArrayOutput)
}

// TeamsProxyEndpointMapInput is an input type that accepts TeamsProxyEndpointMap and TeamsProxyEndpointMapOutput values.
// You can construct a concrete instance of `TeamsProxyEndpointMapInput` via:
//
//          TeamsProxyEndpointMap{ "key": TeamsProxyEndpointArgs{...} }
type TeamsProxyEndpointMapInput interface {
	pulumi.Input

	ToTeamsProxyEndpointMapOutput() TeamsProxyEndpointMapOutput
	ToTeamsProxyEndpointMapOutputWithContext(context.Context) TeamsProxyEndpointMapOutput
}

type TeamsProxyEndpointMap map[string]TeamsProxyEndpointInput

func (TeamsProxyEndpointMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*TeamsProxyEndpoint)(nil)).Elem()
}

func (i TeamsProxyEndpointMap) ToTeamsProxyEndpointMapOutput() TeamsProxyEndpointMapOutput {
	return i.ToTeamsProxyEndpointMapOutputWithContext(context.Background())
}

func (i TeamsProxyEndpointMap) ToTeamsProxyEndpointMapOutputWithContext(ctx context.Context) TeamsProxyEndpointMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TeamsProxyEndpointMapOutput)
}

type TeamsProxyEndpointOutput struct{ *pulumi.OutputState }

func (TeamsProxyEndpointOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TeamsProxyEndpoint)(nil)).Elem()
}

func (o TeamsProxyEndpointOutput) ToTeamsProxyEndpointOutput() TeamsProxyEndpointOutput {
	return o
}

func (o TeamsProxyEndpointOutput) ToTeamsProxyEndpointOutputWithContext(ctx context.Context) TeamsProxyEndpointOutput {
	return o
}

type TeamsProxyEndpointArrayOutput struct{ *pulumi.OutputState }

func (TeamsProxyEndpointArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*TeamsProxyEndpoint)(nil)).Elem()
}

func (o TeamsProxyEndpointArrayOutput) ToTeamsProxyEndpointArrayOutput() TeamsProxyEndpointArrayOutput {
	return o
}

func (o TeamsProxyEndpointArrayOutput) ToTeamsProxyEndpointArrayOutputWithContext(ctx context.Context) TeamsProxyEndpointArrayOutput {
	return o
}

func (o TeamsProxyEndpointArrayOutput) Index(i pulumi.IntInput) TeamsProxyEndpointOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *TeamsProxyEndpoint {
		return vs[0].([]*TeamsProxyEndpoint)[vs[1].(int)]
	}).(TeamsProxyEndpointOutput)
}

type TeamsProxyEndpointMapOutput struct{ *pulumi.OutputState }

func (TeamsProxyEndpointMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*TeamsProxyEndpoint)(nil)).Elem()
}

func (o TeamsProxyEndpointMapOutput) ToTeamsProxyEndpointMapOutput() TeamsProxyEndpointMapOutput {
	return o
}

func (o TeamsProxyEndpointMapOutput) ToTeamsProxyEndpointMapOutputWithContext(ctx context.Context) TeamsProxyEndpointMapOutput {
	return o
}

func (o TeamsProxyEndpointMapOutput) MapIndex(k pulumi.StringInput) TeamsProxyEndpointOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *TeamsProxyEndpoint {
		return vs[0].(map[string]*TeamsProxyEndpoint)[vs[1].(string)]
	}).(TeamsProxyEndpointOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TeamsProxyEndpointInput)(nil)).Elem(), &TeamsProxyEndpoint{})
	pulumi.RegisterInputType(reflect.TypeOf((*TeamsProxyEndpointArrayInput)(nil)).Elem(), TeamsProxyEndpointArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*TeamsProxyEndpointMapInput)(nil)).Elem(), TeamsProxyEndpointMap{})
	pulumi.RegisterOutputType(TeamsProxyEndpointOutput{})
	pulumi.RegisterOutputType(TeamsProxyEndpointArrayOutput{})
	pulumi.RegisterOutputType(TeamsProxyEndpointMapOutput{})
}