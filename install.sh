#!/usr/bin/env bash -l
set -euo pipefail

# Function to check if micromamba is installed
function check_micromamba() {
    if ! command -v micromamba &> /dev/null; then
        echo "Micromamba not found, installing..."
		curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba
		~/.local/bin/micromamba shell init -p "$HOME/micromamba"
		echo 'export MAMBA_ROOT_PREFIX="$HOME/micromamba"' >> ~/.bashrc
        echo 'export PATH="$MAMBA_ROOT_PREFIX/bin:$PATH"' >> ~/.bashrc
        source ~/.bashrc
    else
        echo "Micromamba is already installed"
    fi
}

# Call the function to check micromamba
check_micromamba

# Continue with the script
micromamba create -y --name saezlab python=3.9 pandas=1.5.3 numpy=1.24.3 jupyter=1.0.0 python-graphviz=0.20.1 matplotlib=3.7.1 seaborn=0.12.2 cvxpy=1.3.1 pyscipopt=4.3.0
micromamba activate saezlab
pip install git+https://github.com/saezlab/decoupler-py.git@4b3978f
pip install git+https://github.com/saezlab/omnipath.git@v1.0.7
pip install git+https://github.com/saezlab/corneto.git@0.9.1-alpha.0
pip install cylp==0.91.5
pip install adjustText==0.8
