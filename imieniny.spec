Summary:	Gives a saints names whose name one bears
Summary(pl):	Skrypt wypisuj±cy aktualnych solenizantów
Name:		imieniny
Version:	1.1.0
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://infoludek.com.pl/~slawek/%{name}-%{version}.tar.gz
Source1:        imieniny.sh
URL:		http://infoludek.com.pl/~slawek/imieniny.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch
Requires:	sh-utils

%description
Small utility gives saints whose name one bears current day

%description -l pl
Niewielki skrypt wypisuj±cy solenizantów z danego dnia

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/pl_PL}

install [0-9][0-9].txt	$RPM_BUILD_ROOT%{_datadir}/%{name}/pl_PL
ln -sf pl_PL		$RPM_BUILD_ROOT%{_datadir}/%{name}/pl
install	%{SOURCE1}	$RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%lang(pl) %{_datadir}/%{name}/pl_PL
%lang(pl) %{_datadir}/%{name}/pl
