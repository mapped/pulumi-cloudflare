// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudflare

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a Cloudflare Waiting Room Event resource.
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
// 		_, err := cloudflare.NewWaitingRoomEvent(ctx, "example", &cloudflare.WaitingRoomEventArgs{
// 			EventEndTime:   pulumi.String("2006-01-02T20:04:05Z"),
// 			EventStartTime: pulumi.String("2006-01-02T15:04:05Z"),
// 			Name:           pulumi.String("foo"),
// 			WaitingRoomId:  pulumi.String("d41d8cd98f00b204e9800998ecf8427e"),
// 			ZoneId:         pulumi.String("ae36f999674d196762efcc5abb06b345"),
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
// Waiting room events can be imported using a composite ID formed of zone ID, waiting room ID, and waiting room event ID, e.g.
//
// ```sh
//  $ pulumi import cloudflare:index/waitingRoomEvent:WaitingRoomEvent default ae36f999674d196762efcc5abb06b345/d41d8cd98f00b204e9800998ecf8427e/25756b2dfe6e378a06b033b670413757
// ```
//
//  where* `ae36f999674d196762efcc5abb06b345` - the zone ID * `d41d8cd98f00b204e9800998ecf8427e` - waiting room ID as returned by [API](https://api.cloudflare.com/#waiting-room-list-waiting-rooms) * `25756b2dfe6e378a06b033b670413757` - waiting room event ID as returned by [API](https://api.cloudflare.com/#waiting-room-list-events)
type WaitingRoomEvent struct {
	pulumi.CustomResourceState

	CreatedOn pulumi.StringOutput `pulumi:"createdOn"`
	// This a templated html file that will be rendered at the edge.
	CustomPageHtml pulumi.StringPtrOutput `pulumi:"customPageHtml"`
	// A description to let users add more details about the waiting room event.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Disables automatic renewal of session cookies. If not specified, the event will inherit it from the waiting room.
	DisableSessionRenewal pulumi.BoolPtrOutput `pulumi:"disableSessionRenewal"`
	// ISO 8601 timestamp that marks the end of the event.
	EventEndTime pulumi.StringOutput `pulumi:"eventEndTime"`
	// ISO 8601 timestamp that marks the start of the event. At this time, queued users will be processed with the event's configuration. Must occur at least 1 minute before event_end_time.
	EventStartTime pulumi.StringOutput `pulumi:"eventStartTime"`
	ModifiedOn     pulumi.StringOutput `pulumi:"modifiedOn"`
	// A unique name to identify the event. Only alphanumeric characters, hyphens, and underscores are allowed.
	Name pulumi.StringOutput `pulumi:"name"`
	// The number of new users that will be let into the route every minute.
	NewUsersPerMinute pulumi.IntPtrOutput `pulumi:"newUsersPerMinute"`
	// ISO 8601 timestamp that marks when to begin queueing all users before the event starts. Must occur at least 5 minutes before event_start_time.
	PrequeueStartTime pulumi.StringPtrOutput `pulumi:"prequeueStartTime"`
	// The queueing method to be used by the waiting room during the event. If not specified, the event will inherit it from the waiting room.
	QueueingMethod pulumi.StringPtrOutput `pulumi:"queueingMethod"`
	// Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to the route. Default: 5
	SessionDuration pulumi.IntPtrOutput `pulumi:"sessionDuration"`
	// Users in the prequeue will be shuffled randomly at the `eventStartTime`. Requires that `prequeueStartTime` is not null. Default: false.
	ShuffleAtEventStart pulumi.BoolPtrOutput `pulumi:"shuffleAtEventStart"`
	// If suspended, the traffic doesn't go to the waiting room. Default: false.
	Suspended pulumi.BoolPtrOutput `pulumi:"suspended"`
	// The total number of active user sessions on the route at a point in time.
	TotalActiveUsers pulumi.IntPtrOutput `pulumi:"totalActiveUsers"`
	// The Waiting Room ID the event should apply to.
	WaitingRoomId pulumi.StringOutput `pulumi:"waitingRoomId"`
	// The zone ID to apply to.
	ZoneId pulumi.StringOutput `pulumi:"zoneId"`
}

