{
  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        name = "python-dev";
        buildInputs = with pkgs; [
          python3
        ];
      };
      packages.${system} = {
        default = pkgs.callPackage ./default.nix { };
      };
    };
}
