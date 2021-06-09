// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudflare

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a Cloudflare Access Policy resource. Access Policies are used
// in conjunction with Access Applications to restrict access to a
// particular resource.
//
// ## Import
//
// Access Policies can be imported using a composite ID formed of identifier type (`zone` or `account`), identifier ID (`zone_id` or `account_id`), application ID and policy ID. # import a zone level Access policy
//
// ```sh
//  $ pulumi import cloudflare:index/accessPolicy:AccessPolicy staging zone/cb029e245cfdd66dc8d2e570d5dd3322/d41d8cd98f00b204e9800998ecf8427e/67ea780ce4982c1cfbe6b7293afc765d
// ```
//
// # import an account level Access policy
//
// ```sh
//  $ pulumi import cloudflare:index/accessPolicy:AccessPolicy production account/0d599f0ec05c3bda8c3b8a68c32a1b47/d41d8cd98f00b204e9800998ecf8427e/67ea780ce4982c1cfbe6b7293afc765d
// ```
type AccessPolicy struct {
	pulumi.CustomResourceState

	// The account to which the access rule should be added. Conflicts with `zoneId`.
	AccountId pulumi.StringOutput `pulumi:"accountId"`
	// The ID of the application the policy is associated with.
	ApplicationId pulumi.StringOutput `pulumi:"applicationId"`
	// Defines the action Access will take if the policy matches the user.
	// Allowed values: `allow`, `deny`, `nonIdentity`, `bypass`
	Decision pulumi.StringOutput `pulumi:"decision"`
	// A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
	Excludes AccessPolicyExcludeArrayOutput `pulumi:"excludes"`
	// A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
	Includes AccessPolicyIncludeArrayOutput `pulumi:"includes"`
	// Friendly name of the Access Application.
	Name pulumi.StringOutput `pulumi:"name"`
	// The unique precedence for policies on a single application. Integer.
	Precedence pulumi.IntOutput `pulumi:"precedence"`
	// A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
	Requires AccessPolicyRequireArrayOutput `pulumi:"requires"`
	// The DNS zone to which the access rule should be added. Conflicts with `accountId`.
	ZoneId pulumi.StringOutput `pulumi:"zoneId"`
}

