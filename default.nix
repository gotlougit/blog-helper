{ lib, fetchFromSourcehut, python3Packages }:

with python3Packages;
buildPythonPackage rec {
  pname = "blog-helper";
  version = "1.1";

  src = fetchFromSourcehut {
    owner = "~gotlou";
    repo = pname;
    rev = "c49d8a057af35a82043c064f4bfb0370b929d130";
    sha256 = "sha256-1Mq9W+rpcwHZu8QlsUptFWyUdrUCc4wPztuCtOfeCa0=";
  };

  doCheck = false;
  postInstall = ''
    rm $out/bin/blog-helper
    touch $out/bin/blog-helper
    chmod +x $out/bin/blog-helper
    echo "#!/usr/bin/env python3" > $out/bin/blog-helper
    cat $out/bin/main.py >> $out/bin/blog-helper
  '';

  meta = with lib; {
    description = "Small program to add templates and add blogpost entry to main webpage with easy customization settings.";
    homepage = "https://github.com/gotlougit/blog-helper";
    license = licenses.gpl2Plus;
  };
}
