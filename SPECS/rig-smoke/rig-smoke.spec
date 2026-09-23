# SPDX-License-Identifier: MulanPSL-2.0
Name:           rig-smoke
Version:        1.0
Release:        1
Summary:        Smoke test fixture package for the abaci-bot test rig
License:        GPL-2.0-or-later AND MIT
URL:            https://example.invalid/rig-smoke
Source:         https://example.invalid/rig-smoke-%{version}.tar.xz
BuildSystem:    cmake

%description
Not a real package. Fixture used to validate abaci-bot classification modules.

%prep
%autosetup -n rig-smoke-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_bindir}/rig-smoke