// NewAccessPolicy registers a new resource with the given unique name, arguments, and options.
func NewAccessPolicy(ctx *pulumi.Context,
	name string, args *AccessPolicyArgs, opts ...pulumi.ResourceOption) (*AccessPolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ApplicationId == nil {
		return nil, errors.New("invalid value for required argument 'ApplicationId'")
	}
	if args.Decision == nil {
		return nil, errors.New("invalid value for required argument 'Decision'")
	}
	if args.Includes == nil {
		return nil, errors.New("invalid value for required argument 'Includes'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	if args.Precedence == nil {
		return nil, errors.New("invalid value for required argument 'Precedence'")
	}
	var resource AccessPolicy
	err := ctx.RegisterResource("cloudflare:index/accessPolicy:AccessPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAccessPolicy gets an existing AccessPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAccessPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AccessPolicyState, opts ...pulumi.ResourceOption) (*AccessPolicy, error) {
	var resource AccessPolicy
	err := ctx.ReadResource("cloudflare:index/accessPolicy:AccessPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AccessPolicy resources.
type accessPolicyState struct {
	// The account to which the access rule should be added. Conflicts with `zoneId`.
	AccountId *string `pulumi:"accountId"`
	// The ID of the application the policy is associated with.
	ApplicationId *string `pulumi:"applicationId"`
	// Defines the action Access will take if the policy matches the user.
	// Allowed values: `allow`, `deny`, `nonIdentity`, `bypass`
	Decision *string `pulumi:"decision"`
	// A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
	Excludes []AccessPolicyExclude `pulumi:"excludes"`
	// A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
	Includes []AccessPolicyInclude `pulumi:"includes"`
	// Friendly name of the Access Application.
	Name *string `pulumi:"name"`
	// The unique precedence for policies on a single application. Integer.
	Precedence *int `pulumi:"precedence"`
	// A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
	Requires []AccessPolicyRequire `pulumi:"requires"`
	// The DNS zone to which the access rule should be added. Conflicts with `accountId`.
	ZoneId *string `pulumi:"zoneId"`
}

type AccessPolicyState struct {
	// The account to which the access rule should be added. Conflicts with `zoneId`.
	AccountId pulumi.StringPtrInput
	// The ID of the application the policy is associated with.
	ApplicationId pulumi.StringPtrInput
	// Defines the action Access will take if the policy matches the user.
	// Allowed values: `allow`, `deny`, `nonIdentity`, `bypass`
	Decision pulumi.StringPtrInput
	// A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
	Excludes AccessPolicyExcludeArrayInput
	// A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
	Includes AccessPolicyIncludeArrayInput
	// Friendly name of the Access Application.
	Name pulumi.StringPtrInput
	// The unique precedence for policies on a single application. Integer.
	Precedence pulumi.IntPtrInput
	// A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
	Requires AccessPolicyRequireArrayInput
	// The DNS zone to which the access rule should be added. Conflicts with `accountId`.
	ZoneId pulumi.StringPtrInput
}

func (AccessPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*accessPolicyState)(nil)).Elem()
}

type accessPolicyArgs struct {
	// The account to which the access rule should be added. Conflicts with `zoneId`.
	AccountId *string `pulumi:"accountId"`
	// The ID of the application the policy is associated with.
	ApplicationId string `pulumi:"applicationId"`
	// Defines the action Access will take if the policy matches the user.
	// Allowed values: `allow`, `deny`, `nonIdentity`, `bypass`
	Decision string `pulumi:"decision"`
	// A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
	Excludes []AccessPolicyExclude `pulumi:"excludes"`
	// A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
	Includes []AccessPolicyInclude `pulumi:"includes"`
	// Friendly name of the Access Application.
	Name string `pulumi:"name"`
	// The unique precedence for policies on a single application. Integer.
	Precedence int `pulumi:"precedence"`
	// A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
	Requires []AccessPolicyRequire `pulumi:"requires"`
	// The DNS zone to which the access rule should be added. Conflicts with `accountId`.
	ZoneId *string `pulumi:"zoneId"`
}

// The set of arguments for constructing a AccessPolicy resource.
type AccessPolicyArgs struct {
	// The account to which the access rule should be added. Conflicts with `zoneId`.
	AccountId pulumi.StringPtrInput
	// The ID of the application the policy is associated with.
	ApplicationId pulumi.StringInput
	// Defines the action Access will take if the policy matches the user.
	// Allowed values: `allow`, `deny`, `nonIdentity`, `bypass`
	Decision pulumi.StringInput
	// A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
	Excludes AccessPolicyExcludeArrayInput
	// A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
	Includes AccessPolicyIncludeArrayInput
	// Friendly name of the Access Application.
	Name pulumi.StringInput
	// The unique precedence for policies on a single application. Integer.
	Precedence pulumi.IntInput
	// A series of access conditions, see [Access Groups](https://www.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/access_group#conditions).
	Requires AccessPolicyRequireArrayInput
	// The DNS zone to which the access rule should be added. Conflicts with `accountId`.
	ZoneId pulumi.StringPtrInput
}

func (AccessPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*accessPolicyArgs)(nil)).Elem()
}

type AccessPolicyInput interface {
	pulumi.Input

	ToAccessPolicyOutput() AccessPolicyOutput
	ToAccessPolicyOutputWithContext(ctx context.Context) AccessPolicyOutput
}

func (*AccessPolicy) ElementType() reflect.Type {
	return reflect.TypeOf((*AccessPolicy)(nil))
}

func (i *AccessPolicy) ToAccessPolicyOutput() AccessPolicyOutput {
	return i.ToAccessPolicyOutputWithContext(context.Background())
}

func (i *AccessPolicy) ToAccessPolicyOutputWithContext(ctx context.Context) AccessPolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AccessPolicyOutput)
}

func (i *AccessPolicy) ToAccessPolicyPtrOutput() AccessPolicyPtrOutput {
	return i.ToAccessPolicyPtrOutputWithContext(context.Background())
}

func (i *AccessPolicy) ToAccessPolicyPtrOutputWithContext(ctx context.Context) AccessPolicyPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AccessPolicyPtrOutput)
}

type AccessPolicyPtrInput interface {
	pulumi.Input

	ToAccessPolicyPtrOutput() AccessPolicyPtrOutput
	ToAccessPolicyPtrOutputWithContext(ctx context.Context) AccessPolicyPtrOutput
}

type accessPolicyPtrType AccessPolicyArgs

func (*accessPolicyPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**AccessPolicy)(nil))
}

func (i *accessPolicyPtrType) ToAccessPolicyPtrOutput() AccessPolicyPtrOutput {
	return i.ToAccessPolicyPtrOutputWithContext(context.Background())
}

func (i *accessPolicyPtrType) ToAccessPolicyPtrOutputWithContext(ctx context.Context) AccessPolicyPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AccessPolicyPtrOutput)
}

// AccessPolicyArrayInput is an input type that accepts AccessPolicyArray and AccessPolicyArrayOutput values.
// You can construct a concrete instance of `AccessPolicyArrayInput` via:
//
//          AccessPolicyArray{ AccessPolicyArgs{...} }
type AccessPolicyArrayInput interface {
	pulumi.Input

	ToAccessPolicyArrayOutput() AccessPolicyArrayOutput
	ToAccessPolicyArrayOutputWithContext(context.Context) AccessPolicyArrayOutput
}

