# norootforbuild

Name         : eio
Version      : 1.7.11
Release      : 1%{?dist}
License      : LGPLv2.1
Group        : System Environment/Libraries
Provides     : eina = %{version}, libeina1 = %{version}
URL          : http://enlightenment.org/
Packager     : Guillaume Friloux <guillaume@friloux.me>
Group        : System/Libraries
Summary      : Enlightenment Input/Output Library
Source       : ~/rpmbuild/SOURCES/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig subversion automake doxygen m4 autoconf gzip bzip2 tar
BuildRequires: ecore-devel eina-devel

%description
Core EFL (Enlightenment Foundation Library) to handle various data types.

%package devel
Summary      : EIO headers, static libraries, documentation and test programs
Group        : Development/Libraries
Requires     : %{name} = %{version}

%description devel
Headers, static libraries, test programs and documentation for eio

%prep
rm -rf "$RPM_BUILD_ROOT"
%setup -q

%build
touch config.rpath
./autogen.sh --prefix=/usr                                                     \
             --libdir=/usr/lib64

%install
make %{?_smp_mflags}
%makeinstall

%clean
rm -rf "$RPM_BUILD_ROOT"

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files devel
%defattr(-, root, root)
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