// NewWaitingRoomEvent registers a new resource with the given unique name, arguments, and options.
func NewWaitingRoomEvent(ctx *pulumi.Context,
	name string, args *WaitingRoomEventArgs, opts ...pulumi.ResourceOption) (*WaitingRoomEvent, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.EventEndTime == nil {
		return nil, errors.New("invalid value for required argument 'EventEndTime'")
	}
	if args.EventStartTime == nil {
		return nil, errors.New("invalid value for required argument 'EventStartTime'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	if args.WaitingRoomId == nil {
		return nil, errors.New("invalid value for required argument 'WaitingRoomId'")
	}
	if args.ZoneId == nil {
		return nil, errors.New("invalid value for required argument 'ZoneId'")
	}
	var resource WaitingRoomEvent
	err := ctx.RegisterResource("cloudflare:index/waitingRoomEvent:WaitingRoomEvent", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetWaitingRoomEvent gets an existing WaitingRoomEvent resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetWaitingRoomEvent(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *WaitingRoomEventState, opts ...pulumi.ResourceOption) (*WaitingRoomEvent, error) {
	var resource WaitingRoomEvent
	err := ctx.ReadResource("cloudflare:index/waitingRoomEvent:WaitingRoomEvent", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering WaitingRoomEvent resources.
type waitingRoomEventState struct {
	CreatedOn *string `pulumi:"createdOn"`
	// This a templated html file that will be rendered at the edge.
	CustomPageHtml *string `pulumi:"customPageHtml"`
	// A description to let users add more details about the waiting room event.
	Description *string `pulumi:"description"`
	// Disables automatic renewal of session cookies. If not specified, the event will inherit it from the waiting room.
	DisableSessionRenewal *bool `pulumi:"disableSessionRenewal"`
	// ISO 8601 timestamp that marks the end of the event.
	EventEndTime *string `pulumi:"eventEndTime"`
	// ISO 8601 timestamp that marks the start of the event. At this time, queued users will be processed with the event's configuration. Must occur at least 1 minute before event_end_time.
	EventStartTime *string `pulumi:"eventStartTime"`
	ModifiedOn     *string `pulumi:"modifiedOn"`
	// A unique name to identify the event. Only alphanumeric characters, hyphens, and underscores are allowed.
	Name *string `pulumi:"name"`
	// The number of new users that will be let into the route every minute.
	NewUsersPerMinute *int `pulumi:"newUsersPerMinute"`
	// ISO 8601 timestamp that marks when to begin queueing all users before the event starts. Must occur at least 5 minutes before event_start_time.
	PrequeueStartTime *string `pulumi:"prequeueStartTime"`
	// The queueing method to be used by the waiting room during the event. If not specified, the event will inherit it from the waiting room.
	QueueingMethod *string `pulumi:"queueingMethod"`
	// Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to the route. Default: 5
	SessionDuration *int `pulumi:"sessionDuration"`
	// Users in the prequeue will be shuffled randomly at the `eventStartTime`. Requires that `prequeueStartTime` is not null. Default: false.
	ShuffleAtEventStart *bool `pulumi:"shuffleAtEventStart"`
	// If suspended, the traffic doesn't go to the waiting room. Default: false.
	Suspended *bool `pulumi:"suspended"`
	// The total number of active user sessions on the route at a point in time.
	TotalActiveUsers *int `pulumi:"totalActiveUsers"`
	// The Waiting Room ID the event should apply to.
	WaitingRoomId *string `pulumi:"waitingRoomId"`
	// The zone ID to apply to.
	ZoneId *string `pulumi:"zoneId"`
}

type WaitingRoomEventState struct {
	CreatedOn pulumi.StringPtrInput
	// This a templated html file that will be rendered at the edge.
	CustomPageHtml pulumi.StringPtrInput
	// A description to let users add more details about the waiting room event.
	Description pulumi.StringPtrInput
	// Disables automatic renewal of session cookies. If not specified, the event will inherit it from the waiting room.
	DisableSessionRenewal pulumi.BoolPtrInput
	// ISO 8601 timestamp that marks the end of the event.
	EventEndTime pulumi.StringPtrInput
	// ISO 8601 timestamp that marks the start of the event. At this time, queued users will be processed with the event's configuration. Must occur at least 1 minute before event_end_time.
	EventStartTime pulumi.StringPtrInput
	ModifiedOn     pulumi.StringPtrInput
	// A unique name to identify the event. Only alphanumeric characters, hyphens, and underscores are allowed.
	Name pulumi.StringPtrInput
	// The number of new users that will be let into the route every minute.
	NewUsersPerMinute pulumi.IntPtrInput
	// ISO 8601 timestamp that marks when to begin queueing all users before the event starts. Must occur at least 5 minutes before event_start_time.
	PrequeueStartTime pulumi.StringPtrInput
	// The queueing method to be used by the waiting room during the event. If not specified, the event will inherit it from the waiting room.
	QueueingMethod pulumi.StringPtrInput
	// Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to the route. Default: 5
	SessionDuration pulumi.IntPtrInput
	// Users in the prequeue will be shuffled randomly at the `eventStartTime`. Requires that `prequeueStartTime` is not null. Default: false.
	ShuffleAtEventStart pulumi.BoolPtrInput
	// If suspended, the traffic doesn't go to the waiting room. Default: false.
	Suspended pulumi.BoolPtrInput
	// The total number of active user sessions on the route at a point in time.
	TotalActiveUsers pulumi.IntPtrInput
	// The Waiting Room ID the event should apply to.
	WaitingRoomId pulumi.StringPtrInput
	// The zone ID to apply to.
	ZoneId pulumi.StringPtrInput
}

func (WaitingRoomEventState) ElementType() reflect.Type {
	return reflect.TypeOf((*waitingRoomEventState)(nil)).Elem()
}

type waitingRoomEventArgs struct {
	// This a templated html file that will be rendered at the edge.
	CustomPageHtml *string `pulumi:"customPageHtml"`
	// A description to let users add more details about the waiting room event.
	Description *string `pulumi:"description"`
	// Disables automatic renewal of session cookies. If not specified, the event will inherit it from the waiting room.
	DisableSessionRenewal *bool `pulumi:"disableSessionRenewal"`
	// ISO 8601 timestamp that marks the end of the event.
	EventEndTime string `pulumi:"eventEndTime"`
	// ISO 8601 timestamp that marks the start of the event. At this time, queued users will be processed with the event's configuration. Must occur at least 1 minute before event_end_time.
	EventStartTime string `pulumi:"eventStartTime"`
	// A unique name to identify the event. Only alphanumeric characters, hyphens, and underscores are allowed.
	Name string `pulumi:"name"`
	// The number of new users that will be let into the route every minute.
	NewUsersPerMinute *int `pulumi:"newUsersPerMinute"`
	// ISO 8601 timestamp that marks when to begin queueing all users before the event starts. Must occur at least 5 minutes before event_start_time.
	PrequeueStartTime *string `pulumi:"prequeueStartTime"`
	// The queueing method to be used by the waiting room during the event. If not specified, the event will inherit it from the waiting room.
	QueueingMethod *string `pulumi:"queueingMethod"`
	// Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to the route. Default: 5
	SessionDuration *int `pulumi:"sessionDuration"`
	// Users in the prequeue will be shuffled randomly at the `eventStartTime`. Requires that `prequeueStartTime` is not null. Default: false.
	ShuffleAtEventStart *bool `pulumi:"shuffleAtEventStart"`
	// If suspended, the traffic doesn't go to the waiting room. Default: false.
	Suspended *bool `pulumi:"suspended"`
	// The total number of active user sessions on the route at a point in time.
	TotalActiveUsers *int `pulumi:"totalActiveUsers"`
	// The Waiting Room ID the event should apply to.
	WaitingRoomId string `pulumi:"waitingRoomId"`
	// The zone ID to apply to.
	ZoneId string `pulumi:"zoneId"`
}

// The set of arguments for constructing a WaitingRoomEvent resource.
type WaitingRoomEventArgs struct {
	// This a templated html file that will be rendered at the edge.
	CustomPageHtml pulumi.StringPtrInput
	// A description to let users add more details about the waiting room event.
	Description pulumi.StringPtrInput
	// Disables automatic renewal of session cookies. If not specified, the event will inherit it from the waiting room.
	DisableSessionRenewal pulumi.BoolPtrInput
	// ISO 8601 timestamp that marks the end of the event.
	EventEndTime pulumi.StringInput
	// ISO 8601 timestamp that marks the start of the event. At this time, queued users will be processed with the event's configuration. Must occur at least 1 minute before event_end_time.
	EventStartTime pulumi.StringInput
	// A unique name to identify the event. Only alphanumeric characters, hyphens, and underscores are allowed.
	Name pulumi.StringInput
	// The number of new users that will be let into the route every minute.
	NewUsersPerMinute pulumi.IntPtrInput
	// ISO 8601 timestamp that marks when to begin queueing all users before the event starts. Must occur at least 5 minutes before event_start_time.
	PrequeueStartTime pulumi.StringPtrInput
	// The queueing method to be used by the waiting room during the event. If not specified, the event will inherit it from the waiting room.
	QueueingMethod pulumi.StringPtrInput
	// Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to the route. Default: 5
	SessionDuration pulumi.IntPtrInput
	// Users in the prequeue will be shuffled randomly at the `eventStartTime`. Requires that `prequeueStartTime` is not null. Default: false.
	ShuffleAtEventStart pulumi.BoolPtrInput
	// If suspended, the traffic doesn't go to the waiting room. Default: false.
	Suspended pulumi.BoolPtrInput
	// The total number of active user sessions on the route at a point in time.
	TotalActiveUsers pulumi.IntPtrInput
	// The Waiting Room ID the event should apply to.
	WaitingRoomId pulumi.StringInput
	// The zone ID to apply to.
	ZoneId pulumi.StringInput
}

func (WaitingRoomEventArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*waitingRoomEventArgs)(nil)).Elem()
}

type WaitingRoomEventInput interface {
	pulumi.Input

	ToWaitingRoomEventOutput() WaitingRoomEventOutput
	ToWaitingRoomEventOutputWithContext(ctx context.Context) WaitingRoomEventOutput
}

func (*WaitingRoomEvent) ElementType() reflect.Type {
	return reflect.TypeOf((**WaitingRoomEvent)(nil)).Elem()
}

func (i *WaitingRoomEvent) ToWaitingRoomEventOutput() WaitingRoomEventOutput {
	return i.ToWaitingRoomEventOutputWithContext(context.Background())
}

func (i *WaitingRoomEvent) ToWaitingRoomEventOutputWithContext(ctx context.Context) WaitingRoomEventOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WaitingRoomEventOutput)
}

// WaitingRoomEventArrayInput is an input type that accepts WaitingRoomEventArray and WaitingRoomEventArrayOutput values.
// You can construct a concrete instance of `WaitingRoomEventArrayInput` via:
//
//          WaitingRoomEventArray{ WaitingRoomEventArgs{...} }
type WaitingRoomEventArrayInput interface {
	pulumi.Input

	ToWaitingRoomEventArrayOutput() WaitingRoomEventArrayOutput
	ToWaitingRoomEventArrayOutputWithContext(context.Context) WaitingRoomEventArrayOutput
}

type WaitingRoomEventArray []WaitingRoomEventInput

func (WaitingRoomEventArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*WaitingRoomEvent)(nil)).Elem()
}

