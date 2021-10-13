FROM tomsquest/docker-radicale

COPY radicale_ldap_auth /opt/radicale_ldap_auth
RUN  cd /opt/radicale_ldap_auth && python3 -m pip install .
