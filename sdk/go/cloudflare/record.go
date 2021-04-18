// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudflare

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a Cloudflare record resource.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-cloudflare/sdk/v3/go/cloudflare"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := cloudflare.NewRecord(ctx, "foobar", &cloudflare.RecordArgs{
// 			ZoneId: pulumi.Any(_var.Cloudflare_zone_id),
// 			Name:   pulumi.String("terraform"),
// 			Value:  pulumi.String("192.168.0.11"),
// 			Type:   pulumi.String("A"),
// 			Ttl:    pulumi.Int(3600),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = cloudflare.NewRecord(ctx, "_sipTls", &cloudflare.RecordArgs{
// 			ZoneId: pulumi.Any(_var.Cloudflare_zone_id),
// 			Name:   pulumi.String("_sip._tls"),
// 			Type:   pulumi.String("SRV"),
// 			Data: &cloudflare.RecordDataArgs{
// 				Service:  pulumi.String("_sip"),
// 				Proto:    pulumi.String("_tls"),
// 				Name:     pulumi.String("terraform-srv"),
// 				Priority: pulumi.Int(0),
// 				Weight:   pulumi.Int(0),
// 				Port:     pulumi.Int(443),
// 				Target:   pulumi.String("example.com"),
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
// Records can be imported using a composite ID formed of zone ID and record ID, e.g.
//
// ```sh
//  $ pulumi import cloudflare:index/record:Record default ae36f999674d196762efcc5abb06b345/d41d8cd98f00b204e9800998ecf8427e
// ```
//
//  where* `ae36f999674d196762efcc5abb06b345` - the zone ID * `d41d8cd98f00b204e9800998ecf8427e` - record ID as returned by [API](https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records)
type Record struct {
	pulumi.CustomResourceState

	// The RFC3339 timestamp of when the record was created
	CreatedOn pulumi.StringOutput `pulumi:"createdOn"`
	// Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or `value` must be specified
	Data RecordDataPtrOutput `pulumi:"data"`
	// The FQDN of the record
	Hostname pulumi.StringOutput `pulumi:"hostname"`
	// A key-value map of string metadata Cloudflare associates with the record
	Metadata pulumi.MapOutput `pulumi:"metadata"`
	// The RFC3339 timestamp of when the record was last modified
	ModifiedOn pulumi.StringOutput `pulumi:"modifiedOn"`
	// The name of the record
	Name pulumi.StringOutput `pulumi:"name"`
	// The priority of the record
	Priority pulumi.IntPtrOutput `pulumi:"priority"`
	// Shows whether this record can be proxied, must be true if setting `proxied=true`
	Proxiable pulumi.BoolOutput `pulumi:"proxiable"`
	// Whether the record gets Cloudflare's origin protection; defaults to `false`.
	Proxied pulumi.BoolPtrOutput `pulumi:"proxied"`
	// The TTL of the record ([automatic: '1'](https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record))
	Ttl pulumi.IntOutput `pulumi:"ttl"`
	// The type of the record
	Type pulumi.StringOutput `pulumi:"type"`
	// The (string) value of the record. Either this or `data` must be specified
	Value pulumi.StringOutput `pulumi:"value"`
	// The DNS zone ID to add the record to
	ZoneId pulumi.StringOutput `pulumi:"zoneId"`
}

