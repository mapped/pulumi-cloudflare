// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudflare
{
    /// <summary>
    /// Provides a resource which customizes Cloudflare zone cache variants.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Cloudflare = Pulumi.Cloudflare;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var example = new Cloudflare.ZoneCacheVariants("example", new Cloudflare.ZoneCacheVariantsArgs
    ///         {
    ///             Avifs = 
    ///             {
    ///                 "image/avif",
    ///                 "image/webp",
    ///             },
    ///             Bmps = 
    ///             {
    ///                 "image/bmp",
    ///                 "image/webp",
    ///             },
    ///             Gifs = 
    ///             {
    ///                 "image/gif",
    ///                 "image/webp",
    ///             },
    ///             Jp2s = 
    ///             {
    ///                 "image/jp2",
    ///                 "image/webp",
    ///             },
    ///             Jpegs = 
    ///             {
    ///                 "image/jpeg",
    ///                 "image/webp",
    ///             },
    ///             Jpgs = 
    ///             {
    ///                 "image/jpg",
    ///                 "image/webp",
    ///             },
    ///             Jpg2s = 
    ///             {
    ///                 "image/jpg2",
    ///                 "image/webp",
    ///             },
    ///             Pngs = 
    ///             {
    ///                 "image/png",
    ///                 "image/webp",
    ///             },
    ///             Tifs = 
    ///             {
    ///                 "image/tif",
    ///                 "image/webp",
    ///             },
    ///             Tiffs = 
    ///             {
    ///                 "image/tiff",
    ///                 "image/webp",
    ///             },
    ///             Webps = 
    ///             {
    ///                 "image/jpeg",
    ///                 "image/webp",
    ///             },
    ///             ZoneId = "7df50664b7f90274f4d77cdfee701380",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    [CloudflareResourceType("cloudflare:index/zoneCacheVariants:ZoneCacheVariants")]
    public partial class ZoneCacheVariants : Pulumi.CustomResource
    {
        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for avif
        /// </summary>
        [Output("avifs")]
        public Output<ImmutableArray<string>> Avifs { get; private set; } = null!;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for bmp
        /// </summary>
        [Output("bmps")]
        public Output<ImmutableArray<string>> Bmps { get; private set; } = null!;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for gif
        /// </summary>
        [Output("gifs")]
        public Output<ImmutableArray<string>> Gifs { get; private set; } = null!;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for jp2
        /// </summary>
        [Output("jp2s")]
        public Output<ImmutableArray<string>> Jp2s { get; private set; } = null!;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for jpeg
        /// </summary>
        [Output("jpegs")]
        public Output<ImmutableArray<string>> Jpegs { get; private set; } = null!;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for jpg2
        /// </summary>
        [Output("jpg2s")]
        public Output<ImmutableArray<string>> Jpg2s { get; private set; } = null!;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for jpg
        /// </summary>
        [Output("jpgs")]
        public Output<ImmutableArray<string>> Jpgs { get; private set; } = null!;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for png
        /// </summary>
        [Output("pngs")]
        public Output<ImmutableArray<string>> Pngs { get; private set; } = null!;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for tiff
        /// </summary>
        [Output("tiffs")]
        public Output<ImmutableArray<string>> Tiffs { get; private set; } = null!;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for tif
        /// </summary>
        [Output("tifs")]
        public Output<ImmutableArray<string>> Tifs { get; private set; } = null!;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for webp
        /// </summary>
        [Output("webps")]
        public Output<ImmutableArray<string>> Webps { get; private set; } = null!;

        /// <summary>
        /// The ID of the DNS zone in which to apply the cache variants setting
        /// </summary>
        [Output("zoneId")]
        public Output<string> ZoneId { get; private set; } = null!;


        /// <summary>
        /// Create a ZoneCacheVariants resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ZoneCacheVariants(string name, ZoneCacheVariantsArgs args, CustomResourceOptions? options = null)
            : base("cloudflare:index/zoneCacheVariants:ZoneCacheVariants", name, args ?? new ZoneCacheVariantsArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ZoneCacheVariants(string name, Input<string> id, ZoneCacheVariantsState? state = null, CustomResourceOptions? options = null)
            : base("cloudflare:index/zoneCacheVariants:ZoneCacheVariants", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ZoneCacheVariants resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ZoneCacheVariants Get(string name, Input<string> id, ZoneCacheVariantsState? state = null, CustomResourceOptions? options = null)
        {
            return new ZoneCacheVariants(name, id, state, options);
        }
    }

    public sealed class ZoneCacheVariantsArgs : Pulumi.ResourceArgs
    {
        [Input("avifs")]
        private InputList<string>? _avifs;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for avif
        /// </summary>
        public InputList<string> Avifs
        {
            get => _avifs ?? (_avifs = new InputList<string>());
            set => _avifs = value;
        }

        [Input("bmps")]
        private InputList<string>? _bmps;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for bmp
        /// </summary>
        public InputList<string> Bmps
        {
            get => _bmps ?? (_bmps = new InputList<string>());
            set => _bmps = value;
        }

        [Input("gifs")]
        private InputList<string>? _gifs;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for gif
        /// </summary>
        public InputList<string> Gifs
        {
            get => _gifs ?? (_gifs = new InputList<string>());
            set => _gifs = value;
        }

        [Input("jp2s")]
        private InputList<string>? _jp2s;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for jp2
        /// </summary>
        public InputList<string> Jp2s
        {
            get => _jp2s ?? (_jp2s = new InputList<string>());
            set => _jp2s = value;
        }

        [Input("jpegs")]
        private InputList<string>? _jpegs;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for jpeg
        /// </summary>
        public InputList<string> Jpegs
        {
            get => _jpegs ?? (_jpegs = new InputList<string>());
            set => _jpegs = value;
        }

        [Input("jpg2s")]
        private InputList<string>? _jpg2s;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for jpg2
        /// </summary>
        public InputList<string> Jpg2s
        {
            get => _jpg2s ?? (_jpg2s = new InputList<string>());
            set => _jpg2s = value;
        }

        [Input("jpgs")]
        private InputList<string>? _jpgs;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for jpg
        /// </summary>
        public InputList<string> Jpgs
        {
            get => _jpgs ?? (_jpgs = new InputList<string>());
            set => _jpgs = value;
        }

        [Input("pngs")]
        private InputList<string>? _pngs;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for png
        /// </summary>
        public InputList<string> Pngs
        {
            get => _pngs ?? (_pngs = new InputList<string>());
            set => _pngs = value;
        }

        [Input("tiffs")]
        private InputList<string>? _tiffs;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for tiff
        /// </summary>
        public InputList<string> Tiffs
        {
            get => _tiffs ?? (_tiffs = new InputList<string>());
            set => _tiffs = value;
        }

        [Input("tifs")]
        private InputList<string>? _tifs;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for tif
        /// </summary>
        public InputList<string> Tifs
        {
            get => _tifs ?? (_tifs = new InputList<string>());
            set => _tifs = value;
        }

        [Input("webps")]
        private InputList<string>? _webps;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for webp
        /// </summary>
        public InputList<string> Webps
        {
            get => _webps ?? (_webps = new InputList<string>());
            set => _webps = value;
        }

        /// <summary>
        /// The ID of the DNS zone in which to apply the cache variants setting
        /// </summary>
        [Input("zoneId", required: true)]
        public Input<string> ZoneId { get; set; } = null!;

        public ZoneCacheVariantsArgs()
        {
        }
    }

    public sealed class ZoneCacheVariantsState : Pulumi.ResourceArgs
    {
        [Input("avifs")]
        private InputList<string>? _avifs;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for avif
        /// </summary>
        public InputList<string> Avifs
        {
            get => _avifs ?? (_avifs = new InputList<string>());
            set => _avifs = value;
        }

        [Input("bmps")]
        private InputList<string>? _bmps;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for bmp
        /// </summary>
        public InputList<string> Bmps
        {
            get => _bmps ?? (_bmps = new InputList<string>());
            set => _bmps = value;
        }

        [Input("gifs")]
        private InputList<string>? _gifs;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for gif
        /// </summary>
        public InputList<string> Gifs
        {
            get => _gifs ?? (_gifs = new InputList<string>());
            set => _gifs = value;
        }

        [Input("jp2s")]
        private InputList<string>? _jp2s;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for jp2
        /// </summary>
        public InputList<string> Jp2s
        {
            get => _jp2s ?? (_jp2s = new InputList<string>());
            set => _jp2s = value;
        }

        [Input("jpegs")]
        private InputList<string>? _jpegs;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for jpeg
        /// </summary>
        public InputList<string> Jpegs
        {
            get => _jpegs ?? (_jpegs = new InputList<string>());
            set => _jpegs = value;
        }

        [Input("jpg2s")]
        private InputList<string>? _jpg2s;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for jpg2
        /// </summary>
        public InputList<string> Jpg2s
        {
            get => _jpg2s ?? (_jpg2s = new InputList<string>());
            set => _jpg2s = value;
        }

        [Input("jpgs")]
        private InputList<string>? _jpgs;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for jpg
        /// </summary>
        public InputList<string> Jpgs
        {
            get => _jpgs ?? (_jpgs = new InputList<string>());
            set => _jpgs = value;
        }

        [Input("pngs")]
        private InputList<string>? _pngs;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for png
        /// </summary>
        public InputList<string> Pngs
        {
            get => _pngs ?? (_pngs = new InputList<string>());
            set => _pngs = value;
        }

        [Input("tiffs")]
        private InputList<string>? _tiffs;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for tiff
        /// </summary>
        public InputList<string> Tiffs
        {
            get => _tiffs ?? (_tiffs = new InputList<string>());
            set => _tiffs = value;
        }

        [Input("tifs")]
        private InputList<string>? _tifs;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for tif
        /// </summary>
        public InputList<string> Tifs
        {
            get => _tifs ?? (_tifs = new InputList<string>());
            set => _tifs = value;
        }

        [Input("webps")]
        private InputList<string>? _webps;

        /// <summary>
        /// List of strings with the MIME types of all the variants that should be served for webp
        /// </summary>
        public InputList<string> Webps
        {
            get => _webps ?? (_webps = new InputList<string>());
            set => _webps = value;
        }

        /// <summary>
        /// The ID of the DNS zone in which to apply the cache variants setting
        /// </summary>
        [Input("zoneId")]
        public Input<string>? ZoneId { get; set; }

        public ZoneCacheVariantsState()
        {
        }
    }
}
