FROM alinde/saturdays:e35d147ec675

ARG NB_USER=jovian
ARG NB_UID=1000

ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

WORKDIR ${HOME}

COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}

USER ${USER}
