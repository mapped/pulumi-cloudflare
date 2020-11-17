// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudflare

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a resource which manages Cloudflare Logpush ownership challenges to use
// in a Logpush Job. On it's own, doesn't do much however this resource should
// be used in conjunction to create Logpush jobs.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-cloudflare/sdk/v2/go/cloudflare"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := cloudflare.NewLogPushOwnershipChallenge(ctx, "example", &cloudflare.LogPushOwnershipChallengeArgs{
// 			DestinationConf: pulumi.String("s3://my-bucket-path?region=us-west-2"),
// 			ZoneId:          pulumi.String("d41d8cd98f00b204e9800998ecf8427e"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type LogPushOwnershipChallenge struct {
	pulumi.CustomResourceState

	// Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See [Logpush destination documentation](https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination).
	DestinationConf pulumi.StringOutput `pulumi:"destinationConf"`
	// The filename of the ownership challenge which
	// contains the contents required for Logpush Job creation.
	OwnershipChallengeFilename pulumi.StringOutput `pulumi:"ownershipChallengeFilename"`
	// The zone ID where the logpush ownership challenge should be created.
	ZoneId pulumi.StringOutput `pulumi:"zoneId"`
}

// NewLogPushOwnershipChallenge registers a new resource with the given unique name, arguments, and options.
func NewLogPushOwnershipChallenge(ctx *pulumi.Context,
	name string, args *LogPushOwnershipChallengeArgs, opts ...pulumi.ResourceOption) (*LogPushOwnershipChallenge, error) {
	if args == nil || args.DestinationConf == nil {
		return nil, errors.New("missing required argument 'DestinationConf'")
	}
	if args == nil || args.ZoneId == nil {
		return nil, errors.New("missing required argument 'ZoneId'")
	}
	if args == nil {
		args = &LogPushOwnershipChallengeArgs{}
	}
	var resource LogPushOwnershipChallenge
	err := ctx.RegisterResource("cloudflare:index/logPushOwnershipChallenge:LogPushOwnershipChallenge", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLogPushOwnershipChallenge gets an existing LogPushOwnershipChallenge resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLogPushOwnershipChallenge(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LogPushOwnershipChallengeState, opts ...pulumi.ResourceOption) (*LogPushOwnershipChallenge, error) {
	var resource LogPushOwnershipChallenge
	err := ctx.ReadResource("cloudflare:index/logPushOwnershipChallenge:LogPushOwnershipChallenge", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LogPushOwnershipChallenge resources.
type logPushOwnershipChallengeState struct {
	// Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See [Logpush destination documentation](https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination).
	DestinationConf *string `pulumi:"destinationConf"`
	// The filename of the ownership challenge which
	// contains the contents required for Logpush Job creation.
	OwnershipChallengeFilename *string `pulumi:"ownershipChallengeFilename"`
	// The zone ID where the logpush ownership challenge should be created.
	ZoneId *string `pulumi:"zoneId"`
}

type LogPushOwnershipChallengeState struct {
	// Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See [Logpush destination documentation](https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination).
	DestinationConf pulumi.StringPtrInput
	// The filename of the ownership challenge which
	// contains the contents required for Logpush Job creation.
	OwnershipChallengeFilename pulumi.StringPtrInput
	// The zone ID where the logpush ownership challenge should be created.
	ZoneId pulumi.StringPtrInput
}

func (LogPushOwnershipChallengeState) ElementType() reflect.Type {
	return reflect.TypeOf((*logPushOwnershipChallengeState)(nil)).Elem()
}

type logPushOwnershipChallengeArgs struct {
	// Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See [Logpush destination documentation](https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination).
	DestinationConf string `pulumi:"destinationConf"`
	// The zone ID where the logpush ownership challenge should be created.
	ZoneId string `pulumi:"zoneId"`
}

// The set of arguments for constructing a LogPushOwnershipChallenge resource.
type LogPushOwnershipChallengeArgs struct {
	// Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See [Logpush destination documentation](https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination).
	DestinationConf pulumi.StringInput
	// The zone ID where the logpush ownership challenge should be created.
	ZoneId pulumi.StringInput
}

func (LogPushOwnershipChallengeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*logPushOwnershipChallengeArgs)(nil)).Elem()
}