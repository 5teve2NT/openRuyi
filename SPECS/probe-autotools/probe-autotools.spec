Name: probe-autotools
Version: 0.1.0
Release: 1
Summary: probe
License: MIT
BuildSystem: autotools
BuildRequires: autoconf automake
%description
probe
%build
./autogen.sh
%configure
make
%install
%files
