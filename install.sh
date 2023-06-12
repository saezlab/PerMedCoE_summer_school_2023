#!/usr/bin/env bash -l
set -euo pipefail

# Function to check if micromamba is installed
function check_micromamba() {
    if ! command -v micromamba &> /dev/null; then
        echo "Micromamba not found, installing..."
		curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba
		./bin/micromamba shell init -s bash -p ~/micromamba
		export MAMBA_EXE="$HOME/bin/micromamba";
		export MAMBA_ROOT_PREFIX="$HOME/micromamba";
		__mamba_setup="$("$MAMBA_EXE" shell hook --shell bash --prefix "$MAMBA_ROOT_PREFIX" 2> /dev/null)"
		if [ $? -eq 0 ]; then
			eval "$__mamba_setup"
		else
			if [ -f "$HOME/micromamba/etc/profile.d/micromamba.sh" ]; then
				. "$HOME/micromamba/etc/profile.d/micromamba.sh"
			else
				export  PATH="$HOME/micromamba/bin:$PATH"  # extra space after export prevents interference from conda init
			fi
		fi
		unset __mamba_setup
    else
        echo "Micromamba is already installed"
    fi
}

# Call the function to check micromamba
check_micromamba

# Continue with the script
echo "Preparing environment..."
micromamba create -y -n saezlab python=3.9 pandas=1.5.3 numpy=1.24.3 jupyter=1.0.0 python-graphviz=0.20.1 matplotlib=3.7.1 seaborn=0.12.2 cvxpy=1.3.1 pyscipopt=4.3.0 -c conda-forge
micromamba activate saezlab
pip install git+https://github.com/saezlab/decoupler-py.git@4b3978f
pip install git+https://github.com/saezlab/omnipath.git@v1.0.7
pip install git+https://github.com/saezlab/corneto.git@0.9.1-alpha.0
pip install cylp==0.91.5
pip install adjustText==0.8