func (i WaitingRoomEventArray) ToWaitingRoomEventArrayOutput() WaitingRoomEventArrayOutput {
	return i.ToWaitingRoomEventArrayOutputWithContext(context.Background())
}

func (i WaitingRoomEventArray) ToWaitingRoomEventArrayOutputWithContext(ctx context.Context) WaitingRoomEventArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WaitingRoomEventArrayOutput)
}

// WaitingRoomEventMapInput is an input type that accepts WaitingRoomEventMap and WaitingRoomEventMapOutput values.
// You can construct a concrete instance of `WaitingRoomEventMapInput` via:
//
//          WaitingRoomEventMap{ "key": WaitingRoomEventArgs{...} }
type WaitingRoomEventMapInput interface {
	pulumi.Input

	ToWaitingRoomEventMapOutput() WaitingRoomEventMapOutput
	ToWaitingRoomEventMapOutputWithContext(context.Context) WaitingRoomEventMapOutput
}

type WaitingRoomEventMap map[string]WaitingRoomEventInput

func (WaitingRoomEventMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*WaitingRoomEvent)(nil)).Elem()
}

func (i WaitingRoomEventMap) ToWaitingRoomEventMapOutput() WaitingRoomEventMapOutput {
	return i.ToWaitingRoomEventMapOutputWithContext(context.Background())
}

