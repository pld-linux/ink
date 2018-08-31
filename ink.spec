#
# Conditional build:
%bcond_without	parport	# parallel port (IEEE 1284) support

Summary:	Tool for checking ink level of a printer
Summary(pl.UTF-8):	Narzędzie sprawdzające poziom atramentu w drukarce
Name:		ink
Version:	0.5.3
Release:	1
License:	GPL v2
Group:		Applications/Printing
Source0:	http://downloads.sourceforge.net/ink/%{name}-%{version}.tar.gz
# Source0-md5:	7ddb245c1b0314a4348f2a43e8d37885
Patch0:		%{name}-parport.patch
URL:		http://ink.sourceforge.net/
BuildRequires:	libinklevel-devel >= 0.9.3
Requires:	libinklevel >= 0.9.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ink is a CLI tool for checking the ink level of a printer.

%description -l pl.UTF-8
Ink jest działającym z linii poleceń narzędziem do sprawdzania poziomu
atramentu w drukarce.

%prep
%setup -q
%if %{with parport}
%patch0 -p1
%endif

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/ink
%{_mandir}/man1/ink.1*