// NewRecord registers a new resource with the given unique name, arguments, and options.
func NewRecord(ctx *pulumi.Context,
	name string, args *RecordArgs, opts ...pulumi.ResourceOption) (*Record, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	if args.ZoneId == nil {
		return nil, errors.New("invalid value for required argument 'ZoneId'")
	}
	var resource Record
	err := ctx.RegisterResource("cloudflare:index/record:Record", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRecord gets an existing Record resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRecord(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RecordState, opts ...pulumi.ResourceOption) (*Record, error) {
	var resource Record
	err := ctx.ReadResource("cloudflare:index/record:Record", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Record resources.
type recordState struct {
	// The RFC3339 timestamp of when the record was created
	CreatedOn *string `pulumi:"createdOn"`
	// Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or `value` must be specified
	Data *RecordData `pulumi:"data"`
	// The FQDN of the record
	Hostname *string `pulumi:"hostname"`
	// A key-value map of string metadata Cloudflare associates with the record
	Metadata map[string]interface{} `pulumi:"metadata"`
	// The RFC3339 timestamp of when the record was last modified
	ModifiedOn *string `pulumi:"modifiedOn"`
	// The name of the record
	Name *string `pulumi:"name"`
	// The priority of the record
	Priority *int `pulumi:"priority"`
	// Shows whether this record can be proxied, must be true if setting `proxied=true`
	Proxiable *bool `pulumi:"proxiable"`
	// Whether the record gets Cloudflare's origin protection; defaults to `false`.
	Proxied *bool `pulumi:"proxied"`
	// The TTL of the record ([automatic: '1'](https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record))
	Ttl *int `pulumi:"ttl"`
	// The type of the record
	Type *string `pulumi:"type"`
	// The (string) value of the record. Either this or `data` must be specified
	Value *string `pulumi:"value"`
	// The DNS zone ID to add the record to
	ZoneId *string `pulumi:"zoneId"`
}

type RecordState struct {
	// The RFC3339 timestamp of when the record was created
	CreatedOn pulumi.StringPtrInput
	// Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or `value` must be specified
	Data RecordDataPtrInput
	// The FQDN of the record
	Hostname pulumi.StringPtrInput
	// A key-value map of string metadata Cloudflare associates with the record
	Metadata pulumi.MapInput
	// The RFC3339 timestamp of when the record was last modified
	ModifiedOn pulumi.StringPtrInput
	// The name of the record
	Name pulumi.StringPtrInput
	// The priority of the record
	Priority pulumi.IntPtrInput
	// Shows whether this record can be proxied, must be true if setting `proxied=true`
	Proxiable pulumi.BoolPtrInput
	// Whether the record gets Cloudflare's origin protection; defaults to `false`.
	Proxied pulumi.BoolPtrInput
	// The TTL of the record ([automatic: '1'](https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record))
	Ttl pulumi.IntPtrInput
	// The type of the record
	Type pulumi.StringPtrInput
	// The (string) value of the record. Either this or `data` must be specified
	Value pulumi.StringPtrInput
	// The DNS zone ID to add the record to
	ZoneId pulumi.StringPtrInput
}

func (RecordState) ElementType() reflect.Type {
	return reflect.TypeOf((*recordState)(nil)).Elem()
}

type recordArgs struct {
	// Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or `value` must be specified
	Data *RecordData `pulumi:"data"`
	// The name of the record
	Name string `pulumi:"name"`
	// The priority of the record
	Priority *int `pulumi:"priority"`
	// Whether the record gets Cloudflare's origin protection; defaults to `false`.
	Proxied *bool `pulumi:"proxied"`
	// The TTL of the record ([automatic: '1'](https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record))
	Ttl *int `pulumi:"ttl"`
	// The type of the record
	Type string `pulumi:"type"`
	// The (string) value of the record. Either this or `data` must be specified
	Value *string `pulumi:"value"`
	// The DNS zone ID to add the record to
	ZoneId string `pulumi:"zoneId"`
}

// The set of arguments for constructing a Record resource.
type RecordArgs struct {
	// Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or `value` must be specified
	Data RecordDataPtrInput
	// The name of the record
	Name pulumi.StringInput
	// The priority of the record
	Priority pulumi.IntPtrInput
	// Whether the record gets Cloudflare's origin protection; defaults to `false`.
	Proxied pulumi.BoolPtrInput
	// The TTL of the record ([automatic: '1'](https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record))
	Ttl pulumi.IntPtrInput
	// The type of the record
	Type pulumi.StringInput
	// The (string) value of the record. Either this or `data` must be specified
	Value pulumi.StringPtrInput
	// The DNS zone ID to add the record to
	ZoneId pulumi.StringInput
}

func (RecordArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*recordArgs)(nil)).Elem()
}

type RecordInput interface {
	pulumi.Input

	ToRecordOutput() RecordOutput
	ToRecordOutputWithContext(ctx context.Context) RecordOutput
}

func (*Record) ElementType() reflect.Type {
	return reflect.TypeOf((*Record)(nil))
}

func (i *Record) ToRecordOutput() RecordOutput {
	return i.ToRecordOutputWithContext(context.Background())
}

func (i *Record) ToRecordOutputWithContext(ctx context.Context) RecordOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RecordOutput)
}

func (i *Record) ToRecordPtrOutput() RecordPtrOutput {
	return i.ToRecordPtrOutputWithContext(context.Background())
}

func (i *Record) ToRecordPtrOutputWithContext(ctx context.Context) RecordPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RecordPtrOutput)
}

