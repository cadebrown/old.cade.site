# [cade.site](https://cade.site)

This is the source code for my personal website ([cade.site](https://cade.site)). It's built with Jekyll and deployed with GitHub pages, designed by me to be minimalist, readable, and sleek (and, kind of old-school ugly/simple HTML). 

I'm so tired of all the "sleek bootstrap" themes that are 30MB of JS, take 10 seconds to fully load, and navigating by jolting around the page. This is meant to be a simple, extensible theme that you can use if you care about people actually reading what you're working on.

## Setup

If you want your own copy, [fork the GitHub repo](https://github.com/cadebrown/cade.site/fork). (also, "star" it if you like it, please!). Then, follow these steps:

You'll need to [install Jekyll](https://jekyllrb.com/docs/installation/). Follow the instructions for your platform.

Then, the first time you clone the repository, install the requirements:

```shell
$ bundle install
... a bunch of versions ...
Bundle complete! 7 Gemfile dependencies, 32 gems now installed.
Use `bundle info [gemname]` to see where a bundled gem is installed.
```

Now, every time you want to preview the site on your local machine, run:
  
```shell
$ bundle exec jekyll serve
... setup messages ...
Server address: http://127.0.0.1:4000
Server running... press ctrl-c to stop.
```

Navigate to `localhost:4000` in your web browser to see the site live.

  * give `--drafts` to also include draft posts
  * give `--host 0.0.0.0` to serve to your local network (good for testing on mobile phone)

## Integrations

This blog has a lot of builtin integrations with common tools. here's a quick list:

  * [kramdown](https://kramdown.gettalong.org/syntax.html) for markdown syntax
  * [Disqus](https://disqus.com/) for comments on posts
  * [Prism.js](https://prismjs.com/) for code highlighting
    * [example: shell/commandline highlighting](https://github.com/cadebrown/cadebrown.github.io/blob/main/_posts/2021-09-28-diy-regex-engine.md)
    * [example: tree/directory view](https://prismjs.com/plugins/treeview/)
    * [example: pretty 'diff' output](https://prismjs.com/plugins/diff-highlight/)
    * if you're not satisfied with my Prism config, [use their wizard](https://prismjs.com/download.html)
    * to add more languages, add them in the [js/components](./js/components) folder (TODO: example of this)
  * [KaTeX](https://www.katex.org/) for math formatting (LaTeX-like, and much faster than MathJax)
    * to use it in a post, use `\( x^2 + x + 5 \)` (for inline), or `$$ x^2 + x + 5 $$` (for block mode)
  * [git.io](https://git.io/) for URL shortening (useful for gists)
  * [GitHub Buttons](https://buttons.github.io/) the style is included in the head element, so just paste the element!
  * Google Analytics: for analyzing your web traffic

Most configuration options for software are available in:

  * `_includes/head.html`: this is where you could customize versions/loading order of script tags and whatnot


## Code Structure

All the modular components are in `_includes`, for example:

  * `_includes/post-desc.html`: post description card generator (i.e. thumbnail and exerpt)

All the custom themes and styling are in `css/main.css`

  * to change the font from monospace to something less 1337, change the `:root` rules at the top of the file
  * to add a theme, follow the comments for an existing theme, change the name, and also edit `_layouts/default.html` (comments will explain everything)

### Tips

Here are some tips for better performance/integration with your site:

  * use `.webp` files for images ([use `cwebp` if possible](https://developers.google.com/speed/webp/docs/cwebp))
  * to check your images, use [imagemagick](https://imagemagick.org/script/identify.php)
    * for example, `for f in files/*; do identify -format '%f %wx%y\n' $f; done` and  look for any abnormally large images that could be made smaller
  * to automatically generate low resolution thumbnails, run `python3 scripts/make-img-lowres.py`
    * use `{% include image-srcset.html src=name class="gallery-img" alt=name %}` for responsible image sizing
