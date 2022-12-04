FROM glotzerlab/software

USER root

#RUN apt install openbabel --yes

RUN pip3 install pySCF

USER glotzerlab-software


WORKDIR /home/molmod/

EXPOSE 8000

#CMD ["jupyter", "notebook", "--ip 0.0.0.0", "--port 8000", "--no-browser", "--notebook-dir /home/molmod"]
