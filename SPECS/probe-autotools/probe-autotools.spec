Name: probe-autotools
Version: 0.1.0
Release: 1
Summary: probe
License: MIT
BuildRequires: autoconf automake
%description
probe
%build
./autogen.sh
%configure
make
%install
%files
