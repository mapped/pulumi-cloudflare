// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudflare

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a resource, that manages Cloudflare tunnel virtual networks for Zero Trust. Tunnel
// virtual networks are used for segregation of Tunnel IP Routes via Virtualized Networks to
// handle overlapping private IPs in your origins..
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
// 		_, err := cloudflare.NewTunnelVirtualNetwork(ctx, "example", &cloudflare.TunnelVirtualNetworkArgs{
// 			AccountId: pulumi.String("c4a7362d577a6c3019a474fd6f485821"),
// 			Comment:   pulumi.String("New tunnel virtual network for documentation"),
// 			Name:      pulumi.String("vnet-for-documentation"),
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
// An existing tunnel virtual networks can be imported using the account ID and virtual network ID.
//
// ```sh
//  $ pulumi import cloudflare:index/tunnelVirtualNetwork:TunnelVirtualNetwork cloudflare_tunnel_virtual_network c4a7362d577a6c3019a474fd6f485821/3c8ff8af-b487-45bd-89e3-4c85a1532600
// ```
type TunnelVirtualNetwork struct {
	pulumi.CustomResourceState

	// The ID of the account where the tunnel virtual network is being created.
	AccountId pulumi.StringOutput `pulumi:"accountId"`
	// Description of the tunnel virtual network.
	Comment pulumi.StringPtrOutput `pulumi:"comment"`
	// Whether this virtual network is the default one for the account. This means IP Routes belong to this virtual network and Teams Clients in the account route through this virtual network, unless specified otherwise for each case.
	IsDefaultNetwork pulumi.BoolPtrOutput `pulumi:"isDefaultNetwork"`
	// A user-friendly name chosen when the virtual network is created.
	Name pulumi.StringOutput `pulumi:"name"`
}

