Name: probe-rust
Version: 0.1.0
Release: 1
Summary: probe
License: MIT
BuildRequires: cargo
%description
probe
%build
cargo build --release
%install
%files
