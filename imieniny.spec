Summary:	Gives a saints names whose name one bears
Summary(pl.UTF-8):	Skrypt wypisujący aktualnych solenizantów
Name:		imieniny
Version:	1.1.5
Release:	6
License:	GPL
Group:		Applications/System
Source0:	http://infoludek.com.pl/~slawek/%{name}-%{version}.tar.gz
# Source0-md5:	42187c87d841f9655e0893cb0cb508f8
Source1:	%{name}.sh
URL:		http://infoludek.com.pl/~slawek/imieniny.html
BuildRequires:	iconv
Requires:	coreutils
Requires:	iconv
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small utility gives saints whose name one bears current day.

%description -l pl.UTF-8
Niewielki skrypt wypisujący solenizantów z danego dnia.

%prep
%setup -q -c

%build
mkdir pl_PL.UTF-8
for file in [0-9][0-9].txt; do
	iconv -f latin2 -t utf-8 $file > pl_PL.UTF-8/$file
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/pl_PL.UTF-8}

install	%{SOURCE1}	$RPM_BUILD_ROOT%{_bindir}/%{name}
install pl_PL.UTF-8/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/pl_PL.UTF-8
ln -sf pl_PL.UTF-8	$RPM_BUILD_ROOT%{_datadir}/%{name}/pl_PL
ln -sf pl_PL.UTF-8	$RPM_BUILD_ROOT%{_datadir}/%{name}/pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc czytajto.txt
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%lang(pl) %{_datadir}/%{name}/pl_PL.UTF-8
%lang(pl) %{_datadir}/%{name}/pl_PL
%lang(pl) %{_datadir}/%{name}/pl