func (i WaitingRoomEventMap) ToWaitingRoomEventMapOutputWithContext(ctx context.Context) WaitingRoomEventMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WaitingRoomEventMapOutput)
}

type WaitingRoomEventOutput struct{ *pulumi.OutputState }

func (WaitingRoomEventOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**WaitingRoomEvent)(nil)).Elem()
}

func (o WaitingRoomEventOutput) ToWaitingRoomEventOutput() WaitingRoomEventOutput {
	return o
}

func (o WaitingRoomEventOutput) ToWaitingRoomEventOutputWithContext(ctx context.Context) WaitingRoomEventOutput {
	return o
}

func (o WaitingRoomEventOutput) CreatedOn() pulumi.StringOutput {
	return o.ApplyT(func(v *WaitingRoomEvent) pulumi.StringOutput { return v.CreatedOn }).(pulumi.StringOutput)
}

// This a templated html file that will be rendered at the edge.
func (o WaitingRoomEventOutput) CustomPageHtml() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *WaitingRoomEvent) pulumi.StringPtrOutput { return v.CustomPageHtml }).(pulumi.StringPtrOutput)
}

// A description to let users add more details about the waiting room event.
func (o WaitingRoomEventOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *WaitingRoomEvent) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Disables automatic renewal of session cookies. If not specified, the event will inherit it from the waiting room.
func (o WaitingRoomEventOutput) DisableSessionRenewal() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *WaitingRoomEvent) pulumi.BoolPtrOutput { return v.DisableSessionRenewal }).(pulumi.BoolPtrOutput)
}

