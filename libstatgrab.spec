Summary:	Easy-to-use interface for accessing system statistics and information
Summary(pl.UTF-8):	Łatwy w użyciu interfejs dostępu do statystyk i informacji o systemie
Name:		libstatgrab
Version:	0.15
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.mirrorservice.org/sites/ftp.i-scream.org/pub/i-scream/libstatgrab/%{name}-%{version}.tar.gz
# Source0-md5:	d2738ecd1dfe90c488fd6b1515e84841
Patch0:		%{name}-Makefile_fix.patch
URL:		http://www.i-scream.org/libstatgrab/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	linux-libc-headers >= 7:2.6.11.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libstatgrab library provides an easy-to-use interface for
accessing system statistics and information. Available statistics
include CPU, Load, Memory, Swap, Disk I/O, and Network I/O. It was
developed to work on Linux, FreeBSD, and Solaris. The package also
includes two tools: saidar provides a curses-based interface for
viewing live system statistics, and statgrab is a sysctl-like
interface to the statistics.

%description -l pl.UTF-8
Biblioteka libstatgrab dostarcza łatwego w użyciu interfejsu dostępu
do informacji i statystyk systemowych. Dostępne statystyki obejmują
CPU, obciążenie, pamięć swap, dyskowe i sieciowe operacje we./wy. .
libstatgrab został stworzony by działać na linuksie, FreeBSD i
Solarisie. Pakiet zawiera także dwa narzędzia: saidar dostarcza
bazującego na curses interfejsu do przeglądania statystyk systemu i
statgrab, który jest interfejsem podobnym do sysctl dla statystyk.

%package devel
Summary:	Header files for libstatgrab library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libstatgrab
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libstatgrab library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libstatgrab.

%package static
Summary:	Static libstatgrab library
Summary(pl.UTF-8):	Statyczna biblioteka libstatgrab
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libstatgrab library.

%description static -l pl.UTF-8
Statyczna biblioteka libstatgrab.

%package -n statgrab
Summary:	sysctl-style interface to system statistics
Summary(pl.UTF-8):	Podobny do sysctl interfejs do statystyk systemu
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description -n statgrab
statgrab provides a sysctl-style interface to all the system
statistics available through libstatgrab. This is useful for
applications that don't want to make library calls, but still want to
access the statistics.

An example of such an application is mrtg, for which scripts are
provided to generate configuration files.

%description -n statgrab -l pl.UTF-8
statgrab udostępnia podobny do sysctl interfejs do wszystkich
statystyk systemu dostępnych poprzez libstatgrab. Jest to przydatne
dla aplikacji nie chcących wykonywać wywołań bibliotecznych, ale
chcących mieć dostęp do statystyk.

Przykładem takiej aplikacji jest mrtg, dla którego dostępne są
skrypty do generowania plików konfiguracyjnych.

%package -n saidar
Summary:	A curses-based tool for viewing system statistics
Summary(pl.UTF-8):	Oparte na curses narzędzie do oglądania statystyk systemu
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description -n saidar
saidar is a curses-based tool for viewing the system statistics
available through libstatgrab. Statistics include CPU, processes,
load, memory, swap, network I/O, disk I/O, and file system
information.

%description -n saidar -l pl.UTF-8
saidar to oparte na curses narzędzie do oglądania statystyk systemu
dostępnych poprzez libstatgrab. Statystyki obejmują informacje o
procesorach, procesach, obciążeniu, pamięci, swapie, operacjach we/wy
sieciowych i dyskowych oraz systemach plików.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-curses-prefix=/usr \
	--with-ncurses \
	--disable-setgid-binaries \
	--disable-setuid-binaries
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc examples/*.c
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/sg_*
%{_mandir}/man3/statgrab*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files -n statgrab
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/statgrab*
%{_mandir}/man1/statgrab*

%files -n saidar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/saidar
%{_mandir}/man1/saidar.1*
