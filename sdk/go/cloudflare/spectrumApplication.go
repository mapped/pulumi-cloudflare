// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudflare

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a Cloudflare Spectrum Application. You can extend the power of Cloudflare's DDoS, TLS, and IP Firewall to your other TCP-based services.
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
// 		_, err := cloudflare.NewSpectrumApplication(ctx, "sshProxy", &cloudflare.SpectrumApplicationArgs{
// 			ZoneId:      pulumi.Any(_var.Cloudflare_zone_id),
// 			Protocol:    pulumi.String("tcp/22"),
// 			TrafficType: pulumi.String("direct"),
// 			Dns: &SpectrumApplicationDnsArgs{
// 				Type: pulumi.String("CNAME"),
// 				Name: pulumi.String("ssh.example.com"),
// 			},
// 			OriginDirects: pulumi.StringArray{
// 				pulumi.String("tcp://109.151.40.129:22"),
// 			},
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
// Spectrum resource can be imported using a zone ID and Application ID, e.g.
//
// ```sh
//  $ pulumi import cloudflare:index/spectrumApplication:SpectrumApplication example d41d8cd98f00b204e9800998ecf8427e/9a7806061c88ada191ed06f989cc3dac
// ```
//
//  where* `d41d8cd98f00b204e9800998ecf8427e` - zone ID, as returned from [API](https://api.cloudflare.com/#zone-list-zones) * `9a7806061c88ada191ed06f989cc3dac` - Application ID
type SpectrumApplication struct {
	pulumi.CustomResourceState

	// . Enables Argo Smart Routing. Defaults to `false`.
	ArgoSmartRouting pulumi.BoolPtrOutput `pulumi:"argoSmartRouting"`
	// The name and type of DNS record for the Spectrum application. Fields documented below.
	Dns SpectrumApplicationDnsOutput `pulumi:"dns"`
	// . Choose which types of IP addresses will be provisioned for this subdomain. Valid values are: `all`, `ipv4`, `ipv6`. Defaults to `all`.
	EdgeIpConnectivity pulumi.StringOutput `pulumi:"edgeIpConnectivity"`
	// . A list of edge IPs (IPv4 and/or IPv6) to configure Spectrum application to. Requires [Bring Your Own IP](https://developers.cloudflare.com/spectrum/getting-started/byoip/) provisioned.
	EdgeIps pulumi.StringArrayOutput `pulumi:"edgeIps"`
	// Enables the IP Firewall for this application. Defaults to `true`.
	IpFirewall pulumi.BoolPtrOutput `pulumi:"ipFirewall"`
	// A list of destination addresses to the origin. e.g. `tcp://192.0.2.1:22`.
	OriginDirects pulumi.StringArrayOutput `pulumi:"originDirects"`
	// A destination DNS addresses to the origin. Fields documented below.
	OriginDns SpectrumApplicationOriginDnsPtrOutput `pulumi:"originDns"`
	// If using `originDns` and not `originPortRange`, this is a required attribute. Origin port to proxy traffice to e.g. `22`.
	OriginPort pulumi.IntPtrOutput `pulumi:"originPort"`
	// If using `originDns` and not `originPort`, this is a required attribute. Origin port range to proxy traffice to.  When using a range, the protocol field must also specify a range, e.g. `tcp/22-23`. Fields documented below.
	OriginPortRange SpectrumApplicationOriginPortRangePtrOutput `pulumi:"originPortRange"`
	// The port configuration at Cloudflare’s edge. e.g. `tcp/22`.
	Protocol pulumi.StringOutput `pulumi:"protocol"`
	// Enables a proxy protocol to the origin. Valid values are: `off`, `v1`, `v2`, and `simple`. Defaults to `off`.
	ProxyProtocol pulumi.StringPtrOutput `pulumi:"proxyProtocol"`
	// TLS configuration option for Cloudflare to connect to your origin. Valid values are: `off`, `flexible`, `full` and `strict`. Defaults to `off`.
	Tls pulumi.StringPtrOutput `pulumi:"tls"`
	// Sets application type. Valid values are: `direct`, `http`, `https`.  Defaults to `direct`.
	TrafficType pulumi.StringPtrOutput `pulumi:"trafficType"`
	// The DNS zone ID to add the application to
	ZoneId pulumi.StringOutput `pulumi:"zoneId"`
}

