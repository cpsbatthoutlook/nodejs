FROM docker.io/jupyter/base-notebook
ARG NB_USER="jovyan"
ARG NB_UID="1000"
ARG NB_GID="100"
ARG HOME="/home/${NB_USER}"
#
COPY Dockerfile ${HOME}
COPY Dockerfile.orig.1 ${HOME}
COPY requirements.txt ${HOME}
#COPY requirements.txt /tmp
RUN  python -m pip install -r ${HOME}/requirements.txt
ADD  dash_examples ${HOME}/
#ADD --chown=${NB_USER}:${NB_USER}  dash_examples ${HOME}/
#RUN  python -m pip install mljar-mercury pandas matplotlib itables==0.4.4
EXPOSE 8888 8050
# Configure container startup
ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.sh"]
# Switch back to jovyan to avoid accidental container runs as root
USER ${NB_UID}
WORKDIR "${HOME}"
