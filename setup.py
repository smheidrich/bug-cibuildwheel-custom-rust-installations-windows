from pathlib import Path

from setuptools import setup
from setuptools_rust import Binding, RustExtension

this_directory = Path(__file__).parent

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