// NewSpectrumApplication registers a new resource with the given unique name, arguments, and options.
func NewSpectrumApplication(ctx *pulumi.Context,
	name string, args *SpectrumApplicationArgs, opts ...pulumi.ResourceOption) (*SpectrumApplication, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Dns == nil {
		return nil, errors.New("invalid value for required argument 'Dns'")
	}
	if args.Protocol == nil {
		return nil, errors.New("invalid value for required argument 'Protocol'")
	}
	if args.ZoneId == nil {
		return nil, errors.New("invalid value for required argument 'ZoneId'")
	}
	var resource SpectrumApplication
	err := ctx.RegisterResource("cloudflare:index/spectrumApplication:SpectrumApplication", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSpectrumApplication gets an existing SpectrumApplication resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSpectrumApplication(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SpectrumApplicationState, opts ...pulumi.ResourceOption) (*SpectrumApplication, error) {
	var resource SpectrumApplication
	err := ctx.ReadResource("cloudflare:index/spectrumApplication:SpectrumApplication", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SpectrumApplication resources.
type spectrumApplicationState struct {
	// . Enables Argo Smart Routing. Defaults to `false`.
	ArgoSmartRouting *bool `pulumi:"argoSmartRouting"`
	// The name and type of DNS record for the Spectrum application. Fields documented below.
	Dns *SpectrumApplicationDns `pulumi:"dns"`
	// . Choose which types of IP addresses will be provisioned for this subdomain. Valid values are: `all`, `ipv4`, `ipv6`. Defaults to `all`.
	EdgeIpConnectivity *string `pulumi:"edgeIpConnectivity"`
	// . A list of edge IPs (IPv4 and/or IPv6) to configure Spectrum application to. Requires [Bring Your Own IP](https://developers.cloudflare.com/spectrum/getting-started/byoip/) provisioned.
	EdgeIps []string `pulumi:"edgeIps"`
	// Enables the IP Firewall for this application. Defaults to `true`.
	IpFirewall *bool `pulumi:"ipFirewall"`
	// A list of destination addresses to the origin. e.g. `tcp://192.0.2.1:22`.
	OriginDirects []string `pulumi:"originDirects"`
	// A destination DNS addresses to the origin. Fields documented below.
	OriginDns *SpectrumApplicationOriginDns `pulumi:"originDns"`
	// If using `originDns` and not `originPortRange`, this is a required attribute. Origin port to proxy traffice to e.g. `22`.
	OriginPort *int `pulumi:"originPort"`
	// If using `originDns` and not `originPort`, this is a required attribute. Origin port range to proxy traffice to.  When using a range, the protocol field must also specify a range, e.g. `tcp/22-23`. Fields documented below.
	OriginPortRange *SpectrumApplicationOriginPortRange `pulumi:"originPortRange"`
	// The port configuration at Cloudflare’s edge. e.g. `tcp/22`.
	Protocol *string `pulumi:"protocol"`
	// Enables a proxy protocol to the origin. Valid values are: `off`, `v1`, `v2`, and `simple`. Defaults to `off`.
	ProxyProtocol *string `pulumi:"proxyProtocol"`
	// TLS configuration option for Cloudflare to connect to your origin. Valid values are: `off`, `flexible`, `full` and `strict`. Defaults to `off`.
	Tls *string `pulumi:"tls"`
	// Sets application type. Valid values are: `direct`, `http`, `https`.  Defaults to `direct`.
	TrafficType *string `pulumi:"trafficType"`
	// The DNS zone ID to add the application to
	ZoneId *string `pulumi:"zoneId"`
}

type SpectrumApplicationState struct {
	// . Enables Argo Smart Routing. Defaults to `false`.
	ArgoSmartRouting pulumi.BoolPtrInput
	// The name and type of DNS record for the Spectrum application. Fields documented below.
	Dns SpectrumApplicationDnsPtrInput
	// . Choose which types of IP addresses will be provisioned for this subdomain. Valid values are: `all`, `ipv4`, `ipv6`. Defaults to `all`.
	EdgeIpConnectivity pulumi.StringPtrInput
	// . A list of edge IPs (IPv4 and/or IPv6) to configure Spectrum application to. Requires [Bring Your Own IP](https://developers.cloudflare.com/spectrum/getting-started/byoip/) provisioned.
	EdgeIps pulumi.StringArrayInput
	// Enables the IP Firewall for this application. Defaults to `true`.
	IpFirewall pulumi.BoolPtrInput
	// A list of destination addresses to the origin. e.g. `tcp://192.0.2.1:22`.
	OriginDirects pulumi.StringArrayInput
	// A destination DNS addresses to the origin. Fields documented below.
	OriginDns SpectrumApplicationOriginDnsPtrInput
	// If using `originDns` and not `originPortRange`, this is a required attribute. Origin port to proxy traffice to e.g. `22`.
	OriginPort pulumi.IntPtrInput
	// If using `originDns` and not `originPort`, this is a required attribute. Origin port range to proxy traffice to.  When using a range, the protocol field must also specify a range, e.g. `tcp/22-23`. Fields documented below.
	OriginPortRange SpectrumApplicationOriginPortRangePtrInput
	// The port configuration at Cloudflare’s edge. e.g. `tcp/22`.
	Protocol pulumi.StringPtrInput
	// Enables a proxy protocol to the origin. Valid values are: `off`, `v1`, `v2`, and `simple`. Defaults to `off`.
	ProxyProtocol pulumi.StringPtrInput
	// TLS configuration option for Cloudflare to connect to your origin. Valid values are: `off`, `flexible`, `full` and `strict`. Defaults to `off`.
	Tls pulumi.StringPtrInput
	// Sets application type. Valid values are: `direct`, `http`, `https`.  Defaults to `direct`.
	TrafficType pulumi.StringPtrInput
	// The DNS zone ID to add the application to
	ZoneId pulumi.StringPtrInput
}

func (SpectrumApplicationState) ElementType() reflect.Type {
	return reflect.TypeOf((*spectrumApplicationState)(nil)).Elem()
}

type spectrumApplicationArgs struct {
	// . Enables Argo Smart Routing. Defaults to `false`.
	ArgoSmartRouting *bool `pulumi:"argoSmartRouting"`
	// The name and type of DNS record for the Spectrum application. Fields documented below.
	Dns SpectrumApplicationDns `pulumi:"dns"`
	// . Choose which types of IP addresses will be provisioned for this subdomain. Valid values are: `all`, `ipv4`, `ipv6`. Defaults to `all`.
	EdgeIpConnectivity *string `pulumi:"edgeIpConnectivity"`
	// . A list of edge IPs (IPv4 and/or IPv6) to configure Spectrum application to. Requires [Bring Your Own IP](https://developers.cloudflare.com/spectrum/getting-started/byoip/) provisioned.
	EdgeIps []string `pulumi:"edgeIps"`
	// Enables the IP Firewall for this application. Defaults to `true`.
	IpFirewall *bool `pulumi:"ipFirewall"`
	// A list of destination addresses to the origin. e.g. `tcp://192.0.2.1:22`.
	OriginDirects []string `pulumi:"originDirects"`
	// A destination DNS addresses to the origin. Fields documented below.
	OriginDns *SpectrumApplicationOriginDns `pulumi:"originDns"`
	// If using `originDns` and not `originPortRange`, this is a required attribute. Origin port to proxy traffice to e.g. `22`.
	OriginPort *int `pulumi:"originPort"`
	// If using `originDns` and not `originPort`, this is a required attribute. Origin port range to proxy traffice to.  When using a range, the protocol field must also specify a range, e.g. `tcp/22-23`. Fields documented below.
	OriginPortRange *SpectrumApplicationOriginPortRange `pulumi:"originPortRange"`
	// The port configuration at Cloudflare’s edge. e.g. `tcp/22`.
	Protocol string `pulumi:"protocol"`
	// Enables a proxy protocol to the origin. Valid values are: `off`, `v1`, `v2`, and `simple`. Defaults to `off`.
	ProxyProtocol *string `pulumi:"proxyProtocol"`
	// TLS configuration option for Cloudflare to connect to your origin. Valid values are: `off`, `flexible`, `full` and `strict`. Defaults to `off`.
	Tls *string `pulumi:"tls"`
	// Sets application type. Valid values are: `direct`, `http`, `https`.  Defaults to `direct`.
	TrafficType *string `pulumi:"trafficType"`
	// The DNS zone ID to add the application to
	ZoneId string `pulumi:"zoneId"`
}

// The set of arguments for constructing a SpectrumApplication resource.
type SpectrumApplicationArgs struct {
	// . Enables Argo Smart Routing. Defaults to `false`.
	ArgoSmartRouting pulumi.BoolPtrInput
	// The name and type of DNS record for the Spectrum application. Fields documented below.
	Dns SpectrumApplicationDnsInput
	// . Choose which types of IP addresses will be provisioned for this subdomain. Valid values are: `all`, `ipv4`, `ipv6`. Defaults to `all`.
	EdgeIpConnectivity pulumi.StringPtrInput
	// . A list of edge IPs (IPv4 and/or IPv6) to configure Spectrum application to. Requires [Bring Your Own IP](https://developers.cloudflare.com/spectrum/getting-started/byoip/) provisioned.
	EdgeIps pulumi.StringArrayInput
	// Enables the IP Firewall for this application. Defaults to `true`.
	IpFirewall pulumi.BoolPtrInput
	// A list of destination addresses to the origin. e.g. `tcp://192.0.2.1:22`.
	OriginDirects pulumi.StringArrayInput
	// A destination DNS addresses to the origin. Fields documented below.
	OriginDns SpectrumApplicationOriginDnsPtrInput
	// If using `originDns` and not `originPortRange`, this is a required attribute. Origin port to proxy traffice to e.g. `22`.
	OriginPort pulumi.IntPtrInput
	// If using `originDns` and not `originPort`, this is a required attribute. Origin port range to proxy traffice to.  When using a range, the protocol field must also specify a range, e.g. `tcp/22-23`. Fields documented below.
	OriginPortRange SpectrumApplicationOriginPortRangePtrInput
	// The port configuration at Cloudflare’s edge. e.g. `tcp/22`.
	Protocol pulumi.StringInput
	// Enables a proxy protocol to the origin. Valid values are: `off`, `v1`, `v2`, and `simple`. Defaults to `off`.
	ProxyProtocol pulumi.StringPtrInput
	// TLS configuration option for Cloudflare to connect to your origin. Valid values are: `off`, `flexible`, `full` and `strict`. Defaults to `off`.
	Tls pulumi.StringPtrInput
	// Sets application type. Valid values are: `direct`, `http`, `https`.  Defaults to `direct`.
	TrafficType pulumi.StringPtrInput
	// The DNS zone ID to add the application to
	ZoneId pulumi.StringInput
}

func (SpectrumApplicationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*spectrumApplicationArgs)(nil)).Elem()
}

type SpectrumApplicationInput interface {
	pulumi.Input

	ToSpectrumApplicationOutput() SpectrumApplicationOutput
	ToSpectrumApplicationOutputWithContext(ctx context.Context) SpectrumApplicationOutput
}

func (*SpectrumApplication) ElementType() reflect.Type {
	return reflect.TypeOf((**SpectrumApplication)(nil)).Elem()
}

func (i *SpectrumApplication) ToSpectrumApplicationOutput() SpectrumApplicationOutput {
	return i.ToSpectrumApplicationOutputWithContext(context.Background())
}

func (i *SpectrumApplication) ToSpectrumApplicationOutputWithContext(ctx context.Context) SpectrumApplicationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SpectrumApplicationOutput)
}

