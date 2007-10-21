%define	_lang	ca
%define	_reg	AD
%define _lare	%{_lang}-%{_reg}
Summary:	Catalan resources for SeaMonkey
Summary(ca.UTF-8):	Recursos catalans per a SeaMonkey
Summary(es.UTF-8):	Recursos catalanes para SeaMonkey
Summary(pl.UTF-8):	Katalońskie pliki językowe dla SeaMonkeya
Name:		seamonkey-lang-%{_lang}
Version:	1.1.4
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	ftp://ftp.softcatala.org/pub/softcatala/seamonkey/%{version}/langpack/seamonkey-%{version}.%{_lare}.langpack.xpi
# Source0-md5:	9368268c20076670f6c48fa5a8b8b598
Source1:	http://www.mozilla-enigmail.org/downloads/lang/0.9x/enigmail-%{_lare}-0.9x.xpi
# Source1-md5:	81b64164c89ba771886f1e2c0d8d7044
Source2:	gen-installed-chrome.sh
URL:		http://www.softcatala.org/wiki/SeaMonkey
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
Obsoletes:	mozilla-lang-ca
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
Catalan resources for SeaMonkey.

%description -l ca.UTF-8
Recursos catalans per a SeaMonkey.

%description -l es.UTF-8
Recursos catalanes para SeaMonkey.

%description -l pl.UTF-8
Katalońskie pliki językowe dla SeaMonkeya.

%prep
%setup -qc
%{__unzip} -o -qq %{SOURCE1}
install %{SOURCE2} .
./gen-installed-chrome.sh locale \
	chrome/{%{_reg},%{_lare},%{_lang}-unix,enigmail-%{_lare}}.jar \
		> lang-%{_lang}-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install chrome/{%{_reg},%{_lare},%{_lang}-unix,enigmail-%{_lare}}.jar \
	$RPM_BUILD_ROOT%{_chromedir}
install lang-%{_lang}-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r searchplugins defaults $RPM_BUILD_ROOT%{_datadir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_reg}.jar
%{_chromedir}/%{_lare}.jar
%{_chromedir}/%{_lang}-unix.jar
%{_chromedir}/enigmail-%{_lare}.jar
%{_chromedir}/lang-%{_lang}-installed-chrome.txt
%{_datadir}/seamonkey/searchplugins/*
%{_datadir}/seamonkey/defaults/profile/%{_reg}
