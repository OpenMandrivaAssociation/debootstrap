%define name debootstrap
%define version 1.0.28
%define release %mkrel 1

Summary: Bootstrap a basic Debian system
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.debian.org/debian/pool/main/d/debootstrap/%{name}_%{version}.tar.gz
Source1: devices.tar.gz
License: MIT
Group: System/Configuration/Packaging
Url: http://packages.debian.org/unstable/admin/debootstrap
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
debootstrap is used to create a Debian base system from scratch,
without requiring the availability of dpkg or apt. It does this by
downloading .deb files from a mirror site, and carefully unpacking
them into a directory which can eventually be chrooted into.

%prep
%setup -q -n %{name}
perl -pi -e 's/ -o root -g root//' Makefile
perl -pi -e 's/^(\s+)(chown.*)$/$1#$2/g' Makefile
perl -pi -e 's/^(all:.*?)(\S+.tar.gz)$/$1/g' Makefile
perl -pi -e 's,qw\(%{_prefix}/lib /lib\),qw\(%{_libdir} /%{_lib}\),' functions
cp %{SOURCE1} .

%build
%make

%install
rm -rf %{buildroot}
%makeinstall_std
install -D -m 644 %{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc TODO
%{_sbindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man8/%{name}.8*
