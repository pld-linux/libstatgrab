Summary:	Easy-to-use interface for accessing system statistics and information
Summary(pl):	£atwy w u¿yciu interfejs dostêpu do statystyk i informacji o systemie
Name:		libstatgrab
Version:	0.8.2
Release:	1
License:	LGPL	
Group:		Libraries
Source0:	ftp://ftp.mirror.ac.uk/sites/ftp.i-scream.org/pub/i-scream/libstatgrab/%{name}-%{version}.tar.gz
# Source0-md5:	41ebe054a2579090e1e25ab998b08ed0
URL:		http://www.i-scream.org/libstatgrab/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libstatgrab library provides an easy-to-use interface for accessing
system statistics and information. Available statistics include CPU,
Load, Memory, Swap, Disk I/O, and Network I/O. It was developed to work
on Linux, FreeBSD, and Solaris. The package also includes two tools:
saidar provides a curses-based interface for viewing live system
statistics, and statgrab is a sysctl-like interface to the statistics.

#%description -l pl
#Biblioteka libstatgrab dostarcza ³atwego w u¿yciu interfejsu do 

%package devel
Summary:	Header files for libstatgrab library
Summary(pl):	Pliki nag³ówkowe biblioteki libstatgrab
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libstatgrab library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libstatgrab.

%package static
Summary:	Static libstatgrab library
Summary(pl):	Statyczna biblioteka libstatgrab
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libstatgrab library.

%description static -l pl
Statyczna biblioteka libstatgrab.

%prep
%setup -q

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
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man3/statgrab*

%files devel
%defattr(644,root,root,755)
%doc devel-doc/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/get*
%{_mandir}/man3/cpu*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
