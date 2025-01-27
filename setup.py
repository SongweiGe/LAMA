# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from setuptools import setup, find_packages

requirements = ['Cython==0.29.2', 'numpy==1.15.1', 'torch==1.0.1', 'pytorch-pretrained-bert==0.6.1', 'allennlp==0.8.5', 'spacy==2.1.8', 'tqdm==4.26.0', 'termcolor==1.1.0', 'pandas==0.23.4', 'fairseq==0.8.0', 'scipy==1.3.2', 'overrides==3.1.0', 'colorama==0.4.1']
setup(
    name = 'LAMA',
    version = '0.1.2',
    url = 'https://github.com/fairinternal/LAMA',
    author = 'Fabio Petroni & Facebook AI colleagues',
    author_email = 'fabiopetroni@fb.com',
    description = 'LAMA: LAnguage Model Analysis',
    packages = find_packages(),
    install_requires=requirements,
)
