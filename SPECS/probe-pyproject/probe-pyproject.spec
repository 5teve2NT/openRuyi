Name: probe-pyproject
Version: 0.1.0
Release: 1
Summary: probe
License: MIT
BuildSystem: pyproject
BuildRequires: python3-devel
%description
probe
%build
%pyproject_wheel
%install
%files
