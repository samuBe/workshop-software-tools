# workshop-software-tools

A workshop to learn some software tools, focused on the Python language.

The slides for this workshop can be found on google drive: https://docs.google.com/presentation/d/1ft1aKGnbwRh2cpSvBfY--8RURK3udgJe/edit?usp=sharing&ouid=105743895182186891104&rtpof=true&sd=true

To create the sphinx docs, you can use docker with

    docker run --rm -v /path/to/document:/docs sphinxdoc/sphinx make html

If docker is not installed, use [docker desktop](https://www.docker.com/products/docker-desktop/)

Or install sphinx with conda or [see this website](https://www.sphinx-doc.org/en/master/usage/installation.html).

To watch the rendered, docs you can just open them in a browser like firefox or chrome.