// NewTunnelVirtualNetwork registers a new resource with the given unique name, arguments, and options.
func NewTunnelVirtualNetwork(ctx *pulumi.Context,
	name string, args *TunnelVirtualNetworkArgs, opts ...pulumi.ResourceOption) (*TunnelVirtualNetwork, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AccountId == nil {
		return nil, errors.New("invalid value for required argument 'AccountId'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	var resource TunnelVirtualNetwork
	err := ctx.RegisterResource("cloudflare:index/tunnelVirtualNetwork:TunnelVirtualNetwork", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTunnelVirtualNetwork gets an existing TunnelVirtualNetwork resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTunnelVirtualNetwork(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TunnelVirtualNetworkState, opts ...pulumi.ResourceOption) (*TunnelVirtualNetwork, error) {
	var resource TunnelVirtualNetwork
	err := ctx.ReadResource("cloudflare:index/tunnelVirtualNetwork:TunnelVirtualNetwork", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TunnelVirtualNetwork resources.
type tunnelVirtualNetworkState struct {
	// The ID of the account where the tunnel virtual network is being created.
	AccountId *string `pulumi:"accountId"`
	// Description of the tunnel virtual network.
	Comment *string `pulumi:"comment"`
	// Whether this virtual network is the default one for the account. This means IP Routes belong to this virtual network and Teams Clients in the account route through this virtual network, unless specified otherwise for each case.
	IsDefaultNetwork *bool `pulumi:"isDefaultNetwork"`
	// A user-friendly name chosen when the virtual network is created.
	Name *string `pulumi:"name"`
}

type TunnelVirtualNetworkState struct {
	// The ID of the account where the tunnel virtual network is being created.
	AccountId pulumi.StringPtrInput
	// Description of the tunnel virtual network.
	Comment pulumi.StringPtrInput
	// Whether this virtual network is the default one for the account. This means IP Routes belong to this virtual network and Teams Clients in the account route through this virtual network, unless specified otherwise for each case.
	IsDefaultNetwork pulumi.BoolPtrInput
	// A user-friendly name chosen when the virtual network is created.
	Name pulumi.StringPtrInput
}

func (TunnelVirtualNetworkState) ElementType() reflect.Type {
	return reflect.TypeOf((*tunnelVirtualNetworkState)(nil)).Elem()
}

type tunnelVirtualNetworkArgs struct {
	// The ID of the account where the tunnel virtual network is being created.
	AccountId string `pulumi:"accountId"`
	// Description of the tunnel virtual network.
	Comment *string `pulumi:"comment"`
	// Whether this virtual network is the default one for the account. This means IP Routes belong to this virtual network and Teams Clients in the account route through this virtual network, unless specified otherwise for each case.
	IsDefaultNetwork *bool `pulumi:"isDefaultNetwork"`
	// A user-friendly name chosen when the virtual network is created.
	Name string `pulumi:"name"`
}

// The set of arguments for constructing a TunnelVirtualNetwork resource.
type TunnelVirtualNetworkArgs struct {
	// The ID of the account where the tunnel virtual network is being created.
	AccountId pulumi.StringInput
	// Description of the tunnel virtual network.
	Comment pulumi.StringPtrInput
	// Whether this virtual network is the default one for the account. This means IP Routes belong to this virtual network and Teams Clients in the account route through this virtual network, unless specified otherwise for each case.
	IsDefaultNetwork pulumi.BoolPtrInput
	// A user-friendly name chosen when the virtual network is created.
	Name pulumi.StringInput
}

func (TunnelVirtualNetworkArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*tunnelVirtualNetworkArgs)(nil)).Elem()
}

type TunnelVirtualNetworkInput interface {
	pulumi.Input

	ToTunnelVirtualNetworkOutput() TunnelVirtualNetworkOutput
	ToTunnelVirtualNetworkOutputWithContext(ctx context.Context) TunnelVirtualNetworkOutput
}

func (*TunnelVirtualNetwork) ElementType() reflect.Type {
	return reflect.TypeOf((**TunnelVirtualNetwork)(nil)).Elem()
}

func (i *TunnelVirtualNetwork) ToTunnelVirtualNetworkOutput() TunnelVirtualNetworkOutput {
	return i.ToTunnelVirtualNetworkOutputWithContext(context.Background())
}

func (i *TunnelVirtualNetwork) ToTunnelVirtualNetworkOutputWithContext(ctx context.Context) TunnelVirtualNetworkOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TunnelVirtualNetworkOutput)
}

// TunnelVirtualNetworkArrayInput is an input type that accepts TunnelVirtualNetworkArray and TunnelVirtualNetworkArrayOutput values.
// You can construct a concrete instance of `TunnelVirtualNetworkArrayInput` via:
//
//          TunnelVirtualNetworkArray{ TunnelVirtualNetworkArgs{...} }
type TunnelVirtualNetworkArrayInput interface {
	pulumi.Input

	ToTunnelVirtualNetworkArrayOutput() TunnelVirtualNetworkArrayOutput
	ToTunnelVirtualNetworkArrayOutputWithContext(context.Context) TunnelVirtualNetworkArrayOutput
}

type TunnelVirtualNetworkArray []TunnelVirtualNetworkInput

func (TunnelVirtualNetworkArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*TunnelVirtualNetwork)(nil)).Elem()
}

func (i TunnelVirtualNetworkArray) ToTunnelVirtualNetworkArrayOutput() TunnelVirtualNetworkArrayOutput {
	return i.ToTunnelVirtualNetworkArrayOutputWithContext(context.Background())
}

func (i TunnelVirtualNetworkArray) ToTunnelVirtualNetworkArrayOutputWithContext(ctx context.Context) TunnelVirtualNetworkArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TunnelVirtualNetworkArrayOutput)
}

// TunnelVirtualNetworkMapInput is an input type that accepts TunnelVirtualNetworkMap and TunnelVirtualNetworkMapOutput values.
// You can construct a concrete instance of `TunnelVirtualNetworkMapInput` via:
//
//          TunnelVirtualNetworkMap{ "key": TunnelVirtualNetworkArgs{...} }
type TunnelVirtualNetworkMapInput interface {
	pulumi.Input

	ToTunnelVirtualNetworkMapOutput() TunnelVirtualNetworkMapOutput
	ToTunnelVirtualNetworkMapOutputWithContext(context.Context) TunnelVirtualNetworkMapOutput
}

type TunnelVirtualNetworkMap map[string]TunnelVirtualNetworkInput

func (TunnelVirtualNetworkMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*TunnelVirtualNetwork)(nil)).Elem()
}

func (i TunnelVirtualNetworkMap) ToTunnelVirtualNetworkMapOutput() TunnelVirtualNetworkMapOutput {
	return i.ToTunnelVirtualNetworkMapOutputWithContext(context.Background())
}