// SpectrumApplicationArrayInput is an input type that accepts SpectrumApplicationArray and SpectrumApplicationArrayOutput values.
// You can construct a concrete instance of `SpectrumApplicationArrayInput` via:
//
//          SpectrumApplicationArray{ SpectrumApplicationArgs{...} }
type SpectrumApplicationArrayInput interface {
	pulumi.Input

	ToSpectrumApplicationArrayOutput() SpectrumApplicationArrayOutput
	ToSpectrumApplicationArrayOutputWithContext(context.Context) SpectrumApplicationArrayOutput
}

type SpectrumApplicationArray []SpectrumApplicationInput

func (SpectrumApplicationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SpectrumApplication)(nil)).Elem()
}

func (i SpectrumApplicationArray) ToSpectrumApplicationArrayOutput() SpectrumApplicationArrayOutput {
	return i.ToSpectrumApplicationArrayOutputWithContext(context.Background())
}

func (i SpectrumApplicationArray) ToSpectrumApplicationArrayOutputWithContext(ctx context.Context) SpectrumApplicationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SpectrumApplicationArrayOutput)
}

// SpectrumApplicationMapInput is an input type that accepts SpectrumApplicationMap and SpectrumApplicationMapOutput values.
// You can construct a concrete instance of `SpectrumApplicationMapInput` via:
//
//          SpectrumApplicationMap{ "key": SpectrumApplicationArgs{...} }
type SpectrumApplicationMapInput interface {
	pulumi.Input

	ToSpectrumApplicationMapOutput() SpectrumApplicationMapOutput
	ToSpectrumApplicationMapOutputWithContext(context.Context) SpectrumApplicationMapOutput
}