type RecordPtrInput interface {
	pulumi.Input

	ToRecordPtrOutput() RecordPtrOutput
	ToRecordPtrOutputWithContext(ctx context.Context) RecordPtrOutput
}

type recordPtrType RecordArgs

func (*recordPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**Record)(nil))
}

func (i *recordPtrType) ToRecordPtrOutput() RecordPtrOutput {
	return i.ToRecordPtrOutputWithContext(context.Background())
}

func (i *recordPtrType) ToRecordPtrOutputWithContext(ctx context.Context) RecordPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RecordPtrOutput)
}

// RecordArrayInput is an input type that accepts RecordArray and RecordArrayOutput values.
// You can construct a concrete instance of `RecordArrayInput` via:
//
//          RecordArray{ RecordArgs{...} }
type RecordArrayInput interface {
	pulumi.Input

	ToRecordArrayOutput() RecordArrayOutput
	ToRecordArrayOutputWithContext(context.Context) RecordArrayOutput
}

type RecordArray []RecordInput

func (RecordArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*Record)(nil))
}

func (i RecordArray) ToRecordArrayOutput() RecordArrayOutput {
	return i.ToRecordArrayOutputWithContext(context.Background())
}

func (i RecordArray) ToRecordArrayOutputWithContext(ctx context.Context) RecordArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RecordArrayOutput)
}

// RecordMapInput is an input type that accepts RecordMap and RecordMapOutput values.
// You can construct a concrete instance of `RecordMapInput` via:
//
//          RecordMap{ "key": RecordArgs{...} }
type RecordMapInput interface {
	pulumi.Input

	ToRecordMapOutput() RecordMapOutput
	ToRecordMapOutputWithContext(context.Context) RecordMapOutput
}

type RecordMap map[string]RecordInput

func (RecordMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*Record)(nil))
}

func (i RecordMap) ToRecordMapOutput() RecordMapOutput {
	return i.ToRecordMapOutputWithContext(context.Background())
}

func (i RecordMap) ToRecordMapOutputWithContext(ctx context.Context) RecordMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RecordMapOutput)
}

type RecordOutput struct {
	*pulumi.OutputState
}

func (RecordOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Record)(nil))
}

func (o RecordOutput) ToRecordOutput() RecordOutput {
	return o
}

func (o RecordOutput) ToRecordOutputWithContext(ctx context.Context) RecordOutput {
	return o
}

func (o RecordOutput) ToRecordPtrOutput() RecordPtrOutput {
	return o.ToRecordPtrOutputWithContext(context.Background())
}

func (o RecordOutput) ToRecordPtrOutputWithContext(ctx context.Context) RecordPtrOutput {
	return o.ApplyT(func(v Record) *Record {
		return &v
	}).(RecordPtrOutput)
}

type RecordPtrOutput struct {
	*pulumi.OutputState
}

func (RecordPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Record)(nil))
}

func (o RecordPtrOutput) ToRecordPtrOutput() RecordPtrOutput {
	return o
}

func (o RecordPtrOutput) ToRecordPtrOutputWithContext(ctx context.Context) RecordPtrOutput {
	return o
}

type RecordArrayOutput struct{ *pulumi.OutputState }

func (RecordArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]Record)(nil))
}

func (o RecordArrayOutput) ToRecordArrayOutput() RecordArrayOutput {
	return o
}

func (o RecordArrayOutput) ToRecordArrayOutputWithContext(ctx context.Context) RecordArrayOutput {
	return o
}

func (o RecordArrayOutput) Index(i pulumi.IntInput) RecordOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) Record {
		return vs[0].([]Record)[vs[1].(int)]
	}).(RecordOutput)
}

type RecordMapOutput struct{ *pulumi.OutputState }

func (RecordMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]Record)(nil))
}

func (o RecordMapOutput) ToRecordMapOutput() RecordMapOutput {
	return o
}

func (o RecordMapOutput) ToRecordMapOutputWithContext(ctx context.Context) RecordMapOutput {
	return o
}

func (o RecordMapOutput) MapIndex(k pulumi.StringInput) RecordOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) Record {
		return vs[0].(map[string]Record)[vs[1].(string)]
	}).(RecordOutput)
}

func init() {
	pulumi.RegisterOutputType(RecordOutput{})
	pulumi.RegisterOutputType(RecordPtrOutput{})
	pulumi.RegisterOutputType(RecordArrayOutput{})
	pulumi.RegisterOutputType(RecordMapOutput{})
}
