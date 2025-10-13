let
  rev = "24.05";      # Exemple : version stable 24.05
  sha256 = "0zydsqiaz8qi4zd63zsb2gij2p614cgkcaisnk11wjy3nmiq0x1s";
in
import (builtins.fetchTarball {
  url = "https://github.com/NixOS/nixpkgs/archive/nixos-${rev}.tar.gz";
  inherit sha256;
})
