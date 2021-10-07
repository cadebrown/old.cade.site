---
layout: post
title: "DIY: Regex Engine"
categories: [diy]
tags: [regex, hacks]
thumb: /files/diy-regex-engine.webp
---

I was in need of a regex engine... so I decided I would write my own. In a single file, we implement a regex engine (including a regex pattern parser, compiler, and matching engine), and an implementation of a `mg` (for `my-grep`) in C, in a single file: 

  * [check out `mg.c` on GitHub](https://gist.github.com/CadeBrown/a949ed37fe15022c101cfe92f7abc72f)

<!--more-->

## How It Works

to implement the regex compiler and matcher, we will use [Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction), with a straightforward NFA implementation for various operations. Here's the syntax we're aiming for:

![](/files/diy-regex-engine.webp)

so, it's a little different than normal regex syntax, but in my opinion more straightforward. also, the double-star (`**`) operator that repeats a specific number of time that can be any within a set is something I've not seen... it could be useful for searching for specific depth of functions (for example, `^\t**{1,3,5}func` would look for functions defined at those indentation levels)

the basic parsing algorithm uses a single expandable list of NFA states, which have edges to other NFA states, or a special value (-1 means no edge, -2 means edge into 'accept' state). the NFA is then simulated by input file data, and when a match is encountered, the line is printed out (like `grep`). just compile [the code, `mg.c`](https://gist.github.com/CadeBrown/a949ed37fe15022c101cfe92f7abc72f) and run it yourself:


{:.command-line .no-line-numbers data-prompt="{{ site.shellprompt }}" data-filter-output="out:"}
```bash
# if you have wget
wget -O mg.c https://git.io/JVyoT
out:--2021-10-05 23:07:20--  https://git.io/JVyoT
out:...
out:Saving to: ‘mg.c’
out:
out:mg.c                                 100%[====================================================================>]  29.26K  --.-KB/s    in 0.002s  
out:
out:2021-10-05 23:07:21 (13.5 MB/s) - ‘mg.c’ saved [29962/29962]
cc -o mg mg.c
mg -h
out:usage: mg [re] [src...=./]
out:
out:  -h,--help            prints this help/usage menu and exits
out:  -[DNLS]              set the format columns ([Dd]ate, [Nn]ame, [Ll]ineno, [Ss]ource)
out:
out:see: https://cade.site/2021/09/28/diy-regex-engine
out:author: Cade Brown <cade@cade.site>
```

and, if you want to run it I also include a test file:

{:.command-line .no-line-numbers data-prompt="{{ site.shellprompt }}" data-filter-output="out:"}
```bash
wget -O mgtest.txt https://git.io/JVyMp
out:--2021-10-05 23:11:25--  https://git.io/JVyMp
out:...
out:Saving to: ‘mgtest.txt’
out:
out:mgtest.txt                           100%[====================================================================>]      90  --.-KB/s    in 0s      
out:
out:2021-10-05 23:11:25 (8.59 MB/s) - ‘mgtest.txt’ saved [90/90]
out:
# format is 'filename | lineno | linesrc'
./mg 'a' mgtest.txt                                                                                                                         ─╯
out:mgtest.txt       |    2 | a
out:mgtest.txt       |    3 | aa
out:mgtest.txt       |    4 | aaa
out:mgtest.txt       |    5 | aaaa
out:mgtest.txt       |    6 | aaaaa
out:mgtest.txt       |    9 | ab
out:mgtest.txt       |   10 | ac
out:mgtest.txt       |   12 | abc
out:mgtest.txt       |   13 | aaabbb
out:mgtest.txt       |   14 | cat
out:mgtest.txt       |   15 | bat
out:mgtest.txt       |   16 | rat
out:mgtest.txt       |   17 | mat
out:mgtest.txt       |   18 | map
out:mgtest.txt       |   19 | trap
out:mgtest.txt       |   20 | crap
out:mgtest.txt       |   21 | back
out:mgtest.txt       |   22 | wack
out:mgtest.txt       |   23 | stack
# words that end with 't'
./mg 't$' mgtest.txt                                                                                                                        ─╯
out:mgtest.txt       |   14 | cat
out:mgtest.txt       |   15 | bat
out:mgtest.txt       |   16 | rat
out:mgtest.txt       |   17 | mat
# lines with exactly 1, 2, or 4 'a's
./mg '^a**{1,2,4}$' mgtest.txt                                                                                                                        ─╯
out:mgtest.txt       |    2 | a
out:mgtest.txt       |    3 | aa
out:mgtest.txt       |    5 | aaaa
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


