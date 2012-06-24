Summary:	Hash library
Summary(pl):	Biblioteka funkcji mieszaj�cych (skr�tu)
Summary(pt_BR):	Interface uniforme para v�rios algoritmos hash
Name:		mhash
Version:	0.9.3
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/mhash/%{name}-%{version}.tar.gz
# Source0-md5:	8c2dc7b2bfe84bccf8d25d338bf75760
Patch0:		%{name}-mhash_free.patch
URL:		http://mhash.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mhash is a library which provides a uniform interface to a large
number of hash algorithms. These algorithms can be used to compute
checksums, message digests, and other signatures. The HMAC support
implements the basics for message authentication, following RFC 2104.

%description -l pl
Mhash to biblioteka dostarczaj�ca jednolity interfejs do du�ej liczby
algorytm�w mieszaj�cych (skr�tu). Te algorytmy mog� by� u�ywane do
liczenia sum kontrolnych, oznacze� komunikat�w oraz innych sygnatur.
Obs�uga HMAC daje podstawy dla uwierzytelniania wiadomo�ci, zgodnie z
RFC 2104.

%description -l pt_BR
A biblioteca mhash prov� uma interface uniforme para um grande n�mero
de algoritmos hash. Estes algoritmos podem ser utilizados para
computar checksums, digests de mensagens, e outras assinaturas. O
suporte a HMAC implementa o b�sico para autentica��o de mensagens,
seguindo o RFC 2104. Nas vers�es mais recentes foram adicionados
alguns algoritmos de gera��o de chaves, que utilizam algoritmos hash.
A biblioteca suporta os algoritmos CRC32, MD5, SHA1, HAVAL256, TIGER,
RIPEMD260, GOST, CRC32B, HAVAL224, HAVAL192, HAVAL160, HAVAL128,
TIGER128, TIGER160, MD4, SHA256, and ADLER32.

%package devel
Summary:	Header files and development documentation for libmhash
Summary(es):	Archivos de inclusi�n y bibliotecas de desarrollo
Summary(pl):	Pliki nag��wkowe i dokumentacja do libmhash
Summary(pt_BR):	Arquivos de desenvolvimento para a biblioteca mhash
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for libmhash.

%description devel -l pl
Pliki nag��wkowe i dokumentacja programisty do libmhash.

%description devel -l pt_BR
Esse pacote cont�m arquivos de desenvolvimento para a biblioteca
mhash.

%package static
Summary:	Static version of libmhash
Summary(es):	bibliotecas estaticas mhash
Summary(pl):	Statyczna wersja biblioteki libmhash
Summary(pt_BR):	Bibliotecas est�ticas do mhash para desenvolvimento
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libmhash.

%description static -l pl
Statyczna wersja libmhash.

%description static -l pt_BR
Esse pacote cont�m arquivos de desenvolvimento est�ticos para a
biblioteca mhash.

%prep
%setup -q
%patch0 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO doc/skid2-authentication
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_mandir}/man3/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
