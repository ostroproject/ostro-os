#!/bin/sh

GENKEY=ima.genkey

cat << __EOF__ >$GENKEY
[ req ]
default_bits = 1024
distinguished_name = req_distinguished_name
prompt = no
string_mask = utf8only
x509_extensions = v3_usr

[ req_distinguished_name ]
O = syncev
CN = pohly signing key
emailAddress = pohly@syncev

[ v3_usr ]
basicConstraints=critical,CA:FALSE
#basicConstraints=CA:FALSE
keyUsage=digitalSignature
#keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectKeyIdentifier=hash
authorityKeyIdentifier=keyid
#authorityKeyIdentifier=keyid,issuer
__EOF__

openssl req -new -nodes -utf8 -sha1 -days 365 -batch -config $GENKEY \
        -out csr_ima.pem -keyout privkey_ima.pem
openssl x509 -req -in csr_ima.pem -days 365 -extfile $GENKEY -extensions v3_usr \
        -CA ima-local-ca.pem -CAkey ima-local-ca.priv -CAcreateserial \
        -outform DER -out x509_ima.der
