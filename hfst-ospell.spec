%define major 11
%define oldlibname %mklibname hfstospell %{major}
%define libname %mklibname hfstospell
%define devname %mklibname hfstospell -d

%if %{cross_compiling}
# This workaround can go as soon as we have the filesystem changes in place
%global optflags %{optflags} -I%{_prefix}/%{_target_platform}/include/libxml++-2.6 -I%{_prefix}/%{_target_platform}/include/glibmm-2.4 -I%{_prefix}/%{_target_platform}/%{_lib}/glibmm-2.4/include -I%{_prefix}/%{_target_platform}/%{_lib}/libxml++-2.6/include
%endif

Name: hfst-ospell
Version:	0.5.3
Release:	7
Source0: https://github.com/hfst/hfst-ospell/archive/v%{version}.tar.gz
Patch0: hfst-ospell-0.5.0-compile.patch
Patch1: hfst-ospell-0.5.3-compile.patch
Summary: Spell checker library and command line tool
URL: https://hfst.github.io/
License: Apache 2.0
Group: System/Libraries
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: slibtool
BuildRequires: icu-devel
BuildRequires: pkgconfig(libxml++-2.6)

%description
HFST spell checker library and command line tool


%package -n %{libname}
Summary: Spell checker library
Group: System/Libraries
%rename %{oldlibname}

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
%make_build LIBTOOL=slibtool-shared

%install
%make_install LIBTOOL=slibtool-shared

%files
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
