%define debug_package	%nil

Summary:	Bootstrap a basic Debian system
Name:		debootstrap
Version:	1.0.59
Release:	1
Source0:	http://ftp.debian.org/debian/pool/main/d/debootstrap/%{name}_%{version}.tar.xz
Source1:	devices.tar.gz
License:	MIT
Group:		System/Configuration/Packaging
Url:		http://packages.debian.org/unstable/admin/debootstrap
BuildArch:	noarch

%description
debootstrap is used to create a Debian base system from scratch,
without requiring the availability of dpkg or apt. It does this by
downloading .deb files from a mirror site, and carefully unpacking
them into a directory which can eventually be chrooted into.

%prep
%setup -q
perl -pi -e 's/ -o root -g root//' Makefile
perl -pi -e 's/^(\s+)(chown.*)$/$1#$2/g' Makefile
perl -pi -e 's/^(all:.*?)(\S+.tar.gz)$/$1/g' Makefile
perl -pi -e 's,qw\(%{_prefix}/lib /lib\),qw\(%{_libdir} /%{_lib}\),' functions
cp %{SOURCE1} .

%build
%make

%install
%makeinstall_std
install -D -m 644 %{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8

%files
%doc TODO
%{_sbindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man8/%{name}.8*
