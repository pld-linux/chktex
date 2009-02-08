Summary:	LaTeX semantic checker
Summary(pl.UTF-8):	Narzędzie do sprawdzania składni LaTeX-a
Name:		chktex
Version:	1.6.4
Release:	0.1
License:	GPL v2+
Group:		Applications
Source0:	http://baruch.ev-en.org/proj/chktex/%{name}-%{version}.tar.gz
# Source0-md5:	e1d1f70d37e97734a69c94682a2038a0
URL:		http://baruch.ev-en.org/proj/chktex/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program has been written in frustration because some constructs
in LaTeX are sometimes non-intuitive, and easy to forget. It is _not_
a replacement for the built-in checker in LaTeX; however it catches
some typographic errors LaTeX oversees. In other words, it is Lint for
LaTeX. Filters are also provided for checking the LaTeX parts of CWEB
documents.

%description -l pl.UTF-8
Program ten został napisany z powodu frustruacji pewnymi mało
intuicyjnymi i łatwymi do zapomnienia konstrukacjami w LaTeX-u. Nie
jest to zamiennik dla wbudowanego w LaTeX-a narzędzia do sprawdzania
składni; jednak potrafi wyłapać pewne błędy typograficzne przez niego
pominięte. Innymi słowy, jest to Lint dla LaTeX-a. Dostępne są także
filtry do sprawdzania fragmentów LaTeX-a w dokumentach CWEB.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install chktex.1 chkweb.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/chktexrc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
