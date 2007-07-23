%define name debootstrap
%define version 1.0.0
%define release %mkrel 1

Summary: Bootstrap a basic Debian system
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.debian.org/debian/pool/main/d/debootstrap/%{name}_%{version}.tar.bz2
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
perl -pi -e 's,%{_prefix}/lib/%{name},$1%{_libdir}/%{name},' Makefile %{name}
perl -pi -e 's,qw\(%{_prefix}/lib /lib\),qw\(%{_libdir} /%{_lib}\),' functions

%build

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc TODO
%{_sbindir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man8/debootstrap.8*
