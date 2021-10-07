# cadebrown.github.io ([https://cade.site](https://cade.site))

this is the source for my personal website/blog, and is available to download and customize if you want

## setup

to install/setup and run on a local machine

### Ubuntu/Debian/`apt`-based

run:

```shell
$ sudo apt install ruby-full build-essential zlib1g-dev
$ sudo gem install jekyll bundler
$ bundle install
```

then, to serve locally:

```shell
$ bundle exec jekyll serve
...
    Server address: http://127.0.0.1:4000
  Server running... press ctrl-c to stop.
```

and navigate to `localhost:4000` in your browser


## tips

here are some tips that may make your blog more responsive/efficient:

  * use `.webp` files for images


## software used

this is all the software that I use, with some helpful links to show you how to use/tweak them:

  * [kramdown](https://kramdown.gettalong.org/syntax.html), for markdown parsing
  * [prism.js](https://prismjs.com/), for syntax highlighting
    * to customize your settings, [go here](https://prismjs.com/download.html), and replace `js/prism.js` and `css/prism.css`
    * to add your own languages, [see here](https://prismjs.com/extending.html)
    * to use commandline/shell output, [see here](https://github.com/cadebrown/cadebrown.github.io/blob/main/_posts/2021-09-28-diy-regex-engine.md)
    * to generate a tree view for a directory, [go here](https://prismjs.com/plugins/treeview/)
    * to have a pretty diff/difference, [go here](https://prismjs.com/plugins/diff-highlight/)
  * [MathJax](https://www.mathjax.org/), for math/LaTeX
    * to use it in a post, use `$ x^2 + x + 5$` (for inline), or `$$ x^2 + x + 5 $$` (for block mode)
    * to customize behavior, check `_includes/head.html`
    * to optimize, [go here](https://docs.mathjax.org/en/latest/misc/faq.html#faq-slow-no-math)
  * [git.io](https://git.io/), GitHub's URL shortener (I use it for gists)
  

