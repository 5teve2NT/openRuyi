Name: probe-golang
Version: 0.1.0
Release: 1
Summary: probe
License: MIT
BuildSystem: golang
BuildRequires: golang
%description
probe
%build
go build ./...
%install
%files
