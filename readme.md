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


## software used

this is all the software that I use, with some helpful links to show you how to use/tweak them:

  * [prism.js](https://prismjs.com/), for syntax highlighting
    * To customize this, go to: [https://prismjs.com/download.html](https://prismjs.com/download.html), and replace `js/prism.js` and `css/prism.css` with the files you download
    * [https://prismjs.com/plugins/file-highlight/](https://prismjs.com/plugins/file-highlight/)
    * [https://prismjs.com/plugins/autolinker/](https://prismjs.com/plugins/autolinker/)
    * [https://prismjs.com/plugins/autoloader/](https://prismjs.com/plugins/autoloader/), in `./`
    * [https://prismjs.com/plugins/keep-markup/](https://prismjs.com/plugins/keep-markup/)
    * [https://prismjs.com/plugins/command-line/](https://prismjs.com/plugins/command-line/)
      * use `command-line` in your code blocks (see below with kramdown)
    * [https://prismjs.com/plugins/treeview/](https://prismjs.com/plugins/treeview/)
      * for tree/directory structures
    * [https://prismjs.com/plugins/diff-highlight/](https://prismjs.com/plugins/diff-highlight/)
  * [MathJAX](https://www.mathjax.org/), for Math highlighting/stylizations
    * to use it in a post, do something like `$ x^2 + x + 5 $`
  * [kramdown](https://kramdown.gettalong.org/syntax.html), for markdown parsing
    * you can specify custom classes with `{:.<name>}` (for example, `{:.command-line}`)
  * [git.io](https://git.io/), GitHub's URL shortener
  * FontAwesome
  