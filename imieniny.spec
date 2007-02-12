Summary:	Gives a saints names whose name one bears
Summary(pl.UTF-8):   Skrypt wypisujący aktualnych solenizantów
Name:		imieniny
Version:	1.1.5
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://infoludek.com.pl/~slawek/%{name}-%{version}.tar.gz
# Source0-md5:	42187c87d841f9655e0893cb0cb508f8
Source1:	%{name}.sh
URL:		http://infoludek.com.pl/~slawek/imieniny.html
Requires:	sh-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small utility gives saints whose name one bears current day.

%description -l pl.UTF-8
Niewielki skrypt wypisujący solenizantów z danego dnia.

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
%doc czytajto.txt
%attr(755,root,root) %{_bindir}/%{name}
%dir	%{_datadir}/%{name}
%lang(pl) %{_datadir}/%{name}/pl_PL
%lang(pl) %{_datadir}/%{name}/pl