type AccessPolicyArray []AccessPolicyInput

func (AccessPolicyArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*AccessPolicy)(nil))
}

func (i AccessPolicyArray) ToAccessPolicyArrayOutput() AccessPolicyArrayOutput {
	return i.ToAccessPolicyArrayOutputWithContext(context.Background())
}

func (i AccessPolicyArray) ToAccessPolicyArrayOutputWithContext(ctx context.Context) AccessPolicyArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AccessPolicyArrayOutput)
}

// AccessPolicyMapInput is an input type that accepts AccessPolicyMap and AccessPolicyMapOutput values.
// You can construct a concrete instance of `AccessPolicyMapInput` via:
//
//          AccessPolicyMap{ "key": AccessPolicyArgs{...} }
type AccessPolicyMapInput interface {
	pulumi.Input

	ToAccessPolicyMapOutput() AccessPolicyMapOutput
	ToAccessPolicyMapOutputWithContext(context.Context) AccessPolicyMapOutput
}

type AccessPolicyMap map[string]AccessPolicyInput

func (AccessPolicyMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*AccessPolicy)(nil))
}

func (i AccessPolicyMap) ToAccessPolicyMapOutput() AccessPolicyMapOutput {
	return i.ToAccessPolicyMapOutputWithContext(context.Background())
}

func (i AccessPolicyMap) ToAccessPolicyMapOutputWithContext(ctx context.Context) AccessPolicyMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AccessPolicyMapOutput)
}

type AccessPolicyOutput struct {
	*pulumi.OutputState
}

func (AccessPolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AccessPolicy)(nil))
}

func (o AccessPolicyOutput) ToAccessPolicyOutput() AccessPolicyOutput {
	return o
}

func (o AccessPolicyOutput) ToAccessPolicyOutputWithContext(ctx context.Context) AccessPolicyOutput {
	return o
}

func (o AccessPolicyOutput) ToAccessPolicyPtrOutput() AccessPolicyPtrOutput {
	return o.ToAccessPolicyPtrOutputWithContext(context.Background())
}

func (o AccessPolicyOutput) ToAccessPolicyPtrOutputWithContext(ctx context.Context) AccessPolicyPtrOutput {
	return o.ApplyT(func(v AccessPolicy) *AccessPolicy {
		return &v
	}).(AccessPolicyPtrOutput)
}

type AccessPolicyPtrOutput struct {
	*pulumi.OutputState
}

func (AccessPolicyPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AccessPolicy)(nil))
}

func (o AccessPolicyPtrOutput) ToAccessPolicyPtrOutput() AccessPolicyPtrOutput {
	return o
}

func (o AccessPolicyPtrOutput) ToAccessPolicyPtrOutputWithContext(ctx context.Context) AccessPolicyPtrOutput {
	return o
}

type AccessPolicyArrayOutput struct{ *pulumi.OutputState }

func (AccessPolicyArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AccessPolicy)(nil))
}

func (o AccessPolicyArrayOutput) ToAccessPolicyArrayOutput() AccessPolicyArrayOutput {
	return o
}

func (o AccessPolicyArrayOutput) ToAccessPolicyArrayOutputWithContext(ctx context.Context) AccessPolicyArrayOutput {
	return o
}

func (o AccessPolicyArrayOutput) Index(i pulumi.IntInput) AccessPolicyOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) AccessPolicy {
		return vs[0].([]AccessPolicy)[vs[1].(int)]
	}).(AccessPolicyOutput)
}

type AccessPolicyMapOutput struct{ *pulumi.OutputState }

func (AccessPolicyMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]AccessPolicy)(nil))
}

func (o AccessPolicyMapOutput) ToAccessPolicyMapOutput() AccessPolicyMapOutput {
	return o
}

func (o AccessPolicyMapOutput) ToAccessPolicyMapOutputWithContext(ctx context.Context) AccessPolicyMapOutput {
	return o
}

func (o AccessPolicyMapOutput) MapIndex(k pulumi.StringInput) AccessPolicyOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) AccessPolicy {
		return vs[0].(map[string]AccessPolicy)[vs[1].(string)]
	}).(AccessPolicyOutput)
}

func init() {
	pulumi.RegisterOutputType(AccessPolicyOutput{})
	pulumi.RegisterOutputType(AccessPolicyPtrOutput{})
	pulumi.RegisterOutputType(AccessPolicyArrayOutput{})
	pulumi.RegisterOutputType(AccessPolicyMapOutput{})
}
