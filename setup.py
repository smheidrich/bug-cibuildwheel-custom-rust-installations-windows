from sys import stderr
from pathlib import Path
import os
from subprocess import run

from setuptools import setup
from setuptools_rust import Binding, RustExtension

this_directory = Path(__file__).parent

stderr.write("***HELLO***\n")
stderr.write(str(os.environ)+"\n")
run("rustc")
# run("which which 2>&1", shell=True)
run("where rustc 2>&1", shell=True)

setup(
    name="examplepkg",
    version="0.1.0",
    rust_extensions=[
        RustExtension(
            "examplepkg.example.pkg",
            binding=Binding.PyO3,
            debug=False,
        )
    ],
    packages=["examplepkg"],
    zip_safe=False,
    description="foo",
    long_description="foo",
)
