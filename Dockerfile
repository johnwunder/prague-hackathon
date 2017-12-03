FROM jupyter/minimal-notebook
MAINTAINER John Wunder "jwunder@mitre.org"

USER jovyan
RUN pip install stix2 stix2-patterns stix2-viz stix2-validator