type SpectrumApplicationMap map[string]SpectrumApplicationInput

func (SpectrumApplicationMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SpectrumApplication)(nil)).Elem()
}

func (i SpectrumApplicationMap) ToSpectrumApplicationMapOutput() SpectrumApplicationMapOutput {
	return i.ToSpectrumApplicationMapOutputWithContext(context.Background())
}

func (i SpectrumApplicationMap) ToSpectrumApplicationMapOutputWithContext(ctx context.Context) SpectrumApplicationMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SpectrumApplicationMapOutput)
}

type SpectrumApplicationOutput struct{ *pulumi.OutputState }

func (SpectrumApplicationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SpectrumApplication)(nil)).Elem()
}

func (o SpectrumApplicationOutput) ToSpectrumApplicationOutput() SpectrumApplicationOutput {
	return o
}

func (o SpectrumApplicationOutput) ToSpectrumApplicationOutputWithContext(ctx context.Context) SpectrumApplicationOutput {
	return o
}

// . Enables Argo Smart Routing. Defaults to `false`.
func (o SpectrumApplicationOutput) ArgoSmartRouting() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *SpectrumApplication) pulumi.BoolPtrOutput { return v.ArgoSmartRouting }).(pulumi.BoolPtrOutput)
}

// The name and type of DNS record for the Spectrum application. Fields documented below.
func (o SpectrumApplicationOutput) Dns() SpectrumApplicationDnsOutput {
	return o.ApplyT(func(v *SpectrumApplication) SpectrumApplicationDnsOutput { return v.Dns }).(SpectrumApplicationDnsOutput)
}

