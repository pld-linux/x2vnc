#
Summary:	A dual-screen hack for one keyboard and mouse on two machines
Name:		x2vnc
Version:	1.6
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://fredrik.hubbe.net/x2vnc/%{name}-%{version}.tar.gz
# Source0-md5:	e4bb4dec31bc1b3b56d777bc365c9534
URL:		http://fredrik.hubbe.net/x2vnc.html
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/x2vnc
%{_mandir}/man*/*
