Summary:	Catalan resources for SeaMonkey
Summary(ca):	Recursos catalans per a SeaMonkey
Summary(es):	Recursos catalanes para SeaMonkey
Summary(pl):	Kataloñskie pliki jêzykowe dla SeaMonkeya
Name:		seamonkey-lang-ca
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	ftp://ftp.softcatala.org/pub/softcatala/seamonkey/%{version}/langpack/seamonkey-%{version}.ca-AD.langpack.xpi
# Source0-md5:	660564467a928bee25442fe6133d0cc8
Source1:	gen-installed-chrome.sh
URL:		http://www.softcatala.org/wiki/SeaMonkey
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
Catalan resources for SeaMonkey.

%description -l ca
Recursos catalans per a SeaMonkey.

%description -l es
Recursos catalanes para SeaMonkey.

%description -l pl
Kataloñskie pliki jêzykowe dla SeaMonkeya.

%prep
%setup -q -c -T
unzip %{SOURCE0}
install %{SOURCE1} .
./gen-installed-chrome.sh locale chrome/{AD,ca-AD,ca-unix}.jar > lang-ca-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install chrome/{AD,ca-AD,ca-unix}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-ca-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r searchplugins defaults $RPM_BUILD_ROOT%{_datadir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/ca-AD.jar
%{_chromedir}/ca-unix.jar
%{_chromedir}/AD.jar
%{_chromedir}/lang-ca-installed-chrome.txt
%{_datadir}/seamonkey/searchplugins/*
%{_datadir}/seamonkey/defaults/messenger/AD
%{_datadir}/seamonkey/defaults/profile/AD
