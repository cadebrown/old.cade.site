---
layout: post
title: "DIY: Regex Engine"
categories: [diy]
tags: [regex, hacks]
thumb: /files/diy-regex-engine.png
---

I was in need of a regex engine... so I decided I would write my own. In a single file, we implement a regex engine (including a regex pattern parser, compiler, and matching engine), and an implementation of a `mg` (for `my-grep`) in C, in a single file: 

  * [check out `mg.c` on GitHub](https://gist.github.com/CadeBrown/a949ed37fe15022c101cfe92f7abc72f)

<!--more-->

## How It Works

to implement the regex compiler and matcher, we will use [Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction), with a straightforward NFA implementation for various operations. Here's the syntax we're aiming for:

![/files/diy-regex-engine.png](/files/diy-regex-engine.png)

so, it's a little different than normal regex syntax, but in my opinion more straightforward. also, the double-star (`**`) operator that repeats a specific number of time that can be any within a set is something I've not seen... it could be useful for searching for specific depth of functions (for example, `^\t**{1,3,5}func` would look for functions defined at those indentation levels)

the basic parsing algorithm uses a single expandable list of NFA states, which have edges to other NFA states, or a special value (-1 means no edge, -2 means edge into 'accept' state). the NFA is then simulated by input file data, and when a match is encountered, the line is printed out (like `grep`). just compile [the code, `mg.c`](https://gist.github.com/CadeBrown/a949ed37fe15022c101cfe92f7abc72f) and run it yourself:

```
$ mg -h
usage: mg [re] [src...=./]

  -h,--help            prints this help/usage menu and exits
  -[DNLS]              set the format columns ([Dd]ate, [Nn]ame, [Ll]ineno, [Ss]ource)

see: https://cade.site/2021/09/28/DIY-Regex-Engine
author: Cade Brown <cade@cade.site>
```

## "It's 2021, all regexes have backreferences bruh"

if you're not familiar with [this article](https://swtch.com/~rsc/regexp/regexp1.html), and wonder why backreferences can be considered problematic, please read it first. if you still aren't satisfied... read on

kata regexes are "true" regular expressions, in that they correspond to a [regular language](https://en.wikipedia.org/wiki/Regular_language). for example, many languages (Python's included) aren't really "regular" expressions, as they include backreferences and other non-regular constructions.

many developers insist that the examples provided are unrealistic and the time complexity justification is unjustified in real-world examples. "who would use $a?^na^n$, anyway?"

[people do, but not for the reason you might expect](https://en.wikipedia.org/wiki/ReDoS)

in fact, here are just a few examples of the dangers of non-regular regexes:

  * [OWASP ReDoS](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS)
  * one malicious regex: `(([a-z])+.)+` (could you spot that as a security/performance vulnerability?)

So, I made the decision to not support any non-regular constructions


