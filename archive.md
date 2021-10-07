---
layout: default
title: Archive
permalink: /archive
nomathjax: true
noprism: true
---
<!-- Original snippet for generating archive page found here:
https://gist.github.com/tuananh/743255://gist.github.com/tuananh/7432553 -->

## Archive

<ul>
{% for post in site.posts %}
    {% unless post.next %}
        <h3>{{ post.date | date: '%Y-%m' }}</h3>
    {% else %}
        {% capture year %}{{ post.date | date: '%Y-%m' }}{% endcapture %}
        {% capture nyear %}{{ post.next.date | date: '%Y-%m' }}{% endcapture %}
        {% if year != nyear %}
        <h3>{{ post.date | date: '%Y-%m' }}</h3>
        {% endif %}
    {% endunless %}

    <li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>
