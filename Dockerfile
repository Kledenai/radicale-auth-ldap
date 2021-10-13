FROM tomsquest/docker-radicale

COPY radicale_auth_ldap /opt/radicale_auth_ldap
RUN  cd /opt/radicale_auth_ldap && python3 -m pip install .
