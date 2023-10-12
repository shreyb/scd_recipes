# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RucioClients(PythonPackage):
    """Client interface to Rucio."""

    homepage = "https://rucio.cern.ch"
    pypi = "rucio-clients/rucio-clients-1.30.0.tar.gz"

    # maintainers = ["marcmengel","bari12"]

    version("32.4.0", sha256="847f8db44f6f7f2c53cfb596afcefefd310c5791d5fbee86bc487d904c130801") 

    depends_on("python", type=("build", "run"))
    depends_on("py-pip", type="build")
    depends_on("py-requests", type=("build","run"))
    depends_on("py-urllib3", type=("build","run"))
    depends_on("py-dogpile-cache", type=("build","run"))
    depends_on("py-tabulate", type=("build","run"))
    depends_on("py-jsonschema", type=("build","run"))
    depends_on("py-paramiko", type=("build","run"))
    depends_on("py-kerberos", type=("build","run"))
    depends_on("py-requests-kerberos", type=("build","run"))
    depends_on("py-python-swiftclient", type=("build","run"))
    depends_on("py-argcomplete", type=("build","run"))
    depends_on("py-python-magic", type=("build","run"))
