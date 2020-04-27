// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudflare

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Cloudflare worker route resource. A route will also require a `.WorkerScript`.
type WorkerRoute struct {
	pulumi.CustomResourceState

	// The [route pattern](https://developers.cloudflare.com/workers/about/routes/)
	Pattern pulumi.StringOutput `pulumi:"pattern"`
	// Which worker script to run for requests that match the route pattern. If `scriptName` is empty, workers will be skipped for matching requests.
	ScriptName pulumi.StringPtrOutput `pulumi:"scriptName"`
	// The zone ID to add the route to.
	ZoneId pulumi.StringOutput `pulumi:"zoneId"`
}

// NewWorkerRoute registers a new resource with the given unique name, arguments, and options.
func NewWorkerRoute(ctx *pulumi.Context,
	name string, args *WorkerRouteArgs, opts ...pulumi.ResourceOption) (*WorkerRoute, error) {
	if args == nil || args.Pattern == nil {
		return nil, errors.New("missing required argument 'Pattern'")
	}
	if args == nil || args.ZoneId == nil {
		return nil, errors.New("missing required argument 'ZoneId'")
	}
	if args == nil {
		args = &WorkerRouteArgs{}
	}
	var resource WorkerRoute
	err := ctx.RegisterResource("cloudflare:index/workerRoute:WorkerRoute", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetWorkerRoute gets an existing WorkerRoute resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetWorkerRoute(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *WorkerRouteState, opts ...pulumi.ResourceOption) (*WorkerRoute, error) {
	var resource WorkerRoute
	err := ctx.ReadResource("cloudflare:index/workerRoute:WorkerRoute", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering WorkerRoute resources.
type workerRouteState struct {
	// The [route pattern](https://developers.cloudflare.com/workers/about/routes/)
	Pattern *string `pulumi:"pattern"`
	// Which worker script to run for requests that match the route pattern. If `scriptName` is empty, workers will be skipped for matching requests.
	ScriptName *string `pulumi:"scriptName"`
	// The zone ID to add the route to.
	ZoneId *string `pulumi:"zoneId"`
}

type WorkerRouteState struct {
	// The [route pattern](https://developers.cloudflare.com/workers/about/routes/)
	Pattern pulumi.StringPtrInput
	// Which worker script to run for requests that match the route pattern. If `scriptName` is empty, workers will be skipped for matching requests.
	ScriptName pulumi.StringPtrInput
	// The zone ID to add the route to.
	ZoneId pulumi.StringPtrInput
}

func (WorkerRouteState) ElementType() reflect.Type {
	return reflect.TypeOf((*workerRouteState)(nil)).Elem()
}

type workerRouteArgs struct {
	// The [route pattern](https://developers.cloudflare.com/workers/about/routes/)
	Pattern string `pulumi:"pattern"`
	// Which worker script to run for requests that match the route pattern. If `scriptName` is empty, workers will be skipped for matching requests.
	ScriptName *string `pulumi:"scriptName"`
	// The zone ID to add the route to.
	ZoneId string `pulumi:"zoneId"`
}

// The set of arguments for constructing a WorkerRoute resource.
type WorkerRouteArgs struct {
	// The [route pattern](https://developers.cloudflare.com/workers/about/routes/)
	Pattern pulumi.StringInput
	// Which worker script to run for requests that match the route pattern. If `scriptName` is empty, workers will be skipped for matching requests.
	ScriptName pulumi.StringPtrInput
	// The zone ID to add the route to.
	ZoneId pulumi.StringInput
}

func (WorkerRouteArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*workerRouteArgs)(nil)).Elem()
}