// . Choose which types of IP addresses will be provisioned for this subdomain. Valid values are: `all`, `ipv4`, `ipv6`. Defaults to `all`.
func (o SpectrumApplicationOutput) EdgeIpConnectivity() pulumi.StringOutput {
	return o.ApplyT(func(v *SpectrumApplication) pulumi.StringOutput { return v.EdgeIpConnectivity }).(pulumi.StringOutput)
}

// . A list of edge IPs (IPv4 and/or IPv6) to configure Spectrum application to. Requires [Bring Your Own IP](https://developers.cloudflare.com/spectrum/getting-started/byoip/) provisioned.
func (o SpectrumApplicationOutput) EdgeIps() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *SpectrumApplication) pulumi.StringArrayOutput { return v.EdgeIps }).(pulumi.StringArrayOutput)
}

// Enables the IP Firewall for this application. Defaults to `true`.
func (o SpectrumApplicationOutput) IpFirewall() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *SpectrumApplication) pulumi.BoolPtrOutput { return v.IpFirewall }).(pulumi.BoolPtrOutput)
}

// A list of destination addresses to the origin. e.g. `tcp://192.0.2.1:22`.
func (o SpectrumApplicationOutput) OriginDirects() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *SpectrumApplication) pulumi.StringArrayOutput { return v.OriginDirects }).(pulumi.StringArrayOutput)
}

// A destination DNS addresses to the origin. Fields documented below.
func (o SpectrumApplicationOutput) OriginDns() SpectrumApplicationOriginDnsPtrOutput {
	return o.ApplyT(func(v *SpectrumApplication) SpectrumApplicationOriginDnsPtrOutput { return v.OriginDns }).(SpectrumApplicationOriginDnsPtrOutput)
}

// If using `originDns` and not `originPortRange`, this is a required attribute. Origin port to proxy traffice to e.g. `22`.
func (o SpectrumApplicationOutput) OriginPort() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *SpectrumApplication) pulumi.IntPtrOutput { return v.OriginPort }).(pulumi.IntPtrOutput)
}

