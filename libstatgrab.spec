Summary:	Easy-to-use interface for accessing system statistics and information
Summary(pl):	£atwy w u¿yciu interfejs dostêpu do statystyk i informacji o systemie
Name:		libstatgrab
Version:	0.10.2
Release:	1
License:	LGPL	
Group:		Libraries
Source0:	ftp://ftp.mirrorservice.org/sites/ftp.i-scream.org/pub/i-scream/libstatgrab/%{name}-%{version}.tar.gz
# Source0-md5:	3165015263a7e45e962e6bce27abfbe5
Patch0:		%{name}-Makefile_fix.patch
URL:		http://www.i-scream.org/libstatgrab/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libstatgrab library provides an easy-to-use interface for
accessing system statistics and information. Available statistics
include CPU, Load, Memory, Swap, Disk I/O, and Network I/O. It was
developed to work on Linux, FreeBSD, and Solaris. The package also
includes two tools: saidar provides a curses-based interface for
viewing live system statistics, and statgrab is a sysctl-like
interface to the statistics.

%description -l pl
Biblioteka libstatgrab dostarcza ³atwego w u¿yciu interfejsu dostêpu
do informacji i statystyk systemowych. Dostêpne statystyki obejmuj±
CPU, obci±¿enie, pamiêæ swap, dyskowe i sieciowe operacje we./wy. .
libstatgrab zosta³ stworzony by dzia³aæ na linuksie, FreeBSD i
Solarisie. Pakiet zawiera tak¿e dwa narzêdzia: saidar dostarcza
bazuj±cego na curses interfejsu do przegl±dania statystyk systemu i
statgrab, który jest interfejsem podobnym do sysctl dla statystyk.

%package devel
Summary:	Header files for libstatgrab library
Summary(pl):	Pliki nag³ówkowe biblioteki libstatgrab
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libstatgrab library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libstatgrab.

%package static
Summary:	Static libstatgrab library
Summary(pl):	Statyczna biblioteka libstatgrab
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libstatgrab library.

%description static -l pl
Statyczna biblioteka libstatgrab.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README PLATFORMS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man3/statgrab*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/sg_*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
