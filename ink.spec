Summary:	Tool for checking ink level of a printer
Summary(pl):	Narzêdzie sprawdzaj±ce poziom atramentu w drukarce
Name:		ink
Version:	0.3
Release:	1
License:	GPL
Group:		Applications
Source0:	http://home.arcor.de/markusheinz/%{name}-%{version}.tar.gz
# Source0-md5:	1fca7b488c7e37e6809820bd5aed5053
Patch0:		%{name}-build_fixes.patch
URL:		http://home.arcor.de/markusheinz/ink.html
BuildRequires:	libinklevel-devel >= 0.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ink is a CLI tool for checking the ink level of a printer.

%description -l pl
Ink jest narzêdziem CLI do sprawdzania poziomu atramentu w drukarce.

%prep
%setup -qn %{name}
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
%doc README
%attr(755,root,root) %{_bindir}/*
