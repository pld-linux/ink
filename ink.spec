Summary:	Tool for checking ink level of a printer
Summary(pl.UTF-8):	Narzędzie sprawdzające poziom atramentu w drukarce
Name:		ink
Version:	0.4.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/ink/%{name}-%{version}.tar.gz
# Source0-md5:	ac795dbdb00982aa3627773da2250d55
Patch0:		%{name}-build_fixes.patch
URL:		http://ink.sourceforge.net/
BuildRequires:	libinklevel-devel >= 0.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ink is a CLI tool for checking the ink level of a printer.

%description -l pl.UTF-8
Ink jest narzędziem CLI do sprawdzania poziomu atramentu w drukarce.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
