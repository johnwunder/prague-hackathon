FROM jupyter/minimal-notebook
MAINTAINER John Wunder "jwunder@mitre.org"

USER jovyan
RUN pip install stix2 stix2-patterns stix2-viz stix2-validator stix-pattern-translator

USER root
RUN jupyter nbextension install stix2viz --py
RUN jupyter nbextension enable stix2viz --py