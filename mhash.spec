Summary:	Hash library 
Name:		mhash
Version:	0.8.8
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://mhash.sourceforge.net/dl/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mhash is a library which provides a uniform interface to a large
number of hash algorithms. These algorithms can be used to compute
checksums, message digests, and other signatures. The HMAC support
implements the basics for message authentication, following RFC 2104.

%package devel
Summary:	Header files and development documentation for libmhash
Summary(pl):	Pliki nag³ówkowe i dokumentacja do libmhash
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libmhash.

%package static
Summary:	Static version of libmhash 
Summary(pl):	Statyczna wersja biblioteki libmhash
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static version of libmhash

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

gzip -9nf ChangeLog AUTHORS NEWS README TODO

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz 
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man3/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