// ISO 8601 timestamp that marks the end of the event.
func (o WaitingRoomEventOutput) EventEndTime() pulumi.StringOutput {
	return o.ApplyT(func(v *WaitingRoomEvent) pulumi.StringOutput { return v.EventEndTime }).(pulumi.StringOutput)
}

// ISO 8601 timestamp that marks the start of the event. At this time, queued users will be processed with the event's configuration. Must occur at least 1 minute before event_end_time.
func (o WaitingRoomEventOutput) EventStartTime() pulumi.StringOutput {
	return o.ApplyT(func(v *WaitingRoomEvent) pulumi.StringOutput { return v.EventStartTime }).(pulumi.StringOutput)
}

func (o WaitingRoomEventOutput) ModifiedOn() pulumi.StringOutput {
	return o.ApplyT(func(v *WaitingRoomEvent) pulumi.StringOutput { return v.ModifiedOn }).(pulumi.StringOutput)
}

// A unique name to identify the event. Only alphanumeric characters, hyphens, and underscores are allowed.
func (o WaitingRoomEventOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *WaitingRoomEvent) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The number of new users that will be let into the route every minute.
func (o WaitingRoomEventOutput) NewUsersPerMinute() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *WaitingRoomEvent) pulumi.IntPtrOutput { return v.NewUsersPerMinute }).(pulumi.IntPtrOutput)
}

// ISO 8601 timestamp that marks when to begin queueing all users before the event starts. Must occur at least 5 minutes before event_start_time.
func (o WaitingRoomEventOutput) PrequeueStartTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *WaitingRoomEvent) pulumi.StringPtrOutput { return v.PrequeueStartTime }).(pulumi.StringPtrOutput)
}

