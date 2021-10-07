---
layout: post
title: "Adding Extra Information To Hashes"
categories: [math]
tags: [kata, hacks]
thumb: /files/katastringhash.webp
---

in a long programming session working on [kata.tools](https://kata.tools), specifically the implementation of the `string` type in the builtin namespace.

since strings in kata are immutable, their hash can be stored with the object, and only computed once, making hash(x) O(1) instead of O(N). this isn't new, CPython for example has been using this strategy for some time. however, instead of computing a hash-code summation, what if we augment with a bitmask of a few common boolean optimizations...


<!--more-->

for example, what if you could tell, in O(1) time if a string was all-ASCII, no weird/escape characters, or valid ASCII identifier? it would make IO and serialization quicker for valid identifiers, and take up 0 extra space (all you sacrifice is ~4/32 bits of entropy, or ~4/64 on most platforms... 28 bit is still pretty good!)

## But WHY?


well, I was implementing printf-like IO on duck-typed reference-counted objects. but, instead of the typical build-a-buffer, and then print, and then free, the printf has builtin pathways for common types (including common containers), so that no extra memory is allocated from a `printf()/print()` function, even for dictionary/lists.

while implementing the dictionary format, which looks like `{ a: 1, b: 2, "c invalid-ident": 3 }`. notice how keys can be unquoted (for valid identifiers), or can be quoted if they have invalid characters (so that any string can be used). I realized that every string-print would potentially add O(len(s)) time and I wasn't satisfied (I'm trying to provide Python-style type system operating at native speeds). I realized that I was already including a 32/64 bit hash value as an unsigned as integer, which is computed with a [djb2-like](http://www.cse.yorku.ca/~oz/hash.html) function. so, what if we included that information in the hash? for example:

![](/files/katastringhash.webp)

### But... What about exceptions? If there is arbitrary code executed with string conversion

You bring up a good point... consider the following code:

```ks

type B {
    # called when 'self' should append itself to 'io'
    func __str(self, io) {
        # should do 'io.printf(...)', but what if:
        throw Error()
    }
}

# now, use it in a printf call
printf("This is a fu%Rll sentence", B())

# the output will normally read:
# This is a fu
# Error: ...
# which is not desirable!

```

if this is a concern with your interface, you can use the `sprintf()` function, which works exactly like `printf`, except that it doesn't output any IO and instead returns a string built in memory. so, that line would be come:

```ks

# NOTE: just use 'print' since you're printing a string
print(sprintf("This is a fu%Rll sentence", B()))

# output:
#
# nothing is printed!

```

### What's the added cost to string creation

This is the only thing that I don't have a good accessment on the performance. When talking about dense, linear strings (as opposed to twines) string creation is inherently O(N) because we need to know how many Unicode characters there are and bytes, and to compute the hash. so, the loop to compute the hash would also need to track whether it was ASCII-only, or ASCII-identifier only, or ASCII-unescaped only, and perform a few bitwise operations to mask the values into a single 32/64 bit integer


if we assume the average string is used more than once (which is a fair assumption), we would start to break even at 1 or 2 uses of the string. but even then, it's not a large deficit. but, when a single string is printed often, or used in a dictionary, the savings may be 10-100x in CPU-cycles. therefore, I think it is a worthy feature to investigate and adopt it experimentally until a stable interface is developed... stay tuned, I'll update this article whenever I perfom specific comparisons
