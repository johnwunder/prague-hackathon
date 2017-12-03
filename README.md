## Prague Hackathon

An easy way to play around with scripts is Jupyter notebook. The Dockerfile in this repository will install that along with the python STIX libraries, so that you can immediately start coding.

Building the image:

```
docker build -t stix2 .
```

Running the image (Mac, Linux):

```
docker run --rm -p 8888:8888 -v `pwd`:/home/jovyan/work stix2
```

Running the image (Windows):

```
docker run --rm -p 8888:8888 -v /c/path/to/current/folder:/home/jovyan/work stix2
```

The above command will run the image in the current folder, which will be attached to the `work` folder in the notebook.

After it's running, just copy and paste the URL and you should be good to go!