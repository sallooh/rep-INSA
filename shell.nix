{ pkgs ? import <nixpkgs> {} }:

let
  py = pkgs.python311;
in
pkgs.mkShell {
  packages = [
    py
    pkgs.python311Packages.venvShellHook
  ];

  venvDir = ".venv";

  postVenvCreation = ''
    python -m pip install --upgrade pip
    if [ -f requirements.txt ]; then
      PIP_DISABLE_PIP_VERSION_CHECK=1 python -m pip install -r requirements.txt
    fi
  '';

  postShellHook = ''
    echo "Environnement Python activé : $(python --version)"
    echo "Pour exécuter le script : python tp1_associativity.py"
  '';
}
