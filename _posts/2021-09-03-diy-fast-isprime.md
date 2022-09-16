---
layout: post
title: "DIY: Fast 'isprime()' for Primality Testing (using Miller-Rabin)"
tags: [math]
thumb: /files/diy-fast-isprime-0.webp
---

We've all had to include a little `isprime()` function in our code, right? (well, most people reading my blog probably have). In this article i provide an implementation of a primality test (in C) that is quite a bit faster for larger values, and is still easily embeddable and usable within existing applications

<!--more-->

## Naive Implementation

Most programmers, when asked to check whether a number is prime, would probably write some code like the following (myself included):


```c
// check whether 'n' is prime, using a naive method
bool
isprime_naive(size_t n) {
    // take care of 0,1
    if (n < 2) return false;
    // get rid of even numbers, except 2
    if (n % 2 == 0) return n == 2;

    // do trial division, checking only the odd numbers <= sqrt(n)
    size_t i;
    for (i = 3; i * i <= n; i += 2) {
        // divisible, so not prime
        if (n % i == 0) return false;
    }

    // no factors, so must be prime
    return true;
}

```

While there's nothing wrong with this code, and it arguably is the best solution if you only use it a couple of times, there are more efficient deterministic tests for larger numbers. For example, we'll look at using the [Miller-Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test), modified to be deterministic for a suitable range of 'n'


## Miller-Rabin implementation

I'm just going to include the full implementation here, so you can copy and paste, and read the comments to understand how it works:

```c
/* Miller-Rabin 'isprime()' implementation
 *
 *
 * NOTE: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
 * @author: Cade Brown <cade@cade.site>
 */

// (internal) compute a**b (mod m)
static size_t
my_modpow(size_t a, size_t b, size_t m) {

    // a**2**i (mod m)
    usize a2i = a;

    // the result product
    usize res = 1;

    // basically, iterate over the bits of 'b', and treat it
    //   as a bitset
    while (b) {
        if (b & 1) {
            // this power should be included, since its in the bitset
            res = (res * a2i) % m;
        }

        // compute, and apply modulo to avoid overflow:
        // a**2**(i+1) == (a**2**i)**2
        a2i = (a2i * a2i) % m;

        // now, shift the bitset
        b >>= 1;
    }

    return res;
}

// (internal) perform a witness check in Miller-Rabin, returns whether it is probably prime
//   a: the witness being tested
//   n: the number being checked for primality, n := 2**r * d + 1 (i.e. within the 2-adic number system)
//   r: see 'n'
//   d: see 'n', must be ODD
static bool
my_witness(size_t a, size_t n, size_t r, size_t d) {
    // compute a ** d (mod n)
    size_t x = my_modpow(a, d, n);

    // special case that it's probably true for this witness
    if (x == 1 || x == n - 1) {
        return true;
    }

    // repeat (r-1) times
    size_t ct;
    for (ct = 0; ct < r - 1; ct++) {
        x = (x * x) % n;
        if (x == n - 1) {
            // probably true as well
            return true;
        }
    }

    return false;
}


// tell whether 'n' is prime
bool
isprime(size_t n) {
    if (n < 2) return false;
    if (n % 2 == 0) return n == 2;

    // compute: n := 2 ** r * d + 1
    // (i.e. decompose into 2-adic number)
    size_t d = n - 1;
    size_t r = 0;
    while (d % 2 == 0) {
        r++;
        d >>= 1;
    }

    // utility macro for a single witness
    #define WIT(_a) my_witness((_a), n, r, d)

    // use proven bounds
    /**/ if (n < 2047ULL) return WIT(2);
    else if (n < 1373653ULL) return WIT(2) && WIT(3);
    else if (n < 9080191ULL) return WIT(31) && WIT(73);
    else if (n < 25326001ULL) return WIT(2) && WIT(3) && WIT(5);
    else if (n < 3215031751ULL) return WIT(2) && WIT(3) && WIT(5) && WIT(7);
    else if (n <= 0xFFFFFFFFULL) return WIT(2) && WIT(7) && WIT(61); // 32 bit values
    else {
        // this is a catch all, which should work up to
        // 18446744073709551616 = 2**64
        // so, this is only needed on 32 bit systems
        return WIT(2) && WIT(3) && WIT(5) && WIT(7) && WIT(11) && WIT(13) && WIT(17) && WIT(19) && WIT(23) && WIT(29) && WIT(31) && WIT(37);
    }
}

```

Here's how they perform on my machine, calculating whether 10 million random numbers are prime, within different bounds:

![performance graph up to `2**32`](/files/diy-fast-isprime-0.webp)


Here's a comparison of even larger (> 32 bit values) trends in performance:

![performance graph up to `2**48`](/files/diy-fast-isprime-1.webp)

As you can see, both implementations have similar performance (with naive being a little faster), until $2^{14}$, at which point the trend reverses. The trends become even more pronounced after $2^{32}$, where the Miller-Rabin implementation essentially always hits the 'else' case, and plateaus.

For large values, the Miller-Rabin implementation 30x-50x faster than the naive one! I know this implementation has helped many of my other projects efficiently implement prime checking (check out [PGS](https://github.com/chemicaldevelopment/pgs)!)