// The queueing method to be used by the waiting room during the event. If not specified, the event will inherit it from the waiting room.
func (o WaitingRoomEventOutput) QueueingMethod() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *WaitingRoomEvent) pulumi.StringPtrOutput { return v.QueueingMethod }).(pulumi.StringPtrOutput)
}

// Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to the route. Default: 5
func (o WaitingRoomEventOutput) SessionDuration() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *WaitingRoomEvent) pulumi.IntPtrOutput { return v.SessionDuration }).(pulumi.IntPtrOutput)
}

// Users in the prequeue will be shuffled randomly at the `eventStartTime`. Requires that `prequeueStartTime` is not null. Default: false.
func (o WaitingRoomEventOutput) ShuffleAtEventStart() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *WaitingRoomEvent) pulumi.BoolPtrOutput { return v.ShuffleAtEventStart }).(pulumi.BoolPtrOutput)
}

// If suspended, the traffic doesn't go to the waiting room. Default: false.
func (o WaitingRoomEventOutput) Suspended() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *WaitingRoomEvent) pulumi.BoolPtrOutput { return v.Suspended }).(pulumi.BoolPtrOutput)
}

// The total number of active user sessions on the route at a point in time.
func (o WaitingRoomEventOutput) TotalActiveUsers() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *WaitingRoomEvent) pulumi.IntPtrOutput { return v.TotalActiveUsers }).(pulumi.IntPtrOutput)
}

// The Waiting Room ID the event should apply to.
func (o WaitingRoomEventOutput) WaitingRoomId() pulumi.StringOutput {
	return o.ApplyT(func(v *WaitingRoomEvent) pulumi.StringOutput { return v.WaitingRoomId }).(pulumi.StringOutput)
}

// The zone ID to apply to.
func (o WaitingRoomEventOutput) ZoneId() pulumi.StringOutput {
	return o.ApplyT(func(v *WaitingRoomEvent) pulumi.StringOutput { return v.ZoneId }).(pulumi.StringOutput)
}

type WaitingRoomEventArrayOutput struct{ *pulumi.OutputState }

func (WaitingRoomEventArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*WaitingRoomEvent)(nil)).Elem()
}

func (o WaitingRoomEventArrayOutput) ToWaitingRoomEventArrayOutput() WaitingRoomEventArrayOutput {
	return o
}

func (o WaitingRoomEventArrayOutput) ToWaitingRoomEventArrayOutputWithContext(ctx context.Context) WaitingRoomEventArrayOutput {
	return o
}

func (o WaitingRoomEventArrayOutput) Index(i pulumi.IntInput) WaitingRoomEventOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *WaitingRoomEvent {
		return vs[0].([]*WaitingRoomEvent)[vs[1].(int)]
	}).(WaitingRoomEventOutput)
}

type WaitingRoomEventMapOutput struct{ *pulumi.OutputState }

func (WaitingRoomEventMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*WaitingRoomEvent)(nil)).Elem()
}

func (o WaitingRoomEventMapOutput) ToWaitingRoomEventMapOutput() WaitingRoomEventMapOutput {
	return o
}

func (o WaitingRoomEventMapOutput) ToWaitingRoomEventMapOutputWithContext(ctx context.Context) WaitingRoomEventMapOutput {
	return o
}

func (o WaitingRoomEventMapOutput) MapIndex(k pulumi.StringInput) WaitingRoomEventOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *WaitingRoomEvent {
		return vs[0].(map[string]*WaitingRoomEvent)[vs[1].(string)]
	}).(WaitingRoomEventOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*WaitingRoomEventInput)(nil)).Elem(), &WaitingRoomEvent{})
	pulumi.RegisterInputType(reflect.TypeOf((*WaitingRoomEventArrayInput)(nil)).Elem(), WaitingRoomEventArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*WaitingRoomEventMapInput)(nil)).Elem(), WaitingRoomEventMap{})
	pulumi.RegisterOutputType(WaitingRoomEventOutput{})
	pulumi.RegisterOutputType(WaitingRoomEventArrayOutput{})
	pulumi.RegisterOutputType(WaitingRoomEventMapOutput{})
}
