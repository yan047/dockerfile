FROM ubuntu:22.04

LABEL maintainer="bo.yan@csiro.au"

# get WORKDIR ready
ENV WORKDIR=/work

RUN mkdir -p "$WORKDIR"

# build liboqs

RUN apt-get update && apt-get install -y build-essential
RUN apt-get install -y astyle cmake wget gcc ninja-build libssl-dev python3-pytest python3-pytest-xdist unzip xsltproc doxygen graphviz python3-yaml valgrind  
RUN cd "$WORKDIR" \ 
    && wget https://github.com/open-quantum-safe/liboqs/archive/refs/tags/0.10.0.tar.gz \
    && tar -xvpf 0.10.0.tar.gz \
    && cd liboqs-0.10.0 \
    && mkdir build && cd build \
    && cmake -GNinja .. -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX=/usr \
    && ninja \
    && ninja install

# get more dependencies 
RUN apt-get install -y git automake autoconf libtool pkg-config gettext perl python3 flex bison gperf libgmp-dev libcurl4-openssl-dev libsystemd-dev vim

# download a specific commit of strongswan
RUN cd "$WORKDIR" \
    && git clone https://github.com/strongswan/strongswan.git -b six-beta 

# remove .git and .github folder to skip the version checking in the ./configure process

RUN rm -rf "$WORKDIR"/strongswan/.git*

# build and install strongswan

RUN cd "$WORKDIR"/strongswan \
    && ./autogen.sh \
    && ./configure --enable-systemd --enable-random --enable-drbg --enable-nonce --enable-sha1     --enable-sha2 --enable-sha3 --enable-aes --enable-hmac --enable-pem --enable-pkcs1 --enable-x509 --enable-revocation --enable-constraints --enable-pubkey --enable-curve25519 --enable-oqs --enable-gmp --enable-curl --enable-kernel-netlink --enable-socket-default --enable-updown --enable-vici --enable-load-tester --with-dev-headers --with-systemdsystemunitdir=/lib/systemd/system \
    && make \
    && make install

