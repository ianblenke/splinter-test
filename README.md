This container makes it easy to run
[Splinter](http://splinter.readthedocs.org/) tests on
[PhantomJS](http://phantomjs.org) without installing anything but Docker.

# Usage

Mount your tests in the `/test` folder of the image and run it:

```
docker run --rm -v $(realpath tests):/test -t lascap/splinter-test
```

Your tests need to use:

```
splinter.Browser('phantomjs')
```