func (i TunnelVirtualNetworkMap) ToTunnelVirtualNetworkMapOutputWithContext(ctx context.Context) TunnelVirtualNetworkMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TunnelVirtualNetworkMapOutput)
}

type TunnelVirtualNetworkOutput struct{ *pulumi.OutputState }

func (TunnelVirtualNetworkOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TunnelVirtualNetwork)(nil)).Elem()
}

func (o TunnelVirtualNetworkOutput) ToTunnelVirtualNetworkOutput() TunnelVirtualNetworkOutput {
	return o
}

func (o TunnelVirtualNetworkOutput) ToTunnelVirtualNetworkOutputWithContext(ctx context.Context) TunnelVirtualNetworkOutput {
	return o
}

// The ID of the account where the tunnel virtual network is being created.
func (o TunnelVirtualNetworkOutput) AccountId() pulumi.StringOutput {
	return o.ApplyT(func(v *TunnelVirtualNetwork) pulumi.StringOutput { return v.AccountId }).(pulumi.StringOutput)
}

// Description of the tunnel virtual network.
func (o TunnelVirtualNetworkOutput) Comment() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *TunnelVirtualNetwork) pulumi.StringPtrOutput { return v.Comment }).(pulumi.StringPtrOutput)
}

// Whether this virtual network is the default one for the account. This means IP Routes belong to this virtual network and Teams Clients in the account route through this virtual network, unless specified otherwise for each case.
func (o TunnelVirtualNetworkOutput) IsDefaultNetwork() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *TunnelVirtualNetwork) pulumi.BoolPtrOutput { return v.IsDefaultNetwork }).(pulumi.BoolPtrOutput)
}

// A user-friendly name chosen when the virtual network is created.
func (o TunnelVirtualNetworkOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *TunnelVirtualNetwork) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

type TunnelVirtualNetworkArrayOutput struct{ *pulumi.OutputState }

func (TunnelVirtualNetworkArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*TunnelVirtualNetwork)(nil)).Elem()
}

func (o TunnelVirtualNetworkArrayOutput) ToTunnelVirtualNetworkArrayOutput() TunnelVirtualNetworkArrayOutput {
	return o
}

func (o TunnelVirtualNetworkArrayOutput) ToTunnelVirtualNetworkArrayOutputWithContext(ctx context.Context) TunnelVirtualNetworkArrayOutput {
	return o
}

func (o TunnelVirtualNetworkArrayOutput) Index(i pulumi.IntInput) TunnelVirtualNetworkOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *TunnelVirtualNetwork {
		return vs[0].([]*TunnelVirtualNetwork)[vs[1].(int)]
	}).(TunnelVirtualNetworkOutput)
}

type TunnelVirtualNetworkMapOutput struct{ *pulumi.OutputState }

func (TunnelVirtualNetworkMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*TunnelVirtualNetwork)(nil)).Elem()
}

func (o TunnelVirtualNetworkMapOutput) ToTunnelVirtualNetworkMapOutput() TunnelVirtualNetworkMapOutput {
	return o
}

func (o TunnelVirtualNetworkMapOutput) ToTunnelVirtualNetworkMapOutputWithContext(ctx context.Context) TunnelVirtualNetworkMapOutput {
	return o
}

func (o TunnelVirtualNetworkMapOutput) MapIndex(k pulumi.StringInput) TunnelVirtualNetworkOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *TunnelVirtualNetwork {
		return vs[0].(map[string]*TunnelVirtualNetwork)[vs[1].(string)]
	}).(TunnelVirtualNetworkOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TunnelVirtualNetworkInput)(nil)).Elem(), &TunnelVirtualNetwork{})
	pulumi.RegisterInputType(reflect.TypeOf((*TunnelVirtualNetworkArrayInput)(nil)).Elem(), TunnelVirtualNetworkArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*TunnelVirtualNetworkMapInput)(nil)).Elem(), TunnelVirtualNetworkMap{})
	pulumi.RegisterOutputType(TunnelVirtualNetworkOutput{})
	pulumi.RegisterOutputType(TunnelVirtualNetworkArrayOutput{})
	pulumi.RegisterOutputType(TunnelVirtualNetworkMapOutput{})
}
