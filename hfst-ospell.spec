%define major 10
%define libname %mklibname hfstospell %{major}
%define devname %mklibname hfstospell -d

Name: hfst-ospell
Version: 0.5.0
Release: 2
Source0: https://github.com/hfst/hfst-ospell/archive/v0.5.0.tar.gz
Patch0: hfst-ospell-0.5.0-compile.patch
Summary: Spell checker library and command line tool
URL: http://hfst.github.io/
License: Apache 2.0
Group: System/Libraries
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: icu-devel
BuildRequires: pkgconfig(libxml++-2.6)

%description
HFST spell checker library and command line tool


%package -n %{libname}
Summary: Spell checker library
Group: System/Libraries

%description -n %{libname}
Spell checker library

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
./autogen.sh
%configure

%build
%make_build

%install
%make_install

%files
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