// If using `originDns` and not `originPort`, this is a required attribute. Origin port range to proxy traffice to.  When using a range, the protocol field must also specify a range, e.g. `tcp/22-23`. Fields documented below.
func (o SpectrumApplicationOutput) OriginPortRange() SpectrumApplicationOriginPortRangePtrOutput {
	return o.ApplyT(func(v *SpectrumApplication) SpectrumApplicationOriginPortRangePtrOutput { return v.OriginPortRange }).(SpectrumApplicationOriginPortRangePtrOutput)
}

// The port configuration at Cloudflare’s edge. e.g. `tcp/22`.
func (o SpectrumApplicationOutput) Protocol() pulumi.StringOutput {
	return o.ApplyT(func(v *SpectrumApplication) pulumi.StringOutput { return v.Protocol }).(pulumi.StringOutput)
}

// Enables a proxy protocol to the origin. Valid values are: `off`, `v1`, `v2`, and `simple`. Defaults to `off`.
func (o SpectrumApplicationOutput) ProxyProtocol() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SpectrumApplication) pulumi.StringPtrOutput { return v.ProxyProtocol }).(pulumi.StringPtrOutput)
}

// TLS configuration option for Cloudflare to connect to your origin. Valid values are: `off`, `flexible`, `full` and `strict`. Defaults to `off`.
func (o SpectrumApplicationOutput) Tls() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SpectrumApplication) pulumi.StringPtrOutput { return v.Tls }).(pulumi.StringPtrOutput)
}

// Sets application type. Valid values are: `direct`, `http`, `https`.  Defaults to `direct`.
func (o SpectrumApplicationOutput) TrafficType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SpectrumApplication) pulumi.StringPtrOutput { return v.TrafficType }).(pulumi.StringPtrOutput)
}

// The DNS zone ID to add the application to
func (o SpectrumApplicationOutput) ZoneId() pulumi.StringOutput {
	return o.ApplyT(func(v *SpectrumApplication) pulumi.StringOutput { return v.ZoneId }).(pulumi.StringOutput)
}

type SpectrumApplicationArrayOutput struct{ *pulumi.OutputState }

func (SpectrumApplicationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SpectrumApplication)(nil)).Elem()
}

func (o SpectrumApplicationArrayOutput) ToSpectrumApplicationArrayOutput() SpectrumApplicationArrayOutput {
	return o
}

func (o SpectrumApplicationArrayOutput) ToSpectrumApplicationArrayOutputWithContext(ctx context.Context) SpectrumApplicationArrayOutput {
	return o
}

func (o SpectrumApplicationArrayOutput) Index(i pulumi.IntInput) SpectrumApplicationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *SpectrumApplication {
		return vs[0].([]*SpectrumApplication)[vs[1].(int)]
	}).(SpectrumApplicationOutput)
}

type SpectrumApplicationMapOutput struct{ *pulumi.OutputState }

func (SpectrumApplicationMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SpectrumApplication)(nil)).Elem()
}

func (o SpectrumApplicationMapOutput) ToSpectrumApplicationMapOutput() SpectrumApplicationMapOutput {
	return o
}

func (o SpectrumApplicationMapOutput) ToSpectrumApplicationMapOutputWithContext(ctx context.Context) SpectrumApplicationMapOutput {
	return o
}

func (o SpectrumApplicationMapOutput) MapIndex(k pulumi.StringInput) SpectrumApplicationOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *SpectrumApplication {
		return vs[0].(map[string]*SpectrumApplication)[vs[1].(string)]
	}).(SpectrumApplicationOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SpectrumApplicationInput)(nil)).Elem(), &SpectrumApplication{})
	pulumi.RegisterInputType(reflect.TypeOf((*SpectrumApplicationArrayInput)(nil)).Elem(), SpectrumApplicationArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SpectrumApplicationMapInput)(nil)).Elem(), SpectrumApplicationMap{})
	pulumi.RegisterOutputType(SpectrumApplicationOutput{})
	pulumi.RegisterOutputType(SpectrumApplicationArrayOutput{})
	pulumi.RegisterOutputType(SpectrumApplicationMapOutput{})
}